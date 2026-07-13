# India AY, FY, and Tax Year selection

Use the current date in `Asia/Kolkata`. Infer a candidate; do not silently lock the return to it.

## Definitions and transition

- Under the Income-tax Act, 1961, an **Assessment Year (AY)** is the twelve months beginning on 1 April. Its **Previous Year**, ordinarily the income-earning Financial Year (FY), is the financial year immediately before that AY.
- Therefore FY `Y-1–Y` ordinarily maps to AY `Y–Y+1`. Example: FY 2025-26 maps to AY 2026-27.
- The Income Tax Department states that the Income-tax Act, 2025 uses **Tax Year** instead of Previous Year/Assessment Year for income from FY 2026-27 onward. Tax Year 2026-27 corresponds to FY 2026-27; do not relabel it AY 2027-28 when the applicable portal/form uses Tax Year.
- Earlier years remain governed through the transition. The portal may expose both the 1961 Act and 2025 Act routes; use the law and year label applicable to the income period.

## Date-based inference

For an ordinary filing of the most recently completed income year under the AY system:

1. Let `Y` be today's calendar year in India.
2. If today is on or after 1 April, infer FY `Y-1–Y` and AY `Y–Y+1`.
3. If today is before 1 April, infer FY `Y-2–Y-1` and AY `Y-1–Y`.

On 13 July 2026, this rule infers FY 2025-26 and AY 2026-27. FY 2026-27 is still in progress on that date and is Tax Year 2026-27 under the 2025 Act, not the ordinary completed-year ITR target.

## Confirmation rule

State the candidate and its basis in the consolidated intake: “Based on today's India date, I infer AY … for FY …; correct this if this is not the ordinary current filing.” Confirm it against the portal/utility selector and local evidence before editing or downloading year-filtered reports.

Do not rely on the date inference for a revised, belated, updated, historical, notice-driven, reassessment, block, or prior-year return. In those cases, infer from the acknowledgement, notice, draft, generated JSON, or explicit user request and ask only if evidence conflicts.

## Primary sources

- Income-tax Act, 1961, section 2(9): https://www.incometaxindia.gov.in/w/section-2-31
- Income-tax Act, 1961, section 3: https://www.incometaxindia.gov.in/w/section-3-61
- Income Tax Department, Objective and scope of the New Act: https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act
- Income Tax Department, transition-year ITR FAQs: https://www.incometax.gov.in/iec/foportal/node/11724
