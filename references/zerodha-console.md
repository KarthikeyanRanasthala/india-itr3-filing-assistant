# Zerodha Console evidence retrieval

Use this when Zerodha transactions are in scope and the required broker reports are absent or stale.

## Login handoff

1. Use authenticated browser control and open only `https://console.zerodha.com/`; in Codex, prefer Chrome control.
2. Immediately ask the user to log in. Leave the login page visible and pause Console navigation until the user confirms completion.
3. Never request, read, type, or handle the user ID, PIN, password, OTP, TOTP, or other authentication factor.
4. After confirmation, inspect the visible state and use the income FY or Tax Year established by `tax-year-selection.md`; Zerodha report filters use **Financial year**, not Assessment Year.

If the login session expires or a new authentication gate appears, stop in place and ask the user to complete it rather than navigating away.

On a resumed turn, reclaim the existing Console tab and inspect its URL/title and visible login state before opening a new tab. If authenticated browser control is unavailable, keep the signed-in tab intact and report that limitation; do not use blind coordinate entry or claim that a report was downloaded merely because its page was opened.

After login, prefer the direct report routes below when the normal menu path is slow or ambiguous. Confirm the page title and visible account state before using any controls:

- Tax P&L: `https://console.zerodha.com/reports/taxpnl`
- Funds statement: `https://console.zerodha.com/funds/statement`

## Necessary reports

### Tax P&L / capital-gains statement

1. Reports → **Tax P&L**, or use the direct route above.
2. Select the relevant **Financial year**. As observed in July 2026, the page defaults to the ongoing FY, not the most recently completed FY; never accept the default without checking it.
3. Select the full applicable quarter range and use the arrow action to load the report. Selecting a completed FY may automatically expand the selectors to Q1–Q4, but verify both ends rather than assuming it did.
4. Review the displayed segment tabs and coverage. The live page may show **Equity**, **F&O**, **Commodity**, and **Mutual funds**.
5. Choose **Download report**. Treat this as the current label; older help text may describe **Download Tax P&L report for all segment**.

When using browser automation, arm the browser's download event before clicking **Download report**, then await that event. Clicking first can be treated as a blocked navigation and land on `ERR_BLOCKED_BY_CLIENT`. If that happens, go Back once, rebuild the report, arm the download event, and click once. Do not repeatedly click the control.

The observed filename pattern is `taxpnl-<client-id>-YYYY_YYYY-Q1-Q4.xlsx`. Mask the client identifier in logs and handoffs. A valid FY workbook can contain separate sheets for trade-wise exits, equity/non-equity, mutual funds, F&O, currency, commodity, other debits and credits, opening/closing open positions, equity dividends, and ledger balances. Confirm the report period from workbook content, not only from the filename.

This is the primary Zerodha capital-gains and trading-tax report. It includes trade-wise charges, but Zerodha warns that trade-wise charge totals can differ from the summary where a trade was entered but not exited in the same FY. Reconcile rather than forcing equality.

### Funds statement / ledger

1. Funds → **Statement**, or use the direct route above.
2. Inspect the defaults. As observed in July 2026, **Category** defaults to **All segments** and **Date range** defaults to the most recent seven days. Replace the range explicitly; never treat it as an FY default.
3. Use **All segments** unless the evidence need is intentionally segment-specific. Set the full income-period date range, ordinarily 1 April through 31 March, and verify the rendered start and end dates before loading.
4. Use the arrow action to load the statement. The page can show opening and closing balances plus **Report's empty** when the chosen interval has no entries; that is not evidence for a different interval.
5. After a populated report loads, choose its XLSX or CSV download action. Arm and await the browser download event before clicking, then verify the artifact as below.

Use the funds statement to reconcile credits/debits and charges not shown in contract notes, including DP charges. Do not treat every debit as deductible.

### Conditional supporting reports

- **Tradebook:** Reports → Tradebook; select segment and date range, load, then download XLSX or CSV. Use when trade-level matching, external trades, transfers, corporate actions, or a Tax P&L discrepancy requires it. Zerodha states that a Tradebook download is limited to a 365-day period.
- **Contract notes:** download only for unresolved execution, brokerage, tax, or levy details on specific trade dates. DP charges are not shown there; use the funds statement.
- Do not download holdings, margin statements, invoices, or every contract note unless a confirmed reconciliation need exists.

## Known reconciliation cautions

- Treat the Tax P&L as broker evidence, not final tax classification. Recheck transferred-in/out securities, missing acquisition details, gifts, buybacks, international ETFs, debt/non-equity instruments, corporate-action FMV adjustments, and cancelled dividends when applicable.
- Reconcile dividends with AIS and bank evidence.
- Classify ledger debits line by line under `reconciliation.md`; exclude STT from section 48 deductions and avoid duplicating trade-wise charges.

## Download verification

Snapshot the download directory before each action, wait for completion, identify the new artifact by directory diff and modification time, require nonzero size, and open/parse the workbook or CSV before relying on it. Confirm the FY, date range, segment coverage, and report type from content. Preserve originals and mask client identifiers in reports.

Do not regard a visible report, a changed balance card, or a filename alone as a completed download. Record whether each requested artifact was actually downloaded and parsed; distinguish a verified Tax P&L from a Funds Statement that was only opened or viewed.

## Primary Zerodha sources

- Tax P&L download: https://support.zerodha.com/category/console/reports/taxation/articles/i-need-a-profit-and-loss-report-for-a-tax-audit-where-can-i-get-this-from
- Funds statement download: https://support.zerodha.com/category/console/ledger/articles/where-can-i-see-a-statement-of-all-my-transactions-with-zerodha
- Tax-report cautions: https://support.zerodha.com/category/console/reports/taxation/articles/things-to-consider-when-filing-taxes-using-zerodha-s-reports
- Tradebook download: https://support.zerodha.com/category/console/reports/other-queries/articles/where-can-i-see-all-the-trades-i-ve-taken-for-a-particular-period
