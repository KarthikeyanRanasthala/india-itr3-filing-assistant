# Income Tax e-Filing portal workflow

Use this for online ITR-3 work at `https://www.incometax.gov.in/`.

## Login and browser control

- Use authenticated browser control that can access the user's existing login/session; in Codex, prefer Chrome control.
- Open the official site and immediately ask the user to log in before inspecting filing pages. While the user logs in, inventory local evidence read-only; after login, use the intake's structured-choice prompt round when available, followed by one consolidated factual message. Do not ask serial questions or interact with password, OTP, CAPTCHA, Aadhaar authentication, or other credentials.
- After the user confirms login, inspect the visible page state before acting. Keep the filing tab available for handoff.
- Use semantic roles/names and fresh page snapshots. After navigation, Save, Confirm, or a loading dialog, wait for the UI to settle and reacquire locators.
- AIS and Form 26AS can open in separate Compliance Portal and TRACES tabs. Keep the e-Filing tab available and read `portal-downloads.md` before retrieving evidence.
- After a resumed turn, first reclaim the existing e-Filing/Compliance/TRACES tabs and confirm the visible login state. Do not reopen login or repeat intake if the session and conversation ledger are intact.
- If authenticated browser control becomes unavailable, preserve the tab and report the control limitation. Do not use blind coordinate clicks or brittle GUI scripting for tax entries, schedule removal, declaration, payment, or submission. A read-only fallback may verify a URL/title or downloaded artifact, but must not be represented as successful form operation.
- Before a browser action, identify the expected state transition and success evidence. After it, verify the new page/field/aggregate; do not infer success from a click alone.

## Evidence retrieval and draft safety

- Bundle evidence-download permission into the upfront routine scope. Do not interrupt for each PDF or JSON.
- Never solve or transcribe a CAPTCHA. When one appears for a needed download, leave the dialog visible, prompt the user immediately, and pause browser navigation until the user confirms completion. Do not group this prompt if doing so would discard the dialog or require navigating back.
- Do not enter **Resume Filing** merely to retrieve evidence. It can reopen at schedule selection, and the displayed selected-schedule state may differ from the saved draft. If retrieval would require Continue, Save, or schedule mutation, use the dedicated download routes or stop and report the limitation.
- Verify every downloaded artifact by directory diff, size, signature or JSON parsing, and AY/FY before treating it as evidence.
- When the browser-control capability exposes a download event, arm it before clicking the download control and await it. A download-like link may otherwise be treated as blocked navigation. Retry only after returning to the report and reacquiring the live control.

## Draft edits and recalculation

- The portal may autosave, invalidate downstream confirmations, or display stale computed totals until an input blur, Save, or page reload.
- After entering a numeric value, trigger the field's normal change/blur behavior, then verify both the field and its displayed aggregate. If direct fill updates the field but not the total, Save and re-open before concluding it failed.
- After every material source-schedule change, verify the saved item, the schedule total, the summary confirmation state, and downstream TI/TTI values.
- Expect a Confirm action to reveal schedule-level errors such as missing quarterly dividend data. Correct supported errors within the upfront authorization.

## Schedule cleanup

- Inspect contents and dependencies before deselection. A stale business code or imported amount must be cleared in its source schedule first.
- Under upfront schedule-cleanup authorization, remove empty, factually inapplicable schedules without asking again. Pause for populated or ambiguous schedules.
- Use `schedule-selection.md`, remove all clear candidates in one pass, and recheck the final retained schedule list and count. Do not ask “remove this schedule?” repeatedly after the user has authorized cleanup and confirmed the controlling negative facts.

## Online-specific reconciliation traps

- Schedule PTI may not automatically feed taxable PTI into Schedule OS. Re-open OS and verify the pass-through income/loss field and final other-source total.
- Exempt PTI must flow separately to Schedule EI.
- Schedule OS confirmation can require the five-period dividend breakup even when the dividend total is already present.
- CG/112A changes can affect CYLA, BFLA, SI, Table F, TI, and TTI; confirm the post-set-off amount, not the pre-set-off gain/loss.
- Tax Paid tables distinguish deducted tax from tax credit claimed. Verify the claimed total and corresponding receipt/head rather than relying only on visible TDS rows.
- No-books BS zeros can trigger a defective-return warning. Do not enter zero solely because generated JSON omitted the field.

## Stopping points and terminology

- **Schedules confirmed:** all retained schedules show Confirmed and their schedule-level checks pass.
- **Verification page reached:** the portal shows Preview and Submit Your Return / declaration details. This is not proof that final validation passed.
- **Final validation:** may require the declaration checkbox and verification place. Ticking the declaration is signing and needs separate action-time confirmation.
- **Pay Later:** may be selected only when included in the upfront scope, solely to reach Verification. It does not pay the tax; report the payable amount and warning.
- Never click Pay Now, tick the declaration, proceed past signing, e-verify, or submit without separate action-time confirmation.

At handoff, leave the tab on the agreed stopping page and report the exact state reached.
