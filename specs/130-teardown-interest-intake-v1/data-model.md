# Data model — teardown interest intake V1

| Field | Required now | Purpose | Open control |
|---|---|---|---|
| name | no | response context | confirm minimization |
| email | only if response path approved | response channel | provider/retention review |
| offer_url | no | teardown context | public URL only; no confidential upload |
| goal | no | request context | define retention and access |

## Flow states

`idle → validating → local-success` for the non-sending prototype. A future
adapter may add `submitting`, `submitted`, `error`, and `retrying` only after
privacy and routing approval.

## Prohibited data

No credentials, sensitive personal data, confidential client documents,
unpublished screenshots, or third-party brand material. No upload field in V1.
