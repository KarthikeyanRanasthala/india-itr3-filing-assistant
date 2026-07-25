# India ITR3 Filing Assistant

> **Archived:** This repository is no longer maintained. Use [India Income Tax Filing Skill](https://github.com/KarthikeyanRanasthala/india-income-tax-filing-skill), the actively maintained replacement for Indian individual ITR-1, ITR-2, ITR-3, and ITR-4 workflows.

A safety-first Agent Skill for reviewing, reconciling, and preparing India's ITR-3 return. It supports online e-Filing, the offline utility, broker evidence such as Zerodha Tax P&L, and files-only workflows.

## Install

```sh
npx skills add KarthikeyanRanasthala/india-income-tax-filing-skill
```

## What it does

- Reconciles AIS/prefill data, broker reports, Form 64B/PTI, tax payments, and generated ITR-3 JSON.
- Guides ITR-3 schedule selection, 44ADA, capital gains, other-source income, PTI, tax credits, validation, and verification-stage review.
- Protects sensitive information and requires action-time confirmation before payment, signing, e-verification, or submission.

## Best experience: Codex

The skill works with any Agent Skills-compatible host that can provide equivalent capabilities. Codex is recommended for the strongest end-to-end experience because it can use:

- **Chrome control** to work with an existing signed-in Income Tax portal or Zerodha Console session, observe visible state, and verify downloads.
- **Computer Use** to operate the offline utility when appropriate.
- **Structured prompts and spreadsheet tools** to collect authorization choices and inspect workbook or CSV evidence efficiently.

Other agents can use their browser, desktop, prompt, and spreadsheet equivalents. If safe authenticated browser or desktop control is unavailable, the skill falls back to read-only and files-only review rather than attempting unreliable automation.

## Safety boundaries

The skill never requests or handles passwords, OTPs, CAPTCHAs, PAN, Aadhaar, or full bank credentials. It does not pay tax, sign a declaration, upload, e-verify, or submit a return without separate confirmation immediately before that action.

Tax rules and portal behavior change. Verify current requirements against official Income Tax Department sources and consult a qualified tax professional where needed.
