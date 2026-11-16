# HW 2 — RAG over AWS Prescriptive Guidance and Well-Architected documents

This report is written in step 20. Until then it holds only the sections that other steps need.

## Testset

The testset is `evals/testset.jsonl`. Each item has an `id` made of a short word for its kind and a
number. The number counts the items within one kind. A short word rather than one letter keeps an id
readable in a results table without looking up the kind.

| Prefix | `kind` | What the item checks | Items |
|---|---|---|---|
| `one` | `single` | The answer sits in one place in one document. | one01–one10 |
| `many` | `multi` | The answer combines two documents, and both must be cited. | many01–many04 |
| `sim` | `similar` | A similar best practice from another pillar is nearby. The trap is to answer from the neighbour. | sim01–sim03 |
| `old` | `outdated` | The answer changed between the archived July 2020 Well-Architected Framework (`wa-framework-old`) and the current edition. The trap is the outdated text; the expected answer is the current one. | old01–old03 |
| `none` | `no_answer` | The corpus does not hold the answer; the system must say so. Added in step 19. | none01–none04 |

The `one`, `many`, `sim` and `old` items are answerable. Only these carry `relevant_chunk_ids` and
enter the retrieval eval (step 17).
