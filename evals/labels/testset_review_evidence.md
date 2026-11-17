# Testset review — evidence for the Edit items (step 19)

Answers to the Your edits notes of `testset_review.md`: for each fact of the expected answer, the
sentence of a labelled chunk that states it. The review sheet showed only one chunk per item, so
facts from the other labelled chunks were not visible there.

## one04 — When should I use the ALL distribution style for an Amazon Redshift table?

- **ALL for a small join table (< 1 GB)** — `pg-redshift-tables#0002`

  > …- If the table used in the join condition is small (less than 1 GB), then consider the distribution style ALL.…

---

## one08 — Desired outcome and anti-patterns of SEC08-BP02

- **encrypt private data by default** — `wa-security#0209`

  > …Desired outcome: You have mechanisms that encrypt private data by default when at rest.…

- **inventory of unencrypted data** — `wa-security#0209`

  > …You maintain an inventory of unencrypted data and understand the controls that are in place to protect it.…

- **anti-patterns** — `wa-security#0209`

  > …Common anti-patterns: • Not using encrypt-by-default configurations.…

Your expected answer matches the source word for word: it will replace the current one.

---

## many01 — Iceberg maintenance in Athena and S3 Tables

- **OPTIMIZE … REWRITE DATA** — `athena-iceberg-optimize#0000`

  > …OPTIMIZE The OPTIMIZE table REWRITE DATA compaction action rewrites data files into a more optimized layout based on their size and number of associated delete files.…

- **VACUUM** — `athena-iceberg-optimize#0000`

  > …To address these challenges, Athena supports manual compaction and vacuum operators to optimize table structure.…

- **orphan files** — `athena-iceberg-optimize#0000`

  > …OPTIMIZE iceberg_table REWRITE DATA USING BIN_PACK WHERE category = 'c1' VACUUM VACUUM performs snapshot expiration and orphan file removal.…

- **enabled by default for all tables** — `s3-tables-maintenance#0000`

  > …The following options are enabled by default for all tables in table buckets.…

- **compaction, 512 MB default** — `s3-tables-maintenance#0000`

  > …Compaction is enabled by default for all tables, with a default target file size of 512MB, or a custom value you specify between 64MB to 512MB.…

- **snapshot management** — `s3-tables#0001`

  > …Automated table optimization To optimize your tables for querying, S3 continuously performs automatic maintenance operations, such as compaction, snapshot management, and unreferenced file removal.…

- **unreferenced file removal** — `s3-tables#0001`

  > …Automated table optimization To optimize your tables for querying, S3 continuously performs automatic maintenance operations, such as compaction, snapshot management, and unreferenced file removal.…

Proposed fix: add `s3-tables-maintenance#0000` to the labelled chunks (the only chunk that states the 512 MB default and 'enabled by default'); both expected sources get section `""` (the Athena page and the S3 Tables maintenance page have no heading above the passage, so the section is the whole document).

---

## many02 — Data mesh design goals and AWS options

- **data as a product** — `wa-analytics-lens#0174`

  > …esign The following are data mesh design goals: • Data as a product: Each organizational domain owns their data end-to-end.…

- **federated data governance** — `wa-analytics-lens#0174`

  > …• Federated data governance: Data governance helps ensure that data is secure, accurate, and the right personas have access to the right data.…

- **common access** — `wa-analytics-lens#0174`

  > …• Common access: Data must be easily consumable by subject matter experts, such as data analysts and data scientists, and by purpose-built analytics and machine learning (ML) services.…

- **Amazon DataZone, fully managed** — `pg-data-mesh-aws-offerings#0001`

  > …mazon DataZone If you want to use a fully managed service, consider using Amazon DataZone to implement data mesh for your organization.…

- **data.all** — `pg-data-mesh-aws-offerings#0002`

  > …ata.all If you understand open source and want to build and manage your own solution, consider using open source frameworks such as data.all.…

- **Lake Formation** — `pg-data-mesh-aws-offerings#0002`

  > …AWS Lake Formation If you want to build a custom data mesh solution from the ground up and manage it, consider using AWS Lake Formation.…

---

## many03 — Redshift tables and Spectrum

- **DISTKEY collocation** — `pg-redshift-tables#0002`

  > …For example, by selecting a DISTKEY, you can distribute the fact table and one-dimension table on their common columns.…

- **no skew** — `pg-redshift-tables#0002`

  > …- Make sure there is no skewness on the column where the distribution key is created.…

- **ALL under 1 GB** — `pg-redshift-tables#0002`

  > …- If the table used in the join condition is small (less than 1 GB), then consider the distribution style ALL.…

- **Parquet / ORC** — `pg-redshift-spectrum#0000`

  > …To improve performance, use columnar encoded files such as ORC or Parquet, and use CSV format only for very small dimension tables.…

- **partition pruning** — `pg-redshift-spectrum#0000`

  > …- Use prefix-based partitioning to take advantage of partition pruning.…

- **predicate pushdown** — `pg-redshift-spectrum#0001`

  > …redicate pushdown in Redshift Spectrum Using predicate pushdown avoids consuming resources in the Amazon Redshift cluster.…

---

## many04 — Glue: parallelism and reading less data

- **RDD partitions** — `pg-glue-parallelize-tasks#0000`

  > …To achieve the best performance, you need to understand how the number of RDD partitions is determined and how that number is optimized.…

- **idle executors (CPU load)** — `pg-glue-parallelize-tasks#0000`

  > …CloudWatch metrics Check the CPU Load and Memory Utilization.…

- **Spark UI** — `pg-glue-parallelize-tasks#0000`

  > …If you do not have enough parallelism, the following symptoms will be recorded in CloudWatch metrics and the Spark UI.…

- **columnar Parquet / ORC** — `pg-glue-reduce-data-scan#0003`

  > …File format – Use a columnar format.…

- **push_down_predicate** — `pg-glue-reduce-data-scan#0005`

  > …ou can then restrict the amount of data scan by using partition pruning as follows:For AWS Glue DynamicFrame, set push_down_predicate (or catalogPartitionPredicate).dyf = Glue_context.create_dynamic_frame.from_catalog( database=src_database_name, table_name=src_table_name, push_down_predicate = "year='2023' and month ='03'", ) For Spark DataFrame, set a fixed path to prun…

Proposed fix: add `pg-glue-reduce-data-scan#0003` (File format – Use a columnar format) to the labelled chunks.

---
