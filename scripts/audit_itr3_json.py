#!/usr/bin/env python3
"""Print a privacy-safe summary or comparison of ITR-3 upload JSON files.

Missing paths are reported as null, never as zero. Source filenames and direct
personal identifiers are intentionally omitted from output.
"""

import argparse
import json
from pathlib import Path


def get(obj, path, default=None):
    for key in path.split("."):
        if isinstance(obj, list):
            try:
                obj = obj[int(key)]
            except (ValueError, IndexError):
                return default
        elif isinstance(obj, dict):
            obj = obj.get(key, default)
        else:
            return default
    return obj


def summarize(path, source_label):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    root = get(data, "ITR.ITR3", {})
    if not isinstance(root, dict) or not root:
        return {
            "source": source_label,
            "source_kind": "prefill_or_unknown",
            "assessment_year": None,
            "error": "ITR.ITR3 root not found; do not treat this as an upload-JSON summary",
        }

    verification_place = get(root, "Verification.Place")
    general_businesses = get(root, "PartA_GEN2.NatOfBus.NatureOfBusiness")
    ada_professions = get(root, "PARTA_PL.NatOfBus44ADA")
    summary = {
        "source": source_label,
        "source_kind": "itr3_upload",
        "assessment_year": get(root, "Form_ITR3.AssessmentYear"),
        "gross_receipts_44ada": get(root, "PARTA_PL.PersumptiveInc44ADA.GrsReceipt"),
        "income_44ada": get(root, "PARTA_PL.PersumptiveInc44ADA.TotPersumptiveInc44ADA"),
        "stcg_transfer_expense": get(root, "ScheduleCGFor23.ShortTermCapGainFor23.EquityMFonSTT.0.EquityMFonSTTDtls.DeductSec48.ExpOnTrans"),
        "ltcg_transfer_expense": get(root, "Schedule112A.ExpExclCnctTransfer112A"),
        "net_capital_gains": get(root, "ScheduleCGFor23.TotScheduleCGFor23"),
        "bfla_ltcg_12_5": get(root, "ScheduleBFLA.LTCG12_5Per.IncBFLA.IncOfCurYrAfterSetOffBFLosses"),
        "table_f": {
            "upto_15_june": get(root, "ScheduleCGFor23.AccruOrRecOfCG.LongTermUnder12_5Per.DateRange.Upto15Of6"),
            "16_june_to_15_september": get(root, "ScheduleCGFor23.AccruOrRecOfCG.LongTermUnder12_5Per.DateRange.Upto15Of9"),
            "16_september_to_15_december": get(root, "ScheduleCGFor23.AccruOrRecOfCG.LongTermUnder12_5Per.DateRange.Up16Of9To15Of12"),
            "16_december_to_15_march": get(root, "ScheduleCGFor23.AccruOrRecOfCG.LongTermUnder12_5Per.DateRange.Up16Of12To15Of3"),
            "16_march_to_31_march": get(root, "ScheduleCGFor23.AccruOrRecOfCG.LongTermUnder12_5Per.DateRange.Up16Of3To31Of3"),
        },
        "other_sources": get(root, "ScheduleOS.IncChargeable"),
        "total_income": get(root, "PartB-TI.TotalIncome"),
        "gross_tax": get(root, "PartB_TTI.ComputationOfTaxLiability.TaxPayableOnTI.GrossTaxLiability"),
        "interest_and_fee": get(root, "PartB_TTI.ComputationOfTaxLiability.IntrstPay.TotalIntrstPay"),
        "taxes_paid": get(root, "PartB_TTI.TaxPaid.TaxesPaid.TotalTaxesPaid"),
        "amount_payable": get(root, "PartB_TTI.TaxPaid.BalTaxPayable"),
        "refund": get(root, "PartB_TTI.Refund.RefundDue"),
        "foreign_assets_flag": get(root, "PartB_TTI.AssetOutIndiaFlag", ""),
        "general_business_codes": None if general_businesses is None else [x.get("Code") for x in general_businesses],
        "profession_codes_44ada": None if ada_professions is None else [x.get("CodeADA") for x in ada_professions],
        "verification_place_present": None if verification_place is None else bool(verification_place),
    }
    summary["unknown_fields"] = sorted(find_null_paths(summary))
    return summary


def flatten(obj, prefix=""):
    result = {}
    if isinstance(obj, dict):
        for key, value in obj.items():
            path = f"{prefix}.{key}" if prefix else key
            result.update(flatten(value, path))
    else:
        result[prefix] = obj
    return result


def find_null_paths(obj):
    return [path for path, value in flatten(obj).items() if value is None]


def compare(summaries):
    flattened = [flatten(summary) for summary in summaries]
    ignored = {"source", "unknown_fields"}
    paths = sorted(set().union(*(item.keys() for item in flattened)))
    differences = {}
    for path in paths:
        if path in ignored or path.startswith("unknown_fields"):
            continue
        values = [item.get(path) for item in flattened]
        if any(value != values[0] for value in values[1:]):
            differences[path] = values
    return differences


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("json_files", nargs="+", help="One or more ITR-3 upload JSON files")
    args = parser.parse_args()
    summaries = [summarize(path, f"input_{index}") for index, path in enumerate(args.json_files, 1)]
    output = summaries[0] if len(summaries) == 1 else {
        "summaries": summaries,
        "differences": compare(summaries),
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
