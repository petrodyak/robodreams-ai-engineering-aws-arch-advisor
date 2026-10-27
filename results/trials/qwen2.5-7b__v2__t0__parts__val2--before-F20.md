# Run `qwen2.5-7b__v2__t0__parts__val2`

Generated from the JSONL run file by `src/extract/report_md.py`; do not edit.

- Model: `qwen2.5:7b`
- Prompt version: `v2` (file sha `a3adf0379524`)
- Schema sha: `d4010de95c65`; validation version `2`
- Sampling: `t0` (temperature 0.0, top_p None)
- In parts: the endpoints part and the quotas part of each chapter in one call each, merged by code (step 13)
- Documents: 19

## Summary

| # | Document | Group | Status | Calls | Latency, s | In tokens | Out tokens | Quota table | Endpoints | Quotas |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [006-amazon-aurora-dsql.pdf](#006-amazon-aurora-dsqlpdf) | short | failed | 3 | 56.9 | 4,132 | 2,231 | — | — | — |
| 2 | [076-aws-glue-databrew.pdf](#076-aws-glue-databrewpdf) | short | repaired | 4 | 106.1 | 8,216 | 4,438 | standard | 24 | 7 |
| 3 | [085-aws-lake-formation.pdf](#085-aws-lake-formationpdf) | short | ok | 1 | 100.6 | 2,802 | 4,210 | none | 84 | 0 |
| 4 | [033-amazon-kinesis-data-streams.pdf](#033-amazon-kinesis-data-streamspdf) | short | failed | 3 | 175.2 | 7,371 | 7,230 | — | — | — |
| 5 | [007-amazon-bedrock-agentcore.pdf](#007-amazon-bedrock-agentcorepdf) | short | ok | 1 | 53.9 | 2,446 | 2,129 | none | 39 | 0 |
| 6 | [037-amazon-managed-workflows-for-apache-airflow.pdf](#037-amazon-managed-workflows-for-apache-airflowpdf) | short | failed | 2 | 660.7 | 4,928 | 26,237 | — | — | — |
| 7 | [055-aws-app-mesh.pdf](#055-aws-app-meshpdf) | short | ok | 2 | 129.1 | 4,498 | 5,051 | standard | 89 | 5 |
| 8 | [066-aws-datasync.pdf](#066-aws-datasyncpdf) | short | failed | 3 | 298.0 | 13,535 | 11,296 | — | — | — |
| 9 | [091-aws-resource-groups-and-tagging.pdf](#091-aws-resource-groups-and-taggingpdf) | short | repaired | 3 | 133.3 | 6,585 | 5,590 | standard | 76 | 1 |
| 10 | [018-amazon-ec2-auto-scaling.pdf](#018-amazon-ec2-auto-scalingpdf) | short | ok | 2 | 138.6 | 4,493 | 5,795 | standard | 84 | 9 |
| 11 | [005-amazon-aurora.pdf](#005-amazon-aurorapdf) | medium | failed | 2 | 520.2 | 5,188 | 20,152 | — | — | — |
| 12 | [075-aws-glue.pdf](#075-aws-gluepdf) | medium | failed | 3 | 305.6 | 12,712 | 11,931 | — | — | — |
| 13 | [042-amazon-redshift.pdf](#042-amazon-redshiftpdf) | medium | failed | 3 | 571.8 | 25,289 | 19,209 | — | — | — |
| 14 | [044-amazon-relational-database-service.pdf](#044-amazon-relational-database-servicepdf) | medium | failed | 2 | 563.7 | 6,495 | 21,100 | — | — | — |
| 15 | [048-amazon-simple-queue-service.pdf](#048-amazon-simple-queue-servicepdf) | medium | repaired | 3 | 239.2 | 10,049 | 9,378 | standard | 80 | 18 |
| 16 | [047-amazon-simple-notification-service.pdf](#047-amazon-simple-notification-servicepdf) | medium | repaired | 3 | 330.7 | 14,103 | 12,884 | non_standard | 71 | 0 |
| 17 | [026-amazon-eventbridge.pdf](#026-amazon-eventbridgepdf) | medium | failed | 3 | 175.6 | 9,317 | 7,209 | — | — | — |
| 18 | [092-aws-secrets-manager.pdf](#092-aws-secrets-managerpdf) | medium | failed | 4 | 415.4 | 19,972 | 15,880 | — | — | — |
| 19 | [023-amazon-elastic-kubernetes-service.pdf](#023-amazon-elastic-kubernetes-servicepdf) | medium | ok | 2 | 84.9 | 5,097 | 3,473 | standard | 38 | 13 |

## Documents

### 006-amazon-aurora-dsql.pdf

- Status: **failed**, 3 call(s), 56.9 s, in 4,132 / out 2,231 tokens
- Part `endpoints` (294 words): **ok**, 1 call(s), 34.8 s, in 1,583 / out 1,268 tokens, 25 rows
- Part `quotas` (104 words): **failed**, 2 call(s), 22.1 s, in 2,549 / out 963 tokens, —

#### Error

```text
[quotas]
- endpoints.0.endpoint: Value error, not a single hostname (broken by a line wrap?): 'https://aurora-dsql.us-east-1.amazonaws.com'
- endpoints.1.endpoint: Value error, not a single hostname (broken by a line wrap?): 'https://dsql.us-east-1.ondemand.amazonaws.com'
- endpoints.2.endpoint: Value error, not a single hostname (broken by a line wrap?): 'https://aurora-dsql.us-west-2.amazonaws.com'
- endpoints.3.endpoint: Value error, not a single hostname (broken by a line wrap?): 'https://dsql.us-west-2.ondemand.amazonaws.com'
--- after repair:
- endpoints.0.endpoint: Value error, not a single hostname (broken by a line wrap?): 'https://aurora-dsql.us-east-1.amazonaws.com'
- endpoints.1.endpoint: Value error, not a single hostname (broken by a line wrap?): 'https://dsql.us-east-1.ondemand.amazonaws.com'
- endpoints.2.endpoint: Value error, not a single hostname (broken by a line wrap?): 'https://aurora-dsql.us-west-2.amazonaws.com'
- endpoints.3.endpoint: Value error, not a single hostname (broken by a line wrap?): 'https://dsql.us-west-2.ondemand.amazonaws.com'
```

### 076-aws-glue-databrew.pdf

- Status: **repaired**, 4 call(s), 106.1 s, in 8,216 / out 4,438 tokens
- Part `endpoints` (291 words): **repaired**, 2 call(s), 64.0 s, in 4,707 / out 2,663 tokens, 24 rows
- Part `quotas` (180 words): **repaired**, 2 call(s), 42.1 s, in 3,509 / out 1,775 tokens, 7 rows, 6 ignored of the other kind
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
[quotas]
- endpoints.1.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'databrew.us-east-1.elasticbeanstalk.com'
- endpoints.3.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'databrew.us-west-2.elasticbeanstalk.com'
- endpoints.5.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'databrew.eu-west-1.elasticbeanstalk.com'
- endpoints.7.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'databrew.ap-southeast-2.elasticbeanstalk.com'
- endpoints.9.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'databrew.ap-northeast-1.elasticbeanstalk.com'
- endpoints.11.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'databrew.sa-east-1.elasticbeanstalk.com'
```

### 085-aws-lake-formation.pdf

- Status: **ok**, 1 call(s), 100.6 s, in 2,802 / out 4,210 tokens
- Part `endpoints` (561 words): **ok**, 1 call(s), 100.6 s, in 2,802 / out 4,210 tokens, 84 rows
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

- Status: **failed**, 3 call(s), 175.2 s, in 7,371 / out 7,230 tokens
- Part `endpoints` (534 words): **ok**, 1 call(s), 90.2 s, in 2,628 / out 3,796 tokens, 76 rows
- Part `quotas` (101 words): **failed**, 2 call(s), 85.0 s, in 4,743 / out 3,434 tokens, —

#### Error

```text
[quotas]
- endpoints.0.endpoint: Value error, not a single hostname (broken by a line wrap?): 'kinesis.<Region>.amazonaws.com'
- endpoints.1.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.amazonaws.com'
- endpoints.2.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.api.aws'
- endpoints.3.endpoint: Value error, not a single hostname (broken by a line wrap?): 'kinesis.<Region>.amazonaws.com'
- endpoints.4.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.amazonaws.com'
- endpoints.5.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.api.aws'
- endpoints.6.endpoint: Value error, not a single hostname (broken by a line wrap?): 'kinesis.<Region>.amazonaws.com'
- endpoints.7.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.amazonaws.com'
- endpoints.8.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.api.aws'
- endpoints.9.endpoint: Value error, not a single hostname (broken by a line wrap?): 'kinesis.<Region>.amazonaws.com'
- endpoints.10.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.amazonaws.com'
- endpoints.11.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.api.aws'
- endpoints.12.endpoint: Value error, not a single hostname (broken by a line wrap?): 'kinesis.<Region>.amazonaws.com'
- endpoints.13.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.amazonaws.com'
- endpoints.14.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.api.aws'
- endpoints.15.endpoint: Value error, not a single hostname (broken by a line wrap?): 'kinesis.<Region>.amazonaws.com'
- endpoints.16.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.amazonaws.com'
- endpoints.17.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.api.aws'
- endpoints.18.endpoint: Value error, not a single hostname (broken by a line wrap?): 'kinesis.<Region>.amazonaws.com'
- endpoints.19.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.amazonaws.com'
- endpoints.20.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.api.aws'
- endpoints.21.endpoint: Value error, not a single hostname (broken by a line wrap?): 'kinesis.<Region>.amazonaws.com'
- endpoints.22.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.amazonaws.com'
- endpoints.23.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.api.aws'
- endpoints.24.endpoint: Value error, not a single hostname (broken by a line wrap?): 'kinesis.<Region>.amazonaws.com'
- endpoints.25.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.amazonaws.com'
- endpoints.26.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.api.aws'
- endpoints.27.endpoint: Value error, not a single hostname (broken by a line wrap?): 'kinesis.<Region>.amazonaws.com'
- endpoints.28.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.amazonaws.com'
- endpoints.29.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.<Region>.api.aws'
--- after repair:
- endpoints.1.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.us-east-1.amazonaws.com'
- endpoints.2.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.us-east-1.api.aws'
- endpoints.4.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.us-east-2.amazonaws.com'
- endpoints.5.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.us-east-2.api.aws'
- endpoints.7.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.us-west-2.amazonaws.com'
- endpoints.8.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.us-west-2.api.aws'
- endpoints.10.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.ap-northeast-1.amazonaws.com'
- endpoints.11.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.ap-northeast-1.api.aws'
- endpoints.13.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.ap-south-1.amazonaws.com'
- endpoints.14.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.ap-south-1.api.aws'
- endpoints.16.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.ap-southeast-1.amazonaws.com'
- endpoints.17.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.ap-southeast-1.api.aws'
- endpoints.19.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.ap-southeast-2.amazonaws.com'
- endpoints.20.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.ap-southeast-2.api.aws'
- endpoints.22.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.eu-central-1.amazonaws.com'
- endpoints.23.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.eu-central-1.api.aws'
- endpoints.25.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.eu-west-1.amazonaws.com'
- endpoints.26.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.eu-west-1.api.aws'
- endpoints.28.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.eu-west-3.amazonaws.com'
- endpoints.29.endpoint: Value error, not a single hostname (broken by a line wrap?): '*.control-kinesis.eu-west-3.api.aws'
```

### 007-amazon-bedrock-agentcore.pdf

- Status: **ok**, 1 call(s), 53.9 s, in 2,446 / out 2,129 tokens
- Part `endpoints` (560 words): **ok**, 1 call(s), 53.9 s, in 2,446 / out 2,129 tokens, 39 rows
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

- Status: **failed**, 2 call(s), 660.7 s, in 4,928 / out 26,237 tokens
- Part `endpoints` (711 words): **ok**, 1 call(s), 200.6 s, in 3,968 / out 7,805 tokens, 155 rows
- Part `quotas` (141 words): **failed**, 1 call(s), 460.1 s, in 960 / out 18,432 tokens, —

#### Error

```text
[quotas]
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 2479 column 18
--- no repair call
```

### 055-aws-app-mesh.pdf

- Status: **ok**, 2 call(s), 129.1 s, in 4,498 / out 5,051 tokens
- Part `endpoints` (688 words): **ok**, 1 call(s), 117.4 s, in 3,566 / out 4,566 tokens, 89 rows
- Part `quotas` (105 words): **ok**, 1 call(s), 11.7 s, in 932 / out 485 tokens, 5 rows, 4 ignored of the other kind
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

- Status: **failed**, 3 call(s), 298.0 s, in 13,535 / out 11,296 tokens
- Part `endpoints` (547 words): **failed**, 2 call(s), 286.8 s, in 11,989 / out 10,855 tokens, —
- Part `quotas` (402 words): **ok**, 1 call(s), 11.2 s, in 1,546 / out 441 tokens, 0 rows, 8 ignored of the other kind

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

- Status: **repaired**, 3 call(s), 133.3 s, in 6,585 / out 5,590 tokens
- Part `endpoints` (791 words): **ok**, 1 call(s), 92.9 s, in 3,273 / out 3,846 tokens, 76 rows
- Part `quotas` (241 words): **repaired**, 2 call(s), 40.5 s, in 3,312 / out 1,744 tokens, 1 rows, 16 ignored of the other kind
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

- Status: **ok**, 2 call(s), 138.6 s, in 4,493 / out 5,795 tokens
- Part `endpoints` (767 words): **ok**, 1 call(s), 104.2 s, in 3,338 / out 4,260 tokens, 84 rows
- Part `quotas` (243 words): **ok**, 1 call(s), 34.4 s, in 1,155 / out 1,535 tokens, 9 rows, 20 ignored of the other kind
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

- Status: **failed**, 2 call(s), 520.2 s, in 5,188 / out 20,152 tokens
- Part `endpoints` (758 words): **ok**, 1 call(s), 44.0 s, in 3,164 / out 1,720 tokens, 36 rows
- Part `quotas` (713 words): **failed**, 1 call(s), 476.2 s, in 2,024 / out 18,432 tokens, —

#### Error

```text
[quotas]
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 2354 column 31
--- no repair call
```

### 075-aws-glue.pdf

- Status: **failed**, 3 call(s), 305.6 s, in 12,712 / out 11,931 tokens
- Part `endpoints` (542 words): **ok**, 1 call(s), 96.9 s, in 2,638 / out 3,910 tokens, 78 rows
- Part `quotas` (1,094 words): **failed**, 2 call(s), 208.7 s, in 10,074 / out 8,021 tokens, —

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

- Status: **failed**, 3 call(s), 571.8 s, in 25,289 / out 19,209 tokens
- Part `endpoints` (1,724 words): **failed**, 2 call(s), 549.3 s, in 24,506 / out 18,237 tokens, —
- Part `quotas` (27 words): **ok**, 1 call(s), 22.5 s, in 783 / out 972 tokens, 0 rows, 16 ignored of the other kind

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

- Status: **failed**, 2 call(s), 563.7 s, in 6,495 / out 21,100 tokens
- Part `endpoints` (980 words): **failed**, 1 call(s), 498.5 s, in 4,381 / out 18,432 tokens, —
- Part `quotas` (753 words): **ok**, 1 call(s), 65.2 s, in 2,114 / out 2,668 tokens, 26 rows, 22 ignored of the other kind

#### Error

```text
[endpoints]
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 2337 column 54
--- no repair call
```

### 048-amazon-simple-queue-service.pdf

- Status: **repaired**, 3 call(s), 239.2 s, in 10,049 / out 9,378 tokens
- Part `endpoints` (968 words): **ok**, 1 call(s), 104.2 s, in 3,955 / out 4,061 tokens, 80 rows
- Part `quotas` (464 words): **repaired**, 2 call(s), 135.0 s, in 6,094 / out 5,317 tokens, 18 rows, 32 ignored of the other kind
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

- Status: **repaired**, 3 call(s), 330.7 s, in 14,103 / out 12,884 tokens
- Part `endpoints` (736 words): **ok**, 1 call(s), 86.3 s, in 3,106 / out 3,524 tokens, 71 rows
- Part `quotas` (926 words): **repaired**, 2 call(s), 244.4 s, in 10,997 / out 9,360 tokens, 0 rows, 80 ignored of the other kind
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

- Status: **failed**, 3 call(s), 175.6 s, in 9,317 / out 7,209 tokens
- Part `endpoints` (533 words): **ok**, 1 call(s), 93.3 s, in 2,574 / out 3,910 tokens, 80 rows
- Part `quotas` (745 words): **failed**, 2 call(s), 82.3 s, in 6,743 / out 3,299 tokens, —

#### Error

```text
[quotas]
- endpoints.0.region_code: Value error, not an AWS Region code like us-east-2: 'Each supported Region'
- endpoints.0.endpoint: Value error, not a single hostname (broken by a line wrap?): 'Each supported Region: 100'
--- after repair:
- endpoints.0.region_code: Value error, not an AWS Region code like us-east-2: 'Each supported Region'
- endpoints.0.endpoint: Value error, not a single hostname (broken by a line wrap?): 'Each supported Region: 100'
```

### 092-aws-secrets-manager.pdf

- Status: **failed**, 4 call(s), 415.4 s, in 19,972 / out 15,880 tokens
- Part `endpoints` (713 words): **failed**, 2 call(s), 294.3 s, in 13,750 / out 10,825 tokens, —
- Part `quotas` (510 words): **failed**, 2 call(s), 121.1 s, in 6,222 / out 5,055 tokens, —

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

- Status: **ok**, 2 call(s), 84.9 s, in 5,097 / out 3,473 tokens
- Part `endpoints` (854 words): **ok**, 1 call(s), 48.3 s, in 3,337 / out 1,886 tokens, 38 rows
- Part `quotas` (613 words): **ok**, 1 call(s), 36.6 s, in 1,760 / out 1,587 tokens, 13 rows, 17 ignored of the other kind
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
