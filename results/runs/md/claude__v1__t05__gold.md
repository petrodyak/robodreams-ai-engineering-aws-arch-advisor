# Run `claude__v1__t05__gold`

Generated from the JSONL run file by `src/extract/report_md.py`; do not edit.

- Model: `claude-haiku-4-5`
- Prompt version: `v1` (file sha `8a0da697aa92`)
- Schema sha: `e707d2e9616f`; validation version `1`
- Sampling: `t05` (temperature 0.5, top_p None)
- Documents: 10

## Summary

| # | Document | Group | Status | Calls | Latency, s | In tokens | Out tokens | Quota table | Endpoints | Quotas |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [006-amazon-aurora-dsql.pdf](#006-amazon-aurora-dsqlpdf) | short | ok | 1 | 16.1 | 3,601 | 1,454 | standard | 25 | 4 |
| 2 | [076-aws-glue-databrew.pdf](#076-aws-glue-databrewpdf) | short | ok | 1 | 12.1 | 3,568 | 1,546 | standard | 24 | 7 |
| 3 | [085-aws-lake-formation.pdf](#085-aws-lake-formationpdf) | short | ok | 1 | 30.8 | 4,988 | 4,481 | none | 88 | 0 |
| 4 | [033-amazon-kinesis-data-streams.pdf](#033-amazon-kinesis-data-streamspdf) | short | ok | 1 | 28.9 | 5,097 | 4,125 | standard | 80 | 1 |
| 5 | [007-amazon-bedrock-agentcore.pdf](#007-amazon-bedrock-agentcorepdf) | short | ok | 1 | 16.2 | 4,462 | 2,236 | none | 39 | 0 |
| 6 | [066-aws-datasync.pdf](#066-aws-datasyncpdf) | short | ok | 1 | 30.3 | 5,896 | 4,395 | non_standard | 88 | 0 |
| 7 | [005-amazon-aurora.pdf](#005-amazon-aurorapdf) | medium | ok | 1 | 24.0 | 6,951 | 3,091 | standard | 36 | 25 |
| 8 | [075-aws-glue.pdf](#075-aws-gluepdf) | medium | ok | 1 | 49.1 | 7,439 | 6,647 | standard | 88 | 46 |
| 9 | [048-amazon-simple-queue-service.pdf](#048-amazon-simple-queue-servicepdf) | medium | ok | 1 | 38.0 | 8,102 | 5,317 | standard | 84 | 19 |
| 10 | [038-amazon-opensearch-service.pdf](#038-amazon-opensearch-servicepdf) | edge | ok | 1 | 60.9 | 10,864 | 9,074 | non_standard | 183 | 0 |

## Documents

### 006-amazon-aurora-dsql.pdf

- Status: **ok**, 1 call(s), 16.1 s, in 3,601 / out 1,454 tokens
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
| Canada West (Calgary) | ca-west-1 | dsql.ca-west-1.api.aws | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | dsql-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
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

- Status: **ok**, 1 call(s), 12.1 s, in 3,568 / out 1,546 tokens
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

- Status: **ok**, 1 call(s), 30.8 s, in 4,988 / out 4,481 tokens
- Service: AWS Lake Formation; quota table format: `none`

#### Endpoints (88)

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
| US West (N. California) | us-west-1 | lakeformation.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | lakeformation-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | lakeformation-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | lakeformation.us-west-1.api.aws | HTTPS | dual_stack |
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
| Canada West (Calgary) | ca-west-1 | lakeformation.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | lakeformation-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | lakeformation-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | lakeformation.ca-west-1.api.aws | HTTPS | dual_stack |
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

- Status: **ok**, 1 call(s), 28.9 s, in 5,097 / out 4,125 tokens
- Service: Amazon Kinesis Data Streams; quota table format: `standard`

#### Endpoints (80)

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
| US West (N. California) | us-west-1 | kinesis.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | kinesis-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | kinesis-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | kinesis.us-west-1.api.aws | HTTPS | dual_stack |
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
| Canada West (Calgary) | ca-west-1 | kinesis.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | kinesis.ca-west-1.api.aws | HTTPS | dual_stack |
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

- Status: **ok**, 1 call(s), 16.2 s, in 4,462 / out 2,236 tokens
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
| US West (N. California) | us-west-1 | gatewayId.gateway.bedrock-agentcore.us-west-1.amazonaws.com | HTTPS | ipv4 |
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

### 066-aws-datasync.pdf

- Status: **ok**, 1 call(s), 30.3 s, in 5,896 / out 4,395 tokens
- Service: AWS DataSync; quota table format: `non_standard`

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
| US West (N. California) | us-west-1 | datasync.us-west-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | datasync-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | datasync-fips.us-west-1.amazonaws.com | HTTPS | fips |
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
| Canada West (Calgary) | ca-west-1 | datasync.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | datasync.ca-west-1.api.aws | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | datasync-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | datasync-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
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
| AWS GovCloud (US-West) | us-gov-west-1 | datasync-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | datasync-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | datasync.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (0)

_none_

### 005-amazon-aurora.pdf

- Status: **ok**, 1 call(s), 24.0 s, in 6,951 / out 3,091 tokens
- Service: Amazon Aurora; quota table format: `standard`

#### Endpoints (36)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | rds.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | rds.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | rds.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | rds.us-west-2.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | rds.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | rds.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | rds.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | rds.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | rds.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | rds.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | rds.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | rds.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | rds.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | rds.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | rds.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | rds.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | rds.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | rds.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | rds.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | rds.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | rds.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | rds.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | rds.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | rds.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | rds.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | rds.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | rds.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | rds.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | rds.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | rds.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | rds.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | rds.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | rds.me-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | rds.sa-east-1.amazonaws.com | HTTPS | ipv4 |
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
| Read replicas per primary | Each supported Region: 15 | Yes | The maximum number of read replicas per primary DB instance. This quota cant be adjusted for Amazon Aurora. |
| Reserved DB instances | ap-south-1: 20; Each of the other supported Regions: 40 | Yes | The maximum number of reserved DB instances allowed in this account in the current AWS Region |

### 075-aws-glue.pdf

- Status: **ok**, 1 call(s), 49.1 s, in 7,439 / out 6,647 tokens
- Service: AWS Glue; quota table format: `standard`

#### Endpoints (88)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | glue.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | glue-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | glue-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | glue.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | glue.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | glue-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | glue-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | glue.us-east-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | glue.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | glue-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | glue-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | glue.us-west-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | glue.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | glue-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | glue-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | glue.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | glue.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | glue.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | glue.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | glue.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | glue.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | glue.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | glue.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | glue.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | glue.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | glue.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | glue.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | glue.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | glue.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | glue.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | glue.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | glue.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | glue.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | glue.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | glue.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | glue.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | glue.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | glue.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | glue.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | glue.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | glue.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | glue.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | glue.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | glue.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | glue.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | glue.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | glue.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | glue-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | glue-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | glue.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | glue.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | glue-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | glue-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | glue.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | glue.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | glue.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | glue.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | glue.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | glue.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | glue.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | glue.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | glue.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | glue.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | glue.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | glue.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | glue.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | glue.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | glue.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | glue.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | glue.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | glue.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | glue.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | glue.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | glue.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | glue.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | glue.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | glue.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | glue.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | glue.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | glue.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | glue.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | glue-fips.us-gov-east-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | glue-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | glue.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | glue.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | glue-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | glue-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | glue.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (46)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Concurrent compute capacity for Ray worker instances in M-DPUs per account. | Each supported Region: 50 | No | The maximum number of data processing units that can be concurrently used by Ray jobs or interactive sessions in this account. The capacity provided by a Ray worker instance type is measured in memory optimized data processing units (M-DPUs). |
| Concurrent machine learning task runs per transform | Each supported Region: 3 | Yes | The maximum number of concurrent task runs per machine learning transform for this account. |
| Global max tags | Each supported Region: 10,000 | Yes | Catalog: global max tags |
| Global maximum administrators | Each supported Region: 100 | Yes | Catalog: global maximum administrators |
| Global maximum paths | Each supported Region: 30,000 | Yes | Catalog: global maximum paths |
| Global s3 path max length | Each supported Region: 2,000 | Yes | Catalog: global s3 path max length |
| Label file size | Each supported Region: 10 Megabytes | Yes | The maximum file size of an individual label file that can be imported. |
| Max DPUs per dev endpoint | Each supported Region: 50 | Yes | The maximum number of DPUs in your development endpoint. |
| Max Named Tag Expressions | Each supported Region: 25,000 | Yes | The maximum number of named tag expression allowed per account |
| Max concurrent data quality ruleset evaluation runs per account | Each supported Region: 50 | Yes | The maximum number of concurrent data quality ruleset evaluation runs in your account. |
| Max concurrent data quality ruleset recommendation runs per account | Each supported Region: 25 | Yes | The maximum number of concurrent data quality ruleset recommendation runs in your account. |
| Max concurrent job runs per account | Each supported Region: 2,000 | Yes | The maximum number of concurrent job runs in your account. |
| Max concurrent job runs per job | Each supported Region: 4,000 | Yes | The maximum number of concurrent job runs for a job. |
| Max concurrent observations generation runs per account | Each supported Region: 10 | Yes | The maximum number of concurrent observations generation runs |
| Max connection per account | Each supported Region: 1,000 | Yes | The maximum number of connections in your account. |
| Max data quality rulesets per account | Each supported Region: 1,000,000 | Yes | The maximum number of data quality rulesets per account. |
| Max databases per account | Each supported Region: 10,000 | Yes | The maximum number of databases in your account. |
| Max databases per catalog | Each supported Region: 10,000 | Yes | The maximum number of databases per catalog. |
| Max development endpoint per account | Each supported Region: 25 | Yes | The maximum number of development endpoints in your account. |
| Max functions per account | Each supported Region: 100 | Yes | The maximum number of functions in your account. |
| Max functions per database | Each supported Region: 100 | Yes | The maximum number of functions per database. |
| Max jobs per account | Each supported Region: 2,000 | Yes | The maximum number of jobs in your account. |
| Max jobs per trigger | Each supported Region: 50 | Yes | The maximum number of jobs that a trigger can start. |
| Max partitions per account | Each supported Region: 20,000,000 | Yes | The maximum number of partitions in your account. |
| Max partitions per table | Each supported Region: 10,000,000 | Yes | The maximum number of partitions per table. |
| Max security configurations per account | Each supported Region: 250 | Yes | The maximum number of security configurations in your account. |
| Max spare compute capacity consumed in data processing units (DPUs) per account. | Each supported Region: 4,000 | Yes | The maximum spare compute capacity in data processing units (DPUs) you can use concurrently in your account. |
| Max table versions per account | Each supported Region: 1,000,000 | Yes | The maximum number of table versions in your account. |
| Max table versions per table | Each supported Region: 100,000 | Yes | The maximum number of table versions per table. |
| Max tables per account | Each supported Region: 1,000,000 | Yes | The maximum number of tables in your account. |
| Max tables per database | Each supported Region: 200,000 | Yes | The maximum number of tables per database. |
| Max task DPUs per account | us-east-1: 1,000; us-east-2: 1,000; us-west-2: 1,000; ap-northeast-1: 1,000; ap-southeast-2: 1,000; eu-west-1: 1,000; Each of the other supported Regions: 500 | Yes | The maximum compute capacity in data processing units (DPUs) you can use concurrently in your account. |
| Max triggers per account | Each supported Region: 1,000 | Yes | The maximum number of triggers in your account. |
| Maximum number of in-flight completion requests allowed per account | Each supported Region: 10 | Yes | The maximum number of concurrent generative AI completion requests allowed per account in the current Region. These requests are used for code generation and Spark troubleshooting in AWS Glue. |
| Maximum number of queued job runs | Each supported Region: 1,000 | Yes | Orchestration: maximum number of queued job runs |
| Number of Schema Registries. | Each supported Region: 100 | No | The maximum number of Schema Registries per AWS Region for this account. |
| Number of Schema Versions. | Each supported Region: 10,000 | No | The maximum number of Schema Versions per AWS Region for this account. |
| Number of column statistics tasks running concurrently per account | Each supported Region: 50 | Yes | The maximum number of column statistics tasks running concurrently in your account. |
| Number of connection types | Each supported Region: 1,000 | Yes | The maximum number of connection types per AWS Region for this account. |
| Number of crawlers per account | Each supported Region: 1,000 | Yes | The maximum number of crawlers in your account. |
| Number of crawlers running concurrently per account | Each supported Region: 150 | Yes | The maximum number of crawlers running concurrently in your account. |
| Number of integrations | Each supported Region: 40 | Yes | The maximum number of integrations per AWS Region for this account. |
| Number of machine learning transforms | Each supported Region: 100 | Yes | The maximum number of machine learning transforms for this account. |
| Number of metadata key value pairs per Schema Version. | Each supported Region: 10 | No | The maximum number of Schema Version metadata key value pairs per Schema Version. |
| Number of workflows | Each supported Region: 1,000 | Yes | The maximum number of workflows in your account. |
| The maximum number of concurrent materialized view refresh task runs. | Each supported Region: 50 | Yes | The maximum number of concurrent materialized view refresh task runs. |

### 048-amazon-simple-queue-service.pdf

- Status: **ok**, 1 call(s), 38.0 s, in 8,102 / out 5,317 tokens
- Service: Amazon Simple Queue Service; quota table format: `standard`

#### Endpoints (84)

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
| US West (N. California) | us-west-1 | sqs.us-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| US West (N. California) | us-west-1 | sqs-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | sqs-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | sqs.us-west-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | sqs.us-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | sqs-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | sqs-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | sqs.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | sqs.af-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | sqs.af-south-1.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | sqs.ap-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | sqs.ap-east-1.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | sqs.ap-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | sqs.ap-south-2.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | sqs.ap-southeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | sqs.ap-southeast-3.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | sqs.ap-southeast-5.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | sqs.ap-southeast-5.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | sqs.ap-southeast-4.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | sqs.ap-southeast-4.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | sqs.ap-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | sqs.ap-south-1.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | sqs.ap-southeast-6.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | sqs.ap-southeast-6.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | sqs.ap-northeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | sqs.ap-northeast-3.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | sqs.ap-northeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | sqs.ap-northeast-2.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | sqs.ap-southeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | sqs.ap-southeast-1.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | sqs.ap-southeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | sqs.ap-southeast-2.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | sqs.ap-east-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | sqs.ap-east-2.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | sqs.ap-southeast-7.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | sqs.ap-southeast-7.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | sqs.ap-northeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | sqs.ap-northeast-1.api.aws | HTTP and HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | sqs.ca-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | sqs-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | sqs-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | sqs.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | sqs.ca-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | sqs-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | sqs-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | sqs.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | sqs.eu-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | sqs.eu-central-1.api.aws | HTTP and HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | sqs.eu-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | sqs.eu-west-1.api.aws | HTTP and HTTPS | dual_stack |
| Europe (London) | eu-west-2 | sqs.eu-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (London) | eu-west-2 | sqs.eu-west-2.api.aws | HTTP and HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | sqs.eu-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | sqs.eu-south-1.api.aws | HTTP and HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | sqs.eu-west-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | sqs.eu-west-3.api.aws | HTTP and HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | sqs.eu-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | sqs.eu-south-2.api.aws | HTTP and HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | sqs.eu-north-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | sqs.eu-north-1.api.aws | HTTP and HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | sqs.eu-central-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | sqs.eu-central-2.api.aws | HTTP and HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | sqs.il-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | sqs.il-central-1.api.aws | HTTP and HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | sqs.mx-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | sqs.mx-central-1.api.aws | HTTP and HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | sqs.me-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | sqs.me-south-1.api.aws | HTTP and HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | sqs.me-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | sqs.me-central-1.api.aws | HTTP and HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | sqs.sa-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | sqs.sa-east-1.api.aws | HTTP and HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | sqs.us-gov-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | sqs.us-gov-east-1.api.aws | HTTP and HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | sqs.us-gov-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | sqs.us-gov-west-1.api.aws | HTTP and HTTPS | dual_stack |

#### Quotas (19)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Actions per Queue Policy | Each supported Region: 7 | No | The number of actions in a queue policy. |
| Attributes per Message | Each supported Region: 10 | No | The number of attributes added to a message. |
| Batched Message ID Length | Each supported Region: 80 | No | The length of a batched message ID. |
| Batched Message Throughput for FIFO Queues | Each supported Region: 3,000 | No | The number of batched transactions per second (TPS) for FIFO queues. |
| Batched Message High Throughput for FIFO Queues | Supported Regions (US East (N. Virginia), US West (Oregon), and Europe (Ireland)): 700,000; Europe (Frankfurt) and US East (Ohio): 180,000; Asia Pacific (Mumbai), Asia Pacific (Singapore), Asia Pacific (Sydney) and Asia Pacific (Tokyo): 90,000; Europe (London) and South America (São Paulo): 45,000; All other supported Regions: 24,000 | No | The number of batched transactions per second (TPS) for FIFO queues. |
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

### 038-amazon-opensearch-service.pdf

- Status: **ok**, 1 call(s), 60.9 s, in 10,864 / out 9,074 tokens
- Service: Amazon OpenSearch Service; quota table format: `non_standard`

#### Endpoints (183)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | es.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | es-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | aos.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | es.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | es-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | aos.us-east-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | es.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | es-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | aos.us-west-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | es.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | es-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | aos.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | es.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | aos.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | es.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | aos.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | es.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | aos.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | es.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | aos.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | es.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | aos.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | es.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | aos.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | es.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | aos.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | es.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | aos.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | es.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | aos.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | es.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | aos.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | es.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | aos.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | es.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | aos.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | es.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | aos.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | es.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | aos.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | es.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | aos.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | es.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | aos.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | es.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | aos.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | es.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | aos.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | es.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | aos.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | es.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | aos.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | es.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | aos.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | es.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | aos.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | es.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | aos.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | es.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | aos.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | es.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | aos.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | es.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | aos.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | es.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | aos.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | es.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | aos.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | es.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | aos.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | es.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | aos.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | es.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | es-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | aos.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | es.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | es-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | aos.us-gov-west-1.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | aoss.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | dashboards.us-east-2.aoss-fips.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | us-east-2.aoss.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | dashboards.us-east-2.aoss.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | us-east-2.aoss-fips.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | aoss.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | us-east-1.aoss.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | dashboards.us-east-1.aoss.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | dashboards.us-east-1.aoss-fips.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | us-east-1.aoss-fips.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | aoss.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | dashboards.us-west-1.aoss-fips.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | dashboards.us-west-1.aoss.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | us-west-1.aoss.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | us-west-1.aoss-fips.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | aoss.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | dashboards.us-west-2.aoss-fips.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | dashboards.us-west-2.aoss.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | us-west-2.aoss.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | us-west-2.aoss-fips.amazonaws.com | HTTPS | fips |
| Asia Pacific (Hong Kong) | ap-east-1 | aoss.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | ap-east-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | dashboards.ap-east-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | aoss.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | dashboards.ap-south-2.aoss.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | ap-south-2.aoss.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | aoss.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | dashboards.ap-south-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | ap-south-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | aoss.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | ap-northeast-3.aoss.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | dashboards.ap-northeast-3.aoss.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | aoss.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | dashboards.ap-northeast-2.aoss.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | ap-northeast-2.aoss.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | aoss.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | dashboards.ap-southeast-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | ap-southeast-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | aoss.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | dashboards.ap-southeast-2.aoss.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | ap-southeast-2.aoss.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | aoss.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | dashboards.ap-northeast-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | ap-northeast-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | aoss.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | ca-central-1.aoss-fips.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | dashboards.ca-central-1.aoss-fips.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | dashboards.ca-central-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | ca-central-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | aoss.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | dashboards.eu-central-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | eu-central-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | aoss.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | eu-west-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | dashboards.eu-west-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | aoss.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | eu-west-2.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | dashboards.eu-west-2.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | aoss.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | eu-south-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | dashboards.eu-south-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | aoss.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | eu-west-3.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | dashboards.eu-west-3.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | aoss.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | dashboards.eu-south-2.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | eu-south-2.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | aoss.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | eu-north-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | dashboards.eu-north-1.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | aoss.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | eu-central-2.aoss.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | dashboards.eu-central-2.aoss.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | aoss.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | sa-east-1.aoss.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | dashboards.sa-east-1.aoss.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | aoss.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | us-gov-east-1.aoss-fips.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | dashboards.us-gov-east-1.aoss-fips.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | us-gov-east-1.aoss.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | dashboards.us-gov-east-1.aoss.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | aoss.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | dashboards.us-gov-west-1.aoss.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | us-gov-west-1.aoss-fips.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | us-gov-west-1.aoss.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | dashboards.us-gov-west-1.aoss-fips.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | osis.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | osis.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | osis.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | osis.us-west-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | osis.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | osis.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | osis.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | osis.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | osis.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | osis.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | osis.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | osis.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | osis.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | osis.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | osis.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | osis.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | osis.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | osis.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | osis.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (0)

_none_
