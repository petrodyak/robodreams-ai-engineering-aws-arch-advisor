# Testset review (step 19)

Check each item against its source text below (the labelled chunk with the most key facts; the others are listed).
For each item tick **one** box and, if needed, write the change under **Your edits**:

- `[x] OK` — the question, the expected answer and the key facts are right as written;
- `[x] Edit` — write the corrected question / expected answer / key facts under Your edits;
- `[x] Reject` — the item goes (say why).

The spec asks you to **write the trap questions yourself** (`sim`, `old`): for those six, write
your own wording of the question under **Your question**. If the meaning stays the same, the
chunk labels you checked in step 17 stay. The four `none` items are new drafts: check that the
corpus really does not answer them.

24 items. Ids: `one` single, `many` multi, `sim` similar, `old` outdated, `none` no answer.

## one01 (single)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** What steps does the Reliability pillar recommend to make sure that all workload data that needs a backup is backed up?

**Expected answer:** Identify all data sources of the workload (databases, volumes, file systems, logging systems, object storage), classify them by criticality (RPO and RTO requirements), and create backups with AWS or third-party services such as AWS Backup, AWS Elastic Disaster Recovery or the services' native backup features. Data that can be reproduced from its sources does not need a backup.

**Key facts:** `Identify all data sources`, `criticality`, `AWS Backup`

**Expected sources:** wa-reliability: REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources

**Labelled chunks:** `wa-reliability#0186`, `wa-reliability#0188`, `wa-framework#0761`, `wa-reliability#0189`, `wa-reliability#0187`, `wa-framework#0763`

**Source text** (`wa-reliability#0188`, Reliability Pillar - AWS Well-Architected Framework > Failure management > Back up data > REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources > Implementation guidance, p. 163):

> REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources 1. Identify all data sources for the workload. Data can be stored on a number of resources such as databases, volumes, filesystems, logging systems, and object storage. Refer to the Resources section to find Related documents on different AWS services where data is stored, and the backup capability these services provide. 2. Classify data sources based on criticality. Different data sets will have different levels of criticality for a workload, and therefore different requirements for resiliency. For example, some data might be critical and require a RPO near zero, while other data might be less critical and can tolerate a higher RPO and some data loss. Similarly, different data sets might have different RTO requirements as well. 3. Use AWS or third-party services to create backups of the data. AWS Backup is a managed service that allows creating backups of various data sources on AWS. AWS Elastic Disaster Recovery handles automated sub-second data replication to an AWS Region. Most AWS services also have native capabilities to create backups. The AWS Marketplace has many solutio …

**Your edits:** 

---

## one02 (single)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** What are the default snapshot retention settings of snapshot management in Amazon S3 Tables?

**Expected answer:** MinimumSnapshots is 1 and MaximumSnapshotAge is 120 hours by default. Expired snapshots are removed, and objects referenced only by them become noncurrent and are deleted after the NoncurrentDays of the unreferenced file removal policy.

**Key facts:** `MinimumSnapshots`, `MaximumSnapshotAge`, `120 hours`

**Expected sources:** s3-tables-maintenance: Snapshot management

**Labelled chunks:** `s3-tables-maintenance#0004`

**Source text** (`s3-tables-maintenance#0004`, Amazon S3 User Guide: Maintenance for tables > Snapshot management, p. None):

> Snapshot management Snapshot management determines the number of active snapshots for your table. This is based on the MinimumSnapshots (1 by default) and MaximumSnapshotAge (120 hours by default). Snapshot management expires and removes table snapshots based on these configurations. When a snapshot expires, Amazon S3 marks any objects referenced only by that snapshot as noncurrent. These noncurrent objects are deleted after the number of days specified by the NoncurrentDays property in your unreferenced file removal policy. Note Deletes of noncurrent objects are permanent with no way to recover these objects. To view or recover objects that has been marked as noncurrent you must contact AWS Support. For information about contacting AWS Support, see Contact AWS or the AWS Support Documentation. Snapshot management determines the objects to delete from your table with references only to that table. References to these objects from outside the table will not prevent snapshot management from deleting them. Note Snapshot management does not support retention values that you configure as Apache Iceberg table properties in the metadata.json file or through an ALTER TABLE SET TBLPROPERTIE …

**Your edits:** 

---

## one03 (single)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** Which Apache Iceberg version does Amazon Athena support?

**Expected answer:** Athena supports Apache Iceberg version 1.4.2.

**Key facts:** `1.4.2`

**Expected sources:** athena-iceberg-query: Considerations and limitations

**Labelled chunks:** `athena-iceberg-query#0001`

**Source text** (`athena-iceberg-query#0001`, Amazon Athena User Guide: Query Apache Iceberg tables > Considerations and limitations, p. None):

> Considerations and limitations Athena support for Iceberg tables has the following considerations and limitations: - Iceberg version support – Athena supports Apache Iceberg version 1.4.2. - Tables registered with Lake Formation – Athena does not currently support DDL operations on Iceberg tables that are registered with Lake Formation. - Queries against information schema – When querying the information schema of Iceberg tables, Athena uses S3 metadata as the source of truth for column metadata. This means that column information is derived from the underlying S3 files rather than from the catalog metadata. This behavior differs from other table formats where catalog metadata might be the primary source for column information. - Tables with AWS Glue catalog only – Only Iceberg tables created against the AWS Glue catalog based on specifications defined by the open source glue catalog implementation are supported from Athena. - Table locking support by AWS Glue only – Unlike the open source Glue catalog implementation, which supports plug-in custom locking, Athena supports AWS Glue optimistic locking only. Using Athena to modify an Iceberg table with any other lock implementation wi …

**Your edits:** 

---

## one04 (single)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** When should I use the ALL distribution style for an Amazon Redshift table?

**Expected answer:** When the table used in the join condition is small, less than 1 GB.

**Key facts:** `ALL`, `1 GB`

**Expected sources:** pg-redshift-tables: Choose the right table distribution style

**Labelled chunks:** `pg-redshift-tables#0002`

**Source text** (`pg-redshift-tables#0002`, Query best practices for Amazon Redshift: Best practices for designing Amazon Redshift tables > Choose the right table distribution style, p. None):

> Choose the right table distribution style When you run a query, the query optimizer redistributes the rows to the compute nodes as needed to perform any joins and aggregations. The goal in selecting a table distribution style is to minimize the impact of the redistribution step by locating the data where it needs to be before you run the query. We recommend the following approach to choosing the right table distribution style: - Avoid broadcasting and redistribution in a query execution plan by collocating the rows within the same node. For example, by selecting a DISTKEY, you can distribute the fact table and one-dimension table on their common columns. Choose the largest dimension based on the size of the filtered dataset. Only the rows that are used in the join must be distributed, so consider the size of the dataset after filtering, not the size of the table. - Make sure there is no skewness on the column where the distribution key is created. Otherwise, one compute node could perform more heavy lifting than others. If you notice skewness, then consider changing the distribution key column. A column can be considered as a candidate for a distribution key if its values are unifo …

**Your edits:**

---

## one05 (single)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** How can an AWS Glue job read only the partitions it needs from the Data Catalog when it uses a DynamicFrame?

**Expected answer:** Use partition pruning: set push_down_predicate (or catalogPartitionPredicate) when creating the DynamicFrame from the catalog, for example year='2023' and month='03'.

**Key facts:** `push_down_predicate`, `catalogPartitionPredicate`

**Expected sources:** pg-glue-reduce-data-scan: Amazon S3

**Labelled chunks:** `pg-glue-reduce-data-scan#0005`

**Source text** (`pg-glue-reduce-data-scan#0005`, Best practices for performance tuning AWS Glue for Apache Spark jobs: Reduce the amount of data scan > Spark UI > Amazon S3, p. None):

> You can then restrict the amount of data scan by using partition pruning as follows:For AWS Glue DynamicFrame, set push_down_predicate (or catalogPartitionPredicate).dyf = Glue_context.create_dynamic_frame.from_catalog( database=src_database_name, table_name=src_table_name, push_down_predicate = "year='2023' and month ='03'", ) For Spark DataFrame, set a fixed path to prune partitions.df = spark.read.format("json").load("s3://<YourBucket>/year=2023/month=03/*/*.gz")For Spark SQL, you can set the where clause to prune partitions from the Data Catalog.df = spark.sql("SELECT * FROM <Table> WHERE year= '2023' and month = '03'")To partition by date when writing your data with AWS Glue, you set partitionKeys in DynamicFrame or partitionBy() in DataFrame with the date information in your columns as follows.DynamicFrameglue_context.write_dynamic_frame_from_options( frame= dyf, connection_type='s3',format='parquet' connection_options= { 'partitionKeys': ["year", "month", "day"], 'path': 's3://<YourBucket>/<Prefix>/' } ) DataFramedf.write.mode('append')\ .partitionBy('year','month','day')\ .parquet('s3://<YourBucket>/<Prefix>/') This can improve the performance of the consumers of your outpu …

**Your edits:** 

---

## one06 (single)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** Is Adaptive Query Execution enabled by default in AWS Glue, and how do I turn it on in AWS Glue 3.0?

**Expected answer:** It is enabled by default in AWS Glue 4.0. In AWS Glue 3.0 you enable it by setting spark.sql.adaptive.enabled=true.

**Key facts:** `spark.sql.adaptive.enabled`, `AWS Glue 4.0`

**Expected sources:** pg-glue-optimize-shuffles: Shuffle and broadcast hash joins and hints

**Labelled chunks:** `pg-glue-optimize-shuffles#0004`

**Source text** (`pg-glue-optimize-shuffles#0004`, Best practices for performance tuning AWS Glue for Apache Spark jobs: Optimize shuffles > Spark UI > Optimize the join > Shuffle and broadcast hash joins and hints, p. None):

> In AWS Glue 3.0, you can enable Adaptive Query Execution by setting spark.sql.adaptive.enabled=true. Adaptive Query Execution is enabled by default in AWS Glue 4.0. You can set additional parameters related to shuffles and broadcast hash joins: - spark.sql.adaptive.localShuffleReader.enabled - spark.sql.adaptive.autoBroadcastJoinThreshold For more information about related parameters, see Converting sort-merge join to broadcast join. In AWS Glue 3.0 and or later, you can use other join hints for shuffle to tune your behavior. -- Join Hints for shuffle sort merge join SELECT /*+ SHUFFLE_MERGE(t1) / FROM t1 INNER JOIN t2 ON t1.key = t2.key; SELECT /*+ MERGEJOIN(t2) / FROM t1 INNER JOIN t2 ON t1.key = t2.key; SELECT /*+ MERGE(t1) / FROM t1 INNER JOIN t2 ON t1.key = t2.key; -- Join Hints for shuffle hash join SELECT /*+ SHUFFLE_HASH(t1) / FROM t1 INNER JOIN t2 ON t1.key = t2.key; -- Join Hints for shuffle-and-replicate nested loop join SELECT /*+ SHUFFLE_REPLICATE_NL(t1) / FROM t1 INNER JOIN t2 ON t1.key = t2.key;

**Your edits:** 

---

## one07 (single)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** How can I tell from the Spark UI that an AWS Glue job suffers from data skew?

**Expected answer:** On the Stage tab, the Event Timeline shows tasks distributed unevenly or taking too long; the Summary Metrics page shows very biased values across the percentiles (for example a Max task duration far above the 75th percentile).

**Key facts:** `Event Timeline`, `Summary Metrics`

**Expected sources:** pg-glue-optimize-shuffles: Overcome data skew

**Labelled chunks:** `pg-glue-optimize-shuffles#0006`

**Source text** (`pg-glue-optimize-shuffles#0006`, Best practices for performance tuning AWS Glue for Apache Spark jobs: Optimize shuffles > Spark UI > Overcome data skew, p. None):

> Overcome data skew Data skew is one of the most common causes of a bottleneck for Spark jobs. It occurs when data isn't uniformly distributed across RDD partitions. This causes tasks for that partition to take much longer than others, delaying the overall processing time of the application. To identify data skew, assess the following metrics in the Spark UI: - On the Stage tab in the Spark UI, examine the Event Timeline page. You can see an uneven distribution of tasks in the following screenshot. Tasks that are distributed unevenly or are taking too long to run can indicate data skew. - Another important page is Summary Metrics, which shows statistics for Spark tasks. The following screenshot shows metrics with percentiles for Duration, GC Time, Spill (memory), Spill (disk), and so on.When the tasks are evenly distributed, you will see similar numbers in all the percentiles. When there is data skew, you will see very biased values in each percentile. In the example, task duration is less than 13 seconds in Min, 25th percentile, Median, and 75th percentile. While the Max task processed 100 times more data than the 75th percentile, its duration of 6.4 minutes is about 30 times longe …

**Your edits:** 

---

## one08 (single)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** What is the desired outcome of the Security pillar best practice on encryption at rest, and which anti-patterns does it name?

**Expected answer:** You have mechanisms that encrypt private data by default when at rest, and you keep an inventory of unencrypted data and the controls that protect it. Anti-patterns include not using encrypt-by-default configurations, overly permissive access to decryption keys and not monitoring the use of encryption.

**Key facts:** `encrypt private data by default`, `inventory of unencrypted data`, `decryption keys`

**Expected sources:** wa-security: SEC08-BP02 Enforce encryption at rest

**Labelled chunks:** `wa-security#0209`

**Source text** (`wa-security#0209`, Security Pillar - AWS Well-Architected Framework > Data protection > Protecting data at rest > SEC08-BP02 Enforce encryption at rest, p. 158):

> SEC08-BP02 Enforce encryption at rest Encrypt private data at rest to maintain confidentiality and provide an additional layer of protection against unintended data disclosure or exfiltration. Encryption protects data so that it cannot be read or accessed without first being decrypted. Inventory and control unencrypted data to mitigate risks associated with data exposure. Desired outcome: You have mechanisms that encrypt private data by default when at rest. These mechanisms help maintain the confidentiality of the data and provides an additional layer of protection against unintended data disclosure or exfiltration. You maintain an inventory of unencrypted data and understand the controls that are in place to protect it. Common anti-patterns: • Not using encrypt-by-default configurations. • Providing overly permissive access to decryption keys. • Not monitoring the use of encryption and decryption keys. • Storing data unencrypted. • Using the same encryption key for all data regardless of data usage, types, and classification. Level of risk exposed if this best practice is not established: High

**Your edits:**

---

## one09 (single)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** Who should own cost optimization in an organization, according to the Cost Optimization pillar?

**Expected answer:** A function such as a Cloud Business Office, a Cloud Center of Excellence or a FinOps team, which can be an individual or a team with people from finance, technology and business, responsible for establishing and maintaining cost awareness across the organization.

**Key facts:** `Cloud Business Office`, `Cloud Center of Excellence`, `FinOps`

**Expected sources:** wa-cost-optimization: COST01-BP01 Establish ownership of cost optimization

**Labelled chunks:** `wa-cost-optimization#0006`, `wa-cost-optimization#0007`

**Source text** (`wa-cost-optimization#0006`, Cost Optimization Pillar - AWS Well-Architected Framework > Practice Cloud Financial Management > COST01-BP01 Establish ownership of cost optimization, p. 13):

> COST01-BP01 Establish ownership of cost optimization Create a team (Cloud Business Office, Cloud Center of Excellence, or FinOps team) that is responsible for establishing and maintaining cost awareness across your organization. The owner of cost optimization can be an individual or a team (requires people from finance, technology, and business teams) that understands the entire organization and cloud finance. Level of risk exposed if this best practice is not established: High

**Your edits:** 

---

## one10 (single)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** What does the Generative AI Lens recommend to cut input token costs for prompt parts that repeat across requests?

**Expected answer:** Implement prompt caching on supported foundation models: frequently used prompt portions are cached, cached tokens are billed at a reduced rate, and latency drops because the cached sections are not recomputed.

**Key facts:** `prompt caching`, `reduced rate`

**Expected sources:** wa-genai-lens: GENCOST03-BP03 Implement prompt caching to reduce token costs

**Labelled chunks:** `wa-genai-lens#0276`

**Source text** (`wa-genai-lens#0276`, Generative AI Lens - AWS Well-Architected Framework > Cost optimization > Cost-aware prompting > GENCOST03-BP03 Implement prompt caching to reduce token costs, p. 228):

> GENCOST03-BP03 Implement prompt caching to reduce token costs Implement prompt caching for supported foundation models to reduce inference response latency and input token costs. This best practice helps organizations optimize costs by caching frequently used portions of prompts to avoid recomputation, while maintaining performance and reliability. Desired outcome: Reduce inference costs by caching commonly used prompt components and using cached tokens at a reduced rate. Benefits of establishing this best practice: • Control resource consumption parameters - Reduce token costs by reusing cached prompt components. • Optimize model and inference selection - Decrease latency by avoiding recomputation of cached prompt sections. Level of risk exposed if this best practice is not established: Medium Implementation guidance Prompt caching is an optional feature available on supported models in Amazon Bedrock that can reduce inference response latency and input token costs. By caching portions of your context, the model can use the cache to skip recomputation, allowing Bedrock to achieve cost savings through lower token rates. Prompt caching can help when you have workloads with long and  …

**Your edits:** 

---

## many01 (multi)

- [ ] OK   - [x] Edit   - [ ] Reject

**Q:** Which features keep Apache Iceberg tables efficient as small files and delete files accumulate, in Amazon Athena and in Amazon S3 Tables?

**Expected answer:** In Athena you run maintenance yourself: OPTIMIZE ... REWRITE DATA compacts data files and merges delete files, and VACUUM expires old snapshots and removes orphan files. S3 Tables runs maintenance automatically and enables it by default for every table: compaction (default target file size 512 MB) and snapshot management, with unreferenced file removal.

**Key facts:** `OPTIMIZE`, `VACUUM`, `compaction`, `snapshot management`

**Expected sources:** athena-iceberg-optimize: OPTIMIZE; s3-tables-maintenance: Compaction

**Labelled chunks:** `s3-tables#0001`, `athena-iceberg-optimize#0000`

**Source text** (`s3-tables#0001`, Amazon S3 User Guide: Working with Amazon S3 Tables and table buckets > Features of S3 Tables, p. None):

> Features of S3 Tables Purpose-built storage for tables S3 table buckets are specifically designed for tables. Table buckets provide higher transactions per second (TPS) and better query throughput compared to self-managed tables in S3 general purpose buckets. Table buckets deliver the same durability, availability, and scalability as other Amazon S3 bucket types. Built-in support for Apache Iceberg Tables in your table buckets are stored in Apache Iceberg format. You can query these tables using standard SQL in query engines that support Iceberg. Iceberg has a variety of features to optimize query performance, including schema evolution and partition evolution. With Iceberg, you can change how your data is organized so that it can evolve over time without requiring you to rewrite your queries or rebuild your data structures. Iceberg is designed to help ensure data consistency and reliability through its support for transactions. To help you correct issues or perform time travel queries, you can track how data changes over time and roll back to historical versions. Your table buckets support the Apache Iceberg Version 3 (V3) table format, including deletion vectors, row lineage, col …

**Your edits:**  Align the expected sources and labelled chunks, and include supporting passages for Athena OPTIMIZE and VACUUM, plus S3 Tables compaction, snapshot management, and unreferenced file removal. Verify the default maintenance settings and the 512 MB target file size against those passages before accepting the expected answer.

---

## many02 (multi)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** What are the design goals of a data mesh, and which options does AWS give for building one?

**Expected answer:** Design goals: data as a product (each domain owns its data end to end), federated data governance, and common access. AWS options: Amazon DataZone (fully managed), open-source frameworks such as data.all, or AWS Lake Formation.

**Key facts:** `data as a product`, `federated data governance`, `Amazon DataZone`, `data.all`, `Lake Formation`

**Expected sources:** wa-analytics-lens: Design; pg-data-mesh-aws-offerings: Amazon DataZone

**Labelled chunks:** `pg-data-mesh-aws-offerings#0000`, `pg-data-mesh-aws-offerings#0002`, `wa-analytics-lens#0174`, `pg-data-mesh-aws-offerings#0001`

**Source text** (`pg-data-mesh-aws-offerings#0000`, Strategies for building a data mesh-based enterprise solution on AWS: AWS offerings for data mesh > , p. None):

> Use the capabilities of analytics on AWS to the build the data mesh–based data solution for your organization. The analytics on AWS resource recommends several AWS services to build data mesh at low cost without compromising on performance. Customers have adopted the following options for building a data mesh–based solution: - Implement data mesh by using Amazon DataZone - Implement data mesh by using open source frameworks on AWS such as data.all - Implement data mesh by using AWS Lake Formation These three options use the following AWS services: - Amazon Athena - Amazon Bedrock - Amazon EMR - AWS Glue (including AWS Glue Data Catalog and an AWS Glue crawler) - AWS Identity and Access Management (IAM) - AWS Key Management Service (AWS KMS) - Amazon Kinesis - AWS Lake Formation - Amazon Managed Streaming for Apache Kafka (Amazon MSK) - AWS Quick - Amazon Redshift - AWS Resource Access Manager (AWS RAM) - Amazon SageMaker AI - AWS Secrets Manager - Amazon Simple Storage Service (Amazon S3) The Amazon DataZone option also uses Amazon EventBridge. The data.all and AWS Lake Formation options also use the following AWS services and resources: - Amazon API Gateway - AWS CloudFormation -  …

**Your edits:** 

---

## many03 (multi)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** How do Amazon Redshift tables and Amazon Redshift Spectrum each reduce the data a query has to move or scan?

**Expected answer:** For Redshift tables, choose the distribution style so that joined rows are collocated on the same node (a DISTKEY on the common join columns, no skew on the key, ALL for small tables under 1 GB). For Redshift Spectrum, use columnar files such as Parquet or ORC, partition on frequently filtered columns for partition pruning, and push predicates down to the Spectrum layer.

**Key facts:** `DISTKEY`, `partition pruning`, `predicate pushdown`, `Parquet`

**Expected sources:** pg-redshift-tables: Choose the right table distribution style; pg-redshift-spectrum: Predicate pushdown in Redshift Spectrum

**Labelled chunks:** `pg-redshift-spectrum#0001`, `pg-redshift-spectrum#0000`, `pg-redshift-tables#0002`

**Source text** (`pg-redshift-spectrum#0000`, Query best practices for Amazon Redshift: Best practices for using Amazon Redshift Spectrum > , p. None):

> This section provides an overview of best practices for using Amazon Redshift Spectrum. We recommend that you follow these best practices to achieve optimal performance when you use Redshift Spectrum: - Consider that file types have a significant influence on Redshift Spectrum query performance. To improve performance, use columnar encoded files such as ORC or Parquet, and use CSV format only for very small dimension tables. - Use prefix-based partitioning to take advantage of partition pruning. This means using filters that are keyed to the partitions in your data lake. - Redshift Spectrum scales automatically to process large requests, so do as much as possible in Redshift Spectrum (for example, predicate pushdown). - Pay attention to partition files on frequently filtered columns. If data is partitioned by one or more filtered columns, Redshift Spectrum can take advantage of partition pruning and skip scanning unneeded partitions and files. A common practice is to partition the data based on time. - You can check the effectiveness of your partitions and efficiency of your Redshift Spectrum query by using the following query.Select query, segment, max(assigned_partitions) as tota …

**Your edits:** Include the relevant passage from pg-redshift-tables#0002 supporting collocation with DISTKEY, avoiding distribution-key skew, and using ALL for tables smaller than 1 GB. The provided excerpt supports the Redshift Spectrum recommendations only.

---

## many04 (multi)

- [ ] OK   - [x] Edit   - [ ] Reject

**Q:** An AWS Glue Spark job is slow: how do I see that it lacks parallelism, and how can it read less data?

**Expected answer:** Lack of parallelism shows in CloudWatch metrics (some executors idle in CPU load and memory utilization) and in the Spark UI (few tasks per stage); the number of RDD partitions sets the degree of parallelism. To read less data, use a columnar format such as Parquet or ORC and prune partitions, for example with push_down_predicate on a DynamicFrame.

**Key facts:** `RDD partitions`, `executors`, `Parquet`, `push_down_predicate`

**Expected sources:** pg-glue-parallelize-tasks: ""; pg-glue-reduce-data-scan: Amazon S3

**Labelled chunks:** `pg-glue-parallelize-tasks#0000`, `pg-glue-reduce-data-scan#0005`

**Source text** (`pg-glue-parallelize-tasks#0000`, Best practices for performance tuning AWS Glue for Apache Spark jobs: Parallelize tasks > , p. None):

> To optimize performance, it's important to parallelize tasks for data loads and transformations. As we discussed in Key topics in Apache Spark, the number of resilient distributed dataset (RDD) partitions is important, because it determines the degree of parallelism. Each task that Spark creates corresponds to an RDD partition on a 1:1 basis. To achieve the best performance, you need to understand how the number of RDD partitions is determined and how that number is optimized. If you do not have enough parallelism, the following symptoms will be recorded in CloudWatch metrics and the Spark UI. CloudWatch metrics Check the CPU Load and Memory Utilization. If some executors are not processing during a phase of your job, it's appropriate to improve parallelism. In this case, during the visualized timeframe, Executor 1 was performing a task, but the remaining executors (2, 3, and 4) were not. You can infer that those executors were not assigned tasks by the Spark driver. Spark UI On the Stage tab in the Spark UI, you can see the number of tasks in a stage. In this case, Spark has performed only one task. Additionally, the event timeline shows Executor 1 processing one task. This means  …

**Your edits:** Add a source passage supporting the use of columnar formats such as Parquet or ORC to reduce data scanning, and include its chunk ID in the labelled chunks. The remaining claims are supported by the provided excerpts.

---

## sim01 (similar)

- [ ] OK   - [x] Edit   - [ ] Reject

**Q:** From a sustainability point of view, why should a workload scale its infrastructure dynamically, and which non-compute services should scale with demand too?

**Expected answer:** Elasticity matches the supply of resources to demand, so the workload scales down quickly in periods of low load (EC2 Auto Scaling, Application Auto Scaling, Kubernetes Cluster Autoscaler). Non-compute services should match demand too, such as Amazon DynamoDB read and write capacity units and Amazon Kinesis Data Streams shards.

**Key facts:** `DynamoDB`, `Kinesis Data Streams shards`

**Expected sources:** wa-sustainability: SUS02-BP01 Scale workload infrastructure dynamically

**Labelled chunks:** `wa-sustainability#0022`, `wa-framework#1210`

**Source text** (`wa-sustainability#0022`, Sustainability Pillar - AWS Well-Architected Framework > Best practices for sustainability in the cloud > Alignment to demand > SUS02-BP01 Scale workload infrastructure dynamically > Implementation steps, p. 26):

> Implementation steps • Elasticity matches the supply of resources you have against the demand for those resources. Instances, containers, and functions provide mechanisms for elasticity, either in combination with automatic scaling or as a feature of the service. AWS provides a range of auto scaling mechanisms to ensure that workloads can scale down quickly and easily during periods of low user load. Here are some examples of auto scaling mechanisms: Auto scaling mechanism Where to use Amazon EC2 Auto Scaling Use to verify you have the correct number of Amazon EC2 instances available to handle the user load for your application. Application Auto Scaling Use to automatically scale the resources for individual AWS services beyond Amazon EC2, such as Lambda functions or Amazon Elastic Container Service (Amazon ECS) services. Kubernetes Cluster Autoscaler Use to automatically scale Kubernetes clusters on AWS. • Scaling is often discussed related to compute services like Amazon EC2 instances or AWS Lambda functions. Consider the configuration of non-compute services like Amazon DynamoDB read and write capacity units or Amazon Kinesis Data Streams shards to match the demand. • Verify tha …

**Your question:**  How does scaling our infrastructure with demand make our workload more sustainable, and what should we scale besides compute?

**Your edits:** 

---

## sim02 (similar)

- [ ] OK   - [x] Edit   - [ ] Reject

**Q:** Which data does the Sustainability pillar say I should not back up?

**Expected answer:** Data that has no business value or can be easily recreated, and ephemeral storage that does not help in a recovery. Back up only data that has business value or is needed for compliance.

**Key facts:** `easily recreated`, `business value`, `ephemeral storage`

**Expected sources:** wa-sustainability: SUS04-BP08 Back up data only when difficult to recreate

**Labelled chunks:** `wa-sustainability#0073`, `wa-framework#0071`

**Source text** (`wa-sustainability#0073`, Sustainability Pillar - AWS Well-Architected Framework > Best practices for sustainability in the cloud > Data management > SUS04-BP08 Back up data only when difficult to recreate, p. 68):

> SUS04-BP08 Back up data only when difficult to recreate Avoid backing up data that has no business value to minimize storage resources requirements for your workload. Common anti-patterns: • You do not have a backup strategy for your data. • You back up data that can be easily recreated. Benefits of establishing this best practice: Avoiding back-up of non-critical data reduces the required storage resources for the workload and lowers its environmental impact. Level of risk exposed if this best practice is not established: Medium Implementation guidance Avoiding the back up of unnecessary data can help lower cost and reduce the storage resources used by the workload. Only back up data that has business value or is needed to satisfy compliance requirements. Examine backup policies and exclude ephemeral storage that doesn’t provide value in a recovery scenario. Implementation steps • Classify data: Implement data classification policy as outlined in SUS04-BP01 Implement a data classification policy. • Design a backup strategy: Use the criticality of your data classification and design backup strategy based on your recovery time objective (RTO) and recovery point objective (RPO). Avoi …

**Your question:** We want to reduce unnecessary backup storage — which data can we skip backing up to make our workload more sustainable?

**Your edits:** 

---

## sim03 (similar)

- [ ] OK   - [x] Edit   - [ ] Reject

**Q:** In the Cost Optimization pillar, when should I throttle demand and when should I buffer it?

**Expected answer:** Throttle when the clients can retry their requests; use a buffer when the clients cannot retry. Both flatten the demand peaks and reduce the provisioned capacity the workload needs.

**Key facts:** `retry`, `buffer`, `provisioned capacity`

**Expected sources:** wa-cost-optimization: COST09-BP02 Implement a buffer or throttle to manage demand

**Labelled chunks:** `wa-cost-optimization#0192`, `wa-cost-optimization#0193`, `wa-cost-optimization#0195`, `wa-cost-optimization#0194`

**Source text** (`wa-cost-optimization#0193`, Cost Optimization Pillar - AWS Well-Architected Framework > Manage demand and supply resources > COST09-BP02 Implement a buffer or throttle to manage demand > Implementation guidance, p. 130):

> Implementation guidance Implementing a buffer or throttle is crucial in cloud computing in order to manage demand and reduce the provisioned capacity required for your workload. For optimal performance, it's essential to gauge the total demand, including peaks, the pace of change in requests, and the necessary response time. When clients have the ability to resend their requests, it becomes practical to apply throttling. Conversely, for clients lacking retry functionalities, the ideal approach is implementing a buffer solution. Such buffers streamline the influx of requests and optimize the interaction of applications with varied operational speeds. Demand curve with two distinct peaks that require high provisioned capacity Assume a workload with the demand curve shown in preceding image. This workload has two peaks, and to handle those peaks, the resource capacity as shown by orange line is provisioned. The resources and energy used for this workload are not indicated by the area under the demand curve, but the area under the provisioned capacity line, as provisioned capacity is needed to handle those two peaks. Flattening the workload demand curve can help you to reduce the provi …

**Your question:** Our API gets spiky traffic and I want to keep the bill down — when should we throttle requests, and when should we queue them?

**Your edits:** 

---

## old01 (outdated)

- [ ] OK   - [x] Edit   - [ ] Reject

**Q:** How many pillars does the AWS Well-Architected Framework have, and what are they?

**Expected answer:** Six: operational excellence, security, reliability, performance efficiency, cost optimization and sustainability. (The archived July 2020 edition lists five, without sustainability.)

**Key facts:** `six`, `sustainability`

**Expected sources:** wa-framework: The pillars of the framework

**Labelled chunks:** `wa-framework#0003`, `wa-reliability#0000`, `wa-security#0000`, `wa-serverless-lens#0026`, `wa-framework#0082`, `wa-operational-excellence#0000`, `wa-cost-optimization#0000`, `wa-sustainability#0000`, `wa-performance-efficiency#0000`, `wa-framework#0008`, `wa-serverless-lens#0001`, `wa-genai-lens#0021`

**Source text** (`wa-framework#0003`, AWS Well-Architected Framework > Definitions, p. 7):

> Definitions Every day, experts at AWS assist customers in architecting systems to take advantage of best practices in the cloud. We work with you on making architectural trade-offs as your designs evolve. As you deploy these systems into live environments, we learn how well these systems perform and the consequences of those trade-offs. Based on what we have learned, we have created the AWS Well-Architected Framework, which provides a consistent set of best practices for customers and partners to evaluate architectures, and provides a set of questions you can use to evaluate how well an architecture is aligned to AWS best practices. The AWS Well-Architected Framework is based on six pillars — operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability. Table 1. The pillars of the AWS Well-Architected Framework Name Description Operational excellence The ability to support development and run workloads effectively, gain insight into their operations, and to continuously improve supporting processes and procedures to deliver business value. Security The security pillar describes how to take advantage of cloud technologies to protect Na …

**Your question:** I’m preparing for an architecture review — how many Well-Architected pillars are there, and what are they?

**Your edits:** 

---

## old02 (outdated)

- [ ] OK   - [x] Edit   - [ ] Reject

**Q:** What are the best practice areas of the Well-Architected security pillar?

**Expected answer:** Seven: security foundations, identity and access management, detection, infrastructure protection, data protection, incident response and application security. (The archived July 2020 edition lists six, without application security.)

**Key facts:** `seven`, `Application security`, `Security foundations`

**Expected sources:** wa-framework: Security

**Labelled chunks:** `wa-framework#0306`, `wa-framework#0025`, `wa-security#0002`

**Source text** (`wa-framework#0025`, AWS Well-Architected Framework > The pillars of the framework > Security, p. 26):

> Definition There are seven best practice areas for security in the cloud: • Security foundations • Identity and access management • Detection • Infrastructure protection • Data protection • Incident response • Application security Before you architect any workload, you need to put in place practices that influence security. You will want to control who can do what. In addition, you want to be able to identify security incidents, protect your systems and services, and maintain the confidentiality and integrity of data through data protection. You should have a well-defined and practiced process for responding to security incidents. These tools and techniques are important because they support objectives such as preventing financial loss or complying with regulatory obligations. The AWS Shared Responsibility Model helps organizations that adopt the cloud to achieve their security and compliance goals. Because AWS physically secures the infrastructure that supports our cloud services, as an AWS customer you can focus on using services to accomplish your goals. The AWS Cloud also provides greater access to security data and an automated approach to responding to security events. Best p …

**Your question:** How is the AWS Well-Architected Security pillar broken down into best practice areas?

**Your edits:** 

---

## old03 (outdated)

- [ ] OK   - [x] Edit   - [ ] Reject

**Q:** What are the best practice areas for performance efficiency in the Well-Architected Framework?

**Expected answer:** Five: architecture selection, compute and hardware, data management, networking and content delivery, and process and culture. (The archived July 2020 edition lists four: selection, review, monitoring and tradeoffs.)

**Key facts:** `Architecture selection`, `Compute and hardware`, `Networking and content delivery`

**Expected sources:** wa-framework: Performance efficiency

**Labelled chunks:** `wa-framework#0045`, `wa-performance-efficiency#0000`, `wa-framework#0884`, `wa-performance-efficiency#0115`, `wa-performance-efficiency#0002`

**Source text** (`wa-framework#0045`, AWS Well-Architected Framework > The pillars of the framework > Performance efficiency, p. 45):

> Definition There are five best practice areas for performance efficiency in the cloud: • Architecture selection • Compute and hardware • Data management • Networking and content delivery • Process and culture Take a data-driven approach to building a high-performance architecture. Gather data on all aspects of the architecture, from the high-level design to the selection and configuration of resource types. Reviewing your choices on a regular basis validates that you are taking advantage of the continually evolving AWS Cloud. Monitoring verifies that you are aware of any deviance from expected performance. Make trade-offs in your architecture to improve performance, such as using compression or caching, or relaxing consistency requirements. Best practices Topics • Architecture selection • Compute and hardware • Data management • Networking and content delivery • Process and culture Architecture selection The optimal solution for a particular workload varies, and solutions often combine multiple approaches. Well-Architected workloads use multiple solutions and allow different features to improve performance. AWS resources are available in many types and configurations, which makes i …

**Your question:** How is the Performance Efficiency pillar in AWS Well-Architected broken down into best practice areas?

**Your edits:** 

---

## none01 (no_answer)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** What is the default quota of concurrent executions for AWS Lambda functions in one AWS Region?

**Expected answer:** Not in the corpus: service quota values live in the HW 1 corpus (AWS General Reference), not in the Well-Architected or Prescriptive Guidance documents. The corpus mentions Service Quotas and concurrency only in general terms.

**Key facts:** —

**Expected sources:** —

**Your edits:** 

---

## none02 (no_answer)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** How much does Amazon Athena charge per terabyte of data scanned?

**Expected answer:** Not in the corpus: the Data Analytics Lens says Athena is billed by the data scanned, but no document gives the price.

**Key facts:** —

**Expected sources:** —

**Your edits:** 

---

## none03 (no_answer)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** How do I run OPTIMIZE with Z-ORDER on Delta Lake tables in Databricks?

**Expected answer:** Not in the corpus: Delta Lake appears only as a table format that Athena and Lake Formation support; nothing covers Databricks or Z-ORDER.

**Key facts:** —

**Expected sources:** —

**Your edits:** 

---

## none04 (no_answer)

- [x] OK   - [ ] Edit   - [ ] Reject

**Q:** How do I configure the Horizontal Pod Autoscaler in Google Kubernetes Engine?

**Expected answer:** Not in the corpus: the Reliability Pillar names the Horizontal Pod Autoscaler for Amazon EKS only; nothing covers Google Kubernetes Engine (finding F22).

**Key facts:** —

**Expected sources:** —

**Your edits:** OK as a no-answer item: the corpus names HPA for EKS but not how to configure it in GKE — a refusal is the right answer (F22).

---
