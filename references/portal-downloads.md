# Official portal evidence downloads

Use this only after login and when the user's upfront scope authorizes downloading missing official evidence. Prefer the smallest conditional set. Downloading writes files externally but is reversible; never handle credentials, OTP, Aadhaar authentication, or CAPTCHA.

## What is necessary

- **Prefilled JSON:** retrieve when preparing or reconciling the target return unless an already verified current copy exists.
- **AIS/TIS:** retrieve the smallest format set needed. Prefer TIS PDF for a compact category summary and AIS PDF for readable transaction detail. Add AIS JSON only when structured transaction-level reconciliation materially improves accuracy.
- **Form 26AS:** retrieve when TDS/TCS, claimed tax credit, or a mismatch needs confirmation; do not download it solely to duplicate an already reconciled current statement.
- **Challan receipts:** retrieve only for target-year payments being claimed or investigated.
- **AIS JSON:** its CAPTCHA is user-only. When JSON is needed, open its CAPTCHA while already on the AIS page, leave the dialog open, and immediately ask the user to complete it before navigating to any further documents.
- **Immediately preceding filed-return JSON:** download only when brought-forward losses, regime/Form 10-IEA history, residency, opening facts, or a revised-return comparison can affect the current return.
- **Filed forms:** inspect and download only an applicable form, such as Form 10-IEA. Do not download every filed form.
- **Current draft/upload JSON:** use only when the portal exposes a safe download action. Do not advance, Continue, Save, or alter schedule selection merely to obtain it.
- Broker reports, Form 64B, contract notes, and other third-party evidence must be obtained from their source systems or existing local files.

## Live routes and behavior

Portal labels can change. Use semantic names and a fresh snapshot after every navigation.

### Pre-filled JSON

1. e-File → Income Tax Returns → **Download Pre-Filled Data**.
2. Select the target AY, for example `2026-27 (Current A.Y.)`, then choose **Download**.
3. Expect a name similar to `<PAN>-Prefill-<AY>-<timestamp>.json`.
4. Parse the file as JSON and confirm that its content and AY match the intended return. Do not infer relevance from the filename alone.

The portal warns that profile changes can take about 30 minutes to appear in an updated prefill. Importing refreshed prefill can require a fresh filing; it may not update an existing saved draft.

### AIS and TIS

1. Choose **AIS** in the e-Filing navigation. This opens the Compliance Portal at `ais.insight.gov.in` in another tab.
2. Choose **Download AIS/TIS (F.Y. YYYY-YY)**.
3. The modal offers **Annual Information Statement (AIS) - PDF**, **AIS - JSON (for AIS Utility)**, and **Taxpayer Information Summary (TIS) - PDF**. Select by visible label, not button position.
4. AIS and TIS PDFs can take several seconds to appear. When AIS JSON is needed, choose its download action while this page is open. Its CAPTCHA dialog is a user-only gate: do not read, solve, type, or submit it.
5. Leave the CAPTCHA dialog visible and immediately prompt the user to complete and submit it. Pause browser navigation until the user confirms completion, then verify the JSON download and continue with the remaining document routes.

The PDF password instruction is lowercase PAN followed by DOB in `ddmmyyyy`, without spaces. Never compute, print, log, or repeat the actual password.

If parsing requires a password, ask the user to unlock the document locally or provide an unlocked copy. Do not request, store, or type the PAN/DOB-derived password.

### Form 26AS

1. e-File → Income Tax Returns → **View Form 26AS, Income Tax Act 1961**. TRACES opens in another tab.
2. On the TRACES attention dialog, review the consent text; proceed only within the authorized evidence-download scope.
3. Choose **View Tax Credit (Form 26AS/Annual Tax Statement)**.
4. Select the target AY and **HTML**, then choose **View / Download**.
5. On the HTML statement, choose **Export as PDF**.

From AY 2023-24 onward, the portal states that Form 26AS contains only TDS/TCS data; use AIS for other information. If the text format is used, its password is DOB in `ddmmyyyy`; never expose it.

### Tax challan receipts

1. e-File → **e-Pay Tax**.
2. Select the Income-tax Act applicable to the AY; AY 2026-27 uses the Income-tax Act, 1961 route observed in the portal.
3. Open **Payment History** and wait for the asynchronous table to load.
4. Identify the row by AY, payment type, date, and amount. Open its Actions menu and choose **Download**.

Only challans generated and remitted through e-Filing appear in Payment History. Download the rows supporting the target return; do not collect unrelated AYs. Never choose New Payment or any payment action during evidence retrieval.

### Prior filed returns and forms

- e-File → Income Tax Returns → **View Filed Returns**. The latest filing card exposes **Download Form**, **Download Receipt**, and **Download JSON**. Select the immediately preceding relevant AY by its heading and download only the needed artifact.
- e-File → Income Tax Forms → **View Filed Forms**. Inspect for an applicable form and download only when it affects the target return.

## Artifact verification

For each download:

1. Snapshot the download directory before clicking.
2. When available, arm the browser download event before clicking. Click once, await completion, then compare directory contents and modification times. Portal downloads commonly require several seconds.
3. Confirm exactly which new file appeared. Account for browser duplicate suffixes; never overwrite or rename an original before verification.
4. Require a nonzero size. Check `%PDF-` for PDFs and parse JSON successfully. Then confirm the AY/FY and document type from the content where possible.
5. Classify the verified file in the evidence inventory. Mask PAN, CIN, acknowledgement numbers, bank references, and other identifiers in reports and examples.

If no file appears, reacquire the live locator and retry once only when the UI clearly shows the action did not fire. Do not repeatedly click a working download control.

## User-only gates and in-place handoff

Handle a CAPTCHA where it appears: keep that page and dialog visible, prompt the user immediately, and pause navigation until the user confirms completion. This avoids discarding the dialog or repeating the AIS navigation. Group other user-only gates when doing so does not lose useful page state. A user-only gate does not expand authority to payment, declaration/signing, upload, e-verification, or submission.
