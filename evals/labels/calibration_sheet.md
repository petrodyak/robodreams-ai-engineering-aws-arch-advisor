# Calibration sheet — run `claude-haiku-5-5__v1__medium__k5`

Label each answer by hand; the judges are checked against these labels (spec §7).

- **Correct?** Pass when the answer states the facts of the reference answer and does not
  contradict it. Wording, order and extra detail do not matter.
- **Claim not in its source?** Yes when at least one claim cannot be found in the source it cites
  (shown under the claim), even if the claim is true.

Tick one box on each line. The answers that the deterministic scorers failed come first.

## many04 (multi)

- Correct?          [ ] pass   [x] fail
- Claim not in its source? [ ] yes    [x] no

**Q:** An AWS Glue Spark job is slow: how do I see that it lacks parallelism, and how can it read less data?

**Reference answer:** Lack of parallelism shows in CloudWatch metrics (some executors idle in CPU load and memory utilization) and in the Spark UI (few tasks per stage); the number of RDD partitions sets the degree of parallelism. To read less data, use a columnar format such as Parquet or ORC and prune partitions, for example with push_down_predicate on a DynamicFrame.

*Deterministic scorers: fail, key facts 0.25.*

**Answer, claim by claim:**

1. A lack of parallelism shows up in CloudWatch metrics: check CPU Load and Memory Utilization, and if some executors are not processing during a phase of the job, parallelism should be improved. [S2]
2. In the Spark UI Stage tab, a stage with only one task, and an event timeline where one executor processes that task while the others sit idle, indicates the job lacks parallelism. [S2]
3. To reduce the amount of data a Glue Spark job loads from Amazon S3, consider the file size, compression, file format, and file layout (partitions) of the dataset. [S3]
4. Keep the file size of inputs and outputs within a moderate range, for example about 128 MB, because files that are too small or too large cause issues. [S3]
5. Many small files cause heavy network I/O on Amazon S3 and heavy I/O and processing load on the Spark driver, because they generate many partitions and tasks. [S3]
6. To reduce the excessive parallelism created when a Spark task is made for each small file, use file grouping for DynamicFrames by setting the groupFiles and groupSize parameters, for example groupFiles set to inPartition and groupSize set to 1048576. [S3]
7. If the file type is not splittable, such as gzip, and the files are too large, the Spark application must wait until a single task has finished reading the entire file. [S3]

**Cited sources, full text:**

> **[S2]** `pg-glue-parallelize-tasks#0000` Best practices for performance tuning AWS Glue for Apache Spark jobs: Parallelize tasks > (no section)
>
> To optimize performance, it's important to parallelize tasks for data loads and transformations. As we discussed in Key topics in Apache Spark, the number of resilient distributed dataset (RDD) partitions is important, because it determines the degree of parallelism. Each task that Spark creates corresponds to an RDD partition on a 1:1 basis. To achieve the best performance, you need to understand how the number of RDD partitions is determined and how that number is optimized. If you do not have enough parallelism, the following symptoms will be recorded in CloudWatch metrics and the Spark UI. CloudWatch metrics Check the CPU Load and Memory Utilization. If some executors are not processing during a phase of your job, it's appropriate to improve parallelism. In this case, during the visualized timeframe, Executor 1 was performing a task, but the remaining executors (2, 3, and 4) were not. You can infer that those executors were not assigned tasks by the Spark driver. Spark UI On the Stage tab in the Spark UI, you can see the number of tasks in a stage. In this case, Spark has performed only one task. Additionally, the event timeline shows Executor 1 processing one task. This means that the work in this stage was performed entirely on one executor, while the others were idle. If you observe these symptoms, try the following solutions for each data source.

> **[S3]** `pg-glue-reduce-data-scan#0001` Best practices for performance tuning AWS Glue for Apache Spark jobs: Reduce the amount of data scan > Spark UI > Amazon S3
>
> Amazon S3 To reduce the amount of data loaded into your job when reading from Amazon S3, consider file size, compression, file format, and file layout (partitions) for your dataset. AWS Glue for Spark jobs are often used for ETL of raw data, but for efficient distributed processing, you need to inspect the features of your data source format. - File size – We recommend keeping the file size of inputs and outputs within a moderate range (for example, 128 MB). Files that are too small and files that are too large can cause issues.A large number of small files cause following issues:Heavy network I/O load on Amazon S3 because of the overhead required to make requests (such as List, Get, or Head) for many objects (compared with a few objects that store the same quantity of data).Heavy I/O and processing load on the Spark driver, which will generate many partitions and tasks and lead to excessive parallelism.On the other hand, if your file type is not splittable (such as gzip) and the files are too large, the Spark application must wait until a single task has completed reading the entire file.To reduce excessive parallelism incurred when an Apache Spark task is created for each small file, use file grouping for DynamicFrames. This approach reduces the chances of an OOM exception from the Spark driver. To configure file grouping, set the groupFiles and groupSize parameters. The following code example uses the AWS Glue DynamicFrame API in an ETL script with these parameters.dyf = glueContext.create_dynamic_frame_from_options("s3", {'paths': ["s3://input-s3-path/"], 'recurse':True, 'groupFiles': 'inPartition', 'groupSize': '1048576'}, format="json")

**Note (optional):** 

---

## sim02 (similar)

- Correct?          [x] pass   [ ] fail
- Claim not in its source? [ ] yes    [x] no

**Q:** We want to reduce unnecessary backup storage — which data can we skip backing up to make our workload more sustainable?

**Reference answer:** Data that has no business value or can be easily recreated, and ephemeral storage that does not help in a recovery. Back up only data that has business value or is needed for compliance.

*Deterministic scorers: fail, key facts 0.67.*

**Answer, claim by claim:**

1. You can skip backing up data that has no business value and is not needed to satisfy compliance requirements, because backing up only data with business value or compliance need minimizes storage consumption. [S1][S3]
2. You can skip backing up data that can be easily recreated. [S1]
3. You can exclude ephemeral data from your backups when it provides no value in a recovery scenario. [S1][S3]
4. You can exclude local copies of data from backups, unless restoring that data from a common location would take longer than your service-level agreements allow. [S1]
5. Classify your data first under a data classification policy so you understand its significance to business outcomes and can decide what to back up. [S1][S2]
6. Design the backup strategy based on the criticality of your data classification, your recovery time objective (RTO), and your recovery point objective (RPO), and avoid backing up non-critical data. [S1]
7. Backing up all data without considering its criticality is an anti-pattern that increases storage requirements and environmental impact. [S4]

**Cited sources, full text:**

> **[S1]** `wa-sustainability#0073` Sustainability Pillar - AWS Well-Architected Framework > Best practices for sustainability in the cloud > Data management > SUS04-BP08 Back up data only when difficult to recreate
>
> SUS04-BP08 Back up data only when difficult to recreate Avoid backing up data that has no business value to minimize storage resources requirements for your workload. Common anti-patterns: • You do not have a backup strategy for your data. • You back up data that can be easily recreated. Benefits of establishing this best practice: Avoiding back-up of non-critical data reduces the required storage resources for the workload and lowers its environmental impact. Level of risk exposed if this best practice is not established: Medium Implementation guidance Avoiding the back up of unnecessary data can help lower cost and reduce the storage resources used by the workload. Only back up data that has business value or is needed to satisfy compliance requirements. Examine backup policies and exclude ephemeral storage that doesn’t provide value in a recovery scenario. Implementation steps • Classify data: Implement data classification policy as outlined in SUS04-BP01 Implement a data classification policy. • Design a backup strategy: Use the criticality of your data classification and design backup strategy based on your recovery time objective (RTO) and recovery point objective (RPO). Avoid backing up non-critical data. • Exclude data that can be easily recreated. • Exclude ephemeral data from your backups. • Exclude local copies of data, unless the time required to restore that data from a common location exceeds your service-level agreements (SLAs). • Use automated backup: Use an automated solution or managed service to back up businesscritical data. • AWS Backup is a fully-managed service that makes it easy to centralize and automate data protection across AWS services, in the cloud, and on premises. For hands-on guidance on how to create automated backups using AWS Backup, see Well-Architected Labs - Testing Backup and Restore of Data. • Automate backups and optimize backup costs for Amazon EFS using AWS Backup.

> **[S2]** `wa-framework#0070` AWS Well-Architected Framework > The pillars of the framework > Sustainability > Best practices > Data management
>
> Data management The following question focuses on these considerations for sustainability: SUS 4: How do you take advantage of data management policies and patterns to support your sustainability goals? Implement data management practices to reduce the provisioned storage required to support your workload, and the resources required to use it. Understand your data, and use storage technologies and configurations that most effectively supports the business value of the data and how it’s used. Lifecycle data to more efficient, less performant storage when requirements decrease, and delete data that’s no longer required. Implement a data classification policy: Classify data to understand its significance to business outcomes. Use this information to determine when you can move data to more energy-efficient storage or safely delete it. Use technologies that support data access and storage patterns: Use storage that most effectively supports how your data is accessed and stored to minimize the resources provisioned while supporting your workload. For example, solid state devices (SSDs) are more energy intensive than magnetic drives and should be used only for active data use cases. Use energy-efficient, archivalclass storage for infrequently accessed data. Use lifecycle policies to delete unnecessary data: Manage the lifecycle of all your data and automatically enforce deletion timelines to minimize the total storage requirements of your workload. Minimize over-provisioning in block storage: To minimize total provisioned storage, create block storage with size allocations that are appropriate for the workload. Use elastic volumes to expand storage as data grows without having to resize storage attached to compute resources. Regularly review elastic volumes and shrink over-provisioned volumes to fit the current data size. Remove unneeded or redundant data: Duplicate data only when necessary to minimize total storage consumed. Use backup technologies that deduplicate data at the file and block level. Limit the use of Redundant Array of Independent Drives (RAID) configurations except where required to meet SLAs.

> **[S3]** `wa-framework#0071` AWS Well-Architected Framework > The pillars of the framework > Sustainability > Best practices > Data management
>
> Use shared file systems or object storage to access common data: Adopt shared storage and single sources of truth to avoid data duplication and reduce the total storage requirements of your workload. Fetch data from shared storage only as needed. Detach unused volumes to release resources. Minimize data movement across networks: Use shared storage and access data from Regional data stores to minimize the total networking resources required to support data movement for your workload. Back up data only when difficult to recreate: To minimize storage consumption, only back up data that has business value or is required to satisfy compliance requirements. Examine backup policies and exclude ephemeral storage that doesn’t provide value in a recovery scenario.

> **[S4]** `wa-sustainability#0065` Sustainability Pillar - AWS Well-Architected Framework > Best practices for sustainability in the cloud > Data management > SUS04-BP05 Remove unneeded or redundant data
>
> SUS04-BP05 Remove unneeded or redundant data Remove unneeded or redundant data to minimize the storage resources required to store your datasets. Common anti-patterns: • You duplicate data that can be easily obtained or recreated. • You back up all data without considering its criticality. • You only delete data irregularly, on operational events, or not at all. • You store data redundantly irrespective of the storage service's durability. • You turn on Amazon S3 versioning without any business justification. Benefits of establishing this best practice: Removing unneeded data reduces the storage size required for your workload and the workload environmental impact. Level of risk exposed if this best practice is not established: Medium Implementation guidance When you remove unneeded and redundant datasets, you can reduce storage cost and environmental footprint. This practice may also make computing more efficient, as compute resources only process important data instead of unneeded data. Automate the deletion of unneeded data. Use technologies that deduplicate data at the file and block level. Use service features for native data replication and redundancy.

**Note (optional):** 

---

## many03 (multi)

- Correct?          [ ] pass   [x] fail
- Claim not in its source? [ ] yes    [x] no

**Q:** How do Amazon Redshift tables and Amazon Redshift Spectrum each reduce the data a query has to move or scan?

**Reference answer:** For Redshift tables, choose the distribution style so that joined rows are collocated on the same node (a DISTKEY on the common join columns, no skew on the key, ALL for small tables under 1 GB). For Redshift Spectrum, use columnar files such as Parquet or ORC, partition on frequently filtered columns for partition pruning, and push predicates down to the Spectrum layer.

*Deterministic scorers: fail, key facts 0.75.*

**Answer, claim by claim:**

1. In Amazon Redshift tables, the sort key determines the order in which rows are stored on disk, so a query can skip blocks outside the range of values it needs and read fewer blocks. [S3]
2. In Amazon Redshift tables, the distribution key determines how data is distributed between the nodes in a cluster, and choosing the right distribution keys can improve the performance of joins and aggregations. [S3]
3. Redshift Spectrum uses predicate pushdown, so operations such as GROUP BY, comparison and pattern-matching conditions, and aggregate functions are evaluated in the Spectrum layer, which avoids consuming resources in the Amazon Redshift cluster. [S1][S4]
4. Redshift Spectrum can eliminate columns from scanning when data is in Parquet or ORC format, so queries should use the fewest number of columns. [S1][S2]
5. Columnar encoded file formats such as ORC or Parquet improve Redshift Spectrum query performance, and CSV is recommended only for very small dimension tables. [S2]
6. Redshift Spectrum uses prefix-based partitioning and partition pruning, so filters keyed to the partitions let it skip scanning unneeded partitions and files, especially when data is partitioned by frequently filtered columns such as time. [S2]
7. Avoiding SELECT * FROM and listing only the needed columns reduces query execution time and scan costs for Amazon Redshift Spectrum queries. [S5]

**Cited sources, full text:**

> **[S1]** `pg-redshift-spectrum#0001` Query best practices for Amazon Redshift: Best practices for using Amazon Redshift Spectrum > Predicate pushdown in Redshift Spectrum
>
> Predicate pushdown in Redshift Spectrum Using predicate pushdown avoids consuming resources in the Amazon Redshift cluster. You can push many SQL operations down to the Redshift Spectrum layer. We recommend taking advantage of this wherever possible. Keep in mind the following: - You can evaluate some types of SQL operations completely within the Redshift Spectrum layer, including the following:GROUP BY clausesComparison and pattern-matching conditions (for example, LIKE)Aggregate functions (for example, COUNT, SUM, AVG, MIN, and MAX)regex_replace, to_upper, date_trunc, and other functions - You can't push some operations to the Redshift Spectrum layer, including DISTINCT and ORDER BY. Perform ORDER BY only at the top level of the query if possible, since sorting is done in the leader node. - Examine your query EXPLAIN plan to verify if predicate pushdown is effective. To find Redshift Spectrum portions in an EXPLAIN command, look for these steps:S3 Seq ScanS3 HashAggregateS3 Query ScanSeq Scan PartitionInfoPartition Loop - Use the fewest number of columns in your query. Redshift Spectrum can eliminate columns for scanning if data is in Parquet or ORC format. - Make extensive use of partitions for parallel processing and partition elimination, and keep file sizes to at least 64 MB if possible. - Set the TABLE PROPERTIES 'numRows'='nnn' if you use CREATE EXTERNAL TABLE or ALTER TABLE. Amazon Redshift doesn't analyze external tables to generate table statistics that the query optimizer uses to generate a query plan. If the statistics aren't set, then Amazon Redshift assumes that external tables are the larger tables and local tables are the smaller tables.

> **[S2]** `pg-redshift-spectrum#0000` Query best practices for Amazon Redshift: Best practices for using Amazon Redshift Spectrum > (no section)
>
> This section provides an overview of best practices for using Amazon Redshift Spectrum. We recommend that you follow these best practices to achieve optimal performance when you use Redshift Spectrum: - Consider that file types have a significant influence on Redshift Spectrum query performance. To improve performance, use columnar encoded files such as ORC or Parquet, and use CSV format only for very small dimension tables. - Use prefix-based partitioning to take advantage of partition pruning. This means using filters that are keyed to the partitions in your data lake. - Redshift Spectrum scales automatically to process large requests, so do as much as possible in Redshift Spectrum (for example, predicate pushdown). - Pay attention to partition files on frequently filtered columns. If data is partitioned by one or more filtered columns, Redshift Spectrum can take advantage of partition pruning and skip scanning unneeded partitions and files. A common practice is to partition the data based on time. - You can check the effectiveness of your partitions and efficiency of your Redshift Spectrum query by using the following query.Select query, segment, max(assigned_partitions) as total_partitions, max(qualified_partitions) as qualified_partitions From svl_s3partition Where query=pg_last_query_id() Group by 1,2;The preceding query shows the following:total_partitions – The number of partitions recognized by the AWS Glue Data Catalogqualified_partitions – The number of prefixes on Amazon Simple Storage Service (Amazon S3) that are accessed for the Redshift Spectrum query - You can also check the SVL_S3QUERY_SUMMARY system table to learn about the effectiveness of your partitions and efficiency of your Redshift Spectrum query. To do so, use the following statement.Select * From svl_s3query_summary Where query=pg_last_query_id();The preceding query returns even more information, including is_partitioned, s3_scanned_rows/bytes, and s3_returned_rows/bytes values in addition to files showing the efficiency of partition pruning.

> **[S3]** `wa-analytics-lens#0113` Data Analytics Lens - AWS Well-Architected Framework > Pillars of the Well-Architected Framework > Sustainability > 15 – Sustainability implementation guidance > Best practice 15.5 – Optimize your data modeling and data storage for efficient data retrieval
>
> Suggestion 15.5.2 – Configure and sort distribution keys on your Amazon Redshift tables Amazon Redshift sort keys determine the order in which rows in a table are stored on the disk. When you query a data set in Redshift, it can leverage the sort order of the data to avoid reading blocks that are outside of the range of values you are looking for. By reading fewer blocks of data, this approach can result in a reduction of compute resources required. For more details, refer to the following information: • Amazon Redshift: Choose the best sort key In Amazon Redshift, the distribution key, or distkey, determines how data is distributed between the nodes in a cluster. Choosing the right distribution keys can improve the performance of common analytical operations like joins and aggregations. For more details, refer to the following information: • Amazon Redshift: Automate your Amazon Redshift performance tuning with automatic table optimization • Amazon Redshift: Distribution styles Suggestion 15.5.3 – Enable results and query plan caching Computing the same result over and over again is wasteful. Query engines and data warehouses often support result caching, and/or query plan caching. By enabling these you can reduce the overall amount of compute power needed for your analytics workload by eliminating recomputing results and/or query plans when the data set hasn’t changed. This saves on compute resource and reduce the environmental impact. For more details, refer to the following information: • Amazon Redshift: Performance optimization • Amazon Athena: Query result reuse

> **[S4]** `pg-redshift-spectrum#0002` Query best practices for Amazon Redshift: Best practices for using Amazon Redshift Spectrum > Query tuning tips for Redshift Spectrum
>
> Query tuning tips for Redshift Spectrum We recommend that you keep the following in mind when you tune your queries: - The number of Redshift Spectrum nodes that your Amazon Redshift cluster can engage for a query is tied to the number of slices in your cluster. - Resizing your cluster up can benefit your cluster's local compute profiles, storage profiles, and the query capabilities of the Amazon S3 data lake query. - The Amazon Redshift query planner pushes predicates and aggregations to the Redshift Spectrum query layer whenever possible. - When large amounts of data are returned from Amazon S3, the processing is limited by your cluster's resources. - Because Redshift Spectrum scales automatically to process large requests, your overall performance improves whenever you can push processing to the Redshift Spectrum layer.

> **[S5]** `pg-redshift-queries#0000` Query best practices for Amazon Redshift: Best practices for designing Amazon Redshift queries > (no section)
>
> This section provides an overview of best practices for designing queries. We recommend that you follow the best practices in this section to achieve optimal query performance and efficiency. Avoid using the SELECT * FROM statement We recommend that you avoid using the SELECT * FROM statement. Instead, always list out columns for analysis. This reduces query execution time and scans costs for Amazon Redshift Spectrum queries. Example of what to avoid select * from sales; Best practice example select sales_date, sales_amt from sales; Identify query issues We recommend that you check the STL_ALERT_EVENT_LOG view to identify and correct possible issues with your query. Get summary information on your query We recommend that you use the SVL_QUERY_SUMMARY and SVL_QUERY_REPORT views to get summary information on your queries. You can use this information to optimize your queries. Avoid cross-joins We recommend that you avoid using cross-joins unless absolutely necessary. Without a join condition, cross-joins result in the Cartesian product of two tables. Cross-joins are typically run as nested-loop joins (the slowest of the possible join types). Example of what to avoid select c.c_name, n.n_name from tpch.customer c, tpch.nation n; Best practice example select c.c_name, n.n_name from tpch.customer c, join tpch.nation n on n.n_nationkey = c.c_nationkey;

**Note (optional):** changed after judge review (17.11): pass → fail. The Redshift tables half misses collocation, ALL for tables under 1 GB and key skew, so the answer does not state the facts of the reference answer.

---

## many01 (multi)

- Correct?          [x] pass   [ ] fail
- Claim not in its source? [ ] yes    [x] no

**Q:** Which features keep Apache Iceberg tables efficient as small files and delete files accumulate, in Amazon Athena and in Amazon S3 Tables?

**Reference answer:** In Athena you run maintenance yourself: OPTIMIZE ... REWRITE DATA compacts data files and merges delete files, and VACUUM expires old snapshots and removes orphan files. S3 Tables runs maintenance automatically and enables it by default for every table: compaction (default target file size 512 MB) and snapshot management, with unreferenced file removal.

*Deterministic scorers: pass, key facts 1.00.*

**Answer, claim by claim:**

1. In Amazon Athena, the OPTIMIZE table REWRITE DATA compaction action rewrites data files into a more optimized layout based on their size and number of associated delete files, and it merges delete files into data files. [S1]
2. In Amazon Athena, VACUUM performs snapshot expiration and orphan file removal, which reduces metadata size and removes files that are not in the current table state and are older than the table's retention period. [S1]
3. In Amazon S3 Tables, automated maintenance operations such as compaction, snapshot management, and unreferenced file removal run continuously to optimize tables for querying. [S2]
4. In Amazon S3 Tables, compaction is enabled by default for all tables and combines multiple smaller objects into fewer, larger objects, and when it combines objects it also applies the effects of row-level deletes. [S5]
5. In Amazon S3 Tables, the default compaction target file size is 512MB, and you can set a custom target between 64MB and 512MB. [S5]

**Cited sources, full text:**

> **[S1]** `athena-iceberg-optimize#0000` Amazon Athena User Guide: Optimize Iceberg tables > (no section)
>
> Athena provides several optimization features to improve query performance on Apache Iceberg tables. As data accumulates, queries can become less efficient due to increased file processing overhead and the computational cost of applying row-level deletes stored in Iceberg delete files. To address these challenges, Athena supports manual compaction and vacuum operators to optimize table structure. Athena also works with Iceberg statistics to enable cost-based query optimization and Parquet column indexing for precise data pruning during query execution. These features work together to reduce query execution time, minimize data scanning, and lower costs. This topic describes how to use these optimization capabilities to maintain high-performance queries on your Iceberg tables. OPTIMIZE The OPTIMIZE table REWRITE DATA compaction action rewrites data files into a more optimized layout based on their size and number of associated delete files. For syntax and table property details, see OPTIMIZE. Example The following example merges delete files into data files and produces files near the targeted file size where the value of category is c1. OPTIMIZE iceberg_table REWRITE DATA USING BIN_PACK WHERE category = 'c1' VACUUM VACUUM performs snapshot expiration and orphan file removal. These actions reduce metadata size and remove files not in the current table state that are also older than the retention period specified for the table. For syntax details, see VACUUM.

> **[S2]** `s3-tables#0001` Amazon S3 User Guide: Working with Amazon S3 Tables and table buckets > Features of S3 Tables
>
> Features of S3 Tables Purpose-built storage for tables S3 table buckets are specifically designed for tables. Table buckets provide higher transactions per second (TPS) and better query throughput compared to self-managed tables in S3 general purpose buckets. Table buckets deliver the same durability, availability, and scalability as other Amazon S3 bucket types. Built-in support for Apache Iceberg Tables in your table buckets are stored in Apache Iceberg format. You can query these tables using standard SQL in query engines that support Iceberg. Iceberg has a variety of features to optimize query performance, including schema evolution and partition evolution. With Iceberg, you can change how your data is organized so that it can evolve over time without requiring you to rewrite your queries or rebuild your data structures. Iceberg is designed to help ensure data consistency and reliability through its support for transactions. To help you correct issues or perform time travel queries, you can track how data changes over time and roll back to historical versions. Your table buckets support the Apache Iceberg Version 3 (V3) table format, including deletion vectors, row lineage, column default values, and the variant, geometry, geography, unknown, and nanosecond-precision timestamp data types. For more information, see Working with Apache Iceberg V3. Automated table optimization To optimize your tables for querying, S3 continuously performs automatic maintenance operations, such as compaction, snapshot management, and unreferenced file removal. These operations increase table performance by compacting smaller objects into fewer, larger files. Maintenance operations also reduce your storage costs by cleaning up unused objects. This automated maintenance streamlines the operation of data lakes at scale by reducing the need for manual table maintenance. For each table and table bucket, you can customize maintenance configurations. Access management and security

> **[S5]** `s3-tables-maintenance#0000` Amazon S3 User Guide: Maintenance for tables > (no section)
>
> S3 Tables offers maintenance operations to enhance the management and performance of your individual tables. The following options are enabled by default for all tables in table buckets. You can edit or disable these by specifying maintenance configuration files for your S3 table. Editing this configuration requires the s3tables:GetTableMaintenanceConfiguration and s3tables:PutTableMaintenanceConfiguration permissions. Note You can track S3 Tables automated maintenance operations on your tables through CloudTrail logs, for more information, see CloudTrail management events for S3 Tables maintenance. Compaction Compaction is configured at the table level and combines multiple smaller objects into fewer, larger objects to improve Apache Iceberg query performance. When combining objects, compaction also applies the effects of row-level deletes in your table. Compaction is enabled by default for all tables, with a default target file size of 512MB, or a custom value you specify between 64MB to 512MB. The compacted files are written as the most recent snapshot of your table. Note Compaction is supported on Apache Parquet, Avro, and ORC file types.

**Note (optional):** 

---

## many02 (multi)

- Correct?          [x] pass   [ ] fail
- Claim not in its source? [ ] yes    [x] no

**Q:** What are the design goals of a data mesh, and which options does AWS give for building one?

**Reference answer:** Design goals: data as a product (each domain owns its data end to end), federated data governance, and common access. AWS options: Amazon DataZone (fully managed), open-source frameworks such as data.all, or AWS Lake Formation.

*Deterministic scorers: pass, key facts 1.00.*

**Answer, claim by claim:**

1. A data mesh design goal is data as a product, where each organizational domain owns its data end-to-end and is responsible for building, operating, serving, and resolving issues arising from its use. [S2]
2. A data mesh design goal is federated data governance, where data domains can manage the technical implementation of governance such as lineage, data quality validation, and access controls, while central data discovery, reporting, and auditing make data easy to find and compliance easy to verify. [S2]
3. A data mesh design goal is common access, where data is easily consumable by subject matter experts and purpose-built analytics and machine learning services, with data domains exposing interfaces that enforce access controls and audit tracking. [S2]
4. AWS offers three options for implementing a data mesh: using Amazon DataZone, using open source frameworks on AWS such as data.all, or using AWS Lake Formation. [S1]
5. Data.all is an open source option for organizations that want to build and manage their own solution; it is a modern data marketplace that simplifies data discovery, sharing, and granular data access management. [S5]
6. AWS Lake Formation is an option for organizations that want to build a custom data mesh solution from the ground up and manage it, and it helps centrally govern, secure, and globally share data for analytics and machine learning. [S5]

**Cited sources, full text:**

> **[S1]** `pg-data-mesh-aws-offerings#0000` Strategies for building a data mesh-based enterprise solution on AWS: AWS offerings for data mesh > (no section)
>
> Use the capabilities of analytics on AWS to the build the data mesh–based data solution for your organization. The analytics on AWS resource recommends several AWS services to build data mesh at low cost without compromising on performance. Customers have adopted the following options for building a data mesh–based solution: - Implement data mesh by using Amazon DataZone - Implement data mesh by using open source frameworks on AWS such as data.all - Implement data mesh by using AWS Lake Formation These three options use the following AWS services: - Amazon Athena - Amazon Bedrock - Amazon EMR - AWS Glue (including AWS Glue Data Catalog and an AWS Glue crawler) - AWS Identity and Access Management (IAM) - AWS Key Management Service (AWS KMS) - Amazon Kinesis - AWS Lake Formation - Amazon Managed Streaming for Apache Kafka (Amazon MSK) - AWS Quick - Amazon Redshift - AWS Resource Access Manager (AWS RAM) - Amazon SageMaker AI - AWS Secrets Manager - Amazon Simple Storage Service (Amazon S3) The Amazon DataZone option also uses Amazon EventBridge. The data.all and AWS Lake Formation options also use the following AWS services and resources: - Amazon API Gateway - AWS CloudFormation - Amazon Cognito - AWS Lambda - AWS Systems Manager Parameter Store - AWS WAF The AWS services that you use in your implementation might differ, based on your organization's requirements.

> **[S2]** `wa-analytics-lens#0174` Data Analytics Lens - AWS Well-Architected Framework > Scenarios > Data mesh > Design
>
> Design The following are data mesh design goals: • Data as a product: Each organizational domain owns their data end-to-end. They’re responsible for building, operating, serving, and resolving any issues arising from the use of their data. Data accuracy and accountability lies with the data owner within the domain. • Federated data governance: Data governance helps ensure that data is secure, accurate, and the right personas have access to the right data. The technical implementation of data governance, such as collecting lineage, validating data quality, and enforcing appropriate access controls, can be managed by each of the data domains. However, central data discovery, reporting, and auditing is needed to make it easy for users to find data, and for auditors to verify compliance. • Common access: Data must be easily consumable by subject matter experts, such as data analysts and data scientists, and by purpose-built analytics and machine learning (ML) services. This requires data domains to expose a set of interfaces that make data consumable while enforcing appropriate access controls and audit tracking.

> **[S5]** `pg-data-mesh-aws-offerings#0002` Strategies for building a data mesh-based enterprise solution on AWS: AWS offerings for data mesh > (no section)
>
> Data.all If you understand open source and want to build and manage your own solution, consider using open source frameworks such as data.all. Data.all is a modern data marketplace that supports collaboration among diverse users. Data.all simplifies data discovery, sharing, and granular data access management while builders use the AWS portfolio of data and analytics services. The following diagram shows a data mesh reference architecture based on data.all. The architecture diagram contains following components: - The data producers publish data products in the catalog provided by the data.all frontend. The frontend and backend of data.all are hosted in the central governance account. - Data consumers (users) log in to the data.all frontend by using their single sign-on or Amazon Cognito credentials. They can browse the catalog and search for the data products of their interest. They can filter the search results. - After the data users belonging to the consumer teams find the data product of their interest, they can request access the data. Data.all has a built-in access-management workflow that the data owner uses to review and approve access requests. - The consumer teams can consume the data to empower their AI/ML, analytics and reporting, and ETL use cases. AWS Lake Formation If you want to build a custom data mesh solution from the ground up and manage it, consider using AWS Lake Formation. Lake Formation helps you centrally govern, secure, and globally share data for analytics and machine learning. The following diagram shows a data mesh reference architecture based on Lake Formation. The architecture diagram contains following components: - The data producers publish data products in the AWS Glue Data Catalog of the central governance account. AWS Lake Formation manages access to the entities of the central Data Catalog. - After access is granted, the consumer teams can consume the data to empower their AI/ML, analytics and reporting, and ETL use-cases.

**Note (optional):** 

---

## old01 (outdated)

- Correct?          [x] pass   [ ] fail
- Claim not in its source? [x] yes    [ ] no

**Q:** I'm preparing for an architecture review — how many Well-Architected pillars are there, and what are they?

**Reference answer:** Six: operational excellence, security, reliability, performance efficiency, cost optimization and sustainability. (The archived July 2020 edition lists five, without sustainability.)

*Deterministic scorers: pass, key facts 1.00.*

**Answer, claim by claim:**

1. The AWS Well-Architected Framework has six pillars. The older five-pillar version is superseded by the newer edition. [S5][S2]
2. The six pillars are operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability. [S5]
3. Operational excellence is a commitment to build software correctly while consistently delivering a great customer experience, and its pillar contains best practices for organizing your team, designing your workload, operating it at scale, and evolving it over time. [S5]
4. Architecture choices affect workload behavior across all six Well-Architected pillars. [S2]

**Cited sources, full text:**

> **[S2]** `wa-reliability#0057` Reliability Pillar - AWS Well-Architected Framework > Workload architecture
>
> Workload architecture A reliable workload starts with upfront design decisions for both software and infrastructure. Your architecture choices will impact your workload behavior across all six Well-Architected pillars. For reliability, there are specific patterns you must follow. The following sections explain best practices to use with these patterns for reliability. Topics • Design your workload service architecture • Design interactions in a distributed system to prevent failures • Design interactions in a distributed system to mitigate or withstand failures Design your workload service architecture Build highly scalable and reliable workloads using a service-oriented architecture (SOA) or a microservices architecture. Service-oriented architecture (SOA) is the practice of making software components reusable via service interfaces. Microservices architecture goes further to make components smaller and simpler. Service-oriented architecture (SOA) interfaces use common communication standards so that they can be rapidly incorporated into new workloads. SOA replaced the practice of building monolith architectures, which consisted of interdependent, indivisible units. At AWS, we have always used SOA, but have now embraced building our systems using microservices. While microservices have several attractive qualities, the most important benefit for availability is that microservices are smaller and simpler. They allow you to differentiate the availability required of different services, and thereby focus investments more specifically to the microservices that have the greatest availability needs. For example, to deliver product information pages on Amazon.com (“detail pages”), hundreds of microservices are invoked to build discrete portions of the page. While there are a few services that must be available to provide the price and the product details, the vast majority of content on the page can simply be excluded if the service isn’t available. Even such things as photos and reviews are not required to provide an experience where a customer can buy a product. Best practices • REL03-BP01 Choose how to segment your workload • REL03-BP02 Build services focused on specific business domains and functionality • REL03-BP03 Provide service contracts per API

> **[S5]** `wa-framework#0008` AWS Well-Architected Framework > The pillars of the framework
>
> The pillars of the framework Creating a software system is a lot like constructing a building. If the foundation is not solid, structural problems can undermine the integrity and function of the building. When architecting technology solutions, if you neglect the six pillars of operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability, it can become challenging to build a system that delivers on your expectations and requirements. Incorporating these pillars into your architecture will help you produce stable and efficient systems. This will allow you to focus on the other aspects of design, such as functional requirements. Pillars • Operational excellence • Security • Reliability • Performance efficiency • Cost optimization • Sustainability Operational excellence Operational excellence (OE) is a commitment to build software correctly while consistently delivering a great customer experience. The operational excellence pillar contains best practices for organizing your team, designing your workload, operating it at scale, and evolving it over time. The operational excellence pillar provides an overview of design principles, best practices, and questions. You can find prescriptive guidance on implementation in the Operational Excellence Pillar whitepaper. Topics • Design principles • Definition • Best practices • Resources

**Note (optional):** 

---

## old02 (outdated)

- Correct?          [x] pass   [ ] fail
- Claim not in its source? [x] yes    [ ] no

**Q:** How is the AWS Well-Architected Security pillar broken down into best practice areas?

**Reference answer:** Seven: security foundations, identity and access management, detection, infrastructure protection, data protection, incident response and application security. (The archived July 2020 edition lists six, without application security.)

*Deterministic scorers: pass, key facts 1.00.*

**Answer, claim by claim:**

1. The AWS Well-Architected Security pillar is broken down into seven best practice areas: Security foundations, Identity and access management, Detection, Infrastructure protection, Data protection, Incident response, and Application security. [S2][S4]
2. The Security foundations area is addressed by the question SEC 1, 'How do you securely operate your workload?' [S2][S4]
3. The newer 2024 edition of the Well-Architected Framework replaces the older six-area breakdown, which listed 'Security' as a separate area, so the seven-area breakdown is the current one. [S2][S3]

**Cited sources, full text:**

> **[S2]** `wa-framework#0306` AWS Well-Architected Framework > Appendix: Questions and best practices > Security
>
> Security The Security pillar encompasses the ability to protect data, systems, and assets to take advantage of cloud technologies to improve your security. You can find prescriptive guidance on implementation in the Security Pillar whitepaper. Best practice areas • Security foundations • Identity and access management • Detection • Infrastructure protection • Data protection • Incident response • Application security Security foundations Question • SEC 1. How do you securely operate your workload? SEC 1. How do you securely operate your workload? To operate your workload securely, you must apply overarching best practices to every area of security. Take requirements and processes that you have defined in operational excellence at an organizational and workload level, and apply them to all areas. Staying up to date with AWS and industry recommendations and threat intelligence helps you evolve your threat model and control objectives. Automating security processes, testing, and validation permit you to scale your security operations. Best practices • SEC01-BP01 Separate workloads using accounts • SEC01-BP02 Secure account root user and properties • SEC01-BP03 Identify and validate control objectives • SEC01-BP04 Stay up to date with security threats and recommendations • SEC01-BP05 Reduce security management scope • SEC01-BP06 Automate deployment of standard security controls • SEC01-BP07 Identify threats and prioritize mitigations using a threat model • SEC01-BP08 Evaluate and implement new security services and features regularly

> **[S3]** `wa-framework-old#0024` AWS Well-Architected Framework (older edition) > The Five Pillars of the Framework > Security
>
> Definition There are six best practice areas for security in the cloud: • Security • Identity and Access Management • Detection • Infrastructure Protection • Data Protection • Incident Response Before you architect any workload, you need to put in place practices that influence security. You will want to control who can do what. In addition, you want to be able to identify security incidents, protect your systems and services, and maintain the confidentiality and integrity of data through data protection. You should have a well-defined and practiced process for responding to security incidents. These tools and techniques are important because they support objectives such as preventing financial loss or complying with regulatory obligations. The AWS Shared Responsibility Model enables organizations that adopt the cloud to achieve their security and compliance goals. Because AWS physically secures the infrastructure that supports our cloud services, as an AWS customer you can focus on using services to accomplish your goals. The AWS Cloud also provides greater access to security data and an automated approach to responding to security events. Security To operate your workload securely, you must apply overarching best practices to every area of security. Take requirements and processes that you have defined in operational excellence at an organizational and workload level, and apply them to all areas. Staying up to date with AWS and industry recommendations and threat intelligence helps you evolve your threat model and control objectives. Automating security processes, testing, and validation allow you to scale your security operations. The following questions focus on these considerations for security. (For a list of security questions and best practices, see the Appendix.). SEC 1: How do you securely operate your workload? To operate your workload securely, you must apply overarching best practices to every area of security. Take requirements and processes that you have defined in operational excellence at an organizational and workload level, and apply them to all areas. Staying up to date with AWS and industry recommendations and threat intelligence helps you evolve your threat model and control objectives. Automating security processes, testing, and validation allow you to scale your security operations. In AWS, segregating different workloads by account, based on their function and compliance or data sensitivity requirements, is a recommended approach.

> **[S4]** `wa-framework#0025` AWS Well-Architected Framework > The pillars of the framework > Security
>
> Definition There are seven best practice areas for security in the cloud: • Security foundations • Identity and access management • Detection • Infrastructure protection • Data protection • Incident response • Application security Before you architect any workload, you need to put in place practices that influence security. You will want to control who can do what. In addition, you want to be able to identify security incidents, protect your systems and services, and maintain the confidentiality and integrity of data through data protection. You should have a well-defined and practiced process for responding to security incidents. These tools and techniques are important because they support objectives such as preventing financial loss or complying with regulatory obligations. The AWS Shared Responsibility Model helps organizations that adopt the cloud to achieve their security and compliance goals. Because AWS physically secures the infrastructure that supports our cloud services, as an AWS customer you can focus on using services to accomplish your goals. The AWS Cloud also provides greater access to security data and an automated approach to responding to security events. Best practices Topics • Security foundations • Identity and access management • Detection • Infrastructure protection • Data protection • Incident response • Application security Security foundations The following question focuses on these considerations for security. (For a list of security questions and best practices, see the Appendix.). SEC 1: How do you securely operate your workload? To operate your workload securely, you must apply overarching best practices to every area of security. Take requirements and processes that you have defined in operational excellence at an organizational and workload level, and apply them to all areas. Staying up to date with recommendations from AWS, industry sources, and threat intellige nce helps you evolve your threat model and control objectives. Automating security processes, testing, and validation allow you to scale your security operations. In AWS, segregating different workloads by account, based on their function and compliance or data sensitivity requirements, is a recommended approach.

**Note (optional):** 

---

## old03 (outdated)

- Correct?          [x] pass   [ ] fail
- Claim not in its source? [ ] yes    [x] no

**Q:** How is the Performance Efficiency pillar in AWS Well-Architected broken down into best practice areas?

**Reference answer:** Five: architecture selection, compute and hardware, data management, networking and content delivery, and process and culture. (The archived July 2020 edition lists four: selection, review, monitoring and tradeoffs.)

*Deterministic scorers: pass, key facts 1.00.*

**Answer, claim by claim:**

1. The Performance Efficiency pillar is broken down into five best practice areas: Architecture selection, Compute and hardware, Data management, Networking and content delivery, and Process and culture. [S1][S2][S4]
2. The pillar was restructured in October 2023 to have five best practice areas, down from eight. [S3]

**Cited sources, full text:**

> **[S1]** `wa-framework#0884` AWS Well-Architected Framework > Appendix: Questions and best practices > Performance efficiency
>
> Performance efficiency The Performance Efficiency pillar includes the ability to use cloud resources efficiently to meet performance requirements, and to maintain that efficiency as demand changes and technologies evolve. You can find prescriptive guidance on implementation in the Performance Efficiency Pillar whitepaper. Best practice areas • Architecture selection • Compute and hardware • Data management • Networking and content delivery • Process and culture Architecture selection Questions • PERF 1. How do you select appropriate cloud resources and architecture for your workload? PERF 1. How do you select appropriate cloud resources and architecture for your workload? The optimal solution for a particular workload varies, and solutions often combine multiple approaches. Well-Architected workloads use multiple solutions and allow different features to improve performance. Best practices • PERF01-BP01 Learn about and understand available cloud services and features • PERF01-BP02 Use guidance from your cloud provider or an appropriate partner to learn about architecture patterns and best practices • PERF01-BP03 Factor cost into architectural decisions • PERF01-BP04 Evaluate how trade-offs impact customers and architecture efficiency • PERF01-BP05 Use policies and reference architectures • PERF01-BP06 Use benchmarking to drive architectural decisions • PERF01-BP07 Use a data-driven approach for architectural choices

> **[S2]** `wa-performance-efficiency#0000` Performance Efficiency Pillar - AWS Well-Architected Framework > (no section)
>
> Publication date: November 6, 2024 (Document revisions) This whitepaper focuses on the performance efficiency pillar of the AWS Well-Architected Framework. It provides guidance to help customers apply best practices in the design, delivery, and maintenance of AWS environments. Introduction The AWS Well-Architected Framework helps you understand the pros and cons of decisions you make while building workloads on AWS. Using the Framework helps you learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable workloads in the cloud. The Framework provides a way for you to consistently measure your architectures against best practices and identify areas for improvement. We believe that having well-architected workloads greatly increases the likelihood of business success. The framework is based on six pillars: • Operational Excellence • Security • Reliability • Performance Efficiency • Cost Optimization • Sustainability This paper focuses on applying the principles of the performance efficiency pillar to your workloads. In traditional, on-premises environments, achieving high and lasting performance is challenging. Using the principles in this paper will help you build architectures on AWS that efficiently deliver sustained performance over time. The guidance and best practices in this document are spread across five key focus areas that serve as guiding principles for building performance efficient cloud solutions on AWS. These focus areas are: • Architecture selection • Compute and hardware • Data management • Networking and content delivery • Process and culture This paper is intended for those in technology roles, such as chief technology officers (CTOs), architects, developers, and operations team members. After reading this paper, you’ll understand AWS best practices and strategies to use when designing a performant cloud architecture.

> **[S3]** `wa-performance-efficiency#0115` Performance Efficiency Pillar - AWS Well-Architected Framework > (no section)
>
> Further reading For additional help, consult the following sources: • AWS Well-Architected Framework • AWS Architecture Center Document revisions To be notified about updates to this whitepaper, subscribe to the RSS feed. Change Description Date Minor best practice update PERF03-BP04 was updated with new service recommend ations. November 6, 2024 Updated best practice guidance Multiple small updates throughout the pillar. June 27, 2024 Major update and restructure Pillar restructured to have five best practice areas (down from eight). Content has been consolidated into the five areas and updated. New best practice areas are Architecture selection, Compute and hardware, Data management, Networking and content delivery, and Process and culture. October 3, 2023 Minor update Remove non-inclusive language. April 13, 2023 Updates for new Framework Best practices updated with prescriptive guidance and new best practices added. April 10, 2023 Whitepaper updated Best practices updated with new implementation guidance. December 15, 2022 Whitepaper updated Best practices expanded and improvement plans added. October 20, 2022 Minor update Removed non-inclusive language. April 22, 2022 Minor updates Updated links. March 10, 2021 Minor updates Changed AWS Lambda timeout to 900 seconds and corrected name of Amazon Keyspaces (for Apache Cassandra). October 5, 2020 Minor update Fixed broken link. July 15, 2020 Updates for new Framework Major review and update of content July 8, 2020 Whitepaper updated Minor update for grammatical issues July 1, 2018 Whitepaper updated Refreshed the whitepaper to reflect changes in AWS November 1, 2017 Initial publication Performance Efficiency Pillar - AWS Well-Architected Framework published. November 1, 2016

> **[S4]** `wa-framework#0045` AWS Well-Architected Framework > The pillars of the framework > Performance efficiency
>
> Definition There are five best practice areas for performance efficiency in the cloud: • Architecture selection • Compute and hardware • Data management • Networking and content delivery • Process and culture Take a data-driven approach to building a high-performance architecture. Gather data on all aspects of the architecture, from the high-level design to the selection and configuration of resource types. Reviewing your choices on a regular basis validates that you are taking advantage of the continually evolving AWS Cloud. Monitoring verifies that you are aware of any deviance from expected performance. Make trade-offs in your architecture to improve performance, such as using compression or caching, or relaxing consistency requirements. Best practices Topics • Architecture selection • Compute and hardware • Data management • Networking and content delivery • Process and culture Architecture selection The optimal solution for a particular workload varies, and solutions often combine multiple approaches. Well-Architected workloads use multiple solutions and allow different features to improve performance. AWS resources are available in many types and configurations, which makes it easier to find an approach that closely matches your needs. You can also find options that are not easily achievable with on-premises infrastructure. For example, a managed service such as Amazon DynamoDB provides a fully managed NoSQL database with single-digit millisecond latency at any scale. The following question focuses on these considerations for performance efficiency. (For a list of performance efficiency questions and best practices, see the Appendix.). PERF 1: How do you select appropriate cloud resources and architecture patterns for your workload? Often, multiple approaches are required for more effective performance across a workload. Well-Architected systems use multiple solutions and features to improve performance.

**Note (optional):** 

---

## one01 (single)

- Correct?          [x] pass   [ ] fail
- Claim not in its source? [ ] yes    [x] no

**Q:** What steps does the Reliability pillar recommend to make sure that all workload data that needs a backup is backed up?

**Reference answer:** Identify all data sources of the workload (databases, volumes, file systems, logging systems, object storage), classify them by criticality (RPO and RTO requirements), and create backups with AWS or third-party services such as AWS Backup, AWS Elastic Disaster Recovery or the services' native backup features. Data that can be reproduced from its sources does not need a backup.

*Deterministic scorers: pass, key facts 1.00.*

**Answer, claim by claim:**

1. Identify all data sources for the workload, such as databases, volumes, filesystems, logging systems, and object storage. [S4]
2. Classify the data sources based on criticality, because different data sets have different resiliency requirements, including different RPO and RTO needs. [S4]
3. Use AWS or third-party services to create backups of the data, such as AWS Backup, AWS Elastic Disaster Recovery, or the native backup capabilities of most AWS services. [S4]
4. For data that is not backed up, establish a data reproduction mechanism, weighing tradeoffs such as backup storage cost and whether restoring from a backup would breach the RTO compared with reproducing the data from sources. [S3]
5. Establish a cadence for backing up data, with the backup frequency depending on the RPO. [S3]
6. Determine the RPO for the workload, referring to REL13-BP01 Define recovery objectives for downtime and data loss. [S5]
7. Use an automated backup solution or managed service, such as AWS Backup backup plans that define the resources to back up and the backup frequency informed by the RPO. [S5]
8. For data sources not supported by an automated backup solution or managed service, such as on-premises data sources or message queues, use a trusted third-party solution or automation built with the AWS CLI or SDKs, such as AWS Lambda or AWS Step Functions invoked by Amazon EventBridge at a frequency based on the RPO. [S5]

**Cited sources, full text:**

> **[S3]** `wa-reliability#0189` Reliability Pillar - AWS Well-Architected Framework > Failure management > Back up data > REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources > Implementation guidance
>
> 4. For data that is not backed up, establish a data reproduction mechanism. You might choose not to backup data that can be reproduced from other sources for various reasons. There might be a situation where it is cheaper to reproduce data from sources when needed rather than creating a backup as there may be a cost associated with storing backups. Another example is where restoring from a backup takes longer than reproducing the data from sources, resulting in a breach in RTO. In such situations, consider tradeoffs and establish a well-defined process for how data can be reproduced from these sources when data recovery is necessary. For example, if you have loaded data from Amazon S3 to a data warehouse (like Amazon Redshift), or MapReduce cluster (like Amazon EMR) to do analysis on that data, this may be an example of data that can be reproduced from other sources. As long as the results of these analyses are either stored somewhere or reproducible, you would not suffer a data loss from a failure in the data warehouse or MapReduce cluster. Other examples that can be reproduced from sources include caches (like Amazon ElastiCache) or RDS read replicas. 5. Establish a cadence for backing up data. Creating backups of data sources is a periodic process and the frequency should depend on the RPO. Level of effort for the Implementation Plan: Moderate

> **[S4]** `wa-reliability#0188` Reliability Pillar - AWS Well-Architected Framework > Failure management > Back up data > REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources > Implementation guidance
>
> REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources 1. Identify all data sources for the workload. Data can be stored on a number of resources such as databases, volumes, filesystems, logging systems, and object storage. Refer to the Resources section to find Related documents on different AWS services where data is stored, and the backup capability these services provide. 2. Classify data sources based on criticality. Different data sets will have different levels of criticality for a workload, and therefore different requirements for resiliency. For example, some data might be critical and require a RPO near zero, while other data might be less critical and can tolerate a higher RPO and some data loss. Similarly, different data sets might have different RTO requirements as well. 3. Use AWS or third-party services to create backups of the data. AWS Backup is a managed service that allows creating backups of various data sources on AWS. AWS Elastic Disaster Recovery handles automated sub-second data replication to an AWS Region. Most AWS services also have native capabilities to create backups. The AWS Marketplace has many solutions that provide these capabilites as well. Refer to the Resources listed below for information on how to create backups of data from various AWS services.

> **[S5]** `wa-reliability#0197` Reliability Pillar - AWS Well-Architected Framework > Failure management > Back up data > REL09-BP03 Perform data backup automatically > Implementation guidance
>
> 2. Determine the RPO for the workload. For more detail, see REL13-BP01 Define recovery objectives for downtime and data loss. 3. Use an automated backup solution or managed service. AWS Backup is a fully-managed service that makes it easy to centralize and automate data protection across AWS services, in the cloud, and on-premises. Using backup plans in AWS Backup, create rules which define the resources to backup, and the frequency at which these backups should be created. This frequency should be informed by the RPO established in Step 2. For hands-on guidance on how to create automated backups using AWS Backup, see Testing Backup and Restore of Data. Native backup capabilities are offered by most AWS services that store data. For example, RDS can be leveraged for automated backups with point-in-time recovery (PITR). 4. For data sources not supported by an automated backup solution or managed service such as on-premises data sources or message queues, consider using a trusted third-party solution to create automated backups. Alternatively, you can create automation to do this using the AWS CLI or SDKs. You can use AWS Lambda Functions or AWS Step Functions to define the logic involved in creating a data backup, and use Amazon EventBridge to invoke it at a frequency based on your RPO. Level of effort for the Implementation Plan: Low

**Note (optional):** 

---

## one02 (single)

- Correct?          [ ] pass   [x] fail
- Claim not in its source? [ ] yes    [x] no

**Q:** What are the default snapshot retention settings of snapshot management in Amazon S3 Tables?

**Reference answer:** MinimumSnapshots is 1 and MaximumSnapshotAge is 120 hours by default. Expired snapshots are removed, and objects referenced only by them become noncurrent and are deleted after the NoncurrentDays of the unreferenced file removal policy.

*Deterministic scorers: pass, key facts 1.00.*

**Answer, claim by claim:**

1. The default MinimumSnapshots setting for snapshot management is 1, which sets the minimum number of active snapshots kept for a table. [S1][S2]
2. The default MaximumSnapshotAge setting for snapshot management is 120 hours. [S1][S2]

**Cited sources, full text:**

> **[S1]** `s3-tables-maintenance#0004` Amazon S3 User Guide: Maintenance for tables > Snapshot management
>
> Snapshot management Snapshot management determines the number of active snapshots for your table. This is based on the MinimumSnapshots (1 by default) and MaximumSnapshotAge (120 hours by default). Snapshot management expires and removes table snapshots based on these configurations. When a snapshot expires, Amazon S3 marks any objects referenced only by that snapshot as noncurrent. These noncurrent objects are deleted after the number of days specified by the NoncurrentDays property in your unreferenced file removal policy. Note Deletes of noncurrent objects are permanent with no way to recover these objects. To view or recover objects that has been marked as noncurrent you must contact AWS Support. For information about contacting AWS Support, see Contact AWS or the AWS Support Documentation. Snapshot management determines the objects to delete from your table with references only to that table. References to these objects from outside the table will not prevent snapshot management from deleting them. Note Snapshot management does not support retention values that you configure as Apache Iceberg table properties in the metadata.json file or through an ALTER TABLE SET TBLPROPERTIES SQL command. If any of the following conditions exist, snapshot management will fail for the entire table and Amazon S3 will not expire or remove any snapshots: - User-defined tags or branches – If any user-defined tag or branch exists on the table, snapshot management will fail for the entire table. This applies even if the tag or branch has a short retention period. To restore automated snapshot expiration, remove all user-defined tags and branches from the table. - Iceberg snapshot retention table properties – If the history.expire.max-snapshot-age-ms or history.expire.min-snapshots-to-keep property is set as an Apache Iceberg table property, snapshot management will fail for the entire table regardless of the configured value. To restore automated snapshot expiration, remove these properties: ALTER TABLE mydb.mytable UNSET TBLPROPERTIES ('history.expire.max-snapshot-age-ms'); ALTER TABLE mydb.mytable UNSET TBLPROPERTIES ('history.expire.min-snapshots-to-keep');

> **[S2]** `s3-tables-maintenance#0006` Amazon S3 User Guide: Maintenance for tables > Snapshot management > Snapshot Management Examples
>
> Snapshot Management Examples The following examples show configurations for table snapshot management. To configure the snapshot management by using the AWS CLI The following example will set the MinimumSnapshots to 10 and the MaximumSnapshotAge to 2500 hours using the PutTableMaintenanceConfiguration API. aws s3tables put-table-maintenance-configuration \ --table-bucket-arn arn:aws:s3tables:us-east-1:111122223333:bucket/amzn-s3-demo-table-bucket \ --namespace my_namespace \ --name my_table \ --type icebergSnapshotManagement \ --value '{"status":"enabled","settings":{"icebergSnapshotManagement":{"minSnapshotsToKeep":10,"maxSnapshotAgeHours":2500}}}' To disable snapshot management by using the AWS CLI The following example will disable snapshot management using the PutTableMaintenanceConfiguration API. aws s3tables put-table-maintenance-configuration \ --table-bucket-arn arn:aws:s3tables:us-east-1:111122223333:bucket/amzn-s3-demo-table-bucket \ --namespace my_namespace \ --name my_table \ --type icebergSnapshotManagement \ --value '{"status":"disabled","settings":{"icebergSnapshotManagement":{"minSnapshotsToKeep":1,"maxSnapshotAgeHours":120}}}' For more information, see put-table-maintenance-configuration in the AWS CLI Command Reference.

**Note (optional):** 

---

## one03 (single)

- Correct?          [x] pass   [ ] fail
- Claim not in its source? [ ] yes    [x] no

**Q:** Which Apache Iceberg version does Amazon Athena support?

**Reference answer:** Athena supports Apache Iceberg version 1.4.2.

*Deterministic scorers: pass, key facts 1.00.*

**Answer, claim by claim:**

1. Amazon Athena supports Apache Iceberg version 1.4.2. [S1]

**Cited sources, full text:**

> **[S1]** `athena-iceberg-query#0001` Amazon Athena User Guide: Query Apache Iceberg tables > Considerations and limitations
>
> Considerations and limitations Athena support for Iceberg tables has the following considerations and limitations: - Iceberg version support – Athena supports Apache Iceberg version 1.4.2. - Tables registered with Lake Formation – Athena does not currently support DDL operations on Iceberg tables that are registered with Lake Formation. - Queries against information schema – When querying the information schema of Iceberg tables, Athena uses S3 metadata as the source of truth for column metadata. This means that column information is derived from the underlying S3 files rather than from the catalog metadata. This behavior differs from other table formats where catalog metadata might be the primary source for column information. - Tables with AWS Glue catalog only – Only Iceberg tables created against the AWS Glue catalog based on specifications defined by the open source glue catalog implementation are supported from Athena. - Table locking support by AWS Glue only – Unlike the open source Glue catalog implementation, which supports plug-in custom locking, Athena supports AWS Glue optimistic locking only. Using Athena to modify an Iceberg table with any other lock implementation will cause potential data loss and break transactions. - Supported file formats – Athena engine version 3 supports the following Iceberg file formats. Parquet ORC Avro - Iceberg restricted metadata – Lake Formation does not evaluate the Iceberg metadata tables. Hence, the Iceberg metadata tables are restricted if there are any Lake Formation row or cell filters present on the base table or if you do not have permissions to view all columns in the base table. For such cases, when you query the $partitions, $files, $manifests, and $snapshots Iceberg metadata tables, it fails and you get an AccessDeniedException error. Additionally, the metadata column $path has the same Lake Formation restrictions and fails when selected by the query. All other metadata tables can be queried regardless of the Lake Formation filters. For more information, see Metadata tables. - Iceberg v2 tables – Athena only creates and operates on Iceberg v2 tables. For the difference between v1 and v2 tables, see Format version changes in the Apache Iceberg documentation.

**Note (optional):** 

---

## one04 (single)

- Correct?          [x] pass   [ ] fail
- Claim not in its source? [ ] yes    [x] no

**Q:** When should I use the ALL distribution style for an Amazon Redshift table?

**Reference answer:** When the table used in the join condition is small, less than 1 GB.

*Deterministic scorers: pass, key facts 1.00.*

**Answer, claim by claim:**

1. Consider the ALL distribution style when the table used in the join condition is small, less than 1 GB. [S1]

**Cited sources, full text:**

> **[S1]** `pg-redshift-tables#0002` Query best practices for Amazon Redshift: Best practices for designing Amazon Redshift tables > Choose the right table distribution style
>
> Choose the right table distribution style When you run a query, the query optimizer redistributes the rows to the compute nodes as needed to perform any joins and aggregations. The goal in selecting a table distribution style is to minimize the impact of the redistribution step by locating the data where it needs to be before you run the query. We recommend the following approach to choosing the right table distribution style: - Avoid broadcasting and redistribution in a query execution plan by collocating the rows within the same node. For example, by selecting a DISTKEY, you can distribute the fact table and one-dimension table on their common columns. Choose the largest dimension based on the size of the filtered dataset. Only the rows that are used in the join must be distributed, so consider the size of the dataset after filtering, not the size of the table. - Make sure there is no skewness on the column where the distribution key is created. Otherwise, one compute node could perform more heavy lifting than others. If you notice skewness, then consider changing the distribution key column. A column can be considered as a candidate for a distribution key if its values are uniformly distributed or high cardinal values. - If the table used in the join condition is small (less than 1 GB), then consider the distribution style ALL. - You can compress the distribution key, but you must avoid compressing the sort key column (especially the first column of the sort key). | Note: If you use automatic table optimization, you don't need to choose the distribution style of your table. For more information, see Working with automatic table optimization in the Amazon Redshift documentation. To have Amazon Redshift choose the appropriate distribution style, specify AUTO for the distribution style. | | --- |

**Note (optional):** 

---

## sim01 (similar) — answer of run k=3 (only the top 3 sources in context) `claude-haiku-5-5__v1__medium__k3`

- Correct?          [ ] pass   [x] fail
- Claim not in its source? [x] yes    [ ] no

**Q:** How does scaling our infrastructure with demand make our workload more sustainable, and what should we scale besides compute?

**Reference answer:** Elasticity matches the supply of resources to demand, so the workload scales down quickly in periods of low load (EC2 Auto Scaling, Application Auto Scaling, Kubernetes Cluster Autoscaler). Non-compute services should match demand too, such as Amazon DynamoDB read and write capacity units and Amazon Kinesis Data Streams shards.

*Deterministic scorers: fail, key facts 0.00.*

**Answer, claim by claim:**

1. Matching cloud supply to demand delivers the lowest environmental impact for a workload. [S2]
2. Scaling infrastructure dynamically to match demand helps avoid overprovisioned capacity, so you use only the number of resources needed to meet business requirements. [S1]
3. Scaling should also remove excess capacity when utilization is low, and you should not leave increased capacity in place after a scaling event instead of scaling back down. [S2][S1]
4. Applications can scale vertically by changing instance size, horizontally by changing the number of instances, or both. [S2]
5. Ways to match supply to demand include target-tracking, predictive scaling, schedule-based scaling, and using services that scale natively or provide auto scaling as a feature, such as serverless services. [S2]
6. The sources describe scaling in general terms of infrastructure and cloud resources, and they do not name specific resource types other than compute to scale. [S1][S2]
7. The guidance also says to remove unused assets and to verify that you use only the minimum resources required to support your users. [S1]

**Cited sources, full text:**

> **[S1]** `wa-framework#1207` AWS Well-Architected Framework > Appendix: Questions and best practices > Sustainability > Alignment to demand
>
> Alignment to demand Question • SUS 2 How do you align cloud resources to your demand? SUS 2 How do you align cloud resources to your demand? The way users and applications consume your workloads and other resources can help you identify improvements to meet sustainability goals. Scale infrastructure to continually match demand and verify that you use only the minimum resources required to support your users. Align service levels to customer needs. Position resources to limit the network required for users and applications to consume them. Remove unused assets. Provide your team members with devices that support their needs and minimize their sustainability impact. Best practices • SUS02-BP01 Scale workload infrastructure dynamically • SUS02-BP02 Align SLAs with sustainability goals • SUS02-BP03 Stop the creation and maintenance of unused assets • SUS02-BP04 Optimize geographic placement of workloads based on their networking requirements • SUS02-BP05 Optimize team member resources for activities performed • SUS02-BP06 Implement buffering or throttling to flatten the demand curve SUS02-BP01 Scale workload infrastructure dynamically Use elasticity of the cloud and scale your infrastructure dynamically to match supply of cloud resources to demand and avoid overprovisioned capacity in your workload. Common anti-patterns: • You do not scale your infrastructure with user load. • You manually scale your infrastructure all the time. • You leave increased capacity after a scaling event instead of scaling back down. Benefits of establishing this best practice: Configuring and testing workload elasticity help to efficiently match supply of cloud resources to demand and avoid overprovisioned capacity. You can take advantage of elasticity in the cloud to automatically scale capacity during and after demand spikes to make sure you are only using the right number of resources needed to meet your business requirements. Level of risk exposed if this best practice is not established: Medium

> **[S2]** `wa-sustainability#0021` Sustainability Pillar - AWS Well-Architected Framework > Best practices for sustainability in the cloud > Alignment to demand > SUS02-BP01 Scale workload infrastructure dynamically > Implementation guidance
>
> Implementation guidance The cloud provides the flexibility to expand or reduce your resources dynamically through a variety of mechanisms to meet changes in demand. Optimally matching supply to demand delivers the lowest environmental impact for a workload. Demand can be fixed or variable, requiring metrics and automation to make sure that management does not become burdensome. Applications can scale vertically (up or down) by modifying the instance size, horizontally (in or out) by modifying the number of instances, or a combination of both. You can use a number of different approaches to match supply of resources with demand. • Target-tracking approach: Monitor your scaling metric and automatically increase or decrease capacity as you need it. • Predictive scaling: Scale in anticipation of daily and weekly trends. • Schedule-based approach: Set your own scaling schedule according to predictable load changes. • Service scaling: Pick services (like serverless) that are natively scaling by design or provide auto scaling as a feature. Identify periods of low or no utilization and scale resources to remove excess capacity and improve efficiency.

**Note (optional):** changed after judge review (17.11): claim not in its source no → yes. Claim 6 ("the sources do not name specific resource types other than compute") is the model's conclusion, not text of the cited sources.

---

## many04 (multi) — answer of run k=3 (only the top 3 sources in context) `claude-haiku-5-5__v1__medium__k3`

- Correct?          [ ] pass   [x] fail
- Claim not in its source? [ ] yes    [x] no

**Q:** An AWS Glue Spark job is slow: how do I see that it lacks parallelism, and how can it read less data?

**Reference answer:** Lack of parallelism shows in CloudWatch metrics (some executors idle in CPU load and memory utilization) and in the Spark UI (few tasks per stage); the number of RDD partitions sets the degree of parallelism. To read less data, use a columnar format such as Parquet or ORC and prune partitions, for example with push_down_predicate on a DynamicFrame.

*Deterministic scorers: fail, key facts 0.25.*

**Answer, claim by claim:**

1. A lack of parallelism shows up in CloudWatch metrics: if some executors are not processing during a phase of the job, parallelism should be improved. [S2]
2. In the Spark UI, the Stage tab shows the number of tasks in a stage; if only one task runs, the work was done entirely on one executor while the others were idle. [S2]
3. In the Spark UI event timeline, one executor processing a single task while the other executors sit idle is a symptom of insufficient parallelism. [S2]
4. To reduce the amount of data a Glue Spark job loads from Amazon S3, consider the file size, compression, file format, and file layout (partitions) of the dataset. [S3]
5. Keep the file size of inputs and outputs within a moderate range, for example around 128 MB, because files that are too small or too large can cause issues. [S3]
6. A large number of small files creates heavy network I/O on Amazon S3 from the overhead of many List, Get, or Head requests, and heavy load on the Spark driver that leads to excessive parallelism. [S3]
7. To reduce the excessive parallelism caused by many small files, use file grouping for DynamicFrames by setting the groupFiles and groupSize parameters, which also reduces the chance of an OOM exception on the Spark driver. [S3]
8. If the file type is not splittable, such as gzip, and the files are very large, the Spark application must wait until a single task finishes reading the entire file. [S3]

**Cited sources, full text:**

> **[S2]** `pg-glue-parallelize-tasks#0000` Best practices for performance tuning AWS Glue for Apache Spark jobs: Parallelize tasks > (no section)
>
> To optimize performance, it's important to parallelize tasks for data loads and transformations. As we discussed in Key topics in Apache Spark, the number of resilient distributed dataset (RDD) partitions is important, because it determines the degree of parallelism. Each task that Spark creates corresponds to an RDD partition on a 1:1 basis. To achieve the best performance, you need to understand how the number of RDD partitions is determined and how that number is optimized. If you do not have enough parallelism, the following symptoms will be recorded in CloudWatch metrics and the Spark UI. CloudWatch metrics Check the CPU Load and Memory Utilization. If some executors are not processing during a phase of your job, it's appropriate to improve parallelism. In this case, during the visualized timeframe, Executor 1 was performing a task, but the remaining executors (2, 3, and 4) were not. You can infer that those executors were not assigned tasks by the Spark driver. Spark UI On the Stage tab in the Spark UI, you can see the number of tasks in a stage. In this case, Spark has performed only one task. Additionally, the event timeline shows Executor 1 processing one task. This means that the work in this stage was performed entirely on one executor, while the others were idle. If you observe these symptoms, try the following solutions for each data source.

> **[S3]** `pg-glue-reduce-data-scan#0001` Best practices for performance tuning AWS Glue for Apache Spark jobs: Reduce the amount of data scan > Spark UI > Amazon S3
>
> Amazon S3 To reduce the amount of data loaded into your job when reading from Amazon S3, consider file size, compression, file format, and file layout (partitions) for your dataset. AWS Glue for Spark jobs are often used for ETL of raw data, but for efficient distributed processing, you need to inspect the features of your data source format. - File size – We recommend keeping the file size of inputs and outputs within a moderate range (for example, 128 MB). Files that are too small and files that are too large can cause issues.A large number of small files cause following issues:Heavy network I/O load on Amazon S3 because of the overhead required to make requests (such as List, Get, or Head) for many objects (compared with a few objects that store the same quantity of data).Heavy I/O and processing load on the Spark driver, which will generate many partitions and tasks and lead to excessive parallelism.On the other hand, if your file type is not splittable (such as gzip) and the files are too large, the Spark application must wait until a single task has completed reading the entire file.To reduce excessive parallelism incurred when an Apache Spark task is created for each small file, use file grouping for DynamicFrames. This approach reduces the chances of an OOM exception from the Spark driver. To configure file grouping, set the groupFiles and groupSize parameters. The following code example uses the AWS Glue DynamicFrame API in an ETL script with these parameters.dyf = glueContext.create_dynamic_frame_from_options("s3", {'paths': ["s3://input-s3-path/"], 'recurse':True, 'groupFiles': 'inPartition', 'groupSize': '1048576'}, format="json")

**Note (optional):** 

---

## one01 (single) — answer of run k=3 (only the top 3 sources in context) `claude-haiku-5-5__v1__medium__k3`

- Correct?          [ ] pass   [x] fail
- Claim not in its source? [ ] yes    [x] no

**Q:** What steps does the Reliability pillar recommend to make sure that all workload data that needs a backup is backed up?

**Reference answer:** Identify all data sources of the workload (databases, volumes, file systems, logging systems, object storage), classify them by criticality (RPO and RTO requirements), and create backups with AWS or third-party services such as AWS Backup, AWS Elastic Disaster Recovery or the services' native backup features. Data that can be reproduced from its sources does not need a backup.

*Deterministic scorers: fail, key facts 0.33.*

**Answer, claim by claim:**

1. Identify the data sources that the workload currently backs up and where those backups are stored, as part of REL09-BP01 (identify and back up all data that needs to be backed up, or reproduce it from sources). [S1]
2. Classify the workload's data sources by criticality and establish a data recovery strategy based on the RPO, which involves either backing up those sources or being able to reproduce the data from other sources. [S2]
3. For data that is not backed up, establish a well-defined data reproduction mechanism, because some data may be cheaper to reproduce from sources than to back up, or restoring from a backup may take longer than reproducing it and breach the RTO. [S3]
4. Establish a cadence for backing up data, with the backup frequency depending on the RPO. [S3]

**Cited sources, full text:**

> **[S1]** `wa-reliability#0200` Reliability Pillar - AWS Well-Architected Framework > Failure management > Back up data > REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes > Implementation guidance
>
> Implementation guidance Testing backup and restore capability increases confidence in the ability to perform these actions during an outage. Periodically restore backups to a new location and run tests to verify the integrity of the data. Some common tests that should be performed are checking if all data is available, is not corrupted, is accessible, and that any data loss falls within the RPO for the workload. Such tests can also help ascertain if recovery mechanisms are fast enough to accommodate the workload's RTO. Using AWS, you can stand up a testing environment and restore your backups to assess RTO and RPO capabilities, and run tests on data content and integrity. Additionally, Amazon RDS and Amazon DynamoDB allow point-in-time recovery (PITR). Using continuous backup, you can restore your dataset to the state it was in at a specified date and time. If all the data is available, is not corrupted, is accessible, and any data loss falls within the RPO for the workload. Such tests can also help ascertain if recovery mechanisms are fast enough to accommodate the workload's RTO. AWS Elastic Disaster Recovery offers continual point-in-time recovery snapshots of Amazon EBS volumes. As source servers are replicated, point-in-time states are chronicled over time based on the configured policy. Elastic Disaster Recovery helps you verify the integrity of these snapshots by launching instances for test and drill purposes without redirecting the traffic. Implementation steps 1. Identify data sources that are currently being backed up and where these backups are being stored. For implementation guidance, see REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources. 2. Establish criteria for data validation for each data source. Different types of data will have different properties which might require different validation mechanisms. Consider how this data might be validated before you are confident to use it in production. Some common ways to validate data are using data and backup properties such as data type, format, checksum, size, or a combination of these with custom validation logic. For example, this might be a comparison of the checksum values between the restored resource and the data source at the time the backup was created.

> **[S2]** `wa-reliability#0186` Reliability Pillar - AWS Well-Architected Framework > Failure management > Back up data
>
> Back up data Back up data, applications, and configuration to meet requirements for recovery time objectives (RTO) and recovery point objectives (RPO). Best practices • REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources • REL09-BP02 Secure and encrypt backups • REL09-BP03 Perform data backup automatically • REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources Understand and use the backup capabilities of the data services and resources used by the workload. Most services provide capabilities to back up workload data. Desired outcome: Data sources have been identified and classified based on criticality. Then, establish a strategy for data recovery based on the RPO. This strategy involves either backing up these data sources, or having the ability to reproduce data from other sources. In the case of data loss, the strategy implemented allows recovery or the reproduction of data within the defined RPO and RTO. Cloud maturity phase: Foundational Common anti-patterns: • Not aware of all data sources for the workload and their criticality. • Not taking backups of critical data sources. • Taking backups of only some data sources without using criticality as a criterion. • No defined RPO, or backup frequency cannot meet RPO. • Not evaluating if a backup is necessary or if data can be reproduced from other sources. Benefits of establishing this best practice: Identifying the places where backups are necessary and implementing a mechanism to create backups, or being able to reproduce the data from an external source improves the ability to restore and recover data during an outage. Level of risk exposed if this best practice is not established: High

> **[S3]** `wa-reliability#0189` Reliability Pillar - AWS Well-Architected Framework > Failure management > Back up data > REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources > Implementation guidance
>
> 4. For data that is not backed up, establish a data reproduction mechanism. You might choose not to backup data that can be reproduced from other sources for various reasons. There might be a situation where it is cheaper to reproduce data from sources when needed rather than creating a backup as there may be a cost associated with storing backups. Another example is where restoring from a backup takes longer than reproducing the data from sources, resulting in a breach in RTO. In such situations, consider tradeoffs and establish a well-defined process for how data can be reproduced from these sources when data recovery is necessary. For example, if you have loaded data from Amazon S3 to a data warehouse (like Amazon Redshift), or MapReduce cluster (like Amazon EMR) to do analysis on that data, this may be an example of data that can be reproduced from other sources. As long as the results of these analyses are either stored somewhere or reproducible, you would not suffer a data loss from a failure in the data warehouse or MapReduce cluster. Other examples that can be reproduced from sources include caches (like Amazon ElastiCache) or RDS read replicas. 5. Establish a cadence for backing up data. Creating backups of data sources is a periodic process and the frequency should depend on the RPO. Level of effort for the Implementation Plan: Moderate

**Note (optional):** 

---

## sim02 (similar) — answer of run k=3 (only the top 3 sources in context) `claude-haiku-5-5__v1__medium__k3`

- Correct?          [x] pass   [ ] fail
- Claim not in its source? [ ] yes    [x] no

**Q:** We want to reduce unnecessary backup storage — which data can we skip backing up to make our workload more sustainable?

**Reference answer:** Data that has no business value or can be easily recreated, and ephemeral storage that does not help in a recovery. Back up only data that has business value or is needed for compliance.

*Deterministic scorers: fail, key facts 0.67.*

**Answer, claim by claim:**

1. Only back up data that has business value or is required to satisfy compliance requirements. [S1][S3]
2. Data that can be easily recreated can be excluded from backups. [S1]
3. Ephemeral data that doesn't provide value in a recovery scenario can be excluded from backups. [S1][S3]
4. Local copies of data can be excluded from backups, unless the time required to restore that data from a common location exceeds your service-level agreements (SLAs). [S1]
5. Classify your data first, using a data classification policy, so you can determine which data is critical enough to back up. [S1][S2]
6. Design the backup strategy based on the criticality of your data classification, your recovery time objective (RTO), and your recovery point objective (RPO), and avoid backing up non-critical data. [S1]

**Cited sources, full text:**

> **[S1]** `wa-sustainability#0073` Sustainability Pillar - AWS Well-Architected Framework > Best practices for sustainability in the cloud > Data management > SUS04-BP08 Back up data only when difficult to recreate
>
> SUS04-BP08 Back up data only when difficult to recreate Avoid backing up data that has no business value to minimize storage resources requirements for your workload. Common anti-patterns: • You do not have a backup strategy for your data. • You back up data that can be easily recreated. Benefits of establishing this best practice: Avoiding back-up of non-critical data reduces the required storage resources for the workload and lowers its environmental impact. Level of risk exposed if this best practice is not established: Medium Implementation guidance Avoiding the back up of unnecessary data can help lower cost and reduce the storage resources used by the workload. Only back up data that has business value or is needed to satisfy compliance requirements. Examine backup policies and exclude ephemeral storage that doesn’t provide value in a recovery scenario. Implementation steps • Classify data: Implement data classification policy as outlined in SUS04-BP01 Implement a data classification policy. • Design a backup strategy: Use the criticality of your data classification and design backup strategy based on your recovery time objective (RTO) and recovery point objective (RPO). Avoid backing up non-critical data. • Exclude data that can be easily recreated. • Exclude ephemeral data from your backups. • Exclude local copies of data, unless the time required to restore that data from a common location exceeds your service-level agreements (SLAs). • Use automated backup: Use an automated solution or managed service to back up businesscritical data. • AWS Backup is a fully-managed service that makes it easy to centralize and automate data protection across AWS services, in the cloud, and on premises. For hands-on guidance on how to create automated backups using AWS Backup, see Well-Architected Labs - Testing Backup and Restore of Data. • Automate backups and optimize backup costs for Amazon EFS using AWS Backup.

> **[S2]** `wa-framework#0070` AWS Well-Architected Framework > The pillars of the framework > Sustainability > Best practices > Data management
>
> Data management The following question focuses on these considerations for sustainability: SUS 4: How do you take advantage of data management policies and patterns to support your sustainability goals? Implement data management practices to reduce the provisioned storage required to support your workload, and the resources required to use it. Understand your data, and use storage technologies and configurations that most effectively supports the business value of the data and how it’s used. Lifecycle data to more efficient, less performant storage when requirements decrease, and delete data that’s no longer required. Implement a data classification policy: Classify data to understand its significance to business outcomes. Use this information to determine when you can move data to more energy-efficient storage or safely delete it. Use technologies that support data access and storage patterns: Use storage that most effectively supports how your data is accessed and stored to minimize the resources provisioned while supporting your workload. For example, solid state devices (SSDs) are more energy intensive than magnetic drives and should be used only for active data use cases. Use energy-efficient, archivalclass storage for infrequently accessed data. Use lifecycle policies to delete unnecessary data: Manage the lifecycle of all your data and automatically enforce deletion timelines to minimize the total storage requirements of your workload. Minimize over-provisioning in block storage: To minimize total provisioned storage, create block storage with size allocations that are appropriate for the workload. Use elastic volumes to expand storage as data grows without having to resize storage attached to compute resources. Regularly review elastic volumes and shrink over-provisioned volumes to fit the current data size. Remove unneeded or redundant data: Duplicate data only when necessary to minimize total storage consumed. Use backup technologies that deduplicate data at the file and block level. Limit the use of Redundant Array of Independent Drives (RAID) configurations except where required to meet SLAs.

> **[S3]** `wa-framework#0071` AWS Well-Architected Framework > The pillars of the framework > Sustainability > Best practices > Data management
>
> Use shared file systems or object storage to access common data: Adopt shared storage and single sources of truth to avoid data duplication and reduce the total storage requirements of your workload. Fetch data from shared storage only as needed. Detach unused volumes to release resources. Minimize data movement across networks: Use shared storage and access data from Regional data stores to minimize the total networking resources required to support data movement for your workload. Back up data only when difficult to recreate: To minimize storage consumption, only back up data that has business value or is required to satisfy compliance requirements. Examine backup policies and exclude ephemeral storage that doesn’t provide value in a recovery scenario.

**Note (optional):** 

---

## sim03 (similar) — answer of run k=3 (only the top 3 sources in context) `claude-haiku-5-5__v1__medium__k3`

- Correct?          [ ] pass   [x] fail
- Claim not in its source? [ ] yes    [x] no

**Q:** Our API gets spiky traffic and I want to keep the bill down — when should we throttle requests, and when should we queue them?

**Reference answer:** Throttle when the clients can retry their requests; use a buffer when the clients cannot retry. Both flatten the demand peaks and reduce the provisioned capacity the workload needs.

*Deterministic scorers: fail, key facts 0.67.*

**Answer, claim by claim:**

1. Throttle requests when arrival rates exceed the known capacity the service is designed to process, since that capacity can be established through load testing. [S2]
2. Requests below the throttling rate are processed, while requests over the defined limit are rejected with a message indicating they were throttled. [S1]
3. Throttling lets the consumer handle the error and retry later. [S2]
4. API Gateway can be configured with throttling limits and returns 429 Too Many Requests errors when limits are exceeded. [S3]
5. Queue or stream requests when your system can tolerate asynchronous processing, because putting messages into a queue or stream speeds up responses to service clients and allows bursts to higher throttle rates. [S3]
6. Amazon SQS and Amazon Kinesis can buffer requests to smooth out the request rate and allow higher throttling rates for requests that can be addressed. [S2]
7. Use API Gateway with native service integrations to Amazon SQS or Kinesis to buffer requests. [S3]
8. When Amazon SQS queues trigger Lambda consumers, set maximum concurrency to a value that meets your service level objectives without consuming concurrency limits needed by other Lambda functions. [S3]
9. Test the throttling limits you plan to set and do not increase limits beyond what you established in testing. [S3]

**Cited sources, full text:**

> **[S1]** `wa-reliability#0098` Reliability Pillar - AWS Well-Architected Framework > Workload architecture > Design interactions in a distributed system to mitigate or withstand failures > REL05-BP02 Throttle requests
>
> REL05-BP02 Throttle requests Throttle requests to mitigate resource exhaustion due to unexpected increases in demand. Requests below throttling rates are processed while those over the defined limit are rejected with a return message indicating the request was throttled. Desired outcome: Large volume spikes either from sudden customer traffic increases, flooding attacks, or retry storms are mitigated by request throttling, allowing workloads to continue normal processing of supported request volume. Common anti-patterns: • API endpoint throttles are not implemented or are left at default values without considering expected volumes. • API endpoints are not load tested or throttling limits are not tested. • Throttling request rates without considering request size or complexity. • Testing maximum request rates or maximum request size, but not testing both together. • Resources are not provisioned to the same limits established in testing. • Usage plans have not been configured or considered for application to application (A2A) API consumers. • Queue consumers that horizontally scale do not have maximum concurrency settings configured. • Rate limiting on a per IP address basis has not been implemented. Benefits of establishing this best practice: Workloads that set throttle limits are able to operate normally and process accepted request load successfully under unexpected volume spikes. Sudden or sustained spikes of requests to APIs and queues are throttled and do not exhaust request processing resources. Rate limits throttle individual requestors so that high volumes of traffic from a single IP address or API consumer will not exhaust resources impact other consumers. Level of risk exposed if this best practice is not established: High

> **[S2]** `wa-reliability#0099` Reliability Pillar - AWS Well-Architected Framework > Workload architecture > Design interactions in a distributed system to mitigate or withstand failures > REL05-BP02 Throttle requests > Implementation guidance
>
> Implementation guidance Services should be designed to process a known capacity of requests; this capacity can be established through load testing. If request arrival rates exceed limits, the appropriate response signals that a request has been throttled. This allows the consumer to handle the error and retry later. When your service requires a throttling implementation, consider implementing the token bucket algorithm, where a token counts for a request. Tokens are refilled at a throttle rate per second and emptied asynchronously by one token per request. The token bucket algorithm. Amazon API Gateway implements the token bucket algorithm according to account and region limits and can be configured per-client with usage plans. Additionally, Amazon Simple Queue Service (Amazon SQS) and Amazon Kinesis can buffer requests to smooth out the request rate, and allow higher throttling rates for requests that can be addressed. Finally, you can implement rate limiting with AWS WAF to throttle specific API consumers that generate unusually high load.

> **[S3]** `wa-reliability#0101` Reliability Pillar - AWS Well-Architected Framework > Workload architecture > Design interactions in a distributed system to mitigate or withstand failures > REL05-BP02 Throttle requests > Implementation steps
>
> You can configure API Gateway with throttling limits for your APIs and return 429 Too Many Requests errors when limits are exceeded. You can use AWS WAF with your AWS AppSync and API Gateway endpoints to enable rate limiting on a per IP address basis. Additionally, where your system can tolerate asynchronous processing, you can put messages into a queue or stream to speed up responses to service clients, which allows you to burst to higher throttle rates. With asynchronous processing, when you’ve configured Amazon SQS as an event source for AWS Lambda, you can configure maximum concurrency to avoid high event rates from consuming available account concurrent execution quota needed for other services in your workload or account. While API Gateway provides a managed implementation of the token bucket, in cases where you cannot use API Gateway, you can take advantage of language specific open-source implementations (see related examples in Resources) of the token bucket for your services. • Understand and configure API Gateway throttling limits at the account level per region, API per stage, and API key per usage plan levels. • Apply AWS WAF rate limiting rules to API Gateway and AWS AppSync endpoints to protect against floods and block malicious IPs. Rate limiting rules can also be configured on AWS AppSync API keys for A2A consumers. • Consider whether you require more throttling control than rate limiting for AWS AppSync APIs, and if so, configure an API Gateway in front of your AWS AppSync endpoint. • When Amazon SQS queues are set up as triggers for Lambda queue consumers, set maximum concurrency to a value that processes enough to meet your service level objectives but does not consume concurrency limits impacting other Lambda functions. Consider setting reserved concurrency on other Lambda functions in the same account and region when you consume queues with Lambda. • Use API Gateway with native service integrations to Amazon SQS or Kinesis to buffer requests. • If you cannot use API Gateway, look at language specific libraries to implement the token bucket algorithm for your workload. Check the examples section and do your own research to find a suitable library. • Test limits that you plan to set, or that you plan to allow to be increased, and document the tested limits. • Do not increase limits beyond what you establish in testing. When increasing a limit, verify that provisioned resources are already equivalent to or greater than those in test scenarios before applying the increase.

**Note (optional):** 

---
