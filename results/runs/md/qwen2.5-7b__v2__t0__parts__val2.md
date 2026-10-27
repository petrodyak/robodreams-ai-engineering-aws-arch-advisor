# Run `qwen2.5-7b__v2__t0__parts__val2`

Generated from the JSONL run file by `src/extract/report_md.py`; do not edit.

- Model: `qwen2.5:7b`
- Prompt version: `v2` (file sha `a3adf0379524`)
- Schema sha: `d4010de95c65`; validation version `2`
- Sampling: `t0` (temperature 0.0, top_p None)
- In parts: the endpoints part and the quotas part of each chapter in one call each, merged by code (step 13)
- Documents: 30

## Summary

| # | Document | Group | Status | Calls | Latency, s | In tokens | Out tokens | Quota table | Endpoints | Quotas |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [006-amazon-aurora-dsql.pdf](#006-amazon-aurora-dsqlpdf) | short | ok | 2 | 39.7 | 2,526 | 1,750 | standard | 25 | 4 |
| 2 | [076-aws-glue-databrew.pdf](#076-aws-glue-databrewpdf) | short | repaired | 3 | 89.0 | 5,764 | 3,704 | standard | 24 | 7 |
| 3 | [085-aws-lake-formation.pdf](#085-aws-lake-formationpdf) | short | ok | 1 | 99.2 | 2,802 | 4,210 | none | 84 | 0 |
| 4 | [033-amazon-kinesis-data-streams.pdf](#033-amazon-kinesis-data-streamspdf) | short | ok | 2 | 129.0 | 3,662 | 5,498 | standard | 76 | 1 |
| 5 | [007-amazon-bedrock-agentcore.pdf](#007-amazon-bedrock-agentcorepdf) | short | ok | 1 | 50.9 | 2,446 | 2,129 | none | 39 | 0 |
| 6 | [037-amazon-managed-workflows-for-apache-airflow.pdf](#037-amazon-managed-workflows-for-apache-airflowpdf) | short | failed | 2 | 660.1 | 4,928 | 26,237 | — | — | — |
| 7 | [055-aws-app-mesh.pdf](#055-aws-app-meshpdf) | short | ok | 2 | 126.9 | 4,498 | 5,051 | standard | 89 | 5 |
| 8 | [066-aws-datasync.pdf](#066-aws-datasyncpdf) | short | failed | 3 | 299.2 | 13,535 | 11,296 | — | — | — |
| 9 | [091-aws-resource-groups-and-tagging.pdf](#091-aws-resource-groups-and-taggingpdf) | short | repaired | 3 | 140.1 | 6,585 | 5,590 | standard | 76 | 1 |
| 10 | [018-amazon-ec2-auto-scaling.pdf](#018-amazon-ec2-auto-scalingpdf) | short | ok | 2 | 144.2 | 4,493 | 5,795 | standard | 84 | 9 |
| 11 | [005-amazon-aurora.pdf](#005-amazon-aurorapdf) | medium | failed | 2 | 519.0 | 5,188 | 20,152 | — | — | — |
| 12 | [075-aws-glue.pdf](#075-aws-gluepdf) | medium | failed | 3 | 298.6 | 12,712 | 11,931 | — | — | — |
| 13 | [042-amazon-redshift.pdf](#042-amazon-redshiftpdf) | medium | failed | 3 | 568.3 | 25,289 | 19,209 | — | — | — |
| 14 | [044-amazon-relational-database-service.pdf](#044-amazon-relational-database-servicepdf) | medium | failed | 2 | 557.8 | 6,495 | 21,100 | — | — | — |
| 15 | [048-amazon-simple-queue-service.pdf](#048-amazon-simple-queue-servicepdf) | medium | repaired | 3 | 227.8 | 10,049 | 9,378 | standard | 80 | 18 |
| 16 | [047-amazon-simple-notification-service.pdf](#047-amazon-simple-notification-servicepdf) | medium | repaired | 3 | 322.3 | 14,103 | 12,884 | non_standard | 71 | 0 |
| 17 | [026-amazon-eventbridge.pdf](#026-amazon-eventbridgepdf) | medium | ok | 2 | 130.1 | 5,071 | 5,560 | standard | 80 | 17 |
| 18 | [092-aws-secrets-manager.pdf](#092-aws-secrets-managerpdf) | medium | failed | 4 | 409.8 | 19,972 | 15,880 | — | — | — |
| 19 | [023-amazon-elastic-kubernetes-service.pdf](#023-amazon-elastic-kubernetes-servicepdf) | medium | ok | 2 | 83.3 | 5,097 | 3,473 | standard | 38 | 13 |
| 20 | [078-aws-iam-identity-center.pdf](#078-aws-iam-identity-centerpdf) | medium | ok | 2 | 321.7 | 7,108 | 12,203 | standard | 232 | 6 |
| 21 | [038-amazon-opensearch-service.pdf](#038-amazon-opensearch-servicepdf) | edge | failed | 3 | 996.1 | 22,053 | 36,684 | — | — | — |
| 22 | [086-aws-lambda.pdf](#086-aws-lambdapdf) | edge | ok | 2 | 256.9 | 7,896 | 10,167 | standard | 75 | 73 |
| 23 | [004-amazon-athena.pdf](#004-amazon-athenapdf) | edge | ok | 2 | 206.8 | 8,262 | 8,333 | standard | 78 | 30 |
| 24 | [017-amazon-dynamodb.pdf](#017-amazon-dynamodbpdf) | edge | failed | 2 | 567.4 | 10,554 | 20,628 | — | — | — |
| 25 | [095-aws-step-functions.pdf](#095-aws-step-functionspdf) | edge | ok | 2 | 397.1 | 9,835 | 15,715 | standard | 169 | 97 |
| 26 | [049-amazon-simple-storage-service.pdf](#049-amazon-simple-storage-servicepdf) | edge | failed | 3 | 728.1 | 19,824 | 25,350 | — | — | — |
| 27 | [025-amazon-emr.pdf](#025-amazon-emrpdf) | edge | failed | 3 | 1024.4 | 31,958 | 36,347 | — | — | — |
| 28 | [010-amazon-cloudfront.pdf](#010-amazon-cloudfrontpdf) | edge | failed | 3 | 365.6 | 19,361 | 13,163 | — | — | — |
| 29 | [074-aws-global-accelerator.pdf](#074-aws-global-acceleratorpdf) | edge | repaired | 3 | 382.3 | 16,300 | 14,291 | standard | 138 | 5 |
| 30 | [019-amazon-ecr.pdf](#019-amazon-ecrpdf) | edge | ok | 2 | 314.2 | 7,479 | 12,565 | standard | 190 | 23 |

## Documents

### 006-amazon-aurora-dsql.pdf

- Status: **ok**, 2 call(s), 39.7 s, in 2,526 / out 1,750 tokens
- Part `endpoints` (294 words): **ok**, 1 call(s), 29.0 s, in 1,583 / out 1,268 tokens, 25 rows
- Part `quotas` (104 words): **ok**, 1 call(s), 10.6 s, in 943 / out 482 tokens, 4 rows, 4 ignored of the other kind
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
| Cluster size | Each supported Region: 10,000 Gigabytes | Yes | The maximum capacity (in GB) for an Aurora DSQL cluster. This quota applies to both single-Region and multi-Region clusters. |
| Connections per cluster | Each supported Region: 10,000 | Yes | The maximum number of active connections per cluster that you can have in this account in the current Region. |
| Multi-Region clusters | Each supported Region: 5 | Yes | The maximum number of multi region clusters allowed per account. |
| Single-Region clusters | Each supported Region: 20 | Yes | The maximum number of active clusters allowed |

### 076-aws-glue-databrew.pdf

- Status: **repaired**, 3 call(s), 89.0 s, in 5,764 / out 3,704 tokens
- Part `endpoints` (291 words): **repaired**, 2 call(s), 65.1 s, in 4,707 / out 2,663 tokens, 24 rows
- Part `quotas` (180 words): **ok**, 1 call(s), 23.9 s, in 1,057 / out 1,041 tokens, 7 rows, 12 ignored of the other kind
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

#### First answer rejected (repaired)

```text
[endpoints]
- endpoints.12.endpoint: not printed in an endpoints table of the 'AWS Glue DataBrew' chapter: 'databrew-fips.ap-northeast-2.amazonaws.com'
- endpoints.14.endpoint: not printed in an endpoints table of the 'AWS Glue DataBrew' chapter: 'databrew-fips.ap-southeast-1.amazonaws.com'
- endpoints.16.endpoint: not printed in an endpoints table of the 'AWS Glue DataBrew' chapter: 'databrew-fips.ap-southeast-2.amazonaws.com'
```

### 085-aws-lake-formation.pdf

- Status: **ok**, 1 call(s), 99.2 s, in 2,802 / out 4,210 tokens
- Part `endpoints` (561 words): **ok**, 1 call(s), 99.2 s, in 2,802 / out 4,210 tokens, 84 rows
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
| Africa (Cape Town) | af-south-1 | lakeformation.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | lakeformation.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | lakeformation.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | lakeformation.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | lakeformation.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | lakeformation.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | lakeformation.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | lakeformation.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | lakeformation.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | lakeformation.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | lakeformation.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | lakeformation.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | lakeformation.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | lakeformation.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | lakeformation.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | lakeformation.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | lakeformation.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | lakeformation.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | lakeformation.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | lakeformation.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | lakeformation.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | lakeformation.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | lakeformation.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | lakeformation.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | lakeformation.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | lakeformation.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | lakeformation.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | lakeformation.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | lakeformation.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | lakeformation.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | lakeformation-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | lakeformation-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | lakeformation.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | lakeformation.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | lakeformation-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Calgary) | ca-west-1 | lakeformation-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada (Calgary) | ca-west-1 | lakeformation.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | lakeformation.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | lakeformation.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | lakeformation.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | lakeformation.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | lakeformation.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | lakeformation.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | lakeformation.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | lakeformation.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | lakeformation.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | lakeformation.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | lakeformation.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | lakeformation.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | lakeformation.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | lakeformation.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | lakeformation.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | lakeformation.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | lakeformation.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | lakeformation.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | lakeformation.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | lakeformation.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | lakeformation.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | lakeformation.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | lakeformation.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | lakeformation.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | lakeformation.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | lakeformation.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | lakeformation.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | lakeformation-fips.us-gov-east-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | lakeformation-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | lakeformation.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | lakeformation.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | lakeformation-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | lakeformation-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | lakeformation.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (0)

_none_

### 033-amazon-kinesis-data-streams.pdf

- Status: **ok**, 2 call(s), 129.0 s, in 3,662 / out 5,498 tokens
- Part `endpoints` (534 words): **ok**, 1 call(s), 90.6 s, in 2,628 / out 3,796 tokens, 76 rows
- Part `quotas` (101 words): **ok**, 1 call(s), 38.4 s, in 1,034 / out 1,702 tokens, 1 rows, 30 ignored of the other kind
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
| Asia Pacific (Singapore) | ap-southeast-1 | kinesis.ap-southeast-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Singapore) | ap-southeast-1 | kinesis.ap-southeast-2.api.aws | HTTPS | global |
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

- Status: **ok**, 1 call(s), 50.9 s, in 2,446 / out 2,129 tokens
- Part `endpoints` (560 words): **ok**, 1 call(s), 50.9 s, in 2,446 / out 2,129 tokens, 39 rows
- Service: Amazon Bedrock AgentCore; quota table format: `none`

#### Endpoints (39)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (N. Virginia) | us-east-1 | bedrock-agentcore-control.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | bedrock-agentcore-control.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | bedrock-agentcore-control.us-west-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | bedrock-agentcore-control.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | bedrock-agentcore-control.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | bedrock-agentcore-control.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | bedrock-agentcore-control.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | bedrock-agentcore-control.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | bedrock-agentcore-control.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | bedrock-agentcore.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | bedrock-agentcore.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | bedrock-agentcore.us-west-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | bedrock-agentcore.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | bedrock-agentcore.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | bedrock-agentcore.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | bedrock-agentcore.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | bedrock-agentcore.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | bedrock-agentcore.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | gatewayId.gateway.bedrock-agentcore.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | gatewayId.gateway.bedrock-agentcore.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | gatewayId.gateway.bedrock-agentcore.us-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | gatewayId.gateway.bedrock-agentcore.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | gatewayId.gateway.bedrock-agentcore.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | gatewayId.gateway.bedrock-agentcore.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | gatewayId.gateway.bedrock-agentcore.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | gatewayId.gateway.bedrock-agentcore.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | gatewayId.gateway.bedrock-agentcore.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| US West (California) | us-west-1 | gatewayId.gateway.bedrock-agentcore.us-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | gatewayId.gateway.bedrock-agentcore.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | gatewayId.gateway.bedrock-agentcore.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | gatewayId.gateway.bedrock-agentcore.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | gatewayId.gateway.bedrock-agentcore.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | gatewayId.gateway.bedrock-agentcore.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | gatewayId.gateway.bedrock-agentcore.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | gatewayId.gateway.bedrock-agentcore.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | gatewayId.gateway.bedrock-agentcore.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | gatewayId.gateway.bedrock-agentcore.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | gatewayId.gateway.bedrock-agentcore.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | gatewayId.gateway.bedrock-agentcore.sa-east-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (0)

_none_

### 037-amazon-managed-workflows-for-apache-airflow.pdf

- Status: **failed**, 2 call(s), 660.1 s, in 4,928 / out 26,237 tokens
- Part `endpoints` (711 words): **ok**, 1 call(s), 195.0 s, in 3,968 / out 7,805 tokens, 155 rows
- Part `quotas` (141 words): **failed**, 1 call(s), 465.0 s, in 960 / out 18,432 tokens, —

#### Error

```text
[quotas]
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 2479 column 18
--- no repair call
```

### 055-aws-app-mesh.pdf

- Status: **ok**, 2 call(s), 126.9 s, in 4,498 / out 5,051 tokens
- Part `endpoints` (688 words): **ok**, 1 call(s), 116.1 s, in 3,566 / out 4,566 tokens, 89 rows
- Part `quotas` (105 words): **ok**, 1 call(s), 10.8 s, in 932 / out 485 tokens, 5 rows, 4 ignored of the other kind
- Service: AWS App Mesh; quota table format: `standard`

#### Endpoints (89)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | appmesh.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | appmesh-envoy-management-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | appmesh.us-east-2.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | appmesh-envoy-management-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | appmesh-envoy-management.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | appmesh-envoy-management.us-east-2.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | appmesh-envoy-management-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | appmesh-envoy-management-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | appmesh.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | appmesh-envoy-management.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | appmesh-envoy-management-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | appmesh-envoy-management-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | appmesh-envoy-management.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | appmesh-envoy-management.us-east-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | appmesh.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | appmesh-envoy-management.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | appmesh-envoy-management-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | appmesh-envoy-management-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | appmesh-envoy-management.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | appmesh.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | appmesh-envoy-management.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | appmesh-envoy-management.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | appmesh.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | appmesh-envoy-management.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | appmesh-envoy-management.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | appmesh.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | appmesh-envoy-management.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | appmesh-envoy-management.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | appmesh.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | appmesh-envoy-management.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | appmesh-envoy-management.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | appmesh.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | appmesh-envoy-management.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | appmesh-envoy-management.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | appmesh.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | appmesh-envoy-management.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | appmesh-envoy-management.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | appmesh.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | appmesh-envoy-management.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | appmesh-envoy-management.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | appmesh.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | appmesh-envoy-management.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | appmesh-envoy-management.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | appmesh.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | appmesh-envoy-management.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | appmesh-envoy-management.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | appmesh.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | appmesh-envoy-management-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | appmesh.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | appmesh-envoy-management.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | appmesh-envoy-management.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | appmesh-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Europe (Frankfurt) | eu-central-1 | appmesh.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | appmesh.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | appmesh-envoy-management.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | appmesh-envoy-management.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | appmesh.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | appmesh-envoy-management.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | appmesh-envoy-management.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | appmesh.eu-west-2.amazonaws.com | HTTPS | ipv4 |
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
| Europe (Spain) | eu-south-2 | appmesh.eu-south-2.api.aws | HTTPS | dual_stack |
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

- Status: **failed**, 3 call(s), 299.2 s, in 13,535 / out 11,296 tokens
- Part `endpoints` (547 words): **failed**, 2 call(s), 287.8 s, in 11,989 / out 10,855 tokens, —
- Part `quotas` (402 words): **ok**, 1 call(s), 11.4 s, in 1,546 / out 441 tokens, 0 rows, 8 ignored of the other kind

#### Error

```text
[endpoints]
- endpoints.20.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-east-1.api.aws'
- endpoints.21.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-east-1.amazonaws.com'
- endpoints.24.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-south-1.api.aws'
- endpoints.25.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-south-1.amazonaws.com'
- endpoints.28.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-northeast-3.api.aws'
- endpoints.29.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-northeast-3.amazonaws.com'
- endpoints.32.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-northeast-2.api.aws'
- endpoints.33.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-northeast-2.amazonaws.com'
- endpoints.36.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-southeast-1.api.aws'
- endpoints.37.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-southeast-1.amazonaws.com'
- endpoints.40.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-southeast-2.api.aws'
- endpoints.41.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-southeast-2.amazonaws.com'
- endpoints.44.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-east-2.api.aws'
- endpoints.45.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-east-2.amazonaws.com'
- endpoints.50.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-northeast-1.api.aws'
- endpoints.51.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-northeast-1.amazonaws.com'
- endpoints.62.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-central-1.amazonaws.com'
- endpoints.63.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-central-1.api.aws'
- endpoints.68.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-west-2.api.aws'
- endpoints.69.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-west-2.amazonaws.com'
- endpoints.72.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-south-1.api.aws'
- endpoints.73.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-south-1.amazonaws.com'
- endpoints.76.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-west-3.api.aws'
- endpoints.77.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-west-3.amazonaws.com'
- endpoints.80.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-south-2.api.aws'
- endpoints.81.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-south-2.amazonaws.com'
- endpoints.84.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-north-1.api.aws'
- endpoints.85.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-north-1.amazonaws.com'
- endpoints.90.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.il-central-1.api.aws'
- endpoints.91.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.il-central-1.amazonaws.com'
--- after repair:
- endpoints.20.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-east-1.api.aws'
- endpoints.21.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-east-1.amazonaws.com'
- endpoints.24.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-south-1.api.aws'
- endpoints.25.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-south-1.amazonaws.com'
- endpoints.28.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-northeast-3.api.aws'
- endpoints.29.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-northeast-3.amazonaws.com'
- endpoints.32.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-northeast-2.api.aws'
- endpoints.33.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-northeast-2.amazonaws.com'
- endpoints.36.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-southeast-1.api.aws'
- endpoints.37.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-southeast-1.amazonaws.com'
- endpoints.40.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-southeast-2.api.aws'
- endpoints.41.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-southeast-2.amazonaws.com'
- endpoints.44.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-east-2.api.aws'
- endpoints.45.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-east-2.amazonaws.com'
- endpoints.50.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-northeast-1.api.aws'
- endpoints.51.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.ap-northeast-1.amazonaws.com'
- endpoints.62.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-central-1.amazonaws.com'
- endpoints.63.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-central-1.api.aws'
- endpoints.68.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-west-2.api.aws'
- endpoints.69.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-west-2.amazonaws.com'
- endpoints.72.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-south-1.api.aws'
- endpoints.73.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-south-1.amazonaws.com'
- endpoints.76.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-west-3.api.aws'
- endpoints.77.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-west-3.amazonaws.com'
- endpoints.80.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-south-2.api.aws'
- endpoints.81.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-south-2.amazonaws.com'
- endpoints.84.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-north-1.api.aws'
- endpoints.85.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.eu-north-1.amazonaws.com'
- endpoints.90.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.il-central-1.api.aws'
- endpoints.91.endpoint: not printed in an endpoints table of the 'AWS DataSync' chapter: 'datasync-fips.il-central-1.amazonaws.com'
```

### 091-aws-resource-groups-and-tagging.pdf

- Status: **repaired**, 3 call(s), 140.1 s, in 6,585 / out 5,590 tokens
- Part `endpoints` (791 words): **ok**, 1 call(s), 98.1 s, in 3,273 / out 3,846 tokens, 76 rows
- Part `quotas` (241 words): **repaired**, 2 call(s), 42.0 s, in 3,312 / out 1,744 tokens, 1 rows, 16 ignored of the other kind
- Service: AWS Resource Groups and Tagging; quota table format: `standard`

#### Endpoints (76)

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
| Tagging API (Ohio) | us-east-2 | tagging.us-east-2.amazonaws.com | HTTPS | ipv4 |
| Tagging API (N. Virginia) | us-east-1 | tagging.us-east-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (N. California) | us-west-1 | tagging.us-west-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Oregon) | us-west-2 | tagging.us-west-2.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Cape Town) | af-south-1 | tagging.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Hong Kong) | ap-east-1 | tagging.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Hyderabad) | ap-south-2 | tagging.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Jakarta) | ap-southeast-3 | tagging.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Malaysia) | ap-southeast-5 | tagging.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Melbourne) | ap-southeast-4 | tagging.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Mumbai) | ap-south-1 | tagging.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (New Zealand) | ap-southeast-6 | tagging.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Osaka) | ap-northeast-3 | tagging.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Seoul) | ap-northeast-2 | tagging.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Singapore) | ap-southeast-1 | tagging.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Sydney) | ap-southeast-2 | tagging.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Taipei) | ap-east-2 | tagging.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Thailand) | ap-southeast-7 | tagging.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Tokyo) | ap-northeast-1 | tagging.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Central) | ca-central-1 | tagging.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Calgary) | ca-west-1 | tagging.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Frankfurt) | eu-central-1 | tagging.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Ireland) | eu-west-1 | tagging.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (London) | eu-west-2 | tagging.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Milan) | eu-south-1 | tagging.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Paris) | eu-west-3 | tagging.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Spain) | eu-south-2 | tagging.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Stockholm) | eu-north-1 | tagging.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Zurich) | eu-central-2 | tagging.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Tel Aviv) | il-central-1 | tagging.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Central) | mx-central-1 | tagging.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (Bahrain) | me-south-1 | tagging.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (UAE) | me-central-1 | tagging.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (São Paulo) | sa-east-1 | tagging.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (US-East) | us-gov-east-1 | tagging.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| Tagging API (US-West) | us-gov-west-1 | tagging.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (1)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Resource groups per account | Each supported Region: 100 | Yes | The maximum number of resource groups that you can create in this account. A resource group is a collection of AWS resources that match a specific criteria. |

#### First answer rejected (repaired)

```text
[quotas]
- quota_table_format: 'none', but the chapter prints a table with the columns Name, Default, Adjustable, Description: that is a Standard Quota Table, return its rows with 'standard'
```

### 018-amazon-ec2-auto-scaling.pdf

- Status: **ok**, 2 call(s), 144.2 s, in 4,493 / out 5,795 tokens
- Part `endpoints` (767 words): **ok**, 1 call(s), 107.7 s, in 3,338 / out 4,260 tokens, 84 rows
- Part `quotas` (243 words): **ok**, 1 call(s), 36.6 s, in 1,155 / out 1,535 tokens, 9 rows, 20 ignored of the other kind
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

- Status: **failed**, 2 call(s), 519.0 s, in 5,188 / out 20,152 tokens
- Part `endpoints` (758 words): **ok**, 1 call(s), 45.2 s, in 3,164 / out 1,720 tokens, 36 rows
- Part `quotas` (713 words): **failed**, 1 call(s), 473.8 s, in 2,024 / out 18,432 tokens, —

#### Error

```text
[quotas]
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 2354 column 31
--- no repair call
```

### 075-aws-glue.pdf

- Status: **failed**, 3 call(s), 298.6 s, in 12,712 / out 11,931 tokens
- Part `endpoints` (542 words): **ok**, 1 call(s), 92.3 s, in 2,638 / out 3,910 tokens, 78 rows
- Part `quotas` (1,094 words): **failed**, 2 call(s), 206.3 s, in 10,074 / out 8,021 tokens, —

#### Error

```text
[quotas]
- quotas.0.name: not printed in a Standard Quota Table of the chapter: 'Concurrent compute capacity for Ray worker instances in M-DPUs per account'
- quotas.26.name: not printed in a Standard Quota Table of the chapter: 'Max spare compute capacity consumed in data processing units (DPUs) per account'
- quotas.35.name: not printed in a Standard Quota Table of the chapter: 'Number of Schema Registries'
- quotas.36.name: not printed in a Standard Quota Table of the chapter: 'Number of Schema Versions'
- quotas.43.name: not printed in a Standard Quota Table of the chapter: 'Number of metadata key value pairs per Schema Version'
- quotas.45.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of concurrent materialized view refresh task runs'
--- after repair:
- quotas.0.name: not printed in a Standard Quota Table of the chapter: 'Concurrent compute capacity for Ray worker instances in M-DPUs per account'
- quotas.26.name: not printed in a Standard Quota Table of the chapter: 'Max spare compute capacity consumed in data processing units (DPUs) per account'
- quotas.40.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of concurrent materialized view refresh task runs'
```

### 042-amazon-redshift.pdf

- Status: **failed**, 3 call(s), 568.3 s, in 25,289 / out 19,209 tokens
- Part `endpoints` (1,724 words): **failed**, 2 call(s), 547.7 s, in 24,506 / out 18,237 tokens, —
- Part `quotas` (27 words): **ok**, 1 call(s), 20.5 s, in 783 / out 972 tokens, 0 rows, 16 ignored of the other kind

#### Error

```text
[endpoints]
- endpoints.36.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.il-central-1.amazonaws.com'
- endpoints.37.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift.il-central-1.api.aws'
- endpoints.44.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.us-gov-east-1.amazonaws.com'
- endpoints.45.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift.us-gov-east-1.api.aws'
- endpoints.48.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.us-gov-west-1.amazonaws.com'
- endpoints.49.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift.us-gov-west-1.api.aws'
--- after repair:
- endpoints.36.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.il-central-1.amazonaws.com'
- endpoints.37.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift.il-central-1.api.aws'
- endpoints.44.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.us-gov-east-1.amazonaws.com'
- endpoints.45.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift.us-gov-east-1.api.aws'
- endpoints.48.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift-fips.us-gov-west-1.amazonaws.com'
- endpoints.49.endpoint: not printed in an endpoints table of the 'Amazon Redshift' chapter: 'redshift.us-gov-west-1.api.aws'
```

### 044-amazon-relational-database-service.pdf

- Status: **failed**, 2 call(s), 557.8 s, in 6,495 / out 21,100 tokens
- Part `endpoints` (980 words): **failed**, 1 call(s), 493.7 s, in 4,381 / out 18,432 tokens, —
- Part `quotas` (753 words): **ok**, 1 call(s), 64.1 s, in 2,114 / out 2,668 tokens, 26 rows, 22 ignored of the other kind

#### Error

```text
[endpoints]
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 2337 column 54
--- no repair call
```

### 048-amazon-simple-queue-service.pdf

- Status: **repaired**, 3 call(s), 227.8 s, in 10,049 / out 9,378 tokens
- Part `endpoints` (968 words): **ok**, 1 call(s), 102.0 s, in 3,955 / out 4,061 tokens, 80 rows
- Part `quotas` (464 words): **repaired**, 2 call(s), 125.8 s, in 6,094 / out 5,317 tokens, 18 rows, 32 ignored of the other kind
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

#### Quotas (18)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Attributes per Message | Each supported Region: 10 | No | The number of attributes added to a message. |
| Batched Message ID Length | Each supported Region: 80 | No | The length of a batched message ID. |
| Batched Message Throughput for FIFO Queues | Each supported Region: 3,000 | No | The number of batched transactions per second (TPS) for FIFO queues. |
| Batched Message Throughput for FIFO Queues | Europe (London) and South America (São Paulo): 45,000; All other supported Regions: 24,000 | No | The number of batched transactions per second (TPS) for FIFO queues. |
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

#### First answer rejected (repaired)

```text
[quotas]
- quotas.0.name: not printed in a Standard Quota Table of the chapter: 'Actions per Queue'
```

### 047-amazon-simple-notification-service.pdf

- Status: **repaired**, 3 call(s), 322.3 s, in 14,103 / out 12,884 tokens
- Part `endpoints` (736 words): **ok**, 1 call(s), 84.0 s, in 3,106 / out 3,524 tokens, 71 rows
- Part `quotas` (926 words): **repaired**, 2 call(s), 238.3 s, in 10,997 / out 9,360 tokens, 0 rows, 80 ignored of the other kind
- Service: Amazon Simple Notification Service; quota table format: `non_standard`

#### Endpoints (71)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | sns.us-east-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | sns-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | sns.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | sns.us-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | sns-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | sns.us-east-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | sns.us-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | sns-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | sns.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | sns.af-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | sns.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | sns.ap-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | sns.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | sns.ap-east-2.amazonaws.com | HTTP and HTTPS | global |
| Asia Pacific (Hong Kong) | ap-east-1 | sns.ap-east-2.api.aws | HTTPS | global |
| Asia Pacific (Jakarta) | ap-southeast-3 | sns.ap-southeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | sns.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | sns.ap-southeast-4.amazonaws.com | HTTP and HTTPS | global |
| Asia Pacific (Jakarta) | ap-southeast-3 | sns.ap-southeast-4.api.aws | HTTPS | global |
| Asia Pacific (Mumbai) | ap-south-1 | sns.ap-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | sns.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | sns.ap-northeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | sns.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | sns.ap-northeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | sns.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | sns.ap-southeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | sns.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | sns.ap-southeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | sns.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | sns.ap-east-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | sns.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | sns.ap-southeast-7.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | sns.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | sns.ap-northeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | sns.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | sns.ca-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | sns-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | sns.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | sns.ca-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | sns-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Calgary) | ca-west-1 | sns.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | sns.eu-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | sns.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | sns.eu-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | sns.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | sns.eu-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (London) | eu-west-2 | sns.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | sns.eu-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | sns.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | sns.eu-west-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | sns.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | sns.eu-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | sns.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | sns.eu-north-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | sns.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | sns.eu-central-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | sns.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | sns.il-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | sns.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | sns.mx-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | sns.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | sns.me-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | sns.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | sns.me-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | sns.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | sns.sa-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | sns.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | sns.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | sns.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | sns.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | sns.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (0)

_none_

#### First answer rejected (repaired)

```text
[quotas]
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
- quotas.11.name: not printed in a Standard Quota Table of the chapter: 'Publish API throttling per account'
- quotas.12.name: not printed in a Standard Quota Table of the chapter: 'Other API throttling'
- quotas.13.name: not printed in a Standard Quota Table of the chapter: 'Message Archiving and Replay'
- quota_table_format: 'standard', but the chapter prints no table with the columns Name, Default, Adjustable, Description
```

### 026-amazon-eventbridge.pdf

- Status: **ok**, 2 call(s), 130.1 s, in 5,071 / out 5,560 tokens
- Part `endpoints` (533 words): **ok**, 1 call(s), 90.7 s, in 2,574 / out 3,910 tokens, 80 rows
- Part `quotas` (745 words): **ok**, 1 call(s), 39.4 s, in 2,497 / out 1,650 tokens, 17 rows, 1 ignored of the other kind
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
| Invocations throttle limit in transactions per second | us-east-1: 18,750; us-east-2: 4,500; us-west-1: 2,250; us-west-2: 18,750; ap-east-1: 1,100; ap-northeast-1: 2,250; ap-northeast-2: 1,100; ap-south-1: 1,100; ap-southeast-1: 2,250; ap-southeast-2: 2,250; ca-central-1: 1,100; eu-central-1: 4,500; eu-north-1: 1,100; eu-south-2: 4,500; eu-west-1: 18,750; eu-west-2: 2,250; eu-west-3: 1,100; sa-east-1: 1,100; Each of the other supported Regions: 750 per second | Yes | An invocation is an event matching a rule and being sent on to the rules targets. After the limit is reached, the invocations are throttled; that is, they still happen but they are delayed. |
| Number of rules | af-south-1: 100; eu-south-1: 100; Each of the other supported Regions: 300 | Yes | Maximum number of rules an account can have per event bus |
| PutEvents throttle limit in transactions per second | us-east-1: 10,000; us-east-2: 2,400; us-west-1: 1,200; us-west-2: 10,000; ap-east-1: 600; ap-northeast-1: 1,200; ap-northeast-2: 600; ap-south-1: 600; ap-southeast-1: 1,200; ap-southeast-2: 1,200; ca-central-1: 600; eu-central-1: 2,400; eu-north-1: 600; eu-south-2: 2,400; eu-west-1: 10,000; eu-west-2: 1,200; eu-west-3: 600; sa-east-1: 600; Each of the other supported Regions: 400 per second | Yes | Maximum number of requests per second for PutEvents API. Additional requests are throttled. |
| Rate of invocations per API destination | Each supported Region: 300 per second | Yes | The maximum number of invocations per second to send to each API destination endpoint per account per Region. Once the quota is met, future invocations to that API endpoint are throttled. The invocations will still occur, but are delayed. |
| Targets per rule | Each supported Region: 5 | No | Maximum number of targets that can be associated with a rule |
| Throttle limit in transactions per second for control plane APIs | Each supported Region: 50 per second | No | Maximum number of requests per second for EventBridge control plane API operations. Additional requests are throttled. |
| UpdateEndpoint throttle limit in transactions per second | Each supported Region: 5 per second | No | The maximum number of requests per second for UpdateEndpoint API. Additional requests are throttled. |
| [EventsV2] Combined ingestion throughput and count per Event Group per second | Each supported Region: 1,500 per second | No | The maximum event throughput per Event Group per Second. Counted as the sum of (number of events) + (total size of those events in KB) delivered to a given event group within any one-second window. |
| [EventsV2] Event Buses | Each supported Region: 5 | Yes | The maximum number of V2 Event Buses owned by this account per Region. Does not include buses shared with this account. |

### 092-aws-secrets-manager.pdf

- Status: **failed**, 4 call(s), 409.8 s, in 19,972 / out 15,880 tokens
- Part `endpoints` (713 words): **failed**, 2 call(s), 289.6 s, in 13,750 / out 10,825 tokens, —
- Part `quotas` (510 words): **failed**, 2 call(s), 120.2 s, in 6,222 / out 5,055 tokens, —

#### Error

```text
[endpoints]
- endpoints.2.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-east-2.api.aws'
- endpoints.5.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-east-1.api.aws'
- endpoints.8.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-west-1.api.aws'
- endpoints.11.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-west-2.api.aws'
- endpoints.14.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-east-1.amazonaws.com'
- endpoints.15.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager.ap-east-1.api.aws'
- endpoints.17.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-south-2.amazonaws.com'
- endpoints.18.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-south-2.api.aws'
- endpoints.20.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-3.amazonaws.com'
- endpoints.21.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-3.api.aws'
- endpoints.23.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-5.amazonaws.com'
- endpoints.24.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-5.api.aws'
- endpoints.26.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-4.amazonaws.com'
- endpoints.27.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-4.api.aws'
- endpoints.29.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-south-1.amazonaws.com'
- endpoints.30.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-south-1.api.aws'
- endpoints.32.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-6.amazonaws.com'
- endpoints.33.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-6.api.aws'
- endpoints.35.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-northeast-3.amazonaws.com'
- endpoints.36.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-northeast-3.api.aws'
- endpoints.38.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-northeast-2.amazonaws.com'
- endpoints.39.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-northeast-2.api.aws'
- endpoints.41.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-1.amazonaws.com'
- endpoints.42.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-1.api.aws'
- endpoints.44.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-2.amazonaws.com'
- endpoints.45.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-2.api.aws'
- endpoints.47.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-east-2.amazonaws.com'
- endpoints.48.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-east-2.api.aws'
- endpoints.50.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-7.amazonaws.com'
- endpoints.51.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-7.api.aws'
- endpoints.53.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-northeast-1.amazonaws.com'
- endpoints.54.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-northeast-1.api.aws'
- endpoints.57.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ca-central-1.api.aws'
- endpoints.60.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ca-west-1.api.aws'
- endpoints.62.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-central-1.amazonaws.com'
- endpoints.63.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-central-1.api.aws'
- endpoints.65.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-west-1.amazonaws.com'
- endpoints.66.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-west-1.api.aws'
- endpoints.68.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-west-2.amazonaws.com'
- endpoints.69.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-west-2.api.aws'
- endpoints.71.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-south-1.amazonaws.com'
- endpoints.72.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-south-1.api.aws'
- endpoints.74.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-west-3.amazonaws.com'
- endpoints.75.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-west-3.api.aws'
- endpoints.77.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-south-2.amazonaws.com'
- endpoints.78.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-south-2.api.aws'
- endpoints.80.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-north-1.amazonaws.com'
- endpoints.81.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-north-1.api.aws'
- endpoints.83.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-central-2.amazonaws.com'
- endpoints.84.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-central-2.api.aws'
- endpoints.86.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.il-central-1.amazonaws.com'
- endpoints.87.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.il-central-1.api.aws'
- endpoints.89.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.mx-central-1.amazonaws.com'
- endpoints.90.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.mx-central-1.api.aws'
- endpoints.92.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.me-south-1.amazonaws.com'
- endpoints.93.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.me-south-1.api.aws'
- endpoints.95.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.me-central-1.amazonaws.com'
- endpoints.96.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.me-central-1.api.aws'
- endpoints.100.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-gov-east-1.api.aws'
- endpoints.103.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-gov-west-1.api.aws'
--- after repair:
- endpoints.2.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-east-2.api.aws'
- endpoints.5.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-east-1.api.aws'
- endpoints.8.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-west-1.api.aws'
- endpoints.11.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-west-2.api.aws'
- endpoints.14.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-east-1.amazonaws.com'
- endpoints.15.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-east-1.api.aws'
- endpoints.17.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-south-2.amazonaws.com'
- endpoints.18.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-south-2.api.aws'
- endpoints.20.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-3.amazonaws.com'
- endpoints.21.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-3.api.aws'
- endpoints.23.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-5.amazonaws.com'
- endpoints.24.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-5.api.aws'
- endpoints.26.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-4.amazonaws.com'
- endpoints.27.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-4.api.aws'
- endpoints.29.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-south-1.amazonaws.com'
- endpoints.30.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-south-1.api.aws'
- endpoints.32.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-6.amazonaws.com'
- endpoints.33.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-6.api.aws'
- endpoints.35.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-northeast-3.amazonaws.com'
- endpoints.36.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-northeast-3.api.aws'
- endpoints.38.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-northeast-2.amazonaws.com'
- endpoints.39.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-northeast-2.api.aws'
- endpoints.41.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-1.amazonaws.com'
- endpoints.42.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-1.api.aws'
- endpoints.44.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-2.amazonaws.com'
- endpoints.45.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-2.api.aws'
- endpoints.47.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-east-2.amazonaws.com'
- endpoints.48.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-east-2.api.aws'
- endpoints.50.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-7.amazonaws.com'
- endpoints.51.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-southeast-7.api.aws'
- endpoints.53.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-northeast-1.amazonaws.com'
- endpoints.54.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ap-northeast-1.api.aws'
- endpoints.57.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ca-central-1.api.aws'
- endpoints.60.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.ca-west-1.api.aws'
- endpoints.62.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-central-1.amazonaws.com'
- endpoints.63.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-central-1.api.aws'
- endpoints.65.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-west-1.amazonaws.com'
- endpoints.66.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-west-1.api.aws'
- endpoints.68.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-west-2.amazonaws.com'
- endpoints.69.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-west-2.api.aws'
- endpoints.71.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-south-1.amazonaws.com'
- endpoints.72.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-south-1.api.aws'
- endpoints.74.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-west-3.amazonaws.com'
- endpoints.75.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-west-3.api.aws'
- endpoints.77.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-south-2.amazonaws.com'
- endpoints.78.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-south-2.api.aws'
- endpoints.80.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-north-1.amazonaws.com'
- endpoints.81.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-north-1.api.aws'
- endpoints.83.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-central-2.amazonaws.com'
- endpoints.84.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.eu-central-2.api.aws'
- endpoints.86.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.il-central-1.amazonaws.com'
- endpoints.87.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.il-central-1.api.aws'
- endpoints.89.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.mx-central-1.amazonaws.com'
- endpoints.90.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.mx-central-1.api.aws'
- endpoints.92.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.me-south-1.amazonaws.com'
- endpoints.93.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.me-south-1.api.aws'
- endpoints.95.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.me-central-1.amazonaws.com'
- endpoints.96.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.me-central-1.api.aws'
- endpoints.100.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-gov-east-1.api.aws'
- endpoints.103.endpoint: not printed in an endpoints table of the 'AWS Secrets Manager' chapter: 'secretsmanager-fips.us-gov-west-1.api.aws'
[quotas]
- quotas.1.name: not printed in a Standard Quota Table of the chapter: 'Combined rate of PutSecretValue, RemoveRegionsFromReplication, ReplicateSecretToRegion, StopReplicationToRegion, UpdateSecret, and UpdateSecretVersionStage API requests'
--- after repair:
- quotas.1.name: not printed in a Standard Quota Table of the chapter: 'Combined rate of PutSecretValue, RemoveRegionsFromReplication, ReplicateSecretToRegion, StopReplicationToRegion, UpdateSecret, and UpdateSecretVersionStage API requests'
```

### 023-amazon-elastic-kubernetes-service.pdf

- Status: **ok**, 2 call(s), 83.3 s, in 5,097 / out 3,473 tokens
- Part `endpoints` (854 words): **ok**, 1 call(s), 47.4 s, in 3,337 / out 1,886 tokens, 38 rows
- Part `quotas` (613 words): **ok**, 1 call(s), 35.9 s, in 1,760 / out 1,587 tokens, 13 rows, 17 ignored of the other kind
- Service: Amazon Elastic Kubernetes Service; quota table format: `standard`

#### Endpoints (38)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | eks.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | fips.eks.us-east-2.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | eks.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | fips.eks.us-east-1.amazonaws.com | HTTPS | fips |
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

- Status: **ok**, 2 call(s), 321.7 s, in 7,108 / out 12,203 tokens
- Part `endpoints` (1,380 words): **ok**, 1 call(s), 310.6 s, in 6,015 / out 11,713 tokens, 232 rows
- Part `quotas` (194 words): **ok**, 1 call(s), 11.1 s, in 1,093 / out 490 tokens, 6 rows, 1 ignored of the other kind
- Service: AWS IAM Identity Center; quota table format: `standard`

#### Endpoints (232)

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
| Asia Pacific (Hyderabad) | ap-south-2 | sso.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | sso.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | sso.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | sso.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | sso.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | sso.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | sso.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | sso.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | sso.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | sso.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | sso.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | sso.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | sso.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | sso.ap-northeast-3.api.aws | HTTPS | dual_stack |
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
| Identity Store (US East (Ohio)) | us-east-2 | identitystore.us-east-2.amazonaws.com | HTTPS | ipv4 |
| Identity Store (US East (Ohio)) | us-east-2 | identitystore.us-east-2.api.aws | HTTPS | dual_stack |
| Identity Store (US East (Ohio)) | us-east-2 | identitystore-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| Identity Store (US East (N. Virginia)) | us-east-1 | identitystore.us-east-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (US East (N. Virginia)) | us-east-1 | identitystore.us-east-1.api.aws | HTTPS | dual_stack |
| Identity Store (US East (N. Virginia)) | us-east-1 | identitystore-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| Identity Store (US West (N. California)) | us-west-1 | identitystore.us-west-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (US West (N. California)) | us-west-1 | identitystore.us-west-1.api.aws | HTTPS | dual_stack |
| Identity Store (US West (N. California)) | us-west-1 | identitystore-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| Identity Store (US West (Oregon)) | us-west-2 | identitystore.us-west-2.amazonaws.com | HTTPS | ipv4 |
| Identity Store (US West (Oregon)) | us-west-2 | identitystore.us-west-2.api.aws | HTTPS | dual_stack |
| Identity Store (US West (Oregon)) | us-west-2 | identitystore-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| Identity Store (Cape Town) | af-south-1 | identitystore.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Cape Town) | af-south-1 | identitystore.af-south-1.api.aws | HTTPS | dual_stack |
| Identity Store (Hong Kong) | ap-east-1 | identitystore.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Hong Kong) | ap-east-1 | identitystore.ap-east-1.api.aws | HTTPS | dual_stack |
| Identity Store (Hyderabad) | ap-south-2 | identitystore.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Hyderabad) | ap-south-2 | identitystore.ap-south-2.api.aws | HTTPS | dual_stack |
| Identity Store (Jakarta) | ap-southeast-3 | identitystore.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Jakarta) | ap-southeast-3 | identitystore.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Identity Store (Malaysia) | ap-southeast-5 | identitystore.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Malaysia) | ap-southeast-5 | identitystore.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Identity Store (Melbourne) | ap-southeast-4 | identitystore.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Melbourne) | ap-southeast-4 | identitystore.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Identity Store (Mumbai) | ap-south-1 | identitystore.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Mumbai) | ap-south-1 | identitystore.ap-south-1.api.aws | HTTPS | dual_stack |
| Identity Store (New Zealand) | ap-southeast-6 | identitystore.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Identity Store (New Zealand) | ap-southeast-6 | identitystore.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Identity Store (Osaka) | ap-northeast-3 | identitystore.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Osaka) | ap-northeast-3 | identitystore.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Identity Store (Seoul) | ap-northeast-2 | identitystore.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Seoul) | ap-northeast-2 | identitystore.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Identity Store (Singapore) | ap-southeast-1 | identitystore.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Singapore) | ap-southeast-1 | identitystore.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Identity Store (Sydney) | ap-southeast-2 | identitystore.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Sydney) | ap-southeast-2 | identitystore.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Identity Store (Taipei) | ap-east-2 | identitystore.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Taipei) | ap-east-2 | identitystore.ap-east-2.api.aws | HTTPS | dual_stack |
| Identity Store (Thailand) | ap-southeast-7 | identitystore.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Thailand) | ap-southeast-7 | identitystore.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Identity Store (Tokyo) | ap-northeast-1 | identitystore.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Tokyo) | ap-northeast-1 | identitystore.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Identity Store (Central) | ca-central-1 | identitystore.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Central) | ca-central-1 | identitystore.ca-central-1.api.aws | HTTPS | dual_stack |
| Identity Store (Central) | ca-central-1 | identitystore-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Identity Store (Calgary) | ca-west-1 | identitystore.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Calgary) | ca-west-1 | identitystore.ca-west-1.api.aws | HTTPS | dual_stack |
| Identity Store (Calgary) | ca-west-1 | identitystore-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Identity Store (Frankfurt) | eu-central-1 | identitystore.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Frankfurt) | eu-central-1 | identitystore.eu-central-1.api.aws | HTTPS | dual_stack |
| Identity Store (Ireland) | eu-west-1 | identitystore.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Ireland) | eu-west-1 | identitystore.eu-west-1.api.aws | HTTPS | dual_stack |
| Identity Store (London) | eu-west-2 | identitystore.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Identity Store (London) | eu-west-2 | identitystore.eu-west-2.api.aws | HTTPS | dual_stack |
| Identity Store (Milan) | eu-south-1 | identitystore.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Milan) | eu-south-1 | identitystore.eu-south-1.api.aws | HTTPS | dual_stack |
| Identity Store (Paris) | eu-west-3 | identitystore.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Paris) | eu-west-3 | identitystore.eu-west-3.api.aws | HTTPS | dual_stack |
| Identity Store (Spain) | eu-south-2 | identitystore.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Spain) | eu-south-2 | identitystore.eu-south-2.api.aws | HTTPS | dual_stack |
| Identity Store (Stockholm) | eu-north-1 | identitystore.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Stockholm) | eu-north-1 | identitystore.eu-north-1.api.aws | HTTPS | dual_stack |
| Identity Store (Zurich) | eu-central-2 | identitystore.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Zurich) | eu-central-2 | identitystore.eu-central-2.api.aws | HTTPS | dual_stack |
| Identity Store (Tel Aviv) | il-central-1 | identitystore.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Tel Aviv) | il-central-1 | identitystore.il-central-1.api.aws | HTTPS | dual_stack |
| Identity Store (Central) | mx-central-1 | identitystore.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Central) | mx-central-1 | identitystore.mx-central-1.api.aws | HTTPS | dual_stack |
| Identity Store (Bahrain) | me-south-1 | identitystore.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (Bahrain) | me-south-1 | identitystore.me-south-1.api.aws | HTTPS | dual_stack |
| Identity Store (UAE) | me-central-1 | identitystore.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (UAE) | me-central-1 | identitystore.me-central-1.api.aws | HTTPS | dual_stack |
| Identity Store (São Paulo) | sa-east-1 | identitystore.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (São Paulo) | sa-east-1 | identitystore.sa-east-1.api.aws | HTTPS | dual_stack |
| Identity Store (US-East) | us-gov-east-1 | identitystore.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (US-East) | us-gov-east-1 | identitystore.us-gov-east-1.api.aws | HTTPS | dual_stack |
| Identity Store (US-West) | us-gov-west-1 | identitystore.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| Identity Store (US-West) | us-gov-west-1 | identitystore.us-gov-west-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (US East (Ohio)) | us-east-2 | oidc.us-east-2.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (US East (Ohio)) | us-east-2 | oidc-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| OpenID Connect (US East (Ohio)) | us-east-2 | oidc.us-east-2.api.aws | HTTPS | dual_stack |
| OpenID Connect (US East (N. Virginia)) | us-east-1 | oidc.us-east-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (US East (N. Virginia)) | us-east-1 | oidc-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| OpenID Connect (US East (N. Virginia)) | us-east-1 | oidc.us-east-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (US West (N. California)) | us-west-1 | oidc.us-west-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (US West (N. California)) | us-west-1 | oidc-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| OpenID Connect (US West (N. California)) | us-west-1 | oidc.us-west-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (US West (Oregon)) | us-west-2 | oidc.us-west-2.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (US West (Oregon)) | us-west-2 | oidc-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| OpenID Connect (US West (Oregon)) | us-west-2 | oidc.us-west-2.api.aws | HTTPS | dual_stack |
| OpenID Connect (Cape Town) | af-south-1 | oidc.af-south-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Cape Town) | af-south-1 | oidc.af-south-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (Hong Kong) | ap-east-1 | oidc.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Hong Kong) | ap-east-1 | oidc.ap-east-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (Hyderabad) | ap-south-2 | oidc.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Hyderabad) | ap-south-2 | oidc.ap-south-2.api.aws | HTTPS | dual_stack |
| OpenID Connect (Jakarta) | ap-southeast-3 | oidc.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Jakarta) | ap-southeast-3 | oidc.ap-southeast-3.api.aws | HTTPS | dual_stack |
| OpenID Connect (Malaysia) | ap-southeast-5 | oidc.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Malaysia) | ap-southeast-5 | oidc.ap-southeast-5.api.aws | HTTPS | dual_stack |
| OpenID Connect (Melbourne) | ap-southeast-4 | oidc.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Melbourne) | ap-southeast-4 | oidc.ap-southeast-4.api.aws | HTTPS | dual_stack |
| OpenID Connect (Mumbai) | ap-south-1 | oidc.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Mumbai) | ap-south-1 | oidc.ap-south-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (New Zealand) | ap-southeast-6 | oidc.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (New Zealand) | ap-southeast-6 | oidc.ap-southeast-6.api.aws | HTTPS | dual_stack |
| OpenID Connect (Osaka) | ap-northeast-3 | oidc.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Osaka) | ap-northeast-3 | oidc.ap-northeast-3.api.aws | HTTPS | dual_stack |
| OpenID Connect (Seoul) | ap-northeast-2 | oidc.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Seoul) | ap-northeast-2 | oidc.ap-northeast-2.api.aws | HTTPS | dual_stack |
| OpenID Connect (Singapore) | ap-southeast-1 | oidc.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Singapore) | ap-southeast-1 | oidc.ap-southeast-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (Sydney) | ap-southeast-2 | oidc.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Sydney) | ap-southeast-2 | oidc.ap-southeast-2.api.aws | HTTPS | dual_stack |
| OpenID Connect (Taipei) | ap-east-2 | oidc.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Taipei) | ap-east-2 | oidc.ap-east-2.api.aws | HTTPS | dual_stack |
| OpenID Connect (Thailand) | ap-southeast-7 | oidc.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Thailand) | ap-southeast-7 | oidc.ap-southeast-7.api.aws | HTTPS | dual_stack |
| OpenID Connect (Tokyo) | ap-northeast-1 | oidc.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Tokyo) | ap-northeast-1 | oidc.ap-northeast-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (Central) | ca-central-1 | oidc.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Central) | ca-central-1 | oidc.ca-central-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (Calgary) | ca-west-1 | oidc.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Calgary) | ca-west-1 | oidc.ca-west-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (Frankfurt) | eu-central-1 | oidc.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Frankfurt) | eu-central-1 | oidc.eu-central-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (Ireland) | eu-west-1 | oidc.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Ireland) | eu-west-1 | oidc.eu-west-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (London) | eu-west-2 | oidc.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (London) | eu-west-2 | oidc.eu-west-2.api.aws | HTTPS | dual_stack |
| OpenID Connect (Milan) | eu-south-1 | oidc.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Milan) | eu-south-1 | oidc.eu-south-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (Paris) | eu-west-3 | oidc.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Paris) | eu-west-3 | oidc.eu-west-3.api.aws | HTTPS | dual_stack |
| OpenID Connect (Spain) | eu-south-2 | oidc.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Spain) | eu-south-2 | oidc.eu-south-2.api.aws | HTTPS | dual_stack |
| OpenID Connect (Stockholm) | eu-north-1 | oidc.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Stockholm) | eu-north-1 | oidc.eu-north-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (Zurich) | eu-central-2 | oidc.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Zurich) | eu-central-2 | oidc.eu-central-2.api.aws | HTTPS | dual_stack |
| OpenID Connect (Tel Aviv) | il-central-1 | oidc.il-central-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Tel Aviv) | il-central-1 | oidc.il-central-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (Central) | mx-central-1 | oidc.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Central) | mx-central-1 | oidc.mx-central-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (Bahrain) | me-south-1 | oidc.me-south-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (Bahrain) | me-south-1 | oidc.me-south-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (UAE) | me-central-1 | oidc.me-central-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (UAE) | me-central-1 | oidc.me-central-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (São Paulo) | sa-east-1 | oidc.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (São Paulo) | sa-east-1 | oidc.sa-east-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (US-East) | us-gov-east-1 | oidc.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (US-East) | us-gov-east-1 | oidc.us-gov-east-1.api.aws | HTTPS | dual_stack |
| OpenID Connect (US-West) | us-gov-west-1 | oidc.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| OpenID Connect (US-West) | us-gov-west-1 | oidc.us-gov-west-1.api.aws | HTTPS | dual_stack |

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

- Status: **failed**, 3 call(s), 996.1 s, in 22,053 / out 36,684 tokens
- Part `endpoints` (1,089 words): **failed**, 2 call(s), 526.1 s, in 19,335 / out 18,252 tokens, —
- Part `quotas` (930 words): **failed**, 1 call(s), 470.0 s, in 2,718 / out 18,432 tokens, —

#### Error

```text
[endpoints]
- endpoints.100.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'dashboards.ap-northeast-3.aoss.amazo'
- endpoints.103.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'dashboards.ap-northeast-2.aoss.amazo'
- endpoints.106.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'dashboards.ap-southeast-1.aoss.amazo'
- endpoints.109.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'dashboards.ap-southeast-2.aoss.amazo'
- endpoints.115.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'dashboards.ap-southeast-7.aoss.amazo'
- endpoints.118.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'dashboards.ap-northeast-1.aoss.amazo'
--- after repair:
- endpoints.100.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'dashboards.ap-northeast-3.aoss.amazo'
- endpoints.103.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'dashboards.ap-northeast-2.aoss.amazo'
- endpoints.106.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'dashboards.ap-southeast-1.aoss.amazo'
- endpoints.109.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'dashboards.ap-southeast-2.aoss.amazo'
- endpoints.115.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'dashboards.ap-southeast-7.aoss.amazo'
- endpoints.118.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'dashboards.ap-northeast-1.aoss.amazo'
[quotas]
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 15 column 18363
--- no repair call
```

### 086-aws-lambda.pdf

- Status: **ok**, 2 call(s), 256.9 s, in 7,896 / out 10,167 tokens
- Part `endpoints` (517 words): **ok**, 1 call(s), 86.4 s, in 2,488 / out 3,681 tokens, 75 rows
- Part `quotas` (2,216 words): **ok**, 1 call(s), 170.5 s, in 5,408 / out 6,486 tokens, 73 rows, 30 ignored of the other kind
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
| Asia Pacific (Hyderabad) | ap-south-2 | lambda.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | lambda.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | lambda.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | lambda.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | lambda.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | lambda.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | lambda.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | lambda.ap-southeast-4.api.aws | HTTPS | dual_stack |
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
| Canada (Calgary) | ca-west-1 | lambda.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | lambda.ca-west-1.api.aws | HTTPS | dual_stack |
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
| Arm vCPUs for all Web Functions | Each supported Region: 2,000 | No | The Arm64 vCPU capacity for Lambda Web Function execution environments in this account in the current Region. |
| Asynchronous invocation request throughput on Lambda Managed Instances | Each supported Region: 5 Megabytes/Second | Yes | The maximum invoke request throughput (MB/s) for asynchronous invocations on Lambda Managed Instances. Asynchronous invocations occur when Lambda functions are invoked by services such as Amazon S3 or Amazon SNS. |
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
| Concurrent connections per 1 vCPU MicroVM | Each supported Region: 8 Count | No | Maximum number of concurrent connections per MicroVM with 1 vCPUs. |
| Concurrent connections per 16 vCPU MicroVM | Each supported Region: 128 Count | No | Maximum number of concurrent connections per MicroVM with 16 vCPUs. |
| Concurrent connections per 2 vCPU MicroVM | Each supported Region: 16 Count | No | Maximum number of concurrent connections per MicroVM with 2 vCPUs. |
| Concurrent connections per 4 vCPU MicroVM | Each supported Region: 32 Count | No | Maximum number of concurrent connections per MicroVM with 4 vCPUs. |
| Concurrent connections per 8 vCPU MicroVM | Each supported Region: 64 Count | No | Maximum number of concurrent connections per MicroVM with 8 vCPUs. |
| Concurrent executions | Each supported Region: 1,000 Count | Yes | The maximum number of events that functions can process simultaneously in the current Region. |
| Deployment package size (console editor) | Each supported Region: 3 Megabytes | No | The maximum size of a deployment package or layer archive when you upload it through the console editor. Upload larger files with Amazon S3. |
| Deployment package size (direct upload) | Each supported Region: 50 Megabytes | No | The maximum size of a deployment package or layer archive when you upload it directly to Lambda. Upload larger files with Amazon S3. |
| Deployment package size (unzipped) | Each supported Region: 250 Megabytes | No | The maximum size of the contents of a deployment package or layer archive when its unzipped. |
| Durable execution storage written in megabytes | Each supported Region: 100 Megabytes | No | The maximum cumulative amount of data persisted per durable execution, including input and output payloads, checkpoints and error data, measured in megabytes. |
| DynamoDB Event Source Mapping throughput on Lambda Managed Instances | Each supported Region: 10 Megabytes/Second | Yes | The maximum data throughput (MB/s) per DynamoDB event source mapping on Lambda Managed Instances. |
| Elastic network interfaces per VPC | Each supported Region: 3,000 Count | Yes | The maximum number of network interfaces that Lambda creates for a VPC with functions attached. Lambda creates a network interface for each combination of subnet and security group that functions connect to. |
| Endpoints per Web Function | Each supported Region: 10 Count | No | The maximum number of endpoints allowed per Lambda Web Function. |
| Environment variable size | Each supported Region: 4 Kilobytes | No | The maximum combined size of environment variables that are configured on a function. |
| File descriptors | Each supported Region: 1,024 Count | No | The maximum number of file descriptors that a function can have open. |
| Function and layer storage | Each supported Region: 300 Gigabytes | Yes | The amount of storage that is available for deployment packages and layer archives in the current Region. |
| Function invocation rate to initiate durable executions | us-east-1: 6,000 us-west-2: 6,000 eu-west-1: 6,000 Each of the other supported Regions: 3,000 | Yes | The maximum number of new durable executions that you can initiate per second. |
| Function layers | Each supported Region: 5 Count | No | The maximum number of layers that you can add to your function. |
| Function resource-based policy | Each supported Region: 20 Kilobytes | No | The maximum combined size of resource-based policies that are configured on a function. |
| Function timeout | Each supported Region: 900 | No | The maximum timeout that you can configure for a function. |
| Function versions per capacity provider | Each supported Region: 100 Count | No | The maximum number of function versions per capacity provider. |
| Kafka Event Source Mappings in default mode on Lambda Managed Instances | Each supported Region: 100 Count | No | The maximum number of Kafka event source mappings in default mode on Lambda Managed Instances. |
| Kafka Stream Event Source Mapping throughput in non-provisioned mode | Each supported Region: 5 Megabytes/Second | No | The maximum data throughput (MB/s) per Kafka Stream event source mapping in non-provisioned mode. |
| Kinesis Event Source Mapping throughput on Lambda Managed Instances | Each supported Region: 25 Megabytes/Second | Yes | The maximum data throughput (MB/s) per Kinesis event source mapping on Lambda Managed Instances. |
| Max Execution Duration of a MicroVM (in Hours) | Each supported Region: 8 Hours | No | The maximum execution duration of a MicroVM (in Hours). |
| Max allocated ARM_64 MicroVM memory | us-east-1: 1,024 Gigabytes us-east-2: 1,024 Gigabytes us-west-2: 1,024 Gigabytes ap-northeast-1: 1,024 Gigabytes Each of the other supported Regions: 400 Gigabytes | Yes | The maximum total configured baseline memory across all concurrently running ARM_64 MicroVMs, per account, per region. Individual MicroVMs can burst up to 4x their configured baseline memory. |
| Maximum number of durable operations per durable execution | Each supported Region: 30,000 Count | No | The maximum number of durable operations (including customer-initiated operations and automatic retries) that trigger state persistence within a single durable execution. |
| Maximum running durable executions | us-east-1: 10,000,000 us-west-2: 10,000,000 eu-west-1: 10,000,000 Each of the other supported Regions: 5,000,000 | Yes | The maximum number of durable executions that can be running simultaneously in the current region. |
| Network bandwidth per execution environment | Each supported Region: 625 Megabits/Second | Yes | The maximum sustained network bandwidth, in megabits per second, for a Lambda function execution environment that is not attached to a VPC. |
| Network connectors | Each supported Region: 1,000 Count | No | Number of Network Connectors per account |
| Number of MicroVM images | Each supported Region: 100 Count | Yes | Number of MicroVM images per account per region |
| Number of concurrent MicroVM image builds | us-east-1: 10 Count us-east-2: 10 Count us-west-2: 10 Count ap-northeast-1: 10 Count Each of the other supported Regions: 5 Count | Yes | Number of concurrent MicroVM image builds per account per region |
| Processes and threads | Each supported Region: 1,024 Count | No | The maximum combined number of processes and threads that a function can have open. |
| RPS per 16 vCPU MicroVM | Each supported Region: 160 Count | No | Maximum number of requests per second per MicroVM with 16 vCPUs / 32 GB. |
| RPS per 4 vCPU MicroVM | Each supported Region: 40 Count | No | Maximum number of requests per second per MicroVM with 4 vCPUs / 8 GB. |
| Rate of CheckpointDurableExecution API requests | us-east-1: 20,000 us-west-2: 20,000 eu-west-1: 20,000 Each of the other supported Regions: 10,000 | Yes | The maximum number of CheckpointDurableExecution API requests per second. |
| Rate of CreateMicrovmAuthToken API requests | Each supported Region: 50 Count | Yes | The maximum number of CreateMicrovmAuthToken API requests per second. |
| Rate of CreateMicrovmShell AuthToken API requests | Each supported Region: 5 Count | Yes | The maximum number of CreateMicrovmShell AuthToken API requests per second in this account in the current Region. |
| Rate of GetDurableExecution API requests | Each supported Region: 30 Count | Yes | The maximum number of GetDurableExecution API requests per second. |
| Rate of GetDurableExecutionHistory API requests | Each supported Region: 15 Count | Yes | The maximum number of GetDurableExecutionHistory API requests per second. |
| Rate of GetDurableExecutionState API requests | us-east-1: 20,000 us-west-2: 20,000 eu-west-1: 20,000 Each of the other supported Regions: 10,000 | Yes | The maximum number of GetDurableExecutionState API requests per second. |
| Rate of GetFunction API requests | Each supported Region: 100 Count | No | The maximum number of GetFunction API requests per second. |
| Rate of GetMicrovm API requests | Each supported Region: 100 Count | Yes | The maximum number of GetMicrovm API requests per second. |
| Rate of GetPolicy API requests | Each supported Region: 15 Count | No | The maximum number of GetPolicy API requests per second. |
| Rate of ListDurableExecutionsByFunction API requests | Each supported Region: 15 Count | Yes | The maximum number of ListDurableExecutionsByFunction API requests per second. |
| Rate of ResumeMicrovm API requests | Each supported Region: 5 Count | Yes | The maximum number of ResumeMicrovm API requests per second. |
| Rate of RunMicrovm API requests | Each supported Region: 5 Count | Yes | The maximum number of RunMicrovm API requests per second. |
| Rate of SendDurableExecutionCallbackFailure API requests | us-east-1: 6,000 us-west-2: 6,000 eu-west-1: 6,000 Each of the other supported Regions: 3,000 | Yes | The maximum number of SendDurableExecutionCallbackFailure API requests per second. |
| Rate of SendDurableExecutionCallbackHeartbeat API requests | us-east-1: 6,000 us-west-2: 6,000 eu-west-1: 6,000 Each of the other supported Regions: 3,000 | Yes | The maximum number of SendDurableExecutionCallbackHeartbeat API requests per second. |
| Rate of SendDurableExecutionCallbackSuccess API requests | us-east-1: 6,000 us-west-2: 6,000 eu-west-1: 6,000 Each of the other supported Regions: 3,000 | Yes | The maximum number of SendDurableExecutionCallbackSuccess API requests per second. |
| Rate of StopDurableExecution API requests | us-east-1: 600 us-west-2: 600 eu-west-1: 600 Each of the other supported Regions: 300 | Yes | The maximum number of StopDurableExecution API requests per second. |
| Rate of SuspendMicrovm API requests | Each supported Region: 2 Count | Yes | The maximum number of SuspendMicrovm API requests per second. |
| Rate of TerminateMicrovm API requests | Each supported Region: 10 Count | Yes | The maximum number of TerminateMicrovm API requests per second. |
| Rate of capacity provider read API requests | Each supported Region: 15 Count | No | The maximum combined rate (requests per second) for all capacity provider read APIs. |
| Rate of capacity provider write API requests | Each supported Region: 1 Count | No | The maximum combined rate (requests per second) for all capacity provider write APIs. |
| Rate of control plane API requests (excludes invocation, GetFunction, and GetPolicy requests) | Each supported Region: 15 Count | No | The maximum number of API requests per second (excluding invocation, GetFunction, and GetPolicy requests). |
| Rate of requests per Web Function Endpoint | Each supported Region: 10,000 Count | No | The maximum number of requests per second allowed for a single Lambda Web Function endpoint. |
| Rate of requests to Web Functions | Each supported Region: 100,000 Count | No | The maximum number of requests per second allowed across all your Lambda Web Function endpoints in this account in the current Region. |
| Revisions per Web Function | Each supported Region: 50 Count | No | The maximum number of revisions retained per Lambda Web Function. When this limit is reached, the oldest revisions not referenced by any endpoint are automatically deleted. |
| SQS Event Source Mapping throughput in default mode on Lambda Managed Instances | Each supported Region: 5 Megabytes/Second | No | The maximum data throughput (MB/s) per SQS event source mapping in default mode on Lambda Managed Instances. |
| Synchronous payload | Each supported Region: 6 Megabytes | No | The maximum size of an incoming synchronous invocation request or outgoing response. |

### 004-amazon-athena.pdf

- Status: **ok**, 2 call(s), 206.8 s, in 8,262 / out 8,333 tokens
- Part `endpoints` (603 words): **ok**, 1 call(s), 92.0 s, in 2,879 / out 3,895 tokens, 78 rows
- Part `quotas` (2,169 words): **ok**, 1 call(s), 114.8 s, in 5,383 / out 4,438 tokens, 30 rows, 14 ignored of the other kind
- Service: Amazon Athena; quota table format: `standard`

#### Endpoints (78)

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
| Asia Pacific (Hyderabad) | ap-south-2 | athena.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | athena.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | athena.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | athena.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | athena.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | athena.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | athena.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | athena.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | athena.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | athena.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | athena.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | athena.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | athena.ap-southeast-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Singapore) | ap-southeast-1 | athena.ap-southeast-2.api.aws | HTTPS | global |
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

- Status: **failed**, 2 call(s), 567.4 s, in 10,554 / out 20,628 tokens
- Part `endpoints` (2,034 words): **failed**, 1 call(s), 515.7 s, in 8,230 / out 18,432 tokens, —
- Part `quotas` (600 words): **ok**, 1 call(s), 51.7 s, in 2,324 / out 2,196 tokens, 13 rows, 18 ignored of the other kind

#### Error

```text
[endpoints]
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 2235 column 40
--- no repair call
```

### 095-aws-step-functions.pdf

- Status: **ok**, 2 call(s), 397.1 s, in 9,835 / out 15,715 tokens
- Part `endpoints` (772 words): **ok**, 1 call(s), 203.9 s, in 3,883 / out 8,313 tokens, 169 rows
- Part `quotas` (2,571 words): **ok**, 1 call(s), 193.2 s, in 5,952 / out 7,402 tokens, 97 rows, 15 ignored of the other kind
- Service: AWS Step Functions; quota table format: `standard`

#### Endpoints (169)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | states.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | sync-states.us-east-2.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | sync-states-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | sync-states-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | states-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | states-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | sync-states.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | states.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | states.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | sync-states.us-east-1.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | sync-states-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | sync-states-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | states-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | states-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | sync-states.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | states.us-east-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | states.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | sync-states.us-west-2.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | sync-states-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | sync-states-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | states-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | states-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | sync-states.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | states.us-west-2.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | states.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | sync-states.us-west-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | sync-states-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | sync-states-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | states-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | states-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | sync-states.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | states.us-west-1.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | states.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | sync-states.af-south-1.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | sync-states.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | states.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | states.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | sync-states.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | sync-states.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | states.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | states.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | sync-states.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | sync-states.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | states.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | states.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | sync-states.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | sync-states.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | states.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | states.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | sync-states.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | sync-states.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | states.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | states.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | sync-states.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | sync-states.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | states.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | states.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | sync-states.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | sync-states.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | states.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | states.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | sync-states.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | sync-states.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | states.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | states.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | sync-states.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | sync-states.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | states.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | states.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | sync-states.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | sync-states.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | states.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | states.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | sync-states.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | sync-states.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | states.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | states.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | sync-states.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | sync-states.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | states.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | states.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | sync-states.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | sync-states.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | states.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | states.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | sync-states.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | sync-states.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | states.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | states.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | sync-states.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | sync-states.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | states.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | states.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | sync-states.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | sync-states-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | sync-states-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | states-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | sync-states.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | states-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | states.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | states.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | sync-states.ca-west-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | sync-states-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Calgary) | ca-west-1 | sync-states-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada (Calgary) | ca-west-1 | states-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Calgary) | ca-west-1 | sync-states.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | states-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada (Calgary) | ca-west-1 | states.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | states.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | sync-states.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | sync-states.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | states.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | states.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | sync-states.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | sync-states.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | states.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | states.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | sync-states.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | sync-states.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | states.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | states.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | sync-states.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | sync-states.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | states.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | states.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | sync-states.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | sync-states.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | states.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | states.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | sync-states.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | sync-states.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | states.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | states.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | sync-states.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | sync-states.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | states.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | states.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | sync-states.eu-central-2.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | sync-states.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | states.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | states.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | sync-states.il-central-1.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | sync-states.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | states.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | states.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | sync-states.mx-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | sync-states.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | states.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | states.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | sync-states.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | sync-states.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | states.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | states.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | sync-states.me-central-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | sync-states.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | states.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | states.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | sync-states.sa-east-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | sync-states.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | states.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | states.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | sync-states.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | sync-states-fips.us-gov-east-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | sync-states-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | states-fips.us-gov-east-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | states-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | sync-states.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | states.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | sync-states.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (97)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Open Map Runs | Each supported Region: 1,000 | No | The maximum number of open Map Runs allowed at a time in this account. |
| Activity pollers per ARN | Each supported Region: 1,000 | No | The maximum number of workers concurrently polling an activity per ARN. |
| CreateActivity throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of CreateActivity calls that you can make per second. |
| CreateActivity throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for CreateActivity calls. |
| CreateStateMachine throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of CreateStateMachine calls that you can make per second. |
| CreateStateMachine throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second of CreateStateMachine calls. |
| CreateStateMachineAlias throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of CreateStateMachineAlias calls that you can make per second. |
| CreateStateMachineAlias throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for CreateStateMachineAlias calls. |
| DeleteActivity throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of DeleteActivity calls that you can make per second. |
| DeleteActivity throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second of DeleteActivity calls. |
| DeleteStateMachine throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of DeleteStateMachine calls that you can make per second. |
| DeleteStateMachine throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second of DeleteStateMachine calls. |
| DeleteStateMachineAlias throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of DeleteStateMachineAlias calls that you can make per second. |
| DeleteStateMachineAlias throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for DeleteStateMachineAlias calls. |
| DeleteStateMachineVersion throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of DeleteStateMachineVersion calls that you can make per second. |
| DeleteStateMachineVersion throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for DeleteStateMachineVersion calls. |
| DescribeActivity throttle token bucket size | us-east-1: 200; us-west-2: 200; eu-west-1: 200; Each of the other supported Regions: 200 | Yes | The maximum number of DescribeActivity calls that you can make per second. |
| DescribeActivity throttle token refill rate per second | us-east-1: 200; us-west-2: 200; eu-west-1: 200; Each of the other supported Regions: 200 | Yes | The token refill rate per second of DescribeActivity calls. |
| DescribeExecution throttle token bucket size | us-east-1: 300; us-west-2: 300; eu-west-1: 300; Each of the other supported Regions: 150 | Yes | The maximum number of DescribeExecution calls that you can make per second. |
| DescribeExecution throttle token refill rate per second | us-east-1: 50; us-west-2: 50; eu-west-1: 50; Each of the other supported Regions: 25 | Yes | The token refill rate per second of DescribeExecution calls. |
| DescribeMapRun throttle token bucket size | us-east-1: 200; us-west-2: 200; eu-west-1: 200; Each of the other supported Regions: 100 | Yes | The maximum number of DescribeMapRun calls that you can make per second. |
| DescribeMapRun throttle token refill rate per second | us-east-1: 200; us-west-2: 200; eu-west-1: 200; Each of the other supported Regions: 100 | Yes | The token refill rate per second of DescribeMapRun calls. |
| DescribeStateMachine throttle token bucket size | us-east-1: 200; us-west-2: 200; eu-west-1: 200; Each of the other supported Regions: 100 | Yes | The maximum number of DescribeStateMachine calls that you can make per second. |
| DescribeStateMachine throttle token refill rate per second | us-east-1: 200; us-west-2: 200; eu-west-1: 200; Each of the other supported Regions: 100 | Yes | The token refill rate per second of DescribeStateMachine calls. |
| DescribeStateMachineAlias throttle token bucket size | us-east-1: 200; us-west-2: 200; eu-west-1: 200; Each of the other supported Regions: 100 | Yes | The maximum number of DescribeStateMachineAlias calls that you can make per second. |
| DescribeStateMachineAlias throttle token refill rate per second | us-east-1: 200; us-west-2: 200; eu-west-1: 200; Each of the other supported Regions: 100 | Yes | The token refill rate per second of DescribeStateMachineAlias calls. |
| DescribeStateMachineForExecution throttle token bucket size | us-east-1: 200; us-west-2: 200; eu-west-1: 200; Each of the other supported Regions: 100 | Yes | The maximum number of DescribeStateMachineForExecution calls that you can make per second. |
| DescribeStateMachineForExecution throttle token refill rate per second | us-east-1: 200; us-west-2: 200; eu-west-1: 200; Each of the other supported Regions: 100 | Yes | The token refill rate per second of DescribeStateMachineForExecution calls. |
| Execution history retention time | Each supported Region: 90 | Yes | The maximum time (in days) for which the execution history is stored after an execution completes. |
| Execution history size | Each supported Region: 25,000 | No | The maximum number of events in a state machine's execution history. |
| Execution idle time | Each supported Region: 1 | No | The maximum amount of time (in years) a state machine execution can remain idle. |
| Execution time | Each supported Region: 1 | No | The maximum amount of time (in years) for which an execution can run. |
| GetActivityTask throttle token bucket size | us-east-1: 3,000; us-west-2: 3,000; eu-west-1: 3,000; Each of the other supported Regions: 1,500 | Yes | The maximum number of GetActivityTask calls that you can make per second. |
| GetActivityTask throttle token refill rate per second | us-east-1: 500; us-west-2: 500; eu-west-1: 500; Each of the other supported Regions: 300 | Yes | The token refill rate per second of GetActivityTask calls. |
| GetExecutionHistory throttle token bucket size | us-east-1: 400; us-west-2: 400; eu-west-1: 400; Each of the other supported Regions: 200 | Yes | The maximum number of GetExecutionHistory calls that you can make per second. |
| GetExecutionHistory throttle token refill rate per second | us-east-1: 200; us-west-2: 200; eu-west-1: 200; Each of the other supported Regions: 100 | Yes | The token refill rate per second of GetExecutionHistory calls. |
| Input file data size for a Map Run | Each supported Region: 10 | No | Input file data size for a Map Run Gigabytes |
| Input or result data size in task state or execution | Each supported Region: 262,144 | No | The maximum size of input or output data (in bytes) as a UTF-8 encoded string. This quota affects tasks (activity, Lambda function, or integrated service), state or execution output, and input data when scheduling a task, entering a state, or starting an execution. |
| ListActivities throttle token bucket size | us-east-1: 100; us-west-2: 100; eu-west-1: 100; Each of the other supported Regions: 50 | Yes | The maximum number of ListActivities calls that you can make per second. |
| ListActivities throttle token refill rate per second | us-east-1: 10; us-west-2: 10; eu-west-1: 10; Each of the other supported Regions: 5 | Yes | The token refill rate per second of ListActivities calls. |
| ListExecutions throttle token bucket size | us-east-1: 200; us-west-2: 200; eu-west-1: 200; Each of the other supported Regions: 100 | Yes | The maximum number of ListExecutions calls that you can make per second. |
| ListExecutions throttle token refill rate per second | us-east-1: 5; us-west-2: 5; eu-west-1: 5; Each of the other supported Regions: 2 | Yes | The token refill rate per second of ListExecutions calls. |
| ListMapRuns throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of ListMapRuns calls that you can make per second. |
| ListMapRuns throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for ListMapRuns calls. |
| ListStateMachineAliases throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of ListStateMachineAliases calls that you can make per second. |
| ListStateMachineAliases throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for ListStateMachineAliases calls. |
| ListStateMachineVersions throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of ListStateMachineVersions calls that you can make per second. |
| ListStateMachineVersions throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for ListStateMachineVersions calls. |
| ListStateMachines throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of ListStateMachines calls that you can make per second. |
| ListStateMachines throttle token refill rate per second | Each supported Region: 5 | Yes | The token refill rate per second of ListStateMachines calls. |
| ListTagsForResource throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of ListTagsForResource calls that you can make per second. |
| ListTagsForResource throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second of ListTagsForResource calls. |
| Maximum Concurrency | Each supported Region: 10,000 | No | The maximum number of parallel Map Run child executions |
| Maximum Number of Items Read per Map Run | Each supported Region: 100,000,000 | No | Maximum Number of Items Read per Map Run |
| Maximum redrives of a Map Run | Each supported Region: 1,000 | No | Maximum redrives of a Map Run |
| Maximum size of CSV headers | Each supported Region: 10 | No | Maximum size of CSV headers Kilobytes |
| Open executions | Each supported Region: 1,000,000 | Yes | The maximum number of open executions per account in the current Region. |
| PublishStateMachineVersion throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of PublishStateMachineVersion calls that you can make per second. |
| PublishStateMachineVersion throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for PublishStateMachineVersion calls. |
| Published state machine versions per state machine | Each supported Region: 1,000 | Yes | The maximum number of versions that can be published for a state machine. |
| RedriveExecution throttle token bucket size | Each supported Region: 800 | Yes | The maximum number of RedriveExecution calls that you can make per second. |
| RedriveExecution throttle token refill rate per second | Each supported Region: 150 | Yes | The token refill rate per second for RedriveExecution calls. |
| Registered activities | Each supported Region: 100,000 | Yes | The maximum number of activities that you can create in this account in the current Region. |
| Registered state machines | Each supported Region: 100,000 | Yes | The maximum number of state machines that you can create in this account in the current Region. |
| Request size | Each supported Region: 1 | No | The total data size in Megabytes per Step Functions API request, including the request header and all other associated request data. |
| Resource name length | Each supported Region: 80 | No | The maximum allowed characters for names of state machines, executions, and activity resource types. |
| SendTaskFailure throttle token bucket size | us-east-1: 3,000; us-west-2: 3,000; eu-west-1: 3,000; Each of the other supported Regions: 1,500 | Yes | The maximum number of SendTaskFailure calls that you can make per second. |
| SendTaskFailure throttle token refill rate per second | us-east-1: 500; us-west-2: 500; eu-west-1: 500; Each of the other supported Regions: 300 | Yes | The token refill rate per second of SendTaskFailure calls. |
| SendTaskHeartbeat throttle token bucket size | us-east-1: 3,000; us-west-2: 3,000; eu-west-1: 3,000; Each of the other supported Regions: 1,500 | Yes | The maximum number of SendTaskHeartbeat calls that you can make per second. |
| SendTaskHeartbeat throttle token refill rate per second | us-east-1: 500; us-west-2: 500; eu-west-1: 500; Each of the other supported Regions: 300 | Yes | The token refill rate per second of SendTaskHeartbeat calls. |
| SendTaskSuccess throttle token bucket size | us-east-1: 3,000; us-west-2: 3,000; eu-west-1: 3,000; Each of the other supported Regions: 1,500 | Yes | The maximum number of SendTaskSuccess calls that you can make per second. |
| SendTaskSuccess throttle token refill rate per second | us-east-1: 500; us-west-2: 500; eu-west-1: 500; Each of the other supported Regions: 300 | Yes | The token refill rate per second of SendTaskSuccess calls. |
| StartExecution throttle token bucket size | us-east-1: 1,300; us-west-2: 1,300; eu-west-1: 1,300; Each of the other supported Regions: 800 | Yes | The maximum number of StartExecution calls that you can make per second. |
| StartExecution throttle token refill rate per second | us-east-1: 300; us-west-2: 300; eu-west-1: 300; Each of the other supported Regions: 150 | Yes | The token refill rate per second of StartExecution calls. |
| StartExpressExecution throttle token bucket size | Each supported Region: 6,000 | Yes | The maximum number of StartExpressExecution calls that you can make per second. |
| StartExpressExecution throttle token refill rate per second | Each supported Region: 6,000 | Yes | The token refill rate per second of StartExpressExecution calls. |
| StartMapRun throttle token bucket size | Each supported Region: 25 | Yes | The maximum number of StartMapRun calls that you can make per second. |
| StartMapRun throttle token refill rate per second | Each supported Region: 25 | Yes | The token refill rate per second of StartMapRun calls. |
| State machine aliases per state machine | Each supported Region: 100 | Yes | The maximum number of aliases that can be created for a state machine. |
| StateTransition throttle token bucket size | us-east-1: 5,000; us-west-2: 5,000; eu-west-1: 5,000; Each of the other supported Regions: 800 | Yes | The maximum number of StateTransition calls that you can make per second. |
| StateTransition throttle token refill rate per second | us-east-1: 5,000; us-west-2: 5,000; eu-west-1: 5,000; Each of the other supported Regions: 800 | Yes | The token refill rate per second of StateTransition calls. |
| StopExecution throttle token bucket size | us-east-1: 1,000; us-west-2: 1,000; eu-west-1: 1,000; Each of the other supported Regions: 500 | Yes | The maximum number of StopExecution calls that you can make per second. |
| StopExecution throttle token refill rate per second | us-east-1: 200; us-west-2: 200; eu-west-1: 200; Each of the other supported Regions: 25 | Yes | The token refill rate per second of StopExecution calls. |
| TagResource throttle token bucket size | Each supported Region: 200 | Yes | The maximum number of TagResource calls that you can make per second. |
| TagResource throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second of TagResource calls. |
| Task execution time | Each supported Region: 1 | No | The maximum time (in years) that a task can take to complete an execution. |
| Task retention time in queue | Each supported Region: 1 | No | The maximum time (in years) that Step Functions keeps a task in the queue. |
| TestState throttle token bucket size | Each supported Region: 50 | No | The maximum number of TestState calls that you can make per second. |
| TestState throttle token refill rate per second | Each supported Region: 10 | No | The token refill rate per second of TestState calls. |
| UntagResource throttle token bucket size | Each supported Region: 200 | Yes | The maximum number of UntagResource calls that you can make per second. |
| UntagResource throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second of UntagResource calls. |
| UpdateMapRun throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of UpdateMapRun calls that you can make per second. |
| UpdateMapRun throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for UpdateMapRun calls. |
| UpdateStateMachine throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of UpdateStateMachine calls that you can make per second. |
| UpdateStateMachine throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second of UpdateStateMachine calls. |
| UpdateStateMachineAlias throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of UpdateStateMachineAlias calls that you can make per second. |
| UpdateStateMachineAlias throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for UpdateStateMachineAlias calls. |

### 049-amazon-simple-storage-service.pdf

- Status: **failed**, 3 call(s), 728.1 s, in 19,824 / out 25,350 tokens
- Part `endpoints` (3,370 words): **failed**, 1 call(s), 561.7 s, in 12,572 / out 18,432 tokens, —
- Part `quotas` (547 words): **repaired**, 2 call(s), 166.4 s, in 7,252 / out 6,918 tokens, 18 rows, 46 ignored of the other kind

#### Error

```text
[endpoints]
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 2223 column 49
--- no repair call
[quotas]
- quotas.18.name: not printed in a Standard Quota Table of the chapter: 'S3 Glacier: Number of random restore requests'
- quotas.20.name: not printed in a Standard Quota Table of the chapter: 'S3 Glacier: Retrieval request rate per second'
```

### 025-amazon-emr.pdf

- Status: **failed**, 3 call(s), 1024.4 s, in 31,958 / out 36,347 tokens
- Part `endpoints` (597 words): **failed**, 1 call(s), 474.1 s, in 2,873 / out 18,432 tokens, —
- Part `quotas` (4,372 words): **failed**, 2 call(s), 550.2 s, in 29,085 / out 17,915 tokens, —

#### Error

```text
[endpoints]
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing an object at line 2215 column 0
--- no repair call
[quotas]
- quotas.11.name: not printed in a Standard Quota Table of the chapter: 'Replenishment rate of DescribeJobRuns calls'
- quotas.12.name: not printed in a Standard Quota Table of the chapter: 'Replenishment rate of DescribeManagedClusters calls'
- quotas.13.name: not printed in a Standard Quota Table of the chapter: 'Replenishment rate of DescribeSecurityConfigurations calls'
- quotas.14.name: not printed in a Standard Quota Table of the chapter: 'Replenishment rate of DescribeSteps calls'
- quotas.46.name: not printed in a Standard Quota Table of the chapter: 'Replenishment rate of TerminateManagedClusters calls'
- quotas.47.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of API requests that you can make per second'
- quotas.48.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of AddInstanceFleet API requests that you can make per second'
- quotas.49.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of AddInstanceGroups API requests that you can make per second'
- quotas.50.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of AddJobFlowSteps API requests that you can make per second'
- quotas.51.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of AddTags API requests that you can make per second'
- quotas.52.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of CancelJobRun API requests that you can make per second'
- quotas.53.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of CancelSteps API requests that you can make per second'
- quotas.54.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of CreateManagedCluster API requests that you can make per second'
- quotas.55.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of CreateSecurityConfiguration API requests that you can make per second'
- quotas.56.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of DeleteSecurityConfiguration API requests that you can make per second'
- quotas.57.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of DescribeCluster API requests that you can make per second'
- quotas.58.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of DescribeJobFlows API requests that you can make per second'
- quotas.59.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of DescribeJobRuns API requests that you can make per second'
- quotas.60.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of DescribeManagedClusters API requests that you can make per second'
- quotas.61.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of DescribeSecurityConfigurations API requests that you can make per second'
- quotas.62.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of DescribeSteps API requests that you can make per second'
- quotas.63.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of GetAutoTerminationPolicy API requests that you can make per second'
- quotas.64.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of GetBlockPublicAccessConfiguration API requests that you can make per second'
- quotas.65.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of GetClusterSessionCredentials API requests that you can make per second'
- quotas.66.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of GetJobRunQueryResults API requests that you can make per second'
- quotas.67.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of GetManagedScalingPolicy API requests that you can make per second'
- quotas.68.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of GetResourceDashboard API requests that you can make per second'
- quotas.69.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListBootstrapActions API requests that you can make per second'
- quotas.70.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListClusters API requests that you can make per second'
- quotas.71.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListInstanceFleets API requests that you can make per second'
- quotas.72.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListInstanceGroups API requests that you can make per second'
- quotas.73.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListInstances API requests that you can make per second'
- quotas.74.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListJobRuns API requests that you can make per second'
- quotas.75.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListManagedClusters API requests that you can make per second'
- quotas.76.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListReleaseLabels API requests that you can make per second'
- quotas.77.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListSecurityConfigurations API requests that you can make per second'
- quotas.78.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListSteps API requests that you can make per second'
- quotas.79.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListSupportedInstanceTypes API requests that you can make per second'
- quotas.80.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ModifyCluster API requests that you can make per second'
- quotas.81.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ModifyInstanceFleet API requests that you can make per second'
- quotas.82.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ModifyInstanceGroups API requests that you can make per second'
- quotas.83.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of PutAutoScalingPolicy API requests that you can make per second'
- quotas.84.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of PutManagedScalingPolicy API requests that you can make per second'
- quotas.85.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of RemoveAutoScalingPolicy API requests that you can make per second'
- quotas.86.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of RemoveAutoTerminationPolicy API requests that you can make per second'
- quotas.87.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of RemoveManagedScalingPolicy API requests that you can make per second'
- quotas.88.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of RemoveTags API requests that you can make per second'
- quotas.89.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of RunJobFlow API requests that you can make per second'
- quotas.90.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of SetKeepJobFlowAliveWhenNoSteps API requests that you can make per second'
- quotas.91.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of SetTerminationProtection API requests that you can make per second'
- quotas.92.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of SetVisibleToAllUsers API requests that you can make per second'
- quotas.93.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of StartJobRun API requests that you can make per second'
- quotas.94.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of TerminateJobFlows API requests that you can make per second'
- quotas.95.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of TerminateManagedClusters API requests that you can make per second'
- quotas.96.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of active clusters that can be run at the same time'
- quotas.98.name: not printed in a Standard Quota Table of the chapter: 'The maximum rate at which your bucket replenishes for all EMR operations'
- quotas.99.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of EMR WAL workspaces that can be used at the same time in this account in the current Region'
--- after repair:
- quotas.11.name: not printed in a Standard Quota Table of the chapter: 'Replenishment rate of DescribeJobRuns calls'
- quotas.12.name: not printed in a Standard Quota Table of the chapter: 'Replenishment rate of DescribeManagedClusters calls'
- quotas.13.name: not printed in a Standard Quota Table of the chapter: 'Replenishment rate of DescribeSecurityConfigurations calls'
- quotas.14.name: not printed in a Standard Quota Table of the chapter: 'Replenishment rate of DescribeSteps calls'
- quotas.46.name: not printed in a Standard Quota Table of the chapter: 'Replenishment rate of TerminateManagedClusters calls'
- quotas.47.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of API requests that you can make per second'
- quotas.48.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of AddInstanceFleet API requests that you can make per second'
- quotas.49.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of AddInstanceGroups API requests that you can make per second'
- quotas.50.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of AddJobFlowSteps API requests that you can make per second'
- quotas.51.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of AddTags API requests that you can make per second'
- quotas.52.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of CancelJobRun API requests that you can make per second'
- quotas.53.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of CancelSteps API requests that you can make per second'
- quotas.54.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of CreateManagedCluster API requests that you can make per second'
- quotas.55.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of CreateSecurityConfiguration API requests that you can make per second'
- quotas.56.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of DeleteSecurityConfiguration API requests that you can make per second'
- quotas.57.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of DescribeCluster API requests that you can make per second'
- quotas.58.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of DescribeJobFlows API requests that you can make per second'
- quotas.59.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of DescribeJobRuns API requests that you can make per second'
- quotas.60.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of DescribeManagedClusters API requests that you can make per second'
- quotas.61.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of DescribeSecurityConfigurations API requests that you can make per second'
- quotas.62.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of DescribeSteps API requests that you can make per second'
- quotas.63.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of GetAutoTerminationPolicy API requests that you can make per second'
- quotas.64.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of GetBlockPublicAccessConfiguration API requests that you can make per second'
- quotas.65.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of GetClusterSessionCredentials API requests that you can make per second'
- quotas.66.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of GetJobRunQueryResults API requests that you can make per second'
- quotas.67.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of GetManagedScalingPolicy API requests that you can make per second'
- quotas.68.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of GetResourceDashboard API requests that you can make per second'
- quotas.69.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListBootstrapActions API requests that you can make per second'
- quotas.70.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListClusters API requests that you can make per second'
- quotas.71.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListInstanceFleets API requests that you can make per second'
- quotas.72.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListInstanceGroups API requests that you can make per second'
- quotas.73.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListInstances API requests that you can make per second'
- quotas.74.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListJobRuns API requests that you can make per second'
- quotas.75.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListManagedClusters API requests that you can make per second'
- quotas.76.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListReleaseLabels API requests that you can make per second'
- quotas.77.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListSecurityConfigurations API requests that you can make per second'
- quotas.78.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListSteps API requests that you can make per second'
- quotas.79.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ListSupportedInstanceTypes API requests that you can make per second'
- quotas.80.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ModifyCluster API requests that you can make per second'
- quotas.81.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ModifyInstanceFleet API requests that you can make per second'
- quotas.82.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of ModifyInstanceGroups API requests that you can make per second'
- quotas.83.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of PutAutoScalingPolicy API requests that you can make per second'
- quotas.84.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of PutManagedScalingPolicy API requests that you can make per second'
- quotas.85.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of RemoveAutoScalingPolicy API requests that you can make per second'
- quotas.86.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of RemoveAutoTerminationPolicy API requests that you can make per second'
- quotas.87.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of RemoveManagedScalingPolicy API requests that you can make per second'
- quotas.88.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of RemoveTags API requests that you can make per second'
- quotas.89.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of RunJobFlow API requests that you can make per second'
- quotas.90.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of SetKeepJobFlowAliveWhenNoSteps API requests that you can make per second'
- quotas.91.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of SetTerminationProtection API requests that you can make per second'
- quotas.92.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of SetVisibleToAllUsers API requests that you can make per second'
- quotas.93.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of StartJobRun API requests that you can make per second'
- quotas.94.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of TerminateJobFlows API requests that you can make per second'
- quotas.95.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of TerminateManagedClusters API requests that you can make per second'
- quotas.96.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of active clusters that can be run at the same time'
- quotas.98.name: not printed in a Standard Quota Table of the chapter: 'The maximum rate at which your bucket replenishes for all EMR operations'
- quotas.99.name: not printed in a Standard Quota Table of the chapter: 'The maximum number of EMR WAL workspaces that can be used at the same time in this account in the current Region'
```

### 010-amazon-cloudfront.pdf

- Status: **failed**, 3 call(s), 365.6 s, in 19,361 / out 13,163 tokens
- Part `endpoints` (195 words): **ok**, 1 call(s), 5.9 s, in 1,142 / out 230 tokens, 4 rows
- Part `quotas` (2,902 words): **failed**, 2 call(s), 359.8 s, in 18,219 / out 12,933 tokens, —

#### Error

```text
[quotas]
- quotas.35.name: not printed in a Standard Quota Table of the chapter: 'Maximum compressed size of a Lambda function and any included libraries (Origin request and response event)'
- quotas.36.name: not printed in a Standard Quota Table of the chapter: 'Maximum compressed size of a Lambda function and any included libraries (Viewer request and response event)'
- quotas.74.name: not printed in a Standard Quota Table of the chapter: 'Request body size for origin requests exposed to a Lambda@Edge function'
- quotas.77.name: not printed in a Standard Quota Table of the chapter: 'Request body size for viewer requests exposed to a Lambda@Edge function'
- quotas.81.name: not printed in a Standard Quota Table of the chapter: 'Response headers policies per AWS account'
--- after repair:
- quotas.35.name: not printed in a Standard Quota Table of the chapter: 'Maximum compressed size of a Lambda function and any included libraries (Origin request and response event)'
- quotas.36.name: not printed in a Standard Quota Table of the chapter: 'Maximum compressed size of a Lambda function and any included libraries (Viewer request and response event)'
- quotas.74.name: not printed in a Standard Quota Table of the chapter: 'Request body size for origin requests exposed to a Lambda@Edge function'
- quotas.77.name: not printed in a Standard Quota Table of the chapter: 'Request body size for viewer requests exposed to a Lambda@Edge function'
- quotas.81.name: not printed in a Standard Quota Table of the chapter: 'Response headers policies per AWS account'
```

### 074-aws-global-accelerator.pdf

- Status: **repaired**, 3 call(s), 382.3 s, in 16,300 / out 14,291 tokens
- Part `endpoints` (785 words): **repaired**, 2 call(s), 369.2 s, in 14,634 / out 13,760 tokens, 138 rows
- Part `quotas` (545 words): **ok**, 1 call(s), 13.2 s, in 1,666 / out 531 tokens, 5 rows, 5 ignored of the other kind
- Service: AWS Global Accelerator; quota table format: `standard`

#### Endpoints (138)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US West (Oregon) | us-west-2 | globalaccelerator.amazonaws.com | HTTPS | global |
| US West (Oregon) | us-west-2 | globalaccelerator-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| US East (Ohio) | us-east-2 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| US East (Ohio) | us-east-2 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| US East (Ohio) | us-east-2 | networkmanager.us-west-2.api.aws | HTTPS | global |
| US East (N. Virginia) | us-east-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| US East (N. Virginia) | us-east-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| US East (N. Virginia) | us-east-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| US East (N. Virginia) | us-east-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| US West (N. California) | us-west-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| US West (N. California) | us-west-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| US West (N. California) | us-west-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| US West (N. California) | us-west-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| US West (Oregon) | us-west-2 | networkmanager.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | networkmanager-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | networkmanager.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Africa (Cape Town) | af-south-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Africa (Cape Town) | af-south-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Africa (Cape Town) | af-south-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Hong Kong) | ap-east-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Hong Kong) | ap-east-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Hong Kong) | ap-east-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Hong Kong) | ap-east-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Hyderabad) | ap-south-2 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Hyderabad) | ap-south-2 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Hyderabad) | ap-south-2 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Hyderabad) | ap-south-2 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Jakarta) | ap-southeast-3 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Jakarta) | ap-southeast-3 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Jakarta) | ap-southeast-3 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Jakarta) | ap-southeast-3 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Melbourne) | ap-southeast-4 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Melbourne) | ap-southeast-4 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Melbourne) | ap-southeast-4 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Melbourne) | ap-southeast-4 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Mumbai) | ap-south-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Mumbai) | ap-south-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Mumbai) | ap-south-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Mumbai) | ap-south-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (New Zealand) | ap-southeast-6 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (New Zealand) | ap-southeast-6 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (New Zealand) | ap-southeast-6 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (New Zealand) | ap-southeast-6 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Osaka) | ap-northeast-3 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Osaka) | ap-northeast-3 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Osaka) | ap-northeast-3 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Osaka) | ap-northeast-3 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Seoul) | ap-northeast-2 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Seoul) | ap-northeast-2 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Seoul) | ap-northeast-2 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Seoul) | ap-northeast-2 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Singapore) | ap-southeast-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Singapore) | ap-southeast-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Singapore) | ap-southeast-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Singapore) | ap-southeast-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Sydney) | ap-southeast-2 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Sydney) | ap-southeast-2 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Sydney) | ap-southeast-2 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Sydney) | ap-southeast-2 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Taipei) | ap-southeast-3 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Taipei) | ap-southeast-3 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Taipei) | ap-southeast-3 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Taipei) | ap-southeast-3 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Thailand) | ap-southeast-7 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Thailand) | ap-southeast-7 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Thailand) | ap-southeast-7 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Thailand) | ap-southeast-7 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Tokyo) | ap-northeast-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Tokyo) | ap-northeast-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Asia Pacific (Tokyo) | ap-northeast-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Tokyo) | ap-northeast-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Canada (Central) | ca-central-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Canada (Central) | ca-central-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Canada (Central) | ca-central-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Canada (Central) | ca-central-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Canada (Calgary) | ca-west-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Canada (Calgary) | ca-west-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Canada (Calgary) | ca-west-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Canada (Calgary) | ca-west-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Europe (Frankfurt) | eu-central-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Europe (Frankfurt) | eu-central-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Europe (Frankfurt) | eu-central-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Europe (Frankfurt) | eu-central-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Europe (Ireland) | eu-west-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Europe (Ireland) | eu-west-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Europe (Ireland) | eu-west-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Europe (Ireland) | eu-west-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Europe (London) | eu-west-2 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Europe (London) | eu-west-2 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Europe (London) | eu-west-2 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Europe (London) | eu-west-2 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Europe (Milan) | eu-south-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Europe (Milan) | eu-south-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Europe (Milan) | eu-south-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Europe (Milan) | eu-south-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Europe (Paris) | eu-west-3 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Europe (Paris) | eu-west-3 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Europe (Paris) | eu-west-3 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Europe (Paris) | eu-west-3 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Europe (Spain) | eu-south-2 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Europe (Spain) | eu-south-2 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Europe (Spain) | eu-south-2 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Europe (Spain) | eu-south-2 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Europe (Stockholm) | eu-north-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Europe (Stockholm) | eu-north-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Europe (Stockholm) | eu-north-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Europe (Stockholm) | eu-north-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Europe (Zurich) | eu-central-2 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Europe (Zurich) | eu-central-2 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Europe (Zurich) | eu-central-2 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Europe (Zurich) | eu-central-2 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Israel (Tel Aviv) | il-central-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Israel (Tel Aviv) | il-central-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Israel (Tel Aviv) | il-central-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Israel (Tel Aviv) | il-central-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Mexico (Central) | mx-central-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Mexico (Central) | mx-central-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Mexico (Central) | mx-central-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Mexico (Central) | mx-central-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Middle East (Bahrain) | me-south-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Middle East (Bahrain) | me-south-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Middle East (Bahrain) | me-south-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Middle East (Bahrain) | me-south-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| Middle East (UAE) | me-central-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| Middle East (UAE) | me-central-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| Middle East (UAE) | me-central-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| Middle East (UAE) | me-central-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| South America (São Paulo) | sa-east-1 | networkmanager.us-west-2.amazonaws.com | HTTPS | global |
| South America (São Paulo) | sa-east-1 | networkmanager-fips.us-west-2.api.aws | HTTPS | global |
| South America (São Paulo) | sa-east-1 | networkmanager-fips.us-west-2.amazonaws.com | HTTPS | global |
| South America (São Paulo) | sa-east-1 | networkmanager.us-west-2.api.aws | HTTPS | global |
| AWS GovCloud (US-East) | us-gov-east-1 | networkmanager.us-gov-west-1.amazonaws.com | HTTPS | global |
| AWS GovCloud (US-East) | us-gov-east-1 | networkmanager.us-gov-west-1.api.aws | HTTPS | global |
| AWS GovCloud (US-West) | us-gov-west-1 | networkmanager.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | networkmanager.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (5)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Cross-account attachments per AWS account | Each supported Region: 10 | Yes | The maximum number of cross-account attachments for each AWS account. |
| Custom routing accelerators per AWS account | Each supported Region: 10 | Yes | The maximum number of custom routing accelerators for each AWS account. |
| Endpoint groups per accelerator | Each supported Region: 42 | No | The maximum number of endpoint groups per accelerator. |
| Endpoint resources per cross-account attachment | Each supported Region: 500 | No | The maximum number of endpoint resources per cross-account attachment. |
| Endpoints per endpoint group - Application Load Balancers | Each supported Region: 10 | No | The maximum number of Application Load Balancers in an endpoint group. |

#### First answer rejected (repaired)

```text
[endpoints]
- endpoints.1.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'globalaccelerator-fips.us-west-2.zonaws.com'
```

### 019-amazon-ecr.pdf

- Status: **ok**, 2 call(s), 314.2 s, in 7,479 / out 12,565 tokens
- Part `endpoints` (1,036 words): **ok**, 1 call(s), 247.8 s, in 5,023 / out 9,701 tokens, 190 rows
- Part `quotas` (907 words): **ok**, 1 call(s), 66.4 s, in 2,456 / out 2,864 tokens, 23 rows, 23 ignored of the other kind
- Service: Amazon ECR; quota table format: `standard`

#### Endpoints (190)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | ecr.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | ecr-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | dkr-ecr.us-east-2.on.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | dkr.ecr.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | ecr.us-east-2.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | dkr-ecr-fips.us-east-2.on.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | ecr-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | api.ecr-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | api.ecr.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | dkr.ecr-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | ecr.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | dkr.ecr-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | ecr-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | dkr.ecr.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | dkr-ecr.us-east-1.on.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | ecr.us-east-1.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | dkr-ecr-fips.us-east-1.on.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | api.ecr.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | api.ecr-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | ecr-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | ecr.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | ecr-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | ecr.us-west-2.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | ecr-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | dkr.ecr.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | dkr.ecr-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | api.ecr-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | dkr-ecr.us-west-2.on.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | dkr-ecr-fips.us-west-2.on.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | api.ecr.us-west-2.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | ecr.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | api.ecr.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | ecr.af-south-1.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | dkr.ecr.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | dkr-ecr.af-south-1.on.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | ecr.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | dkr-ecr.ap-east-1.on.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | dkr.ecr.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | api.ecr.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | ecr.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | api.ecr.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | dkr-ecr.ap-south-2.on.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | dkr.ecr.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | ecr.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | ecr.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | api.ecr.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | dkr-ecr.ap-southeast-3.on.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | dkr.ecr.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | ecr.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | ecr.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | api.ecr.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | dkr-ecr.ap-southeast-5.on.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | dkr.ecr.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | ecr.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | api.ecr.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | ecr.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | dkr-ecr.ap-southeast-4.on.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | dkr.ecr.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | ecr.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | api.ecr.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | dkr-ecr.ap-south-1.on.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | dkr.ecr.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | ecr.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | ecr.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | dkr-ecr.ap-southeast-6.on.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | ecr.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | api.ecr.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | dkr.ecr.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | ecr.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | dkr-ecr.ap-northeast-3.on.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | ecr.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | api.ecr.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | ecr.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | ecr.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | dkr.ecr.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | dkr-ecr.ap-northeast-2.on.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | ecr.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | api.ecr.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | dkr.ecr.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | dkr-ecr.ap-southeast-1.on.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | ecr.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | ecr.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | ecr.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | api.ecr.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | dkr.ecr.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | dkr-ecr.ap-southeast-2.on.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | ecr.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | api.ecr.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | dkr.ecr.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | dkr-ecr.ap-east-2.on.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | ecr.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | ecr.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | dkr-ecr.ap-southeast-7.on.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | ecr.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | api.ecr.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | ecr.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | dkr-ecr.ap-northeast-1.on.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | api.ecr.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | ecr.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | ecr.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | ecr.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | dkr-ecr.ca-central-1.on.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | dkr.ecr.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | api.ecr.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | ecr.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | ecr.ca-west-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | api.ecr.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | dkr.ecr.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | dkr-ecr.ca-west-1.on.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | ecr.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | ecr.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | dkr-ecr.eu-central-1.on.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | dkr.ecr.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | ecr.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | api.ecr.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | dkr-ecr.eu-west-1.on.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | dkr.ecr.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | ecr.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | ecr.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | api.ecr.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | dkr.ecr.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | dkr-ecr.eu-west-2.on.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | ecr.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | ecr.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | api.ecr.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | dkr-ecr.eu-south-1.on.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | dkr.ecr.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | ecr.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | ecr.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | api.ecr.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | dkr.ecr.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | dkr-ecr.eu-west-3.on.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | ecr.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | ecr.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | api.ecr.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | dkr-ecr.eu-south-2.on.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | dkr.ecr.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | ecr.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | ecr.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | api.ecr.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | dkr-ecr.eu-north-1.on.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | dkr.ecr.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | ecr.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | ecr.eu-central-2.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | api.ecr.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | dkr-ecr.eu-central-2.on.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | dkr.ecr.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | ecr.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | ecr.il-central-1.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | api.ecr.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | dkr-ecr.il-central-1.on.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | dkr.ecr.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | ecr.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | ecr.mx-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | api.ecr.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | dkr-ecr.mx-central-1.on.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | ecr.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | ecr.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | api.ecr.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | dkr-ecr.me-south-1.on.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | dkr.ecr.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | ecr.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | ecr.me-central-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | api.ecr.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | dkr-ecr.me-central-1.on.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | dkr.ecr.me-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | ecr.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | ecr.sa-east-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | api.ecr.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | dkr-ecr.sa-east-1.on.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | dkr.ecr.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | ecr.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | ecr.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | dkr.ecr.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | ecr-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | api.ecr-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | api.ecr.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | ecr-fips.us-gov-east-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | dkr.ecr-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | dkr-ecr-fips.us-gov-east-1.on.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | dkr-ecr.us-gov-east-1.on.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | ecr.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | ecr.us-gov-west-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | dkr.ecr.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | ecr-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | api.ecr-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | api.ecr.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | ecr-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | dkr-ecr-fips.us-gov-west-1.on.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | dkr-ecr.us-gov-west-1.on.aws | HTTPS | dual_stack |

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
