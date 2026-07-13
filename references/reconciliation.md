# ITR-3 reconciliation reference

## Core equations

- `44ADA income = max(50% of eligible gross receipts, income declared by taxpayer)`.
- `Capital gains = consideration - acquisition/improvement cost - eligible transfer expenditure`.
- `Part B-TI total income = business/profession + net capital gains + house property + other sources - permitted deductions`.
- `Amount payable = aggregate tax and interest - taxes paid`.
- Each Table F category must equal its corresponding post-set-off BFLA amount.

## Evidence hierarchy and zeros

1. Use statutory statements and source transaction/challan records first.
2. Use AIS/prefill as a cross-check, not proof that every item is complete or correctly classified.
3. Use third-party computations and generated JSON as reconciliation baselines.
4. Treat blanks, missing keys, disabled fields, and omitted JSON objects as `unknown` unless another reliable source proves zero.
5. A generated JSON can contain informational fields that are excluded from its displayed total. Trace both the component and the form arithmetic before copying it online.

## PTI, other sources, exempt income, and TDS

- Reconcile each Form 64B/business-trust record by entity, head of income, section code, current-year income/loss, exempt component, and TDS.
- In Schedule PTI, enter taxable other-source PTI and exempt PTI separately.
- In Schedule OS, ensure taxable PTI is included in the portal field for income in the nature of pass-through income/loss. Do not assume Schedule PTI auto-populates Schedule OS.
- In Schedule EI, ensure only exempt PTI flows to the pass-through exempt line.
- Reconcile `taxable PTI in PTI = taxable PTI included in OS` and `exempt PTI in PTI = PTI shown in EI`.
- Trace section 56(2)(xii), return-of-capital, and other business-trust distributions independently. Do not silently include or exclude an unexplained amount merely because generated JSON arithmetic omits it.
- For related TDS, distinguish current-year TDS, credit claimed this year, corresponding gross receipt/head of income, and credit carried forward. Reconcile Tax Paid totals to TTI.

## Dividend timing

- Schedule OS quarterly dividend values must equal taxable dividend income after applicable reductions.
- Derive the five buckets from receipt/accrual evidence or the trusted baseline: up to 15 June; 16 June–15 September; 16 September–15 December; 16 December–15 March; 16–31 March.
- Enter the timing breakup before confirming Schedule OS; never distribute a difference merely to clear validation.

## Broker expense classification

| Item | Default treatment for investment capital gains |
|---|---|
| Brokerage related to acquisition/sale | Include once in acquisition cost or transfer expense |
| Exchange, SEBI, IPFT and associated GST | Include when transaction-linked; avoid duplication |
| DP charge triggered by sale/debit | Allocate to the relevant sale |
| STT | Exclude from section 48 deduction |
| Demat AMC/custody/maintenance | Exclude unless facts and authority establish a direct transfer nexus |
| Delayed-payment interest | Exclude from transfer expense |
| Penalties, margin charges, payment gateway fees | Exclude unless independently supported and directly connected |

When a broker's “Other debits” sheet mixes categories, classify every line instead of deducting the total.

## Allocation method

1. Parse each realized transaction: asset, ISIN/symbol, acquisition date, exit date, holding period, sale value, gain/loss, and transaction charges.
2. Match DP ledger entries by exit date and symbol. Resolve renamed symbols using ISIN or documented aliases.
3. If one DP charge relates to both ST and LT lots of the same asset/date, allocate by sale value unless a more precise broker allocation exists.
4. Aggregate ST and LT eligible expenses separately and round only at the form's required precision.
5. Reconcile `ST expense + LT expense = total eligible expense`.

## Table F method

1. Start from realized transactions grouped by the statutory date buckets:
   - up to 15 June;
   - 16 June–15 September;
   - 16 September–15 December;
   - 16 December–15 March;
   - 16–31 March.
2. Apply the same current-year loss set-off presentation used by Schedule CG/CYLA.
3. Reconcile each rate category to Schedule BFLA.
4. If the utility previously collapsed later losses into an earlier positive bucket, preserve that demonstrated set-off pattern while applying the verified adjustment; document the derivation.
5. Never distribute a difference proportionally without evidence.

## Preview checklist

- General: AY, status, residence, new/old regime choice, filing section/due date, audit/books answers, only relevant nature codes, intended refund bank.
- No books: confirm sundry debtors, creditors, stock-in-trade, and physical cash as of 31 March.
- P&L/BP: profession code, receipts by mode, 44ADA amount, zero speculative/specified business unless supported.
- CG/112A: expense totals, losses, LTCG balance, Table F.
- OS/PTI/EI: taxable PTI included in OS, exempt PTI included in EI, dividend timing, interest, section 56 components, and related TDS.
- VI-A: consistent with the chosen regime.
- FA/FSI/TR: empty only when the taxpayer confirms no foreign assets/income/relief.
- TI/TTI: arithmetic, special-rate income, cess, interest, taxes paid, payable/refund.
- Verification: name, capacity, PAN mask, place spelling, and date.

## Cross-schedule invariants

- `Schedule OS total = interest + dividends + taxable PTI + other included components - permitted deductions`, following the form's presentation. Do not classify all taxable PTI as interest; trace it to the applicable pass-through/head field.
- `Part B-TI other sources = final Schedule OS income`, including taxable PTI.
- `Part B-TI total income = business + post-set-off capital gains + house property + final other sources - allowed deductions`.
- Schedule SI must show the applicable special-rate income and statutory minimum-threshold adjustment; reconcile its tax to TTI.
- `TTI taxes paid = claimed advance/self-assessment tax + claimed TDS + claimed TCS`.
- `TTI payable/refund = aggregate liability - taxes paid`, subject to form rounding.
