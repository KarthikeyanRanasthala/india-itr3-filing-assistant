---
name: india-itr3-filing-assistant
description: Review, reconcile, and safely operate India's ITR-3 across the Income Tax e-Filing portal, offline utility, broker portals such as Zerodha Console, or files-only workflows for individual taxpayers with presumptive professional income, capital gains, broker tax-P&L files, Form 64B/PTI data, AIS/prefill JSON, tax payments, and generated upload JSON. Use for AY/FY or Tax Year selection, evidence retrieval, schedule selection and cleanup, BP/44ADA, CG/112A, OS/PTI/EI, CYLA/BFLA, Table F, VI-A, Tax Paid, Part B-TI/TTI, preview, validation, and mismatches among source evidence, third-party computations, generated JSON, the portal, and the utility. Routine reversible work may be authorized once upfront; never pay, sign the declaration, e-verify, or submit without separate action-time confirmation.
---

# India ITR3 Filing Assistant

## Capability conventions

- Use the capabilities available in the host agent. When this skill names a Codex capability, prefer it in Codex; another agent may use an equivalent capability.
- If an instruction requires authenticated browser or desktop control and no safe, observable equivalent is available, preserve the current session, report the limitation, and continue only with read-only or files-only work.
- `agents/openai.yaml` is optional Codex UI metadata. It is not a runtime dependency for other agents.

## Operating principles

- Treat tax filing as high stakes. Distinguish inspection, reversible draft edits, schedule confirmation, validation, payment, declaration/signing, e-verification, and submission.
- Prefer source evidence over third-party totals. Reconcile broker files, Form 64B, AIS/prefill, challans, and generated JSON.
- Never invent a factual tax value. A blank or omitted JSON field is not evidence of zero. Record unresolved values as `unknown` and surface them before confirming the affected schedule.
- Preserve personal data. Do not copy PAN, Aadhaar, full bank details, addresses, email, phone, passwords, or OTPs into skill files, logs, or examples.
- Browse current official Income Tax Department sources for unstable rules, dates, forms, rates, and portal behavior. Use primary sources for legal or technical claims.

## Choose the operating surface

- **Online portal:** use authenticated browser control that can access the user's existing login state; in Codex, prefer Chrome control. Read `references/portal-workflow.md` and, when evidence is missing, `references/portal-downloads.md` before operating. Open only the official `https://www.incometax.gov.in/` site, then ask the user to log in. Never request, read, type, or handle the password, OTP, or CAPTCHA.
- **Broker portal:** when Zerodha evidence is missing, read `references/zerodha-console.md`, then use authenticated browser control (in Codex, Chrome control) to open only `https://console.zerodha.com/` and immediately ask the user to log in. Never request, read, type, or handle credentials, PIN, password, OTP, or TOTP.
- **Offline utility:** use safe interactive desktop control; in Codex, prefer Computer Use. Follow the host agent's confirmation policy.
- **Files only:** use read-only file tools and a spreadsheet/CSV inspection capability; in Codex, prefer the spreadsheet skill. Use `scripts/audit_itr3_json.py` for generated ITR-3 JSON.
- Do not switch surfaces silently. State which surface is being used and which artifact is the baseline.
- On a resumed or compacted turn, reconstruct the known-facts and authorization ledger from the conversation and existing artifacts before asking anything. Reacquire the existing tab/session when possible; do not restart intake or login merely because the control surface was reloaded.

## Upfront intake and authorization

- Read `references/intake.md` and inspect the working directory. When a structured-choice prompt capability is available, use one upfront round of up to three high-leverage choices: stopping point, routine-edit scope, and Pay-Later behavior; in Codex, use `request_user_input`. Ask remaining factual or free-form items in one structured message. When no such capability is available, ask the same choices in normal chat. Use a second round only for genuinely conditional issues discovered from evidence.
- Keep structured-choice questions short, mutually exclusive, and decision-oriented; put the recommended option first. Do not force the full tax questionnaire into repeated prompt rounds.
- Restate facts already known from the conversation or reliable files; ask the user to correct them instead of re-asking one at a time.
- Maintain a compact session ledger containing: filing year/posture, confirmed positive and negative facts, evidence status, authorized reversible scope, authorized stopping point, Pay-Later choice, completed stages, unresolved facts, and irreversible actions still gated. Update it after every user answer or material browser transition.
- Obtain one scope authorization covering any combination of:
  - read-only inspection;
  - routine reversible entries and corrections supported by evidence;
  - removal of empty, inapplicable, nondependent schedules after inspection;
  - schedule confirmation, dependency recalculation, and correction of validation errors;
  - validation and progress up to the selected surface's Verification stage;
  - downloading missing tax-portal and broker evidence into the working directory and verifying the artifacts;
  - selecting **Pay Later** solely to reach Verification when tax remains payable.
- Once granted, do not repeatedly ask for confirmation for actions within that scope. Pause only for a new material fact, conflicting evidence, an unsupported factual value, a change outside the authorized scope, or an irreversible/gated action.
- Treat vague permission such as “fill anything needed” as permission to make supported entries, not permission to fabricate facts.
- Always require separate action-time confirmation for making a payment, ticking the declaration/signing, uploading a return, e-verifying, or submitting. State the amount and immediate consequence before asking.

## Workflow

1. **Establish filing posture.**
   - Read `references/tax-year-selection.md`. Infer the ordinary filing candidate from today's India date, state the inferred AY/FY or Tax Year pair and basis, then ask the user to correct it in the consolidated intake rather than asking an isolated year question.
   - Confirm the inferred year against the portal/utility label, return type, and filing context; then confirm individual status, residential status, return section, regime and Form 10-IEA facts, ITR-3 applicability, profession/business, books/audit position, income sources, foreign-asset facts, and authorized stopping point.
   - For section 44ADA, verify profession code, receipts by payment mode, and declared income.

2. **Inventory and classify evidence.**
   - Identify the newest relevant files by modification time and content; do not assume a filename is current.
   - Distinguish AIS/prefill source JSON from an ITR-3 upload JSON generated by the portal, utility, or another filing workflow. Treat generated JSON as a reconciliation baseline, not independent proof of facts.
   - If core official evidence is missing and portal downloads were authorized upfront, read `references/portal-downloads.md`, download only the applicable files, and verify each artifact before relying on it.
   - If Zerodha transactions are in scope and the relevant broker files are missing, read `references/zerodha-console.md`, use the inferred income FY/Tax Year for report filters, and retrieve only the necessary reports within the authorized scope.
   - Read `references/reconciliation.md` for capital gains, PTI, Table F, other-source timing, or third-party mismatches.

3. **Review schedule selection.**
   - Read `references/schedule-selection.md` and build the fact-to-schedule map before changing selection.
   - Map every selected schedule to a confirmed fact, income source, tax credit, disclosure, mandatory requirement, or dependency.
   - Inspect imported/entered contents and downstream dependencies before removal.
   - Under the upfront authorization, remove only empty, factually inapplicable, nonmandatory, nondependent schedules. Clear stale source data correctly before removal.
   - Remove all authorized empty candidates in one pass, then recheck and report retained and removed schedules. Do not stop for another confirmation unless the schedule is populated, ambiguous, or fact-dependent.

4. **Reconcile source schedules before editing.**
   - General/BS/P&L/BP: filing answers, business codes, refund bank, no-books disclosures, receipts, 44ADA, and audit answers.
   - CG/112A: consideration, cost, transfer expenditure, holding classification, set-off, and Table F.
   - OS/PTI/EI: dividends and timing, interest, taxable PTI, exempt PTI, section 56 items, and TDS.
   - Tax Paid: challans, TDS/TCS, credit claimed this year, corresponding receipts/head, and carry-forward credit.

5. **Handle securities expenses narrowly.**
   - Exclude STT from section 48 deductions.
   - Include sale-linked DP charges and non-STT transaction charges only once when supported.
   - Exclude demat AMC, delayed-payment interest, maintenance/custody, penalties, and unrelated debits unless facts and authority establish a direct transfer nexus.
   - Allocate verified expenses by transaction date, symbol/ISIN, holding period, and sale value; document unresolved aliases.

6. **Keep dependencies synchronized.**
   - After CG/112A changes, recheck CG, CYLA, BFLA, SI, Part B-TI, Part B-TTI, and Table F.
   - After PTI changes, explicitly recheck Schedule OS taxable PTI, Schedule EI exempt PTI, Tax Paid/TDS, CYLA/BFLA, Part B-TI, and TTI. Do not assume the portal propagated values.
   - Recalculate tax and interest and compare with the baseline JSON and independent arithmetic.

7. **Preview and validate within scope.**
   - Review General, BS/no-books item 6, P&L, BP, CG, 112A, OS, PTI, EI, CYLA/BFLA/CFL, SI, VI-A, FA/FSI/TR, Tax Paid, TI, TTI, and Verification.
   - Correct supported validation errors without re-asking when covered by the upfront authorization.
   - Online, distinguish “all schedules confirmed” from “final validation passed.” If final validation requires ticking the declaration, stop at Verification unless signing was separately authorized.

8. **Report accurately.**
   - State the surface used, exact supported changes, retained/removed schedules, reconciled totals, payable/refund, validation level actually reached, unresolved facts, warnings, and gated actions not taken.
   - Mask identifiers and avoid unnecessary sensitive values.

## Safety boundaries

- Do not infer that every broker debit is deductible or that an imported/validated value is correct.
- Do not overwrite a schedule total without tracing its components and downstream effects.
- Do not use zero merely to silence a warning. No-books debtors, creditors, stock, and cash require factual support.
- Do not treat “Proceed to verification” or “Pay Later” as payment or submission, but obtain upfront permission for them and report their effect.
- Do not tick a declaration, sign, pay, upload, e-verify, or submit under a blanket editing authorization.

## Resources

- `references/intake.md`: mandatory consolidated intake and authorization matrix.
- `references/tax-year-selection.md`: India-date inference for AY/FY, the 2026 Tax Year transition, and confirmation rules.
- `references/portal-workflow.md`: Chrome workflow, portal state, recalculation, and stopping points.
- `references/portal-downloads.md`: conditional evidence set, live portal routes, user-only gates, and artifact verification.
- `references/schedule-selection.md`: fact-to-schedule matrix, one-pass cleanup, and high-risk negative facts.
- `references/zerodha-console.md`: Chrome login handoff, Tax P&L/funds statement routes, conditional reports, and verification.
- `references/reconciliation.md`: schedule mappings, PTI/OS flow, dividend timing, expense rules, and Table F.
- `scripts/audit_itr3_json.py`: extract and compare high-value ITR-3 JSON fields without printing personal identifiers.
