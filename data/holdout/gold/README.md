# Held-out Golden Set

The reference for the Held-out Set (contract item 20, step 12): one Service Document per
`data/holdout/manifest.csv` row with `gold=1`, five of the ten held-out documents — the five
lightest `medium` ones. Same format as `data/gold/` (`ServiceDocument`, schema version 1,
without the computed `endpoint_type`).

## Procedure: model-assisted, human-verified — with grounding

1. **Draft.** `python -m scripts.make_gold_drafts --set holdout` copied the answer of run
   **`claude__v2__t0__holdout__gold__val2`** (claude-haiku-4-5, prompt v2, temperature 0,
   validation "2"; 25.10.2026, 5/5 `ok` on the first answer, $0.17). Unlike the step 5 drafts,
   every drafted row had already passed grounding (ADR-0005): each hostname is printed in an
   endpoints table of the chapter, each quota name in a Standard Quota Table, and the format
   follows the printed header.
2. **Narrow.** `python -m scripts.check_gold --set holdout` — endpoints and quota names against
   the text: nothing flagged.
3. **Verify by hand against the PDF** (Petro, 25.10): the fields grounding does not see —
   missing rows, `region_name`, `default`, `adjustable`, `description`, `quota_table_format`.
   No corrections were needed; the five files are the drafts byte for byte.

**The drafting model has an advantage** — the same one as for `data/gold/`: a Claude error the
check did not catch stays in the reference. The report states it next to the held-out numbers.

| File | Endpoint rows | Quota rows (format) | Checked |
|---|---|---|---|
| `027-amazon-eventbridge-scheduler.json` | 88 | 14 (`standard`) | ✅ |
| `028-amazon-fsx.json` | 52 | 28 (`standard`) | ✅ |
| `051-amazon-timestream.json` | 84 | 32 (`standard`) | ✅ |
| `068-aws-elastic-beanstalk.json` | 108 | 3 (`standard`) | ✅ |
| `073-aws-firewall-manager.json` | 58 | 28 (`standard`) | ✅ |
