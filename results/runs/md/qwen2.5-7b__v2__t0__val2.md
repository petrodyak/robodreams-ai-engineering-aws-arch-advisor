# Run `qwen2.5-7b__v2__t0__val2`

Generated from the JSONL run file by `src/extract/report_md.py`; do not edit.

- Model: `qwen2.5:7b`
- Prompt version: `v2` (file sha `a3adf0379524`)
- Schema sha: `d4010de95c65`; validation version `2`
- Sampling: `t0` (temperature 0.0, top_p None)
- Documents: 30

## Summary

| # | Document | Group | Status | Calls | Latency, s | In tokens | Out tokens | Quota table | Endpoints | Quotas |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [006-amazon-aurora-dsql.pdf](#006-amazon-aurora-dsqlpdf) | short | ok | 1 | 40.4 | 1,972 | 1,491 | standard | 25 | 4 |
| 2 | [076-aws-glue-databrew.pdf](#076-aws-glue-databrewpdf) | short | ok | 1 | 37.8 | 1,963 | 1,638 | standard | 24 | 7 |
| 3 | [085-aws-lake-formation.pdf](#085-aws-lake-formationpdf) | short | ok | 1 | 100.6 | 2,885 | 4,225 | none | 84 | 0 |
| 4 | [033-amazon-kinesis-data-streams.pdf](#033-amazon-kinesis-data-streamspdf) | short | ok | 1 | 95.0 | 3,063 | 3,992 | standard | 76 | 1 |
| 5 | [007-amazon-bedrock-agentcore.pdf](#007-amazon-bedrock-agentcorepdf) | short | failed | 2 | 95.4 | 7,420 | 3,837 | — | — | — |
| 6 | [037-amazon-managed-workflows-for-apache-airflow.pdf](#037-amazon-managed-workflows-for-apache-airflowpdf) | short | failed | 2 | 453.9 | 16,853 | 16,420 | — | — | — |
| 7 | [055-aws-app-mesh.pdf](#055-aws-app-meshpdf) | short | ok | 1 | 104.4 | 4,034 | 4,231 | standard | 78 | 5 |
| 8 | [066-aws-datasync.pdf](#066-aws-datasyncpdf) | short | repaired | 2 | 239.4 | 12,167 | 9,246 | none | 88 | 0 |
| 9 | [091-aws-resource-groups-and-tagging.pdf](#091-aws-resource-groups-and-taggingpdf) | short | ok | 1 | 53.5 | 3,725 | 2,094 | standard | 40 | 1 |
| 10 | [018-amazon-ec2-auto-scaling.pdf](#018-amazon-ec2-auto-scalingpdf) | short | ok | 1 | 116.6 | 3,964 | 4,739 | standard | 84 | 9 |
| 11 | [005-amazon-aurora.pdf](#005-amazon-aurorapdf) | medium | ok | 1 | 80.2 | 4,452 | 3,144 | standard | 35 | 25 |
| 12 | [075-aws-glue.pdf](#075-aws-gluepdf) | medium | failed | 2 | 336.8 | 16,201 | 12,349 | — | — | — |
| 13 | [042-amazon-redshift.pdf](#042-amazon-redshiftpdf) | medium | failed | 2 | 994.6 | 33,921 | 32,717 | — | — | — |
| 14 | [044-amazon-relational-database-service.pdf](#044-amazon-relational-database-servicepdf) | medium | failed | 2 | 530.3 | 21,397 | 18,599 | — | — | — |
| 15 | [048-amazon-simple-queue-service.pdf](#048-amazon-simple-queue-servicepdf) | medium | ok | 1 | 140.1 | 4,915 | 5,425 | standard | 80 | 23 |
| 16 | [047-amazon-simple-notification-service.pdf](#047-amazon-simple-notification-servicepdf) | medium | repaired | 2 | 275.8 | 15,776 | 10,106 | non_standard | 94 | 0 |
| 17 | [026-amazon-eventbridge.pdf](#026-amazon-eventbridgepdf) | medium | ok | 1 | 138.5 | 4,333 | 5,496 | standard | 80 | 17 |
| 18 | [092-aws-secrets-manager.pdf](#092-aws-secrets-managerpdf) | medium | failed | 2 | 276.9 | 15,326 | 10,060 | — | — | — |
| 19 | [023-amazon-elastic-kubernetes-service.pdf](#023-amazon-elastic-kubernetes-servicepdf) | medium | ok | 1 | 72.9 | 4,524 | 2,690 | standard | 40 | 13 |
| 20 | [078-aws-iam-identity-center.pdf](#078-aws-iam-identity-centerpdf) | medium | ok | 1 | 108.8 | 6,504 | 3,886 | standard | 70 | 6 |
| 21 | [038-amazon-opensearch-service.pdf](#038-amazon-opensearch-servicepdf) | edge | failed | 2 | 599.3 | 25,547 | 20,190 | — | — | — |
| 22 | [086-aws-lambda.pdf](#086-aws-lambdapdf) | edge | ok | 1 | 236.8 | 7,427 | 8,655 | standard | 75 | 73 |
| 23 | [004-amazon-athena.pdf](#004-amazon-athenapdf) | edge | ok | 1 | 205.5 | 7,599 | 7,403 | standard | 74 | 30 |
| 24 | [017-amazon-dynamodb.pdf](#017-amazon-dynamodbpdf) | edge | failed | 1 | 532.2 | 9,816 | 18,432 | — | — | — |
| 25 | [095-aws-step-functions.pdf](#095-aws-step-functionspdf) | edge | failed | 2 | 897.6 | 33,007 | 29,389 | — | — | — |
| 26 | [049-amazon-simple-storage-service.pdf](#049-amazon-simple-storage-servicepdf) | edge | failed | 1 | 570.4 | 13,868 | 18,432 | — | — | — |
| 27 | [025-amazon-emr.pdf](#025-amazon-emrpdf) | edge | failed | 1 | 560.5 | 11,318 | 18,432 | — | — | — |
| 28 | [010-amazon-cloudfront.pdf](#010-amazon-cloudfrontpdf) | edge | failed | 2 | 348.1 | 19,236 | 12,148 | — | — | — |
| 29 | [074-aws-global-accelerator.pdf](#074-aws-global-acceleratorpdf) | edge | failed | 2 | 59.5 | 10,802 | 2,037 | — | — | — |
| 30 | [019-amazon-ecr.pdf](#019-amazon-ecrpdf) | edge | ok | 1 | 255.5 | 6,924 | 9,321 | standard | 151 | 23 |

## Documents

### 006-amazon-aurora-dsql.pdf

- Status: **ok**, 1 call(s), 40.4 s, in 1,972 / out 1,491 tokens
- Service: Amazon Aurora DSQL; quota table format: `standard`

#### Endpoints (25)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | dsql.us-east-2.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | dsql-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | dsql.us-east-1.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | dsql-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | dsql.us-west-2.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | dsql-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | dsql.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | dsql.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | dsql.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | dsql.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | dsql.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | dsql.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | dsql.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | dsql.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | dsql.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | dsql-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Calgary) | ca-west-1 | dsql.ca-west-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | dsql-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Europe (Frankfurt) | eu-central-1 | dsql.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | dsql.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | dsql.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | dsql.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | dsql.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | dsql.eu-north-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | dsql.sa-east-1.api.aws | HTTPS | dual_stack |

#### Quotas (4)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Cluster size | Region: 10,000 Gigabytes | Yes | The maximum capacity (in GB) for an Aurora DSQL cluster. This quota applies to both single-Region and multi-Region clusters. |
| Connections per cluster | Region: 10,000 | Yes | The maximum number of active connections per cluster that you can have in this account in the current Region. |
| Multi-Region clusters | Region: 5 | Yes | The maximum number of multi region clusters allowed per account. |
| Single-Region clusters | Region: 20 | Yes | The maximum number of active clusters allowed |

### 076-aws-glue-databrew.pdf

- Status: **ok**, 1 call(s), 37.8 s, in 1,963 / out 1,638 tokens
- Service: AWS Glue DataBrew; quota table format: `standard`

#### Endpoints (24)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | databrew.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | databrew-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | databrew.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | databrew-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | databrew.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | databrew-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | databrew.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | databrew-fips.us-west-2.amazonaws.com | HTTPS | fips |
| Africa (Cape Town) | af-south-1 | databrew.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | databrew.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | databrew.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | databrew.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | databrew.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | databrew.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | databrew.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | databrew.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | databrew.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | databrew.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | databrew.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | databrew.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | databrew.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | databrew.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | databrew.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | databrew.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (7)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Concurrent jobs per AWS account | Each supported Region: 10 | Yes | The maximum number of jobs that you can run at the same time in this AWS account. |
| Datasets per AWS account | Each supported Region: 100 | Yes | The maximum number of datasets that you can create in this AWS account. |
| Jobs per AWS account | Each supported Region: 100 | Yes | The maximum number of jobs that you can create in this AWS account. |
| Node capacity per AWS account | Each supported Region: 300 | Yes | The maximum number of nodes available to jobs running in this AWS account. |
| Open projects per AWS account | Each supported Region: 10 | Yes | The maximum number of projects that you can open concurrently in this AWS account. |
| Projects per AWS account | Each supported Region: 100 | Yes | The maximum number of projects that you can create in this AWS account. |
| Recipes per AWS account | Each supported Region: 500 | Yes | The maximum number of recipes that you can create in this AWS account. |

### 085-aws-lake-formation.pdf

- Status: **ok**, 1 call(s), 100.6 s, in 2,885 / out 4,225 tokens
- Service: AWS Lake Formation; quota table format: `none`

#### Endpoints (84)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | lakeformation.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | lakeformation-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | lakeformation-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | lakeformation.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | lakeformation.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | lakeformation-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | lakeformation-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | lakeformation.us-east-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | lakeformation.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | lakeformation-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | lakeformation-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | lakeformation.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | lakeformation.af-south-1.amazonaws.com | HTTPS | ipv4 |
| af-south-1 | af-south-1 | lakeformation.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | lakeformation.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| ap-east-1 | ap-east-1 | lakeformation.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | lakeformation.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| ap-south-2 | ap-south-2 | lakeformation.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | lakeformation.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-3 | ap-southeast-3 | lakeformation.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | lakeformation.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-5 | ap-southeast-5 | lakeformation.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | lakeformation.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-4 | ap-southeast-4 | lakeformation.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | lakeformation.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| ap-south-1 | ap-south-1 | lakeformation.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | lakeformation.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-6 | ap-southeast-6 | lakeformation.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | lakeformation.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-3 | ap-northeast-3 | lakeformation.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | lakeformation.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-2 | ap-northeast-2 | lakeformation.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | lakeformation.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-1 | ap-southeast-1 | lakeformation.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | lakeformation.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-2 | ap-southeast-2 | lakeformation.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | lakeformation.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| ap-east-2 | ap-east-2 | lakeformation.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | lakeformation.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-7 | ap-southeast-7 | lakeformation.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | lakeformation.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-1 | ap-northeast-1 | lakeformation.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | lakeformation.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| ca-central-1 | ca-central-1 | lakeformation-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| ca-central-1 | ca-central-1 | lakeformation-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| ca-central-1 | ca-central-1 | lakeformation.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | lakeformation.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| ca-west-1 | ca-west-1 | lakeformation-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| ca-west-1 | ca-west-1 | lakeformation-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| ca-west-1 | ca-west-1 | lakeformation.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | lakeformation.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| eu-central-1 | eu-central-1 | lakeformation.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | lakeformation.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| eu-west-1 | eu-west-1 | lakeformation.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | lakeformation.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| eu-west-2 | eu-west-2 | lakeformation.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | lakeformation.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| eu-south-1 | eu-south-1 | lakeformation.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | lakeformation.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| eu-west-3 | eu-west-3 | lakeformation.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | lakeformation.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| eu-south-2 | eu-south-2 | lakeformation.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | lakeformation.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| eu-north-1 | eu-north-1 | lakeformation.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | lakeformation.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| eu-central-2 | eu-central-2 | lakeformation.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | lakeformation.il-central-1.amazonaws.com | HTTPS | ipv4 |
| il-central-1 | il-central-1 | lakeformation.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | lakeformation.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| mx-central-1 | mx-central-1 | lakeformation.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | lakeformation.me-south-1.amazonaws.com | HTTPS | ipv4 |
| me-south-1 | me-south-1 | lakeformation.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | lakeformation.me-central-1.amazonaws.com | HTTPS | ipv4 |
| me-central-1 | me-central-1 | lakeformation.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | lakeformation.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| sa-east-1 | sa-east-1 | lakeformation.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | lakeformation.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| us-gov-east-1 | us-gov-east-1 | lakeformation-fips.us-gov-east-1.api.aws | HTTPS | fips_dual_stack |
| us-gov-east-1 | us-gov-east-1 | lakeformation-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| us-gov-east-1 | us-gov-east-1 | lakeformation.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | lakeformation.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| us-gov-west-1 | us-gov-west-1 | lakeformation-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |
| us-gov-west-1 | us-gov-west-1 | lakeformation-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| us-gov-west-1 | us-gov-west-1 | lakeformation.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (0)

_none_

### 033-amazon-kinesis-data-streams.pdf

- Status: **ok**, 1 call(s), 95.0 s, in 3,063 / out 3,992 tokens
- Service: Amazon Kinesis Data Streams; quota table format: `standard`

#### Endpoints (76)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | kinesis.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | kinesis-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | kinesis-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | kinesis.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | kinesis.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | kinesis-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | kinesis-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | kinesis.us-east-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | kinesis.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | kinesis-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | kinesis-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | kinesis.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | kinesis.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | kinesis.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | kinesis.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | kinesis.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | kinesis.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | kinesis.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | kinesis.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | kinesis.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | kinesis.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | kinesis.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | kinesis.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | kinesis.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | kinesis.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | kinesis.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | kinesis.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | kinesis.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | kinesis.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | kinesis.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | kinesis.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | kinesis.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | kinesis.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | kinesis.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | kinesis.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | kinesis.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | kinesis.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | kinesis.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | kinesis.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | kinesis.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | kinesis.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | kinesis.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | kinesis.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | kinesis.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | kinesis.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | kinesis.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | kinesis.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | kinesis.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | kinesis.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | kinesis.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | kinesis.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | kinesis.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | kinesis.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | kinesis.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | kinesis.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | kinesis.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | kinesis.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | kinesis.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | kinesis.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | kinesis.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | kinesis.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | kinesis.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | kinesis.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | kinesis.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | kinesis.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | kinesis.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | kinesis.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | kinesis.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | kinesis.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | kinesis.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | kinesis.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | kinesis.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | kinesis.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | kinesis.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | kinesis.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | kinesis.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (1)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Shards per Region | us-east-1: 20,000; us-east-2: 6,000; us-west-2: 20,000; ap-northeast-1: 6,000; ap-south-1: 6,000; ap-southeast-1: 6,000; ap-southeast-2: 6,000; eu-central-1: 6,000; eu-west-1: 20,000; eu-west-3: 6,000; Each of the other supported Regions: 1,000 | Yes | The maximum number of shards that you can create in this account in the current Region. |

### 007-amazon-bedrock-agentcore.pdf

- Status: **failed**, 2 call(s), 95.4 s, in 7,420 / out 3,837 tokens

#### Error

```text
- endpoints.18.endpoint: not printed in an endpoints table of the 'Amazon Bedrock AgentCore' chapter: 'bedrock-agentcore.us-west-1.amazonaws.com'
- endpoints.19.endpoint: not printed in an endpoints table of the 'Amazon Bedrock AgentCore' chapter: 'bedrock-agentcore.eu-west-2.amazonaws.com'
- endpoints.20.endpoint: not printed in an endpoints table of the 'Amazon Bedrock AgentCore' chapter: 'bedrock-agentcore.eu-west-3.amazonaws.com'
- endpoints.21.endpoint: not printed in an endpoints table of the 'Amazon Bedrock AgentCore' chapter: 'bedrock-agentcore.eu-south-1.amazonaws.com'
- endpoints.22.endpoint: not printed in an endpoints table of the 'Amazon Bedrock AgentCore' chapter: 'bedrock-agentcore.eu-south-2.amazonaws.com'
- endpoints.23.endpoint: not printed in an endpoints table of the 'Amazon Bedrock AgentCore' chapter: 'bedrock-agentcore.eu-north-1.amazonaws.com'
- endpoints.24.endpoint: not printed in an endpoints table of the 'Amazon Bedrock AgentCore' chapter: 'bedrock-agentcore.ap-northeast-2.amazonaws.com'
- endpoints.25.endpoint: not printed in an endpoints table of the 'Amazon Bedrock AgentCore' chapter: 'bedrock-agentcore.ap-south-2.amazonaws.com'
- endpoints.26.endpoint: not printed in an endpoints table of the 'Amazon Bedrock AgentCore' chapter: 'bedrock-agentcore.ap-southeast-5.amazonaws.com'
- endpoints.27.endpoint: not printed in an endpoints table of the 'Amazon Bedrock AgentCore' chapter: 'bedrock-agentcore.ap-southeast-7.amazonaws.com'
- endpoints.28.endpoint: not printed in an endpoints table of the 'Amazon Bedrock AgentCore' chapter: 'bedrock-agentcore.ca-central-1.amazonaws.com'
- endpoints.29.endpoint: not printed in an endpoints table of the 'Amazon Bedrock AgentCore' chapter: 'bedrock-agentcore.sa-east-1.amazonaws.com'
--- after repair:
- endpoints.24.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.24.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.us-east-1.amazonaws.com'
- endpoints.25.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.25.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.us-east-2.amazonaws.com'
- endpoints.26.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.26.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.us-west-2.amazonaws.com'
- endpoints.27.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.27.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.ap-southeast-1.amazonaws.com'
- endpoints.28.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.28.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.ap-southeast-2.amazonaws.com'
- endpoints.29.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.29.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.ap-south-1.amazonaws.com'
- endpoints.30.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.30.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.ap-northeast-1.amazonaws.com'
- endpoints.31.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.31.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.eu-west-1.amazonaws.com'
- endpoints.32.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.32.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.eu-central-1.amazonaws.com'
- endpoints.33.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.33.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.eu-west-2.amazonaws.com'
- endpoints.34.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.34.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.eu-west-3.amazonaws.com'
- endpoints.35.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.35.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.eu-south-1.amazonaws.com'
- endpoints.36.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.36.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.eu-south-2.amazonaws.com'
- endpoints.37.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.37.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.eu-north-1.amazonaws.com'
- endpoints.38.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.38.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.ap-northeast-2.amazonaws.com'
- endpoints.39.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.39.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.ap-south-2.amazonaws.com'
- endpoints.40.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.40.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.ap-southeast-5.amazonaws.com'
- endpoints.41.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.41.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.ap-southeast-7.amazonaws.com'
- endpoints.42.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.42.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.ca-central-1.amazonaws.com'
- endpoints.43.region_code: Value error, not an AWS Region code like us-east-2: 'gateway'
- endpoints.43.endpoint: Value error, not a single hostname (broken by a line wrap?): 'gatewayId .gateway.bedrock-agentcore.sa-east-1.amazonaws.com'
```

### 037-amazon-managed-workflows-for-apache-airflow.pdf

- Status: **failed**, 2 call(s), 453.9 s, in 16,853 / out 16,420 tokens

#### Error

```text
- quota_table_format: 'none', but the chapter prints a table with the columns Name, Default, Adjustable, Description: that is a Standard Quota Table, return its rows with 'standard'
--- after repair:
- quotas.0.name: not printed in a Standard Quota Table of the chapter: 'Environments per account per Region'
```

### 055-aws-app-mesh.pdf

- Status: **ok**, 1 call(s), 104.4 s, in 4,034 / out 4,231 tokens
- Service: AWS App Mesh; quota table format: `standard`

#### Endpoints (78)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | appmesh.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | appmesh-envoy-management-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | appmesh.us-east-2.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | appmesh-envoy-management-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | appmesh-envoy-management.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | appmesh-envoy-management.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | appmesh.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | appmesh-envoy-management.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | appmesh-envoy-management-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | appmesh-envoy-management-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | appmesh.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | appmesh-envoy-management.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | appmesh-envoy-management-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | appmesh-envoy-management-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | appmesh.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | appmesh-envoy-management.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | appmesh-envoy-management-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | appmesh-envoy-management-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| Africa (Cape Town) | af-south-1 | appmesh.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | appmesh-envoy-management.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | appmesh.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | appmesh-envoy-management.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | appmesh.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | appmesh-envoy-management.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | appmesh.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | appmesh-envoy-management.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | appmesh.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | appmesh-envoy-management.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | appmesh.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | appmesh-envoy-management.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | appmesh.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | appmesh-envoy-management.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | appmesh.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | appmesh-envoy-management.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | appmesh.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | appmesh-envoy-management.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | appmesh.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | appmesh-envoy-management.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | appmesh-envoy-management-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | appmesh.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | appmesh-envoy-management-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Europe (Frankfurt) | eu-central-1 | appmesh.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | appmesh.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | appmesh-envoy-management.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | appmesh.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | appmesh-envoy-management.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | appmesh-envoy-management.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | appmesh.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | appmesh.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | appmesh-envoy-management.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | appmesh-envoy-management.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | appmesh.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | appmesh-envoy-management.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | appmesh-envoy-management.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | appmesh.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | appmesh-envoy-management.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | appmesh-envoy-management.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | appmesh.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | appmesh-envoy-management.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | appmesh-envoy-management.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | appmesh.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | appmesh-envoy-management.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | appmesh-envoy-management.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | appmesh.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | appmesh-envoy-management.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | appmesh-envoy-management.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | appmesh.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | appmesh-envoy-management.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | appmesh-envoy-management.il-central-1.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | appmesh.il-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | appmesh.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | appmesh-envoy-management.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | appmesh-envoy-management.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | appmesh.me-south-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | appmesh.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | appmesh.sa-east-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | appmesh-envoy-management.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | appmesh-envoy-management.sa-east-1.api.aws | HTTPS | dual_stack |

#### Quotas (5)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Backends per virtual node | Each supported Region: 50 | No | Number of backends per virtual node |
| Connected Envoy processes per virtual gateway | Each supported Region: 50 | Yes | Number of concurrently connected Envoy processes per virtual gateway |
| Connected Envoy processes per virtual node | Each supported Region: 50 | Yes | Number of concurrently connected Envoy processes per virtual node |
| Gateway routes per virtual gateway | Each supported Region: 10 | Yes | Number of gateway routes per virtual gateway |
| Meshes per account | Each supported Region: 15 | Yes | Number of meshes per account |

### 066-aws-datasync.pdf

- Status: **repaired**, 2 call(s), 239.4 s, in 12,167 / out 9,246 tokens
- Service: AWS DataSync; quota table format: `none`

#### Endpoints (88)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | datasync.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | datasync-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | datasync.us-east-2.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | datasync-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | datasync.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | datasync-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | datasync-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | datasync.us-east-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | datasync.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | datasync-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | datasync-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | datasync.us-west-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | datasync.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | datasync-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | datasync.us-west-2.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | datasync-fips.us-west-2.amazonaws.com | HTTPS | fips |
| Africa (Cape Town) | af-south-1 | datasync.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | datasync.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | datasync.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | datasync.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | datasync.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | datasync.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | datasync.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | datasync.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | datasync.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | datasync.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | datasync.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | datasync.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | datasync.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | datasync.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | datasync.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | datasync.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | datasync.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | datasync.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | datasync.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | datasync.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | datasync.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | datasync.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | datasync.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | datasync.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | datasync.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | datasync.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | datasync.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | datasync.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | datasync.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | datasync.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | datasync.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | datasync.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | datasync-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | datasync-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Calgary) | ca-west-1 | datasync.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | datasync.ca-west-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | datasync-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada (Calgary) | ca-west-1 | datasync-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Europe (Frankfurt) | eu-central-1 | datasync.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | datasync.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | datasync.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | datasync.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | datasync.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | datasync.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | datasync.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | datasync.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | datasync.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | datasync.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | datasync.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | datasync.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | datasync.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | datasync.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | datasync.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | datasync.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | datasync.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | datasync.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | datasync.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | datasync.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | datasync.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | datasync.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | datasync.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | datasync.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | datasync.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | datasync.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | datasync.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | datasync.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | datasync-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | datasync-fips.us-gov-east-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | datasync.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | datasync.us-gov-west-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | datasync-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | datasync-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |

#### Quotas (0)

_none_

#### First answer rejected (repaired)

```text
- quotas.0.name: not printed in a Standard Quota Table of the chapter: 'Maximum number of tasks you can create'
- quotas.1.name: not printed in a Standard Quota Table of the chapter: 'Maximum number of (Enhanced mode tasks) source and destination objects that DataSync can work with per task execution'
- quotas.2.name: not printed in a Standard Quota Table of the chapter: 'Maximum number of (Basic mode tasks) source and destination files, objects, and directories that DataSync can work with per task execution between self-managed storage or other clouds and AWS services'
- quotas.3.name: not printed in a Standard Quota Table of the chapter: 'Maximum number of (Basic mode tasks) source and destination files, objects, and directories that DataSync can work with per task execution between AWS storage services'
- quota_table_format: 'standard', but the chapter prints no table with the columns Name, Default, Adjustable, Description
```

### 091-aws-resource-groups-and-tagging.pdf

- Status: **ok**, 1 call(s), 53.5 s, in 3,725 / out 2,094 tokens
- Service: AWS Resource Groups and Tagging; quota table format: `standard`

#### Endpoints (40)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | resource-groups.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | resource-groups-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | resource-groups.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | resource-groups-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | resource-groups.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | resource-groups-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | resource-groups.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | resource-groups-fips.us-west-2.amazonaws.com | HTTPS | fips |
| Africa (Cape Town) | af-south-1 | resource-groups.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | resource-groups.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | resource-groups.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | resource-groups.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | resource-groups.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | resource-groups.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | resource-groups.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | resource-groups.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | resource-groups.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | resource-groups.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | resource-groups.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | resource-groups.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | resource-groups.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | resource-groups.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | resource-groups.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | resource-groups.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | resource-groups.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | resource-groups.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | resource-groups.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | resource-groups.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | resource-groups.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | resource-groups.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | resource-groups.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | resource-groups.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | resource-groups.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | resource-groups.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | resource-groups.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | resource-groups.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | resource-groups.me-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | resource-groups.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | resource-groups.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | resource-groups.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (1)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Resource groups per account | Each supported Region: 100 | Yes | The maximum number of resource groups that you can create in this account. A resource group is a collection of AWS resources that match a specific criteria. |

### 018-amazon-ec2-auto-scaling.pdf

- Status: **ok**, 1 call(s), 116.6 s, in 3,964 / out 4,739 tokens
- Service: Amazon EC2 Auto Scaling; quota table format: `standard`

#### Endpoints (84)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | autoscaling.us-east-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | autoscaling-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | autoscaling-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | autoscaling.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | autoscaling.us-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | autoscaling-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | autoscaling-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | autoscaling.us-east-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | autoscaling.us-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| US West (N. California) | us-west-1 | autoscaling-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | autoscaling-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | autoscaling.us-west-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | autoscaling.us-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | autoscaling-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | autoscaling-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | autoscaling.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | autoscaling.af-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | autoscaling.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | autoscaling.ap-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | autoscaling.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | autoscaling.ap-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | autoscaling.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | autoscaling.ap-southeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | autoscaling.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | autoscaling.ap-southeast-5.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | autoscaling.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | autoscaling.ap-southeast-4.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | autoscaling.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | autoscaling.ap-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | autoscaling.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | autoscaling.ap-southeast-6.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | autoscaling.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | autoscaling.ap-northeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | autoscaling.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | autoscaling.ap-northeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | autoscaling.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | autoscaling.ap-southeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | autoscaling.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | autoscaling.ap-southeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | autoscaling.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | autoscaling.ap-east-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | autoscaling.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | autoscaling.ap-southeast-7.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | autoscaling.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | autoscaling.ap-northeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | autoscaling.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | autoscaling.ca-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | autoscaling-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | autoscaling-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | autoscaling.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | autoscaling.ca-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | autoscaling-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Calgary) | ca-west-1 | autoscaling-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada (Calgary) | ca-west-1 | autoscaling.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | autoscaling.eu-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | autoscaling.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | autoscaling.eu-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | autoscaling.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | autoscaling.eu-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (London) | eu-west-2 | autoscaling.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | autoscaling.eu-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | autoscaling.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | autoscaling.eu-west-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | autoscaling.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | autoscaling.eu-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | autoscaling.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | autoscaling.eu-north-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | autoscaling.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | autoscaling.eu-central-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | autoscaling.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | autoscaling.il-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | autoscaling.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | autoscaling.mx-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | autoscaling.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | autoscaling.me-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | autoscaling.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | autoscaling.me-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | autoscaling.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | autoscaling.sa-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | autoscaling.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | autoscaling.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | autoscaling.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | autoscaling.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | autoscaling.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (9)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Auto Scaling groups per region | Each supported Region: 500 | Yes | The maximum number of Auto Scaling groups allowed for your AWS account |
| Classic Load Balancers per Auto Scaling group | Each supported Region: 50 | No | The maximum number of Classic Load Balancers per Auto Scaling group |
| Launch configurations per region | Each supported Region: 200 | Yes | The maximum number of launch configurations allowed for your AWS account |
| Lifecycle hooks per Auto Scaling group | Each supported Region: 50 | No | The maximum number of lifecycle hooks per Auto Scaling group |
| SNS topics per Auto Scaling group | Each supported Region: 10 | No | The maximum number of SNS topics per Auto Scaling group |
| Scaling policies per Auto Scaling group | Each supported Region: 50 | No | The maximum number of scaling policies per Auto Scaling group |
| Scheduled actions per Auto Scaling group | Each supported Region: 125 | No | The maximum number of scheduled actions per Auto Scaling group |
| Step adjustments per step scaling policy | Each supported Region: 20 | No | The maximum number of step adjustments per step scaling policy |
| Target groups per Auto Scaling group | Each supported Region: 50 | No | The maximum number of target groups per Auto Scaling group |

### 005-amazon-aurora.pdf

- Status: **ok**, 1 call(s), 80.2 s, in 4,452 / out 3,144 tokens
- Service: Amazon Aurora; quota table format: `standard`

#### Endpoints (35)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East | us-east-2 | rds.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East | us-east-1 | rds.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US West | us-west-1 | rds.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West | us-west-2 | rds.us-west-2.amazonaws.com | HTTPS | ipv4 |
| Africa | af-south-1 | rds.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific | ap-east-1 | rds.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific | ap-south-2 | rds.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific | ap-southeast-3 | rds.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific | ap-southeast-5 | rds.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific | ap-southeast-4 | rds.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific | ap-south-1 | rds.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific | ap-southeast-6 | rds.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific | ap-northeast-3 | rds.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific | ap-northeast-2 | rds.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific | ap-southeast-1 | rds.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific | ap-southeast-2 | rds.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific | ap-east-2 | rds.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific | ap-southeast-7 | rds.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific | ap-northeast-1 | rds.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada | ca-central-1 | rds.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada | ca-west-1 | rds.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe | eu-central-1 | rds.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe | eu-west-1 | rds.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe | eu-west-2 | rds.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe | eu-south-1 | rds.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe | eu-west-3 | rds.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe | eu-south-2 | rds.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe | eu-north-1 | rds.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe | eu-central-2 | rds.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Israel | il-central-1 | rds.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico | mx-central-1 | rds.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East | me-south-1 | rds.me-south-1.amazonaws.com | HTTPS | ipv4 |
| South America | sa-east-1 | rds.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | rds.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | rds.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (25)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Authorizations per DB security group | Each supported Region: 20 | No | Number of security group authorizations per DB security group |
| Custom endpoints per DB cluster | Each supported Region: 5 | Yes | The maximum number of custom endpoints that you can create per Aurora DB cluster in this account in the current Region. This value reflects the highest number of custom endpoints in a DB cluster in the account. Other DB clusters in the account might have a lower number of custom endpoints. |
| Custom engine versions | Each supported Region: 40 | Yes | The maximum number of custom engine versions allowed in this account in the current Region |
| DB cluster parameter groups | Each supported Region: 50 | Yes | The maximum number of DB cluster parameter groups |
| DB clusters | Each supported Region: 40 | Yes | The maximum number of Aurora clusters allowed in this account in the current Region |
| DB instances | ap-south-1: 20; Each of the other supported Regions: 40 | Yes | The maximum number of DB instances allowed in this account in the current Region |
| DB shard groups | Each supported Region: 5 | Yes | The maximum number of DB shard groups for Aurora Limitless Database in this account in the current Region |
| DB subnet groups | ap-south-1: 20; Each of the other supported Regions: 50 | Yes | The maximum number of DB subnet groups |
| Data API HTTP request body size | Each supported Region: 4 Megabytes | No | The maximum size allowed for the HTTP request body. |
| Data API maximum concurrent cluster-secret pairs | Each supported Region: 30 | No | The maximum number of unique pairs of Aurora Serverless v1 DB clusters and secrets in concurrent Data API requests for this account in the current AWS Region. |
| Data API maximum concurrent requests | Each supported Region: 500 | No | The maximum number of Data API requests to an Aurora Serverless v1 DB cluster that use the same secret and can be processed at the same time. Additional requests are queued and processed as in-process requests complete. |
| Data API maximum result set size | Each supported Region: 1 Megabytes | No | The maximum size of the database result set that can be returned by the Data API. |
| Data API maximum size of JSON response string | Each supported Region: 10 Megabytes | No | The maximum size of the simplified JSON response string returned by the RDS Data API. |
| Data API requests per second | Each supported Region: 1,000 per second | No | The maximum number of requests to the Data API per second allowed for this account in the current AWS Region. This quota only applies to Amazon Aurora Serverless v1 clusters. |
| Event subscriptions | Each supported Region: 20 | Yes | The maximum number of event subscriptions |
| IAM roles per DB cluster | Each supported Region: 5 | Yes | The maximum number of IAM roles associated with a DB cluster |
| IAM roles per DB instance | Each supported Region: 5 | Yes | The maximum number of IAM roles associated with a DB instance |
| Integrations | Each supported Region: 100 | No | The maximum number of integrations allowed in this account in the current AWS Region |
| Manual DB cluster snapshots | Each supported Region: 100 | Yes | The maximum number of manual DB cluster snapshots |
| Manual DB instance snapshots | Each supported Region: 100 | Yes | The maximum number of manual DB instance snapshots |
| Option groups | Each supported Region: 20 | Yes | The maximum number of option groups |
| Parameter groups | ap-south-1: 20; Each of the other supported Regions: 50 | Yes | The maximum number of parameter groups |
| Proxies | Each supported Region: 20 | Yes | The maximum number of proxies allowed in this account in the current AWS Region |
| Read replicas per primary | Each supported Region: 15 | Yes | The maximum number of read replicas per primary DB instance. This quota can't be adjusted for Amazon Aurora. |
| Reserved DB instances | ap-south-1: 20; Each of the other supported Regions: 40 | Yes | The maximum number of reserved DB instances allowed in this account in the current AWS Region |

### 075-aws-glue.pdf

- Status: **failed**, 2 call(s), 336.8 s, in 16,201 / out 12,349 tokens

#### Error

```text
- quotas.0.name: not printed in a Standard Quota Table of the chapter: 'Concurrent compute capacity for Ray worker instances in M-DPUs per account'
- quotas.26.name: not printed in a Standard Quota Table of the chapter: 'Max spare compute capacity consumed in data processing units (DPUs) per account'
- quotas.35.name: not printed in a Standard Quota Table of the chapter: 'Number of Schema Registries'
- quotas.36.name: not printed in a Standard Quota Table of the chapter: 'Number of Schema Versions'
- quotas.43.name: not printed in a Standard Quota Table of the chapter: 'Number of metadata key value pairs per Schema Version'
- quotas.45.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of concurrent materialized view refresh task runs'
--- after repair:
- quotas.0.name: not printed in a Standard Quota Table of the chapter: 'Concurrent compute capacity for Ray worker instances in M-DPUs per account'
- quotas.26.name: not printed in a Standard Quota Table of the chapter: 'Max spare compute capacity consumed in data processing units (DPUs) per account'
```

### 042-amazon-redshift.pdf

- Status: **failed**, 2 call(s), 994.6 s, in 33,921 / out 32,717 tokens

#### Error

```text
- endpoints.10.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-3.amazonaws.com'
- endpoints.11.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-3.amazonaws.com'
- endpoints.14.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-5.amazonaws.com'
- endpoints.15.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-5.amazonaws.com'
- endpoints.18.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-4.amazonaws.com'
- endpoints.19.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-4.amazonaws.com'
- endpoints.22.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-south-1.amazonaws.com'
- endpoints.23.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-south-1.amazonaws.com'
- endpoints.26.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-6.amazonaws.com'
- endpoints.27.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-6.amazonaws.com'
- endpoints.30.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-northeast-3.amazonaws.com'
- endpoints.31.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-northeast-3.amazonaws.com'
- endpoints.34.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-northeast-2.amazonaws.com'
- endpoints.35.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-northeast-2.amazonaws.com'
- endpoints.38.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-1.amazonaws.com'
- endpoints.39.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-1.amazonaws.com'
- endpoints.42.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-2.amazonaws.com'
- endpoints.43.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-2.amazonaws.com'
- endpoints.46.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-east-2.amazonaws.com'
- endpoints.47.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-east-2.amazonaws.com'
- endpoints.50.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-7.amazonaws.com'
- endpoints.51.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-7.amazonaws.com'
- endpoints.54.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-northeast-1.amazonaws.com'
- endpoints.55.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-northeast-1.amazonaws.com'
- endpoints.66.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-central-1.amazonaws.com'
- endpoints.67.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-central-1.amazonaws.com'
- endpoints.70.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-west-1.amazonaws.com'
- endpoints.71.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-west-1.amazonaws.com'
- endpoints.74.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-west-2.amazonaws.com'
- endpoints.75.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-west-2.amazonaws.com'
- endpoints.78.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-south-1.amazonaws.com'
- endpoints.79.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-south-1.amazonaws.com'
- endpoints.82.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-west-3.amazonaws.com'
- endpoints.83.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-west-3.amazonaws.com'
- endpoints.86.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-south-2.amazonaws.com'
- endpoints.87.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-south-2.amazonaws.com'
- endpoints.90.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-north-1.amazonaws.com'
- endpoints.91.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-north-1.amazonaws.com'
- endpoints.94.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-central-2.amazonaws.com'
- endpoints.95.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-central-2.amazonaws.com'
- endpoints.98.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.il-central-1.amazonaws.com'
- endpoints.99.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.il-central-1.amazonaws.com'
- endpoints.102.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.mx-central-1.amazonaws.com'
- endpoints.103.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.mx-central-1.amazonaws.com'
- endpoints.106.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.me-south-1.amazonaws.com'
- endpoints.107.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.me-south-1.amazonaws.com'
- endpoints.110.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.me-central-1.amazonaws.com'
- endpoints.111.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.me-central-1.amazonaws.com'
- endpoints.114.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.sa-east-1.amazonaws.com'
- endpoints.115.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.sa-east-1.amazonaws.com'
- endpoints.118.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.us-gov-east-1.amazonaws.com'
- endpoints.119.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.us-gov-east-1.amazonaws.com'
- endpoints.122.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.us-gov-west-1.amazonaws.com'
- endpoints.123.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.us-gov-west-1.amazonaws.com'
- endpoints.168.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-serverless-ca-central-1.api.aws'
- endpoints.170.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-serverless-ca-central-1.api.aws'
- endpoints.172.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-serverless-ca-west-1.api.aws'
- endpoints.174.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-serverless-ca-west-1.api.aws'
- endpoints.195.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-serverless.me-south-1.amazonaws.com'
- endpoints.196.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-serverless.me-south-1.api.aws'
- endpoints.244.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-data-ca-central-1.api.aws'
- endpoints.246.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-data-ca-central-1.api.aws'
- endpoints.248.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-data-ca-west-1.api.aws'
- endpoints.250.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-data-ca-west-1.api.aws'
- endpoints.293.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'api.sqlworkbench.ap-east-2.amazonaws.com'
--- after repair:
- endpoints.10.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-3.amazonaws.com'
- endpoints.11.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-3.amazonaws.com'
- endpoints.14.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-5.amazonaws.com'
- endpoints.15.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-5.amazonaws.com'
- endpoints.18.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-4.amazonaws.com'
- endpoints.19.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-4.amazonaws.com'
- endpoints.22.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-south-1.amazonaws.com'
- endpoints.23.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-south-1.amazonaws.com'
- endpoints.26.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-6.amazonaws.com'
- endpoints.27.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-6.amazonaws.com'
- endpoints.30.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-northeast-3.amazonaws.com'
- endpoints.31.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-northeast-3.amazonaws.com'
- endpoints.34.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-northeast-2.amazonaws.com'
- endpoints.35.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-northeast-2.amazonaws.com'
- endpoints.38.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-1.amazonaws.com'
- endpoints.39.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-1.amazonaws.com'
- endpoints.42.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-2.amazonaws.com'
- endpoints.43.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-2.amazonaws.com'
- endpoints.46.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-east-2.amazonaws.com'
- endpoints.47.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-east-2.amazonaws.com'
- endpoints.50.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-7.amazonaws.com'
- endpoints.51.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-southeast-7.amazonaws.com'
- endpoints.54.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-northeast-1.amazonaws.com'
- endpoints.55.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.ap-northeast-1.amazonaws.com'
- endpoints.66.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-central-1.amazonaws.com'
- endpoints.67.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-central-1.amazonaws.com'
- endpoints.70.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-west-1.amazonaws.com'
- endpoints.71.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-west-1.amazonaws.com'
- endpoints.74.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-west-2.amazonaws.com'
- endpoints.75.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-west-2.amazonaws.com'
- endpoints.78.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-south-1.amazonaws.com'
- endpoints.79.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-south-1.amazonaws.com'
- endpoints.82.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-west-3.amazonaws.com'
- endpoints.83.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-west-3.amazonaws.com'
- endpoints.86.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-south-2.amazonaws.com'
- endpoints.87.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-south-2.amazonaws.com'
- endpoints.90.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-north-1.amazonaws.com'
- endpoints.91.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-north-1.amazonaws.com'
- endpoints.94.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-central-2.amazonaws.com'
- endpoints.95.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.eu-central-2.amazonaws.com'
- endpoints.98.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.il-central-1.amazonaws.com'
- endpoints.99.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.il-central-1.amazonaws.com'
- endpoints.102.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.mx-central-1.amazonaws.com'
- endpoints.103.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.mx-central-1.amazonaws.com'
- endpoints.106.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.me-south-1.amazonaws.com'
- endpoints.107.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.me-south-1.amazonaws.com'
- endpoints.110.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.me-central-1.amazonaws.com'
- endpoints.111.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.me-central-1.amazonaws.com'
- endpoints.114.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.sa-east-1.amazonaws.com'
- endpoints.115.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.sa-east-1.amazonaws.com'
- endpoints.118.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.us-gov-east-1.amazonaws.com'
- endpoints.119.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.us-gov-east-1.amazonaws.com'
- endpoints.122.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.us-gov-west-1.amazonaws.com'
- endpoints.123.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.us-gov-west-1.amazonaws.com'
- endpoints.168.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-serverless-ca-central-1.api.aws'
- endpoints.170.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-serverless-ca-central-1.api.aws'
- endpoints.172.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-serverless-ca-west-1.api.aws'
- endpoints.174.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-serverless-ca-west-1.api.aws'
- endpoints.195.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-serverless.me-south-1.amazonaws.com'
- endpoints.196.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-serverless.me-south-1.api.aws'
- endpoints.244.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-data-ca-central-1.api.aws'
- endpoints.246.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-data-ca-central-1.api.aws'
- endpoints.248.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-data-ca-west-1.api.aws'
- endpoints.250.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-data-ca-west-1.api.aws'
- endpoints.293.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'api.sqlworkbench.ap-east-2.amazonaws.com'
```

### 044-amazon-relational-database-service.pdf

- Status: **failed**, 2 call(s), 530.3 s, in 21,397 / out 18,599 tokens

#### Error

```text
- endpoints.33.endpoint: not printed in an endpoints table of the 'Amazon Relational Database Service' chapter: 'rds.ap-southeast-6.api.aws'
- endpoints.67.endpoint: not printed in an endpoints table of the 'Amazon Relational Database Service' chapter: 'rds-fips.us-gov-east-1.api.aws'
- endpoints.68.endpoint: not printed in an endpoints table of the 'Amazon Relational Database Service' chapter: 'rds-fips.us-gov-east-1.amazonaws.com'
- endpoints.71.endpoint: not printed in an endpoints table of the 'Amazon Relational Database Service' chapter: 'rds-fips.us-gov-west-1.api.aws'
- endpoints.72.endpoint: not printed in an endpoints table of the 'Amazon Relational Database Service' chapter: 'rds-fips.us-gov-west-1.amazonaws.com'
--- after repair:
- endpoints.33.endpoint: not printed in an endpoints table of the 'Amazon Relational Database Service' chapter: 'rds.ap-southeast-6.api.aws'
- endpoints.67.endpoint: not printed in an endpoints table of the 'Amazon Relational Database Service' chapter: 'rds-fips.us-gov-east-1.api.aws'
- endpoints.68.endpoint: not printed in an endpoints table of the 'Amazon Relational Database Service' chapter: 'rds-fips.us-gov-east-1.amazonaws.com'
- endpoints.71.endpoint: not printed in an endpoints table of the 'Amazon Relational Database Service' chapter: 'rds-fips.us-gov-west-1.api.aws'
- endpoints.72.endpoint: not printed in an endpoints table of the 'Amazon Relational Database Service' chapter: 'rds-fips.us-gov-west-1.amazonaws.com'
```

### 048-amazon-simple-queue-service.pdf

- Status: **ok**, 1 call(s), 140.1 s, in 4,915 / out 5,425 tokens
- Service: Amazon Simple Queue Service; quota table format: `standard`

#### Endpoints (80)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | sqs.us-east-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | sqs-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | sqs-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | sqs.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | sqs.us-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | sqs-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | sqs-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | sqs.us-east-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | sqs.us-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | sqs-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | sqs-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | sqs.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | sqs.af-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | sqs.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | sqs.ap-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | sqs.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | sqs.ap-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | sqs.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | sqs.ap-southeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | sqs.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | sqs.ap-southeast-5.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | sqs.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | sqs.ap-southeast-4.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | sqs.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | sqs.ap-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | sqs.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | sqs.ap-southeast-6.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | sqs.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | sqs.ap-northeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | sqs.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | sqs.ap-northeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | sqs.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | sqs.ap-southeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | sqs.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | sqs.ap-southeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | sqs.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | sqs.ap-east-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | sqs.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | sqs.ap-southeast-7.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | sqs.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | sqs.ap-northeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | sqs.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | sqs.ca-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | sqs-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | sqs-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | sqs.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | sqs.ca-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | sqs-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Calgary) | ca-west-1 | sqs-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada (Calgary) | ca-west-1 | sqs.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | sqs.eu-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | sqs.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | sqs.eu-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | sqs.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | sqs.eu-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (London) | eu-west-2 | sqs.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | sqs.eu-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | sqs.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | sqs.eu-west-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | sqs.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | sqs.eu-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | sqs.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | sqs.eu-north-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | sqs.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | sqs.eu-central-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | sqs.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | sqs.il-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | sqs.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | sqs.mx-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | sqs.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | sqs.me-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | sqs.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | sqs.me-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | sqs.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | sqs.sa-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | sqs.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | sqs.us-gov-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | sqs.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | sqs.us-gov-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | sqs.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (23)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Actions per Queue Policy | Each supported Region: 7 | No | The number of actions in a queue policy. |
| Attributes per Message | Each supported Region: 10 | No | The number of attributes added to a message. |
| Batched Message ID Length | Each supported Region: 80 | No | The length of a batched message ID. |
| Batched Message Throughput for FIFO Queues | Each supported Region: 3,000 | No | The number of batched transactions per second (TPS) for FIFO queues. |
| Batched Message Throughput for FIFO Queues | Supported Regions (US East (N. Virginia), US West (Oregon), and Europe (Ireland)): 700,000 | No | The number of batched transactions per second (TPS) for FIFO queues. |
| Batched Message Throughput for FIFO Queues | Europe (Frankfurt) and US East (Ohio): 180,000 | No | The number of batched transactions per second (TPS) for FIFO queues. |
| Batched Message Throughput for FIFO Queues | Asia Pacific (Mumbai), Asia Pacific (Singapore), Asia Pacific (Sydney), and Asia Pacific (Tokyo): 90,000 | No | The number of batched transactions per second (TPS) for FIFO queues. |
| Batched Message Throughput for FIFO Queues | Europe (London) and South America (São Paulo): 45,000 | No | The number of batched transactions per second (TPS) for FIFO queues. |
| Batched Message Throughput for FIFO Queues | All other supported Regions: 24,000 | No | The number of batched transactions per second (TPS) for FIFO queues. |
| Conditions per Queue Policy | Each supported Region: 10 | No | The number of conditions in a queue policy. |
| In-Flight Messages per FIFO Queue | Each supported Region: 120,000 | No | The number of in-flight messages in a FIFO queue. |
| In-Flight Messages per Standard Queue | Each supported Region: 120,000 | Yes | The number of in-flight messages in a standard queue. |
| Message Invisibility Period | Each supported Region: 0 Seconds | No | The length of time, in seconds, for which Amazon SQS retains a message if it isn't deleted. The maximum is 14 days (1,209,600 seconds). |
| Message Size | Each supported Region: 256 Kilobytes | No | The size of a message, in kilobytes. |
| Message Size in Amazon S3 Bucket | Each supported Region: 2 Gigabytes | No | The size of a message, in gigabytes, in an Amazon S3 bucket. |
| Messages per Batch | Each supported Region: 10 | No | The number of messages in a message batch. |
| Principals per Queue Policy | Each supported Region: 50 | No | The length of time, in minutes, by which to delay the initial delivery of messages to a queue. |
| Queue Name Length | Each supported Region: 80 | No | The queue name length. |
| Queue Policy Size | Each supported Region: 8,192 Bytes | No | The size, in bytes, of a queue policy. |
| Statements per Queue Policy | Each supported Region: 20 | No | The number of tags added to a queue. |
| UTF-8 Queue Tag Key Length | Each supported Region: 128 | No | The length of a UTF-8 queue tag key. |
| UTF-8 Queue Tag Value Length | Each supported Region: 256 | No | The length of a UTF-8 queue tag value. |
| Unbatched Message Throughput for FIFO Queues | Each supported Region: 300 | No | The number of unbatched transactions per second (TPS) for FIFO queues. |

### 047-amazon-simple-notification-service.pdf

- Status: **repaired**, 2 call(s), 275.8 s, in 15,776 / out 10,106 tokens
- Service: Amazon Simple Notification Service; quota table format: `non_standard`

#### Endpoints (94)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | sns.us-east-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | sns-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | sns.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | sns.us-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | sns-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | sns.us-east-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | sns.us-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| US West (N. California) | us-west-1 | sns-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | sns.us-west-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | sns.us-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | sns-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | sns.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | sns.af-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.af-south-1.amazonaws.com | af-south-1 | sns.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | sns.ap-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ap-east-1.amazonaws.com | ap-east-1 | sns.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | sns.ap-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ap-south-2.amazonaws.com | ap-south-2 | sns.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | sns.ap-southeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ap-southeast-3.amazonaws.com | ap-southeast-3 | sns.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | sns.ap-southeast-5.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ap-southeast-5.amazonaws.com | ap-southeast-5 | sns.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | sns.ap-southeast-4.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ap-southeast-4.amazonaws.com | ap-southeast-4 | sns.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | sns.ap-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ap-south-1.amazonaws.com | ap-south-1 | sns.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | sns.ap-southeast-6.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ap-southeast-6.amazonaws.com | ap-southeast-6 | sns.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | sns.ap-northeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ap-northeast-3.amazonaws.com | ap-northeast-3 | sns.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | sns.ap-northeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ap-northeast-2.amazonaws.com | ap-northeast-2 | sns.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | sns.ap-southeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ap-southeast-1.amazonaws.com | ap-southeast-1 | sns.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | sns.ap-southeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ap-southeast-2.amazonaws.com | ap-southeast-2 | sns.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | sns.ap-east-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ap-east-2.amazonaws.com | ap-east-2 | sns.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | sns.ap-southeast-7.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ap-southeast-7.amazonaws.com | ap-southeast-7 | sns.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | sns.ap-northeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ap-northeast-1.amazonaws.com | ap-northeast-1 | sns.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | sns.ca-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ca-central-1.amazonaws.com | ca-central-1 | sns.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | sns-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | sns.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | sns-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | sns.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (West) | ca-west-1 | sns.ca-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.ca-west-1.amazonaws.com | ca-west-1 | sns.ca-west-1.api.aws | HTTPS | dual_stack |
| sns.ca-west-1.amazonaws.com | ca-west-1 | sns.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | sns.eu-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.eu-central-1.amazonaws.com | eu-central-1 | sns.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | sns.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | sns.eu-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.eu-west-1.amazonaws.com | eu-west-1 | sns.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | sns.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | sns.eu-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.eu-west-2.amazonaws.com | eu-west-2 | sns.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | sns.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | sns.eu-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.eu-south-1.amazonaws.com | eu-south-1 | sns.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | sns.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | sns.eu-west-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.eu-west-3.amazonaws.com | eu-west-3 | sns.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | sns.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | sns.eu-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.eu-south-2.amazonaws.com | eu-south-2 | sns.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | sns.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | sns.eu-north-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.eu-north-1.amazonaws.com | eu-north-1 | sns.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | sns.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | sns.eu-central-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.eu-central-2.amazonaws.com | eu-central-2 | sns.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | sns.il-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.il-central-1.amazonaws.com | il-central-1 | sns.il-central-1.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | sns.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | sns.mx-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.mx-central-1.amazonaws.com | mx-central-1 | sns.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | sns.me-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.me-south-1.amazonaws.com | me-south-1 | sns.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | sns.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | sns.me-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.me-central-1.amazonaws.com | me-central-1 | sns.me-central-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | sns.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | sns.sa-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| sns.sa-east-1.amazonaws.com | sa-east-1 | sns.sa-east-1.api.aws | HTTPS | dual_stack |
| sns.sa-east-1.amazonaws.com | sa-east-1 | sns.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | sns.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| sns.us-gov-east-1.amazonaws.com | us-gov-east-1 | sns.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | sns.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | sns.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| sns.us-gov-west-1.amazonaws.com | us-gov-west-1 | sns.us-gov-west-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | sns.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (0)

_none_

#### First answer rejected (repaired)

```text
- quotas.0.name: not printed in a Standard Quota Table of the chapter: 'Topics'
- quotas.1.name: not printed in a Standard Quota Table of the chapter: 'Subscriptions'
- quotas.2.name: not printed in a Standard Quota Table of the chapter: 'Pending subscriptions'
- quotas.3.name: not printed in a Standard Quota Table of the chapter: 'Account spend threshold for SMS'
- quotas.4.name: not printed in a Standard Quota Table of the chapter: 'Delivery rate for promotional SMS messages'
- quotas.5.name: not printed in a Standard Quota Table of the chapter: 'Delivery rate for transactional SMS messages'
- quotas.6.name: not printed in a Standard Quota Table of the chapter: 'Delivery rate for email messages'
- quotas.7.name: not printed in a Standard Quota Table of the chapter: 'Maximum number of messages in PublishBatchRequest'
- quotas.8.name: not printed in a Standard Quota Table of the chapter: 'Subscription filter policies'
- quotas.9.name: not printed in a Standard Quota Table of the chapter: 'Message header'
- quotas.10.name: not printed in a Standard Quota Table of the chapter: 'Message size'
- quota_table_format: 'standard', but the chapter prints no table with the columns Name, Default, Adjustable, Description
```

### 026-amazon-eventbridge.pdf

- Status: **ok**, 1 call(s), 138.5 s, in 4,333 / out 5,496 tokens
- Service: Amazon EventBridge; quota table format: `standard`

#### Endpoints (80)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | events.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | events-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | events-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | events.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | events.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | events-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | events-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | events.us-east-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | events.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | events-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | events-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | events.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | events.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | events.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | events.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | events.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | events.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | events.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | events.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | events.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | events.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | events.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | events.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | events.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | events.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | events.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | events.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | events.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | events.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | events.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | events.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | events.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | events.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | events.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | events.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | events.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | events.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | events.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | events.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | events.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | events.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | events.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | events.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | events-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | events-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | events.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | events.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | events-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Calgary) | ca-west-1 | events-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada (Calgary) | ca-west-1 | events.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | events.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | events.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | events.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | events.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | events.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | events.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | events.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | events.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | events.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | events.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | events.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | events.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | events.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | events.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | events.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | events.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | events.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | events.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | events.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | events.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | events.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | events.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | events.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | events.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | events.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | events.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | events.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | events.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | events.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | events.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (17)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Api destinations | Each supported Region: 3,000 | Yes | The maximum number of API destinations per account per Region. |
| Connections | Each supported Region: 3,000 | Yes | The maximum number of connections per account per Region. |
| CreateEndpoint throttle limit in transactions per second | Each supported Region: 5 per second | No | The maximum number of requests per second for CreateEndpoint API. Additional requests are throttled. |
| DeleteEndpoint throttle limit in transactions per second | Each supported Region: 5 per second | No | The maximum number of requests per second for DeleteEndpoint API. Additional requests are throttled. |
| Endpoints | Each supported Region: 100 | Yes | The maximum number of endpoints per account per Region. |
| Event bus policy size | Each supported Region: 10,240 | Yes | Maximum policy size, in characters. This policy size increases each time you grant access to another account. You can see your current policy and its size by using the DescribeEventBus API. |
| Event buses | Each supported Region: 100 | Yes | Maximum event buses per account. |
| Event pattern size | Each supported Region: 2,048 | Yes | Maximum size of an event pattern, in characters. |
| Invocations throttle limit in transactions per second | us-east-1: 18,750; us-east-2: 4,500; us-west-1: 2,250; us-west-2: 18,750; ap-east-1: 1,100; ap-northeast-1: 2,250 per second; ap-northeast-2: 1,100 per second; ap-south-1: 1,100 per second; ap-southeast-1: 2,250 per second; ap-southeast-2: 2,250 per second; ca-central-1: 1,100 per second; eu-central-1: 4,500 per second; eu-north-1: 1,100 per second; eu-south-2: 4,500 per second; eu-west-1: 18,750 per second; eu-west-2: 2,250 per second; eu-west-3: 1,100 per second; sa-east-1: 1,100 per second; Each of the other supported Regions: 750 per second | Yes | An invocation is an event matching a rule and being sent on to the rules targets. After the limit is reached, the invocations are throttled; that is, they still happen but they are delayed. |
| Number of rules | af-south-1: 100; eu-south-1: 100; Each of the other supported Regions: 300 | Yes | Maximum number of rules an account can have per event bus |
| PutEvents throttle limit in transactions per second | us-east-1: 10,000; us-east-2: 2,400; us-west-1: 1,200; us-west-2: 10,000; ap-east-1: 600; ap-northeast-1: 1,200; ap-northeast-2: 600; ap-south-1: 600; ap-southeast-1: 1,200; ap-southeast-2: 1,200; ca-central-1: 600; eu-central-1: 2,400; eu-north-1: 600; eu-south-2: 2,400; eu-west-1: 10,000; eu-west-2: 1,200; eu-west-3: 600; sa-east-1: 600 per second | Yes | Maximum number of requests per second for PutEvents API. Additional requests are throttled. The invocations will still occur, but are delayed. |
| Rate of invocations per API destination | Each supported Region: 300 per second | Yes | The maximum number of invocations per second to send to each API destination endpoint per account per Region. Once the quota is met, future invocations to that API destination are throttled. The invocations will still occur, but are delayed. |
| Targets per rule | Each supported Region: 5 | No | Maximum number of targets that can be associated with a rule |
| Throttle limit in transactions per second for control plane APIs | Each supported Region: 50 per second | No | Maximum number of requests per second for EventBridge control plane API operations. Additional requests are throttled. |
| UpdateEndpoint throttle limit in transactions per second | Each supported Region: 5 per second | No | The maximum number of requests per second for UpdateEndpoint API. Additional requests are throttled. |
| [EventsV2] Combined ingestion throughput and count per Event Group per second | Each supported Region: 1,500 per second | No | The maximum event throughput per Event Group per Second. Counted as the sum of (number of events) + (total size of those events in KB) delivered to a given event group within any one-second window. |
| [EventsV2] Event Buses | Each supported Region: 5 | Yes | The maximum number of V2 Event Buses owned by this account per Region. Does not include buses shared with this account. |

### 092-aws-secrets-manager.pdf

- Status: **failed**, 2 call(s), 276.9 s, in 15,326 / out 10,060 tokens

#### Error

```text
- endpoints.2.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-east-2.api.aws'
- endpoints.5.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-east-1.api.aws'
- endpoints.6.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.us-east-1.api.aws'
- endpoints.9.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-west-2.api.aws'
- endpoints.10.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.us-west-2.api.aws'
- endpoints.12.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-southeast-1.api.aws'
- endpoints.14.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-southeast-2.api.aws'
- endpoints.16.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-northeast-1.api.aws'
- endpoints.18.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-northeast-3.api.aws'
- endpoints.20.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-northeast-2.api.aws'
- endpoints.22.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-south-1.api.aws'
- endpoints.24.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-southeast-2.api.aws'
- endpoints.26.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-southeast-4.api.aws'
- endpoints.28.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-southeast-6.api.aws'
- endpoints.30.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-south-2.api.aws'
- endpoints.32.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-southeast-3.api.aws'
- endpoints.34.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-southeast-5.api.aws'
- endpoints.36.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ca-central-1.api.aws'
- endpoints.38.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ca-central-1.api.aws'
- endpoints.40.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ca-west-1.api.aws'
- endpoints.42.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ca-west-1.api.aws'
- endpoints.44.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-central-1.api.aws'
- endpoints.46.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-west-1.api.aws'
- endpoints.48.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-west-2.api.aws'
- endpoints.50.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-south-1.api.aws'
- endpoints.52.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-west-3.api.aws'
- endpoints.54.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-south-2.api.aws'
- endpoints.56.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-north-1.api.aws'
- endpoints.58.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-central-2.api.aws'
- endpoints.60.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.il-central-1.api.aws'
- endpoints.62.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.mx-central-1.api.aws'
- endpoints.64.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.me-south-1.api.aws'
- endpoints.66.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.me-central-1.api.aws'
- endpoints.69.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.us-gov-east-1.api.aws'
- endpoints.71.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-gov-east-1.api.aws'
- endpoints.73.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.us-gov-west-1.api.aws'
- endpoints.75.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-gov-west-1.api.aws'
- quotas.1.name: not printed in a Standard Quota Table of the chapter: 'Combined rate of PutSecretValue, RemoveRegionsFromReplication, ReplicateSecretToRegion, StopReplicationToRegion, UpdateSecret, and UpdateSecretVersionStage API requests'
--- after repair:
- endpoints.6.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.us-east-1.api.aws'
- endpoints.10.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.us-west-2.api.aws'
- endpoints.12.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-southeast-1.api.aws'
- endpoints.14.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-southeast-2.api.aws'
- endpoints.16.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-northeast-1.api.aws'
- endpoints.18.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-northeast-3.api.aws'
- endpoints.20.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-northeast-2.api.aws'
- endpoints.22.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-south-1.api.aws'
- endpoints.24.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-southeast-2.api.aws'
- endpoints.26.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-southeast-4.api.aws'
- endpoints.28.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-southeast-6.api.aws'
- endpoints.30.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-south-2.api.aws'
- endpoints.32.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-southeast-3.api.aws'
- endpoints.34.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-southeast-5.api.aws'
- endpoints.36.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ca-central-1.api.aws'
- endpoints.38.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ca-central-1.api.aws'
- endpoints.40.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ca-west-1.api.aws'
- endpoints.42.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ca-west-1.api.aws'
- endpoints.44.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-central-1.api.aws'
- endpoints.46.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-west-1.api.aws'
- endpoints.48.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-west-2.api.aws'
- endpoints.50.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-south-1.api.aws'
- endpoints.52.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-west-3.api.aws'
- endpoints.54.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-south-2.api.aws'
- endpoints.56.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-north-1.api.aws'
- endpoints.58.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.eu-central-2.api.aws'
- endpoints.60.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.il-central-1.api.aws'
- endpoints.62.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.mx-central-1.api.aws'
- endpoints.64.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.me-south-1.api.aws'
- endpoints.66.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.me-central-1.api.aws'
- endpoints.69.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.us-gov-east-1.api.aws'
- endpoints.71.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-gov-east-1.api.aws'
- endpoints.73.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.us-gov-west-1.api.aws'
- endpoints.75.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-gov-west-1.api.aws'
- quotas.1.name: not printed in a Standard Quota Table of the chapter: 'Combined rate of PutSecretValue, RemoveRegionsFromReplication, ReplicateSecretToRegion, StopReplicationToRegion, UpdateSecret, and UpdateSecretVersionStage API requests'
```

### 023-amazon-elastic-kubernetes-service.pdf

- Status: **ok**, 1 call(s), 72.9 s, in 4,524 / out 2,690 tokens
- Service: Amazon Elastic Kubernetes Service; quota table format: `standard`

#### Endpoints (40)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | eks.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | fips.eks.us-east-2.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | eks.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | fips.eks.us-east-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | eks.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | fips.eks.us-west-1.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | eks.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | fips.eks.us-west-2.amazonaws.com | HTTPS | fips |
| Africa (Cape Town) | af-south-1 | eks.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | eks.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | eks.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | eks.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | eks.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | eks.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | eks.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | eks.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | eks.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | eks.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | eks.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | eks.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | eks.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | eks.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | eks.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | eks.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | eks.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | eks.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | eks.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | eks.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | eks.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | eks.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | eks.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | eks.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | eks.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | eks.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | eks.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | eks.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | eks.me-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | eks.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | eks.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | eks.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (13)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Access entries per cluster | Each supported Region: 3,000 | No | The maximum number of access entries per cluster. |
| Clusters | Each supported Region: 100 | Yes | The maximum number of EKS clusters in this account in the current Region. |
| Control plane security groups per cluster | Each supported Region: 4 | No | The maximum number of control plane security groups per cluster (these are specified when you create the cluster). |
| EKS Anywhere Enterprise Subscriptions | Each supported Region: 10 | Yes | The maximum number of EKS Anywhere Enterprise Subscriptions in this account in the current Region. |
| Fargate profiles per cluster | Each supported Region: 10 | Yes | The maximum number of Fargate profiles per cluster. |
| Label pairs per Fargate profile selector | Each supported Region: 5 | Yes | The maximum number of label pairs per Fargate profile selector. |
| Managed node groups per cluster | Each supported Region: 30 | Yes | The maximum number of managed node groups per cluster. |
| Nodes per managed node group | Each supported Region: 450 | Yes | The maximum number of nodes per managed node group. |
| Public endpoint access CIDR ranges per cluster | Each supported Region: 40 | No | The maximum number of public endpoint access CIDR ranges per cluster (these are specified when you create or update the cluster). |
| Registered clusters | Each supported Region: 10 | Yes | The maximum number of registered clusters in this account in the current Region. |
| Remote node networks per cluster | Each supported Region: 15 | Yes | The maximum number of remote node networks per cluster. |
| Remote pod networks per cluster | Each supported Region: 15 | Yes | The maximum number of remote pod networks per cluster. |
| Selectors per Fargate profile | Each supported Region: 5 | Yes | The maximum number of selectors per Fargate profile. |

### 078-aws-iam-identity-center.pdf

- Status: **ok**, 1 call(s), 108.8 s, in 6,504 / out 3,886 tokens
- Service: AWS IAM Identity Center; quota table format: `standard`

#### Endpoints (70)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | sso.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | sso-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | sso.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | sso.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | sso-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | sso.us-east-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | sso.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | sso-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | sso.us-west-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | sso.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | sso-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | sso.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | sso.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | sso.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | sso.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | sso.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | sso.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | sso.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | sso.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | sso.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-1 | sso.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-1 | sso.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | sso.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | sso.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | sso.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | sso.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | sso.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | sso.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | sso.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | sso.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | sso.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | sso.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | sso.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | sso.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | sso.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | sso-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | sso.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | sso.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | sso-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Calgary) | ca-west-1 | sso.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | sso.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | sso.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | sso.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | sso.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | sso.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | sso.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | sso.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | sso.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | sso.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | sso.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | sso.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | sso.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | sso.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | sso.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | sso.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | sso.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | sso.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | sso.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | sso.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | sso.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | sso.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | sso.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | sso.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | sso.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | sso.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | sso.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | sso.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | sso.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | sso.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | sso.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (6)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| File size of service provider SAML 2.0 certificates (in PEM format) | Each supported Region: 2 Kilobytes | No | The maximum file size (in KB) of service provider SAML 2.0 certificates (in PEM format). |
| Number of groups supported in IAM Identity Center | Each supported Region: 100,000 | Yes | The maximum number of groups supported in IAM Identity Center. |
| Number of permission sets allowed in IAM Identity Center | Each supported Region: 3,500 | Yes | The default number of permission sets in IAM Identity Center. |
| Number of permission sets allowed per AWS account | Each supported Region: 500 | Yes | The default number of permission sets allowed per AWS account. |
| Number of users supported in IAM Identity Center | Each supported Region: 200,000 | Yes | The default number of users supported in IAM Identity Center. |
| Total number of AWS accounts or applications that can be configured | Each supported Region: 7,000 | Yes | The default number of AWS accounts or applications that can be configured. This quota applies separately to AWS accounts and to applications. You can configure up to 7000 accounts and up to 7000 applications. |

### 038-amazon-opensearch-service.pdf

- Status: **failed**, 2 call(s), 599.3 s, in 25,547 / out 20,190 tokens

#### Error

```text
- endpoints.174.endpoint: not printed in an endpoints table of the 'Amazon OpenSearch Service' chapter: 'osis.eu-south-1.amazonaws.com'
- endpoints.178.endpoint: not printed in an endpoints table of the 'Amazon OpenSearch Service' chapter: 'osis.eu-central-2.amazonaws.com'
- quotas.5.name: not printed in a Standard Quota Table of the chapter: 'Total storage per domain'
- quotas.6.name: not printed in a Standard Quota Table of the chapter: 'Custom packages per Region'
- quotas.7.name: not printed in a Standard Quota Table of the chapter: 'Custom packages per domain'
- quotas.8.name: not printed in a Standard Quota Table of the chapter: 'Default indexing capacity (OCUs)'
- quotas.9.name: not printed in a Standard Quota Table of the chapter: 'Default search capacity (OCUs)'
- quotas.10.name: not printed in a Standard Quota Table of the chapter: 'Maximum indexing capacity (OCUs)'
- quotas.11.name: not printed in a Standard Quota Table of the chapter: 'Maximum search capacity (OCUs)'
- quotas.12.name: not printed in a Standard Quota Table of the chapter: 'Data access policies'
- quotas.13.name: not printed in a Standard Quota Table of the chapter: 'Encryption policies'
- quotas.14.name: not printed in a Standard Quota Table of the chapter: 'Network policies'
- quotas.15.name: not printed in a Standard Quota Table of the chapter: 'SAML providers'
- quotas.16.name: not printed in a Standard Quota Table of the chapter: 'Data access policy size'
- quotas.17.name: not printed in a Standard Quota Table of the chapter: 'Network policy size'
- quotas.18.name: not printed in a Standard Quota Table of the chapter: 'SAML provider size'
- quotas.19.name: not printed in a Standard Quota Table of the chapter: 'Encryption policy size'
- quotas.20.name: not printed in a Standard Quota Table of the chapter: 'Collection tags'
- quotas.21.name: not printed in a Standard Quota Table of the chapter: 'Collections per collection group (Classic)'
- quotas.22.name: not printed in a Standard Quota Table of the chapter: 'Collections per collection group (NextGen)'
- quotas.23.name: not printed in a Standard Quota Table of the chapter: 'Collections with unique KMS keys (not in a collection group)'
- quotas.24.name: not printed in a Standard Quota Table of the chapter: 'OpenSearch Serverless-managed VPC endpoints'
- quotas.25.name: not printed in a Standard Quota Table of the chapter: 'Indexes per Amazon OpenSearch Serverless collection'
- quotas.26.name: not printed in a Standard Quota Table of the chapter: 'Index templates per Amazon OpenSearch Serverless collection'
- quotas.27.name: not printed in a Standard Quota Table of the chapter: 'Collection groups per account'
--- after repair:
- endpoints.174.endpoint: not printed in an endpoints table of the 'Amazon OpenSearch Service' chapter: 'osis.eu-south-1.amazonaws.com'
- endpoints.178.endpoint: not printed in an endpoints table of the 'Amazon OpenSearch Service' chapter: 'osis.eu-central-2.amazonaws.com'
- quotas.5.name: not printed in a Standard Quota Table of the chapter: 'Total storage per domain'
```

### 086-aws-lambda.pdf

- Status: **ok**, 1 call(s), 236.8 s, in 7,427 / out 8,655 tokens
- Service: AWS Lambda; quota table format: `standard`

#### Endpoints (75)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | lambda.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | lambda-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | lambda.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | lambda.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | lambda-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | lambda.us-east-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | lambda.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | lambda-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | lambda.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | lambda.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | lambda.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | lambda.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | lambda.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | lambda.ap-south-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Hong Kong) | ap-south-2 | lambda.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | lambda.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | lambda.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-5 | lambda.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-5 | lambda.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-4 | lambda.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-4 | lambda.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | lambda.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | lambda.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | lambda.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | lambda.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | lambda.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | lambda.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | lambda.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | lambda.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | lambda.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | lambda.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | lambda.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | lambda.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | lambda.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | lambda.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | lambda.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | lambda.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | lambda.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | lambda.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | lambda.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | lambda.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | lambda.ca-west-1.amazonaws.com | HTTPS | global |
| Canada (Central) | ca-central-1 | lambda.ca-west-1.api.aws | HTTPS | global |
| Europe (Frankfurt) | eu-central-1 | lambda.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | lambda.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | lambda.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | lambda.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | lambda.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | lambda.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | lambda.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | lambda.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | lambda.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | lambda.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | lambda.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | lambda.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | lambda.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | lambda.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | lambda.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | lambda.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | lambda.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | lambda.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | lambda.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | lambda.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | lambda.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | lambda.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | lambda.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | lambda.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | lambda.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | lambda.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | lambda.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | lambda-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | lambda.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | lambda.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | lambda-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | lambda.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (73)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Arm vCPUs for all Web Functions | Each supported Region: 2,000 | Yes | The Arm64 vCPU capacity for Lambda Web Function execution environments in this account in the current Region. |
| Asynchronous invocation request throughput on Lambda Managed Instances | Each supported Region: 5 | Yes | The maximum invoke request throughput (MB/s) for asynchronous invocations on Lambda Managed Instances. Asynchronous invocations occur when Lambda functions are invoked by services such as Amazon S3 or Amazon SNS. |
| Asynchronous payload | Each supported Region: 1,024 Kilobytes | No | The maximum size of an incoming asynchronous invocation request. |
| Burst rate of CreateMicrovmAuthToken API requests | Each supported Region: 50 | Yes | The maximum number of CreateMicrovmAuthToken API requests that can be sent in one burst. |
| Burst rate of CreateMicrovmShell AuthToken API requests | Each supported Region: 5 | Yes | The maximum number of CreateMicrovmShell AuthToken API requests that can be sent in one burst. |
| Burst rate of GetMicrovm API requests | Each supported Region: 100 | Yes | The maximum number of GetMicrovm API requests that can be sent in one burst. |
| Burst rate of ResumeMicrovm API requests | Each supported Region: 5 | Yes | The maximum number of ResumeMicrovm API requests that can be sent in one burst. |
| Burst rate of RunMicrovm API requests | Each supported Region: 5 | Yes | The maximum number of RunMicrovm API requests that can be sent in one burst. |
| Burst rate of SuspendMicrovm API requests | Each supported Region: 2 | Yes | The maximum number of SuspendMicrovm API requests that can be sent in one burst. |
| Burst rate of TerminateMicrovm API requests | Each supported Region: 10 | Yes | The maximum number of TerminateMicrovm API requests that can be sent in one burst. |
| Capacity providers | Each supported Region: 1,000 | Yes | The maximum number of capacity providers that can be created in an account. |
| Concurrency scaling rate | Each supported Region: 1,000 | No | The maximum immediate increase in function concurrency that can occur in response to an increase in traffic or execution duration. Every 10 seconds, each synchronously invoked Lambda function can scale by an additional 1,000 concurrent executions until the total concurrency across your functions in a Region reaches the account concurrency limit. |
| Concurrent connections per 1 vCPU MicroVM | Each supported Region: 8 Count | No | The maximum number of concurrent connections per MicroVM with 1 vCPU. |
| Concurrent connections per 16 vCPU MicroVM | Each supported Region: 128 Count | No | The maximum number of concurrent connections per MicroVM with 16 vCPUs. |
| Concurrent connections per 2 vCPU MicroVM | Each supported Region: 16 Count | No | The maximum number of concurrent connections per MicroVM with 2 vCPUs. |
| Concurrent connections per 4 vCPU MicroVM | Each supported Region: 32 Count | No | The maximum number of concurrent connections per MicroVM with 4 vCPUs. |
| Concurrent connections per 8 vCPU MicroVM | Each supported Region: 64 Count | No | The maximum number of concurrent connections per MicroVM with 8 vCPUs. |
| Concurrent executions | Each supported Region: 1,000 Count | Yes | The maximum number of events that functions can process simultaneously in the current Region. |
| Deployment package size (console editor) | Each supported Region: 3 Megabytes | No | The maximum size of a deployment package or layer archive when you upload it through the console editor. Upload larger files with Amazon S3. |
| Deployment package size (direct upload) | Each supported Region: 50 Megabytes | No | The maximum size of a deployment package or layer archive when you upload it directly to Lambda. Upload larger files with Amazon S3. |
| Deployment package size (unzipped) | Each supported Region: 250 Megabytes | No | The maximum size of the contents of a deployment package or layer archive when its unzipped. |
| Durable execution storage written in megabytes | Each supported Region: 100 Megabytes | No | The maximum cumulative amount of data persisted per durable execution, including input and output payloads, checkpoints, and error data, measured in megabytes. |
| DynamoDB Event Source Mapping throughput on Lambda Managed Instances | Each supported Region: 10 Megabytes/Second | Yes | The maximum throughput (MB/s) per DynamoDB event source mapping on Lambda Managed Instances. |
| Elastic network interfaces per VPC | Each supported Region: 3,000 | Yes | The maximum number of network interfaces that Lambda creates for a VPC with functions attached. Lambda creates a network interface for each combination of subnet and security group that functions connect to. |
| Endpoints per Web Function | Each supported Region: 10 | No | The maximum number of endpoints allowed per Lambda Web Function. |
| Environment variable size | Each supported Region: 4 Kilobytes | No | The maximum combined size of environment variables that are configured on a function. |
| File descriptors | Each supported Region: 1,024 | No | The maximum number of file descriptors that a function can have open. |
| Function and layer storage | Each supported Region: 300 Gigabytes | Yes | The amount of storage that is available for deployment packages and layer archives in the current Region. |
| Function invocation rate to initiate durable executions | us-east-1: 6,000; us-west-2: 6,000; eu-west-1: 6,000; Each of the other supported Regions: 3,000 | Yes | The maximum number of new durable executions that you can initiate per second. |
| Function layers | Each supported Region: 5 | No | The maximum number of layers that you can add to your function. |
| Function resource-based policy | Each supported Region: 20 Kilobytes | No | The maximum combined size of resource-based policies that are configured on a function. |
| Function timeout | Each supported Region: 900 | No | The maximum timeout that you can configure for a function. |
| Function versions per capacity provider | Each supported Region: 100 | No | The maximum number of function versions per capacity provider. |
| Kafka Event Source Mappings in default mode on Lambda Managed Instances | Each supported Region: 100 | No | The maximum number of Kafka event source mappings in default mode on Lambda Managed Instances. |
| Kafka Stream Event Source Mapping throughput in non-provisioned mode | Each supported Region: 5 Megabytes/Second | No | The maximum data throughput (MB/s) per Kafka Stream event source mapping in non-provisioned mode. |
| Kinesis Event Source Mapping throughput on Lambda Managed Instances | Each supported Region: 25 Megabytes/Second | Yes | The maximum data throughput (MB/s) per Kinesis event source mapping on Lambda Managed Instances. |
| Max Execution Duration of a MicroVM (in Hours) | Each supported Region: 8 Hours | No | The maximum execution duration of a MicroVM (in Hours). |
| Max allocated ARM_64 MicroVM memory | us-east-1: 1,024 Gigabytes; us-east-2: 1,024 Gigabytes; us-west-2: 1,024 Gigabytes; ap-northeast-1: 1,024 Gigabytes; Each of the other supported Regions: 400 Gigabytes | Yes | The maximum total configured baseline memory across all concurrently running ARM_64 MicroVMs, per account, per region. Individual MicroVMs can burst up to 4x their configured baseline memory. |
| Maximum number of durable operations per durable execution | Each supported Region: 30,000 | No | The maximum number of durable operations (including customer-initiated operations and automatic retries) that trigger state persistence within a single durable execution. |
| Maximum running durable executions | us-east-1: 10,000,000; us-west-2: 10,000,000; eu-west-1: 10,000,000; Each of the other supported Regions: 5,000,000 | Yes | The maximum number of durable executions that can be running simultaneously in the current region. |
| Network bandwidth per execution environment | Each supported Region: 625 Megabits/Second | Yes | The maximum sustained network bandwidth, in megabits per second, for a Lambda function execution environment that is not attached to a VPC. |
| Network connectors | Each supported Region: 1,000 | No | The maximum number of Network Connectors per account. |
| Number of MicroVM images | Each supported Region: 100 | Yes | The maximum number of MicroVM images per account per region. |
| Number of concurrent MicroVM image builds | us-east-1: 10 Count; us-east-2: 10 Count; us-west-2: 10 Count; ap-northeast-1: 10 Count; Each of the other supported Regions: 5 Count | Yes | The maximum number of concurrent MicroVM image builds per account per region. |
| Processes and threads | Each supported Region: 1,024 | No | The maximum combined number of processes and threads that a function can have open. |
| RPS per 16 vCPU MicroVM | Each supported Region: 160 Count | No | The maximum number of requests per second per MicroVM with 16 vCPUs / 32 GB. |
| RPS per 4 vCPU MicroVM | Each supported Region: 40 Count | No | The maximum number of requests per second per MicroVM with 4 vCPUs / 8 GB. |
| Rate of CheckpointDurableExecution API requests | us-east-1: 20,000; us-west-2: 20,000; eu-west-1: 20,000; Each of the other supported Regions: 10,000 | Yes | The maximum number of CheckpointDurableExecution API requests per second. |
| Rate of CreateMicrovmAuthToken API requests | Each supported Region: 50 | Yes | The maximum number of CreateMicrovmAuthToken API requests per second. |
| Rate of CreateMicrovmShell AuthToken API requests | Each supported Region: 5 | Yes | The maximum number of CreateMicrovmShell AuthToken API requests per second in this account in the current Region. |
| Rate of GetDurableExecution API requests | Each supported Region: 30 | Yes | The maximum number of GetDurableExecution API requests per second. |
| Rate of GetDurableExecutionHistory API requests | Each supported Region: 15 | Yes | The maximum number of GetDurableExecutionHistory API requests per second. |
| Rate of GetDurableExecutionState API requests | us-east-1: 20,000; us-west-2: 20,000; eu-west-1: 20,000; Each of the other supported Regions: 10,000 | Yes | The maximum number of GetDurableExecutionState API requests per second. |
| Rate of GetFunction API requests | Each supported Region: 100 | No | The maximum number of GetFunction API requests per second. |
| Rate of GetMicrovm API requests | Each supported Region: 100 | Yes | The maximum number of GetMicrovm API requests per second. |
| Rate of GetPolicy API requests | Each supported Region: 15 | No | The maximum number of GetPolicy API requests per second. |
| Rate of ListDurableExecutionsByFunction API requests | Each supported Region: 15 | Yes | The maximum number of ListDurableExecutionsByFunction API requests per second. |
| Rate of ResumeMicrovm API requests | Each supported Region: 5 | Yes | The maximum number of ResumeMicrovm API requests per second. |
| Rate of RunMicrovm API requests | Each supported Region: 5 | Yes | The maximum number of RunMicrovm API requests per second. |
| Rate of SendDurableExecutionCallbackFailure API requests | us-east-1: 6,000; us-west-2: 6,000; eu-west-1: 6,000; Each of the other supported Regions: 3,000 | Yes | The maximum number of SendDurableExecutionCallbackFailure API requests per second. |
| Rate of SendDurableExecutionCallbackHeartbeat API requests | us-east-1: 6,000; us-west-2: 6,000; eu-west-1: 6,000; Each of the other supported Regions: 3,000 | Yes | The maximum number of SendDurableExecutionCallbackHeartbeat API requests per second. |
| Rate of SendDurableExecutionCallbackSuccess API requests | us-east-1: 6,000; us-west-2: 6,000; eu-west-1: 6,000; Each of the other supported Regions: 3,000 | Yes | The maximum number of SendDurableExecutionCallbackSuccess API requests per second. |
| Rate of StopDurableExecution API requests | us-east-1: 600; us-west-2: 600; eu-west-1: 600; Each of the other supported Regions: 300 | Yes | The maximum number of StopDurableExecution API requests per second. |
| Rate of SuspendMicrovm API requests | Each supported Region: 2 | Yes | The maximum number of SuspendMicrovm API requests per second. |
| Rate of TerminateMicrovm API requests | Each supported Region: 10 | Yes | The maximum number of TerminateMicrovm API requests per second. |
| Rate of capacity provider read API requests | Each supported Region: 15 | No | The maximum combined rate (requests per second) for all capacity provider read APIs. |
| Rate of capacity provider write API requests | Each supported Region: 1 | No | The maximum combined rate (requests per second) for all capacity provider write APIs. |
| Rate of control plane API requests (excludes invocation, GetFunction, and GetPolicy requests) | Each supported Region: 15 | No | The maximum number of API requests per second (excluding invocation, GetFunction, and GetPolicy requests). |
| Rate of requests per Web Function Endpoint | Each supported Region: 10,000 | No | The maximum number of requests per second allowed for a single Lambda Web Function endpoint. |
| Rate of requests to Web Functions | Each supported Region: 100,000 | No | The maximum number of requests per second allowed across all your Lambda Web Function endpoints in this account in the current Region. |
| Revisions per Web Function | Each supported Region: 50 | No | The maximum number of revisions retained per Lambda Web Function. When this limit is reached, the oldest revisions not referenced by any endpoint are automatically deleted. |
| SQS Event Source Mapping throughput in default mode on Lambda Managed Instances | Each supported Region: 5 Megabytes/Second | No | The maximum data throughput (MB/s) per SQS event source mapping in default mode on Lambda Managed Instances. |
| Synchronous payload | Each supported Region: 6 Megabytes | No | The maximum size of an incoming synchronous invocation request or outgoing response. |

### 004-amazon-athena.pdf

- Status: **ok**, 1 call(s), 205.5 s, in 7,599 / out 7,403 tokens
- Service: Amazon Athena; quota table format: `standard`

#### Endpoints (74)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | athena.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | athena-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | athena-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | athena.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | athena.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | athena-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | athena-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | athena.us-east-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | athena.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | athena-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | athena-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | athena.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | athena.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | athena.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | athena.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | athena.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | athena.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | athena.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | athena.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | athena.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | athena.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | athena.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | athena.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | athena.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | athena.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | athena.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | athena.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | athena.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | athena.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | athena.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | athena.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | athena.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | athena.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | athena-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | athena-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | athena.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | athena.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | athena-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Calgary) | ca-west-1 | athena-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada (Calgary) | ca-west-1 | athena.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | athena.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | athena.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | athena.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | athena.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | athena.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | athena.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | athena.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | athena.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | athena.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | athena.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | athena.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | athena.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | athena.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | athena.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | athena.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | athena.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | athena.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | athena.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | athena.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | athena.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | athena.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | athena.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | athena.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | athena.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | athena.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | athena.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | athena.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | athena-fips.us-gov-east-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | athena-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | athena.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | athena.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | athena-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | athena-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | athena.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (30)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Active DDL queries | Each supported Region: 20 | Yes | The number of active DDL queries. DDL queries include CREATE TABLE and ALTER TABLE ADD PARTITION queries. |
| Active DML queries | us-east-1: 200; us-east-2: 150; us-west-2: 150; ap-northeast-1: 150; ap-northeast-2: 100; ap-south-1: 100; ap-southeast-1: 100; ap-southeast-2: 100; eu-central-1: 150; eu-west-1: 150; eu-west-2: 100; Each of the other supported Regions: 20 | Yes | The number of active DML queries. DML queries include SELECT, CREATE TABLE AS (CTAS), and INSERT INTO queries. The specific quotas vary by AWS Region. |
| Apache Spark DPU concurrency | Each supported Region: 160 | No | The maximum number of DPUs you can consume concurrently for Apache Spark calculations. |
| Burst multiplier quota for BatchGetNamedQuery API | Each supported Region: 2 | No | Multiplier factor to scale burst capacity for BatchGetNamedQuery API based on the rate quota (Burst = Rate * BurstMultiplierQuota). BatchGetNamedQuery Burst is the maximum number of BatchGetNamedQuery API tokens you can accumulate in the account in the region |
| Burst multiplier quota for BatchGetQueryExecution API | Each supported Region: 2 | No | Multiplier factor to scale burst capacity for BatchGetQueryExecution API based on the rate quota (Burst = Rate * BurstMultiplierQuota). BatchGetQueryExecution Burst is the maximum number of BatchGetQueryExecution API tokens you can accumulate in the account in the region |
| Burst multiplier quota for CreateNamedQuery API | Each supported Region: 4 | No | Multiplier factor to scale burst capacity for CreateNamedQuery API based on the rate quota (Burst = Rate * BurstMultiplierQuota). CreateNamedQuery Burst is the maximum number of CreateNamedQuery API tokens you can accumulate in the account in the region |
| Burst multiplier quota for DeleteNamedQuery API | Each supported Region: 4 | No | Multiplier factor to scale burst capacity for DeleteNamedQuery API based on the rate quota (Burst = Rate * BurstMultiplierQuota). DeleteNamedQuery Burst is the maximum number of DeleteNamedQuery API tokens you can accumulate in the account in the region |
| Burst multiplier quota for GetNamedQuery API | Each supported Region: 4 | No | Multiplier factor to scale burst capacity for GetNamedQuery API based on the rate quota (Burst = Rate * BurstMultiplierQuota). GetNamedQuery Burst is the maximum number of GetNamedQuery API tokens you can accumulate in the account in the region |
| Burst multiplier quota for GetQueryExecution API | us-west-1: 2; af-south-1: 2; ap-east-1: 2; ap-northeast-3: 2; ap-south-2: 2; ap-southeast-3: 2; ap-southeast-4: 2; ca-central-1: 2; ca-west-1: 2; eu-central-2: 2; eu-north-1: 2; eu-south-1: 2; eu-south-2: 2; eu-west-3: 2; il-central-1: 2; sa-east-1: 2; Each of the other supported Regions: 1 | No | Multiplier factor to scale burst capacity for GetQueryExecution API based on the rate quota (Burst = Rate * BurstMultiplierQuota). GetQueryExecution Burst is the maximum number of GetQueryExecution API tokens you can accumulate in the account in the region |
| Burst multiplier quota for GetQueryResults API | us-east-1: 5; us-east-2: 5; us-west-2: 5; ap-northeast-1: 5; ap-northeast-2: 5; ap-south-1: 5; ap-southeast-1: 5; ap-southeast-2: 5; eu-central-1: 5; eu-west-1: 5; eu-west-2: 5; Each of the other supported Regions: 2 | No | Multiplier factor to scale burst capacity for GetQueryResults API based on the rate quota (Burst = Rate * BurstMultiplierQuota). GetQueryResults Burst is the maximum number of GetQueryResults API tokens you can accumulate in the account in the region |
| Burst multiplier quota for ListNamedQueries API | Each supported Region: 2 | No | Multiplier factor to scale burst capacity for ListNamedQueries API based on the rate quota (Burst = Rate * BurstMultiplierQuota). ListNamedQueries Burst is the maximum number of ListNamedQueries API tokens you can accumulate in the account in the region |
| Burst multiplier quota for ListQueryExecutions API | Each supported Region: 2 | No | Multiplier factor to scale burst capacity for ListQueryExecutions API based on the rate quota (Burst = Rate * BurstMultiplierQuota). ListQueryExecutions Burst is the maximum number of ListQueryExecutions API tokens you can accumulate in the account in the region |
| Burst multiplier quota for StartQueryExecution API | us-east-1: 5; us-east-2: 5; us-west-2: 5; ap-northeast-1: 5; eu-central-1: 5; eu-west-1: 5; eu-west-2: 5; Each of the other supported Regions: 4 | No | Multiplier factor to scale burst capacity for StartQueryExecution API based on the rate quota (Burst = Rate * BurstMultiplierQuota). StartQueryExecution Burst is the maximum number of StartQueryExecution API tokens you can accumulate in the account in the region |
| Burst multiplier quota for StopQueryExecution API | Each supported Region: 4 | No | Multiplier factor to scale burst capacity for StopQueryExecution API based on the rate quota (Burst = Rate * BurstMultiplierQuota). StopQueryExecution Burst is the maximum number of StopQueryExecution API tokens you can accumulate in the account in the region |
| DDL query timeout | Each supported Region: 600 | No | The maximum amount of time in minutes a DDL query can run before it gets cancelled. DDL queries include CREATE TABLE and CREATE TABLE ADD PARTITION queries. |
| DML query timeout | Each supported Region: 30 | Yes | The maximum amount of time in minutes a DML query can run before it gets cancelled. DML queries include SELECT, CTAS and INSERT queries. |
| Maximum number of workgroups per account | Each supported Region: 1,000 | No | The maximum number of workgroups that can be created in an account. |
| On-demand DPUs per account | Each supported Region: 4 | Yes | The maximum number of DPUs (Data Processing Units) that can be active across all Spark workloads in this account. This limit applies only to Athena Spark Version 3.5 and does not affect Athena Engine Version 3. |
| Provisioned DPU | Each supported Region: 1,000 | No | Maximum number of DPUs provisioned for the account. |
| Replenishment rate of BatchGetNamedQuery API calls | Each supported Region: 5 per second | Yes | Maximum call rate per second for BatchGetNamedQuery API in this account in the current Region. For this API, the service adds tokens to your account at a fixed rate. One token allows you to make one API call. You accumulate tokens for an API up to a maximum of (Replenishment rate quota of the API * Burst multiplier quota of the API) |
| Replenishment rate of BatchGetQueryExecution API calls | Each supported Region: 10 per second | Yes | Maximum call rate per second for BatchGetQueryExecution API in this account in the current Region. For this API, the service adds tokens to your account at a fixed rate. One token allows you to make one API call. You accumulate tokens for an API up to a maximum of (Replenishment rate quota of the API * Burst multiplier quota of the API) |
| Replenishment rate of CreateNamedQuery API calls | Each supported Region: 5 per second | Yes | Maximum call rate per second for CreateNamedQuery API in this account in the current Region. For this API, the service adds tokens to your account at a fixed rate. One token allows you to make one API call. You accumulate tokens for an API up to a maximum of (Replenishment rate quota of the API * Burst multiplier quota of the API) |
| Replenishment rate of DeleteNamedQuery API calls | Each supported Region: 5 per second | Yes | Maximum call rate per second for DeleteNamedQuery API in this account in the current Region. For this API, the service adds tokens to your account at a fixed rate. One token allows you to make one API call. You accumulate tokens for an API up to a maximum of (Replenishment rate quota of the API * Burst multiplier quota of the API) |
| Replenishment rate of GetNamedQuery API calls | Each supported Region: 5 per second | Yes | Maximum call rate per second for GetNamedQuery API in this account in the current Region. For this API, the service adds tokens to your account at a fixed rate. One token allows you to make one API call. You accumulate tokens for an API up to a maximum of (Replenishment rate quota of the API * Burst multiplier quota of the API) |
| Replenishment rate of GetQueryExecution API calls | us-east-1: 500 per second; us-east-2: 500 per second; us-west-2: 500 per second; ap-northeast-1: 500 per second; ap-northeast-2: 500 per second; ap-south-1: 500 per second; ap-southeast-1: 500 per second; ap-southeast-2: 500 per second; eu-central-1: 500 per second; eu-west-1: 500 per second; eu-west-2: 500 per second; Each of the other supported Regions: 100 per second | Yes | Maximum call rate per second for GetQueryExecution API in this account in the current Region. For this API, the service adds tokens to your account at a fixed rate. One token allows you to make one API call. You accumulate tokens for an API up to a maximum of (Replenishment rate quota of the API * Burst multiplier quota of the API) |
| Replenishment rate of GetQueryResults API calls | Each supported Region: 100 per second | Yes | Maximum call rate per second for GetQueryResults API in this account in the current Region. For this API, the service adds tokens to your account at a fixed rate. One token allows you to make one API call. You accumulate tokens for an API up to a maximum of (Replenishment rate quota of the API * Burst multiplier quota of the API) |
| Replenishment rate of ListNamedQueries API calls | Each supported Region: 5 per second | Yes | Maximum call rate per second for ListNamedQueries API in this account in the current Region. For this API, the service adds tokens to your account at a fixed rate. One token allows you to make one API call. You accumulate tokens for an API up to a maximum of (Replenishment rate quota of the API * Burst multiplier quota of the API) |
| Replenishment rate of ListQueryExecutions API calls | Each supported Region: 5 per second | Yes | Maximum call rate per second for ListQueryExecutions API in this account in the current Region. For this API, the service adds tokens to your account at a fixed rate. One token allows you to make one API call. You accumulate tokens for an API up to a maximum of (Replenishment rate quota of the API * Burst multiplier quota of the API) |
| Replenishment rate of StartQueryExecution API calls | us-east-1: 100 per second; us-east-2: 100 per second; us-west-2: 100 per second; ap-northeast-1: 100 per second; ap-northeast-2: 100 per second; ap-south-1: 100 per second; ap-southeast-1: 100 per second; ap-southeast-2: 100 per second; eu-central-1: 100 per second; eu-west-1: 100 per second; eu-west-2: 100 per second; Each of the other supported Regions: 20 per second | Yes | Maximum call rate per second for StartQueryExecution API in this account in the current Region. For this API, the service adds tokens to your account at a fixed rate. One token allows you to make one API call. You accumulate tokens for an API up to a maximum of (Replenishment rate quota of the API * Burst multiplier quota of the API) |
| Replenishment rate of StopQueryExecution API calls | us-east-1: 50 per second; us-east-2: 50 per second; us-west-2: 50 per second; ap-northeast-1: 50 per second; ap-northeast-2: 50 per second; ap-south-1: 50 per second; ap-southeast-1: 50 per second; ap-southeast-2: 50 per second; eu-central-1: 50 per second; eu-west-1: 50 per second; eu-west-2: 50 per second; Each of the other supported Regions: 20 per second | Yes | Maximum call rate per second for StopQueryExecution API in this account in the current Region. For this API, the service adds tokens to your account at a fixed rate. One token allows you to make one API call. You accumulate tokens for an API up to a maximum of (Replenishment rate quota of the API * Burst multiplier quota of the API) |

### 017-amazon-dynamodb.pdf

- Status: **failed**, 1 call(s), 532.2 s, in 9,816 / out 18,432 tokens

#### Error

```text
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 2263 column 30
--- no repair call
```

### 095-aws-step-functions.pdf

- Status: **failed**, 2 call(s), 897.6 s, in 33,007 / out 29,389 tokens

#### Error

```text
- endpoints.170.endpoint: not printed in an endpoints table of the 'AWS Step Functions' chapter: 'sync-states-fips.us-gov-west-1.amazonaws.com'
- endpoints.172.endpoint: not printed in an endpoints table of the 'AWS Step Functions' chapter: 'states-fips.us-gov-west-1.amazonaws.com'
--- after repair:
- endpoints.170.endpoint: not printed in an endpoints table of the 'AWS Step Functions' chapter: 'sync-states-fips.us-gov-west-1.amazonaws.com'
- endpoints.172.endpoint: not printed in an endpoints table of the 'AWS Step Functions' chapter: 'states-fips.us-gov-west-1.amazonaws.com'
```

### 049-amazon-simple-storage-service.pdf

- Status: **failed**, 1 call(s), 570.4 s, in 13,868 / out 18,432 tokens

#### Error

```text
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 2205 column 15
--- no repair call
```

### 025-amazon-emr.pdf

- Status: **failed**, 1 call(s), 560.5 s, in 11,318 / out 18,432 tokens

#### Error

```text
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 2173 column 26
--- no repair call
```

### 010-amazon-cloudfront.pdf

- Status: **failed**, 2 call(s), 348.1 s, in 19,236 / out 12,148 tokens

#### Error

```text
- endpoints.2.endpoint: not printed in an endpoints table of the 'Amazon CloudFront' chapter: 'cloudfront.global-api.amazonaws.com'
- endpoints.3.endpoint: not printed in an endpoints table of the 'Amazon CloudFront' chapter: 'cloudfront-fips.global-api.amazonaws.com'
- quotas.35.name: not printed in a Standard Quota Table of the chapter: 'Maximum compressed size of a Lambda function and any included libraries (Origin request and response event)'
- quotas.36.name: not printed in a Standard Quota Table of the chapter: 'Maximum compressed size of a Lambda function and any included libraries (Viewer request and response event)'
- quotas.64.name: not printed in a Standard Quota Table of the chapter: 'Maximum number of origin access identities per account'
- quotas.65.name: not printed in a Standard Quota Table of the chapter: 'Maximum number of origin groups per distribution'
- quotas.66.name: not printed in a Standard Quota Table of the chapter: 'Maximum number of origin request policies per AWS account'
- quotas.67.name: not printed in a Standard Quota Table of the chapter: 'Maximum origin response timeout (idle timeout) in minutes'
- quotas.68.name: not printed in a Standard Quota Table of the chapter: 'Maximum origins per distribution'
- quotas.69.name: not printed in a Standard Quota Table of the chapter: 'Maximum public keys in a single key group'
- quotas.70.name: not printed in a Standard Quota Table of the chapter: 'Maximum query strings per cache policy'
- quotas.71.name: not printed in a Standard Quota Table of the chapter: 'Maximum query strings per origin request policy'
- quotas.74.name: not printed in a Standard Quota Table of the chapter: 'Request body size for origin requests exposed to a Lambda@Edge function'
- quotas.77.name: not printed in a Standard Quota Table of the chapter: 'Request body size for viewer requests exposed to a Lambda@Edge function'
- quotas.81.name: not printed in a Standard Quota Table of the chapter: 'Response headers policies per AWS account'
- quotas.82.name: not printed in a Standard Quota Table of the chapter: 'Response timeout per origin (1-120 seconds)'
--- after repair:
- endpoints.2.endpoint: not printed in an endpoints table of the 'Amazon CloudFront' chapter: 'cloudfront.global-api.amazonaws.com'
- endpoints.3.endpoint: not printed in an endpoints table of the 'Amazon CloudFront' chapter: 'cloudfront-fips.global-api.amazonaws.com'
- quotas.35.name: not printed in a Standard Quota Table of the chapter: 'Maximum compressed size of a Lambda function and any included libraries (Origin request and response event)'
- quotas.36.name: not printed in a Standard Quota Table of the chapter: 'Maximum compressed size of a Lambda function and any included libraries (Viewer request and response event)'
- quotas.64.name: not printed in a Standard Quota Table of the chapter: 'Maximum number of origin access identities per account'
- quotas.65.name: not printed in a Standard Quota Table of the chapter: 'Maximum number of origin groups per distribution'
- quotas.66.name: not printed in a Standard Quota Table of the chapter: 'Maximum number of origin request policies per AWS account'
- quotas.67.name: not printed in a Standard Quota Table of the chapter: 'Maximum origin response timeout (idle timeout) in minutes'
- quotas.68.name: not printed in a Standard Quota Table of the chapter: 'Maximum origins per distribution'
- quotas.69.name: not printed in a Standard Quota Table of the chapter: 'Maximum public keys in a single key group'
- quotas.70.name: not printed in a Standard Quota Table of the chapter: 'Maximum query strings per cache policy'
- quotas.71.name: not printed in a Standard Quota Table of the chapter: 'Maximum query strings per origin request policy'
- quotas.74.name: not printed in a Standard Quota Table of the chapter: 'Request body size for origin requests exposed to a Lambda@Edge function'
- quotas.77.name: not printed in a Standard Quota Table of the chapter: 'Request body size for viewer requests exposed to a Lambda@Edge function'
- quotas.81.name: not printed in a Standard Quota Table of the chapter: 'Response headers policies per AWS account'
- quotas.82.name: not printed in a Standard Quota Table of the chapter: 'Response timeout per origin (1-120 seconds)'
```

### 074-aws-global-accelerator.pdf

- Status: **failed**, 2 call(s), 59.5 s, in 10,802 / out 2,037 tokens

#### Error

```text
- endpoints.1.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'globalaccelerator-fips.us-west-2.zonaws.com'
--- after repair:
- endpoints.1.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'globalaccelerator-fips.us-west-2.zonaws.com'
```

### 019-amazon-ecr.pdf

- Status: **ok**, 1 call(s), 255.5 s, in 6,924 / out 9,321 tokens
- Service: Amazon ECR; quota table format: `standard`

#### Endpoints (151)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| us-east-2 | us-east-2 | ecr.us-east-2.amazonaws.com | HTTPS | ipv4 |
| us-east-2 | us-east-2 | ecr-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| us-east-2 | us-east-2 | dkr-ecr.us-east-2.on.aws | HTTPS | dual_stack |
| us-east-2 | us-east-2 | dkr.ecr.us-east-2.amazonaws.com | HTTPS | ipv4 |
| us-east-2 | us-east-2 | ecr.us-east-2.api.aws | HTTPS | dual_stack |
| us-east-2 | us-east-2 | dkr-ecr-fips.us-east-2.on.aws | HTTPS | fips_dual_stack |
| us-east-2 | us-east-2 | ecr-fips.us-east-2.amazonaws.com | HTTPS | fips |
| us-east-2 | us-east-2 | api.ecr-fips.us-east-2.amazonaws.com | HTTPS | fips |
| us-east-2 | us-east-2 | api.ecr.us-east-2.amazonaws.com | HTTPS | ipv4 |
| us-east-2 | us-east-2 | dkr.ecr-fips.us-east-2.amazonaws.com | HTTPS | fips |
| us-east-1 | us-east-1 | ecr.us-east-1.amazonaws.com | HTTPS | ipv4 |
| us-east-1 | us-east-1 | dkr.ecr-fips.us-east-1.amazonaws.com | HTTPS | fips |
| us-east-1 | us-east-1 | ecr-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| us-west-1 | us-west-1 | ecr.us-west-1.amazonaws.com | HTTPS | ipv4 |
| us-west-1 | us-west-1 | api.ecr-fips.us-west-1.amazonaws.com | HTTPS | fips |
| us-west-1 | us-west-1 | ecr.us-west-1.api.aws | HTTPS | dual_stack |
| us-west-2 | us-west-2 | ecr.us-west-2.amazonaws.com | HTTPS | ipv4 |
| us-west-2 | us-west-2 | ecr-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| us-west-2 | us-west-2 | ecr.us-west-2.api.aws | HTTPS | dual_stack |
| us-west-2 | us-west-2 | ecr-fips.us-west-2.amazonaws.com | HTTPS | fips |
| af-south-1 | af-south-1 | ecr.af-south-1.amazonaws.com | HTTPS | ipv4 |
| af-south-1 | af-south-1 | api.ecr.af-south-1.amazonaws.com | HTTPS | ipv4 |
| af-south-1 | af-south-1 | ecr.af-south-1.api.aws | HTTPS | dual_stack |
| af-south-1 | af-south-1 | dkr.ecr.af-south-1.amazonaws.com | HTTPS | ipv4 |
| af-south-1 | af-south-1 | dkr-ecr.af-south-1.on.aws | HTTPS | dual_stack |
| ap-east-1 | ap-east-1 | ecr.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| ap-east-1 | ap-east-1 | dkr-ecr.ap-east-1.on.aws | HTTPS | dual_stack |
| ap-east-1 | ap-east-1 | dkr.ecr.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| ap-east-1 | ap-east-1 | ecr.ap-east-1.api.aws | HTTPS | dual_stack |
| ap-east-1 | ap-east-1 | api.ecr.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| ap-south-2 | ap-south-2 | ecr.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| ap-south-2 | ap-south-2 | api.ecr.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| ap-south-2 | ap-south-2 | dkr-ecr.ap-south-2.on.aws | HTTPS | dual_stack |
| ap-south-2 | ap-south-2 | dkr.ecr.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-3 | ap-southeast-3 | ecr.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-3 | ap-southeast-3 | api.ecr.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-3 | ap-southeast-3 | dkr-ecr.ap-southeast-3.on.aws | HTTPS | dual_stack |
| ap-southeast-3 | ap-southeast-3 | dkr.ecr.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-5 | ap-southeast-5 | ecr.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-5 | ap-southeast-5 | api.ecr.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-5 | ap-southeast-5 | dkr-ecr.ap-southeast-5.on.aws | HTTPS | dual_stack |
| ap-southeast-5 | ap-southeast-5 | dkr.ecr.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-4 | ap-southeast-4 | ecr.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-4 | ap-southeast-4 | api.ecr.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-4 | ap-southeast-4 | dkr-ecr.ap-southeast-4.on.aws | HTTPS | dual_stack |
| ap-southeast-4 | ap-southeast-4 | dkr.ecr.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| ap-south-1 | ap-south-1 | ecr.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| ap-south-1 | ap-south-1 | api.ecr.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| ap-south-1 | ap-south-1 | dkr-ecr.ap-south-1.on.aws | HTTPS | dual_stack |
| ap-south-1 | ap-south-1 | dkr.ecr.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| ap-south-1 | ap-south-1 | ecr.ap-south-1.api.aws | HTTPS | dual_stack |
| ap-southeast-2 | ap-southeast-2 | ecr.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-2 | ap-southeast-2 | ecr.ap-southeast-2.api.aws | HTTPS | dual_stack |
| ap-southeast-2 | ap-southeast-2 | api.ecr.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-2 | ap-southeast-2 | dkr.ecr.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-2 | ap-southeast-2 | dkr-ecr.ap-southeast-2.on.aws | HTTPS | dual_stack |
| ap-east-2 | ap-east-2 | ecr.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| ap-east-2 | ap-east-2 | api.ecr.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| ap-east-2 | ap-east-2 | dkr.ecr.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| ap-east-2 | ap-east-2 | dkr-ecr.ap-east-2.on.aws | HTTPS | dual_stack |
| ap-east-2 | ap-east-2 | ecr.ap-east-2.api.aws | HTTPS | dual_stack |
| ap-southeast-7 | ap-southeast-7 | ecr.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-7 | ap-southeast-7 | dkr-ecr.ap-southeast-7.on.aws | HTTPS | dual_stack |
| ap-southeast-7 | ap-southeast-7 | dkr.ecr.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-7 | ap-southeast-7 | ecr.ap-southeast-7.api.aws | HTTPS | dual_stack |
| ap-northeast-1 | ap-northeast-1 | ecr.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-1 | ap-northeast-1 | dkr-ecr.ap-northeast-1.on.aws | HTTPS | dual_stack |
| ap-northeast-1 | ap-northeast-1 | api.ecr.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-1 | ap-northeast-1 | ecr.ap-northeast-1.api.aws | HTTPS | dual_stack |
| ap-northeast-1 | ap-northeast-1 | dkr.ecr.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| ca-central-1 | ca-central-1 | ecr.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| ca-central-1 | ca-central-1 | ecr.ca-central-1.api.aws | HTTPS | dual_stack |
| ca-central-1 | ca-central-1 | dkr-ecr.ca-central-1.on.aws | HTTPS | dual_stack |
| ca-central-1 | ca-central-1 | dkr.ecr.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| ca-west-1 | ca-west-1 | ecr.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| ca-west-1 | ca-west-1 | ecr.ca-west-1.api.aws | HTTPS | dual_stack |
| ca-west-1 | ca-west-1 | api.ecr.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| ca-west-1 | ca-west-1 | dkr.ecr.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| ca-west-1 | ca-west-1 | dkr-ecr.ca-west-1.on.aws | HTTPS | dual_stack |
| eu-central-1 | eu-central-1 | ecr.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| eu-central-1 | eu-central-1 | ecr.eu-central-1.api.aws | HTTPS | dual_stack |
| eu-central-1 | eu-central-1 | dkr-ecr.eu-central-1.on.aws | HTTPS | dual_stack |
| eu-central-1 | eu-central-1 | dkr.ecr.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| eu-west-1 | eu-west-1 | ecr.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| eu-west-1 | eu-west-1 | api.ecr.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| eu-west-1 | eu-west-1 | dkr-ecr.eu-west-1.on.aws | HTTPS | dual_stack |
| eu-west-1 | eu-west-1 | dkr.ecr.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| eu-west-2 | eu-west-2 | ecr.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| eu-west-2 | eu-west-2 | ecr.eu-west-2.api.aws | HTTPS | dual_stack |
| eu-west-2 | eu-west-2 | api.ecr.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| eu-west-2 | eu-west-2 | dkr.ecr.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| eu-south-1 | eu-south-1 | ecr.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| eu-south-1 | eu-south-1 | ecr.eu-south-1.api.aws | HTTPS | dual_stack |
| eu-south-1 | eu-south-1 | api.ecr.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| eu-south-1 | eu-south-1 | dkr-ecr.eu-south-1.on.aws | HTTPS | dual_stack |
| eu-south-1 | eu-south-1 | dkr.ecr.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| eu-west-3 | eu-west-3 | ecr.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| eu-west-3 | eu-west-3 | ecr.eu-west-3.api.aws | HTTPS | dual_stack |
| eu-west-3 | eu-west-3 | api.ecr.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| eu-west-3 | eu-west-3 | dkr.ecr.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| eu-south-2 | eu-south-2 | ecr.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| eu-south-2 | eu-south-2 | ecr.eu-south-2.api.aws | HTTPS | dual_stack |
| eu-south-2 | eu-south-2 | api.ecr.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| eu-south-2 | eu-south-2 | dkr-ecr.eu-south-2.on.aws | HTTPS | dual_stack |
| eu-south-2 | eu-south-2 | dkr.ecr.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| eu-north-1 | eu-north-1 | ecr.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| eu-north-1 | eu-north-1 | ecr.eu-north-1.api.aws | HTTPS | dual_stack |
| eu-north-1 | eu-north-1 | api.ecr.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| eu-north-1 | eu-north-1 | dkr-ecr.eu-north-1.on.aws | HTTPS | dual_stack |
| eu-north-1 | eu-north-1 | dkr.ecr.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| eu-central-2 | eu-central-2 | ecr.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| eu-central-2 | eu-central-2 | ecr.eu-central-2.api.aws | HTTPS | dual_stack |
| eu-central-2 | eu-central-2 | api.ecr.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| eu-central-2 | eu-central-2 | dkr.ecr.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| il-central-1 | il-central-1 | ecr.il-central-1.amazonaws.com | HTTPS | ipv4 |
| il-central-1 | il-central-1 | ecr.il-central-1.api.aws | HTTPS | dual_stack |
| il-central-1 | il-central-1 | api.ecr.il-central-1.amazonaws.com | HTTPS | ipv4 |
| il-central-1 | il-central-1 | dkr-ecr.il-central-1.on.aws | HTTPS | dual_stack |
| il-central-1 | il-central-1 | dkr.ecr.il-central-1.amazonaws.com | HTTPS | ipv4 |
| mx-central-1 | mx-central-1 | ecr.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| mx-central-1 | mx-central-1 | ecr.mx-central-1.api.aws | HTTPS | dual_stack |
| mx-central-1 | mx-central-1 | api.ecr.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| mx-central-1 | mx-central-1 | dkr-ecr.mx-central-1.on.aws | HTTPS | dual_stack |
| mx-central-1 | mx-central-1 | dkr.ecr.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| me-south-1 | me-south-1 | ecr.me-south-1.amazonaws.com | HTTPS | ipv4 |
| me-south-1 | me-south-1 | ecr.me-south-1.api.aws | HTTPS | dual_stack |
| me-south-1 | me-south-1 | api.ecr.me-south-1.amazonaws.com | HTTPS | ipv4 |
| me-south-1 | me-south-1 | dkr-ecr.me-south-1.on.aws | HTTPS | dual_stack |
| me-south-1 | me-south-1 | dkr.ecr.me-south-1.amazonaws.com | HTTPS | ipv4 |
| me-central-1 | me-central-1 | ecr.me-central-1.amazonaws.com | HTTPS | ipv4 |
| me-central-1 | me-central-1 | ecr.me-central-1.api.aws | HTTPS | dual_stack |
| me-central-1 | me-central-1 | api.ecr.me-central-1.amazonaws.com | HTTPS | ipv4 |
| me-central-1 | me-central-1 | dkr-ecr.me-central-1.on.aws | HTTPS | dual_stack |
| me-central-1 | me-central-1 | dkr.ecr.me-central-1.amazonaws.com | HTTPS | ipv4 |
| sa-east-1 | sa-east-1 | ecr.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| sa-east-1 | sa-east-1 | dkr-ecr.sa-east-1.on.aws | HTTPS | dual_stack |
| sa-east-1 | sa-east-1 | dkr.ecr.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| sa-east-1 | sa-east-1 | ecr.sa-east-1.api.aws | HTTPS | dual_stack |
| sa-east-1 | sa-east-1 | api.ecr.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| us-gov-east-1 | us-gov-east-1 | ecr.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| us-gov-east-1 | us-gov-east-1 | ecr.us-gov-east-1.api.aws | HTTPS | dual_stack |
| us-gov-east-1 | us-gov-east-1 | dkr.ecr.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| us-gov-east-1 | us-gov-east-1 | ecr-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| us-gov-east-1 | us-gov-east-1 | api.ecr-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| us-gov-east-1 | us-gov-east-1 | api.ecr.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| us-gov-east-1 | us-gov-east-1 | ecr-fips.us-gov-east-1.api.aws | HTTPS | fips_dual_stack |
| us-gov-west-1 | us-gov-west-1 | ecr.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| us-gov-west-1 | us-gov-west-1 | ecr.us-gov-west-1.api.aws | HTTPS | dual_stack |
| us-gov-west-1 | us-gov-west-1 | dkr.ecr.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| us-gov-west-1 | us-gov-west-1 | ecr-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| us-gov-west-1 | us-gov-west-1 | api.ecr.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (23)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Basic image scans per 24 hours | Each supported Region: 100,000 | No | The maximum number of images that can be scanned within a 24 hour period in the current account and region using basic scanning. This limit includes both scan on push and manual scans. |
| Filters per rule in a replication configuration | Each supported Region: 100 | No | The maximum number of filters per rule in a replication configuration. |
| Images per repository | Each supported Region: 100,000 | Yes | The maximum number of images per repository. |
| Layer parts | Each supported Region: 4,200 | No | The maximum number of layer parts. This is only applicable if you are using Amazon ECR API actions directly to initiate multipart uploads for image push operations. |
| Lifecycle policy length | Each supported Region: 30,720 | No | The maximum number of characters in a lifecycle policy. |
| Maximum layer part size | Each supported Region: 10 | No | The maximum size (MiB) of a layer part. This is only applicable if you are using Amazon ECR API actions directly to initiate multipart uploads for image push operations. |
| Maximum layer size | Each supported Region: 52,000 | No | The maximum size (MiB) of a layer. |
| Minimum layer part size | Each supported Region: 5 | No | The minimum size (MiB) of a layer part. This is only applicable if you are using Amazon ECR API actions directly to initiate multipart uploads for image push operations. |
| Pull through cache rules per registry | Each supported Region: 50 | No | The maximum number of pull-through cache rules. |
| Rate of BatchCheckLayerAvailability requests | Each supported Region: 1,000 per second | Yes | The maximum number of BatchCheckLayerAvailability requests that you can make per second in the current Region. When an image is pushed to a repository, each image layer is checked to verify if it has been uploaded before. If it has been uploaded, then the image layer is skipped. |
| Rate of BatchGetImage requests | Each supported Region: 2,000 per second | Yes | The maximum number of BatchGetImage requests that you can make per second in the current Region. When an image is pulled, the BatchGetImage API is called once to retrieve the image manifest. If you request a quota increase for this API, review your GetDownloadUrlForLayer usage as well. |
| Rate of CompleteLayerUpload requests | Each supported Region: 100 per second | Yes | The maximum number of CompleteLayerUpload requests that you can make per second in the current Region. When an image is pushed, the CompleteLayerUpload API is called once per each new image layer to verify that the upload has completed. |
| Rate of GetAuthorizationToken requests | Each supported Region: 500 per second | Yes | The maximum number of GetAuthorizationToken requests that you can make per second in the current Region. |
| Rate of GetDownloadUrlForLayer requests | Each supported Region: 3,000 per second | Yes | The maximum number of GetDownloadUrlForLayer requests that you can make per second in the current Region. When an image is pulled, the GetDownloadUrlForLayer API is called once per image layer that is not already cached. If you request a quota increase for this API, review your BatchGetImage usage as well. |
| Rate of InitiateLayerUpload requests | Each supported Region: 100 per second | Yes | The maximum number of InitiateLayerUpload requests that you can make per second in the current Region. When an image is pushed, the InitiateLayerUpload API is called once per image layer that has not already been uploaded. Whether or not an image layer has been uploaded is determined by the BatchCheckLayerAvailability API action. |
| Rate of PutImage requests | Each supported Region: 10 per second | Yes | The maximum number of PutImage requests that you can make per second in the current Region. When an image is pushed and all new image layers have been uploaded, the PutImage API is called once to create or update the image manifest and the tags associated with the image. |
| Rate of UploadLayerPart requests | Each supported Region: 500 per second | Yes | The maximum number of UploadLayerPart requests that you can make per second in the current Region. When an image is pushed, each new image layer is uploaded in parts and the UploadLayerPart API is called once per each new image layer part. |
| Rate of image scans | Each supported Region: 1 | No | The maximum number of image scans per image, per 24 hours. |
| Registered repositories | Each supported Region: 100,000 | Yes | The maximum number of repositories that you can create in this account in the current Region. |
| Rules per lifecycle policy | Each supported Region: 50 | No | The maximum number of rules in a lifecycle policy. |
| Rules per replication configuration | Each supported Region: 25 | No | The maximum number of rules in a replication configuration. |
| Tags per image | Each supported Region: 1,000 | No | The maximum number of tags per image. |
| Unique destinations across all rules in a replication configuration | Each supported Region: 25 | No | The maximum number of unique destinations across all rules in a replication configuration. |
