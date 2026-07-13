# ITR-3 schedule selection and cleanup

Use this after the factual intake and evidence inventory. Treat it as a decision aid, not a substitute for the notified form, current validation rules, or a dependency shown by the portal/utility.

## Cleanup method

1. Build a fact-to-schedule map before changing selection.
2. Classify every selected schedule as `required by fact`, `required dependency`, `mandatory core`, `populated but unresolved`, or `empty candidate for removal`.
3. Inspect the schedule and its source answers. Clear stale imported/source data before deselecting it.
4. Remove all authorized empty candidates in one pass; do not ask schedule-by-schedule.
5. Re-open schedule selection and record the final retained and removed lists. Recalculate and reconfirm any invalidated dependent schedules.

Never remove a populated or ambiguous schedule merely because the taxpayer does not recognize its name. Never remove a computational schedule that the portal or utility requires as a dependency.

## Common fact-to-schedule rules

| Fact | Usually retain or enable | Candidate for removal when empty and no dependency |
|---|---|---|
| Business or professional income | Part A General, BS, P&L, BP and applicable business/depreciation schedules | Inapplicable depreciation, audit, manufacturing, trading, ICDS, ESR or other business schedules |
| Presumptive profession under 44ADA with no regular books | P&L 44ADA/no-books disclosures, BP, mandatory core schedules | Regular-books and depreciation schedules unless another activity requires them |
| Salary or pension | Schedule S | Schedule S when no salary/pension fact exists |
| House-property income or loss | Schedule HP | Schedule HP when no property income/loss exists |
| Capital-asset sales | Schedule CG and rate/asset-specific schedules such as 112A, 115AD or VDA when applicable | Asset/rate schedules unsupported by transactions |
| Other-source income | Schedule OS | Schedule OS only when no other-source item or dependency exists |
| Pass-through income from Form 64B/business trust/AIF | PTI plus the receiving head schedules; EI for exempt PTI | PTI when there is no pass-through evidence |
| Partner in a firm | Schedule IF and related exempt/remuneration/interest treatment | **Schedule IF when the taxpayer confirms they were not a partner and it is empty** |
| Exempt income | Schedule EI when reportable exempt income exists | EI only when there is no reportable exempt item or dependency |
| Current-year or brought-forward losses | CYLA, BFLA, CFL and relevant source schedules | Do not manually remove portal-generated set-off schedules while a loss exists |
| Special-rate income | Schedule SI and its source schedule | SI when no special-rate income exists and the portal does not require it |
| TDS/TCS or tax payments | Applicable TDS/TCS/IT schedules | Empty tax-credit schedules unsupported by evidence |
| Deductions permitted under the selected regime | Schedule VI-A and applicable deduction details | Unsupported deduction schedules; do not remove VI-A solely because the new regime is selected |
| Foreign-source income, foreign tax or foreign assets | FSI, TR and/or FA as applicable | FSI/TR/FA only after residence and foreign-fact answers establish inapplicability |
| Partner/spouse income clubbing | Schedule SPI and receiving head | SPI when no clubbing fact exists |
| Portuguese Civil Code community-property apportionment | Schedule 5A | Schedule 5A when the taxpayer is not governed by that system |
| Total income above the applicable asset-disclosure threshold | Schedule AL | AL only after confirming the current threshold and total-income test |

## High-risk negative facts to obtain once

Ask once, preferably as a correction-oriented statement, whether any exception exists for partnership in a firm, directorship/unlisted shares, foreign assets/accounts/income/signing authority, foreign tax relief, Portuguese community property, VDA/crypto, brought-forward losses, pass-through income, agricultural/exempt income, and total income triggering Schedule AL. Do not ask each as a separate yes/no turn.

Absence from AIS, prefill, broker evidence, or generated JSON does not prove a negative fact. Once the taxpayer clearly confirms a negative fact, store it in the session ledger and do not ask again.

## Current-source check

Before relying on exact schedule names, thresholds, or validation dependencies, check the target AY's notified ITR-3, schema and validation document on the official downloads page:

- https://www.incometax.gov.in/iec/foportal/downloads/income-tax-returns
- https://www.incometax.gov.in/iec/foportal/help/identification-and-generation-of-applicable-itr-individual

For AY 2026-27, the official validation rules and notified form were released in June/April 2026. Recheck newer versions before applying exact dependencies.
