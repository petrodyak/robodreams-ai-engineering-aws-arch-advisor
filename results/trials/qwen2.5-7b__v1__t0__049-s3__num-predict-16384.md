# Run `qwen2.5-7b__v1__t0`

Generated from the JSONL run file by `src/extract/report_md.py`; do not edit.

- Model: `qwen2.5:7b`
- Prompt version: `v1`
- Sampling: `t0` (temperature 0.0, top_p None)
- Documents: 1

## Summary

| # | Document | Group | Status | Calls | Latency, s | In tokens | Out tokens | Quota table | Endpoints | Quotas |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [049-amazon-simple-storage-service.pdf](#049-amazon-simple-storage-servicepdf) | edge | failed | 1 | 504.6 | 13,714 | 16,384 | — | — | — |

## Documents

### 049-amazon-simple-storage-service.pdf

- Status: **failed**, 1 call(s), 504.6 s, in 13,714 / out 16,384 tokens

#### Error

```text
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 1886 column 7
--- no repair call
```
