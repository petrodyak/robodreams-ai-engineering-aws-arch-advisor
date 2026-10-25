# Run `qwen2.5-7b__v1__t05__gold`

Generated from the JSONL run file by `src/extract/report_md.py`; do not edit.

- Model: `qwen2.5:7b`
- Prompt version: `v1` (file sha `8a0da697aa92`)
- Schema sha: `e707d2e9616f`; validation version `1`
- Sampling: `t05` (temperature 0.5, top_p None)
- Documents: 10

## Summary

| # | Document | Group | Status | Calls | Latency, s | In tokens | Out tokens | Quota table | Endpoints | Quotas |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [006-amazon-aurora-dsql.pdf](#006-amazon-aurora-dsqlpdf) | short | repaired | 2 | 70.6 | 5,182 | 2,983 | standard | 25 | 4 |
| 2 | [076-aws-glue-databrew.pdf](#076-aws-glue-databrewpdf) | short | repaired | 2 | 79.1 | 5,311 | 3,277 | standard | 24 | 7 |
| 3 | [085-aws-lake-formation.pdf](#085-aws-lake-formationpdf) | short | repaired | 2 | 204.7 | 9,727 | 8,421 | none | 84 | 0 |
| 4 | [033-amazon-kinesis-data-streams.pdf](#033-amazon-kinesis-data-streamspdf) | short | repaired | 2 | 194.2 | 9,863 | 7,981 | standard | 76 | 1 |
| 5 | [007-amazon-bedrock-agentcore.pdf](#007-amazon-bedrock-agentcorepdf) | short | repaired | 2 | 104.4 | 7,302 | 4,415 | none | 42 | 0 |
| 6 | [066-aws-datasync.pdf](#066-aws-datasyncpdf) | short | repaired | 2 | 195.5 | 11,223 | 7,636 | standard | 88 | 4 |
| 7 | [005-amazon-aurora.pdf](#005-amazon-aurorapdf) | medium | repaired | 2 | 159.2 | 11,795 | 6,289 | standard | 35 | 25 |
| 8 | [075-aws-glue.pdf](#075-aws-gluepdf) | medium | failed | 2 | 324.3 | 15,743 | 11,938 | — | — | — |
| 9 | [048-amazon-simple-queue-service.pdf](#048-amazon-simple-queue-servicepdf) | medium | failed | 2 | 368.7 | 17,949 | 12,842 | — | — | — |
| 10 | [038-amazon-opensearch-service.pdf](#038-amazon-opensearch-servicepdf) | edge | failed | 1 | 494.4 | 6,933 | 18,432 | — | — | — |

## Documents

### 006-amazon-aurora-dsql.pdf

- Status: **repaired**, 2 call(s), 70.6 s, in 5,182 / out 2,983 tokens
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

#### First answer rejected (repaired)

```text
- schema_version: Input should be '1'
```

### 076-aws-glue-databrew.pdf

- Status: **repaired**, 2 call(s), 79.1 s, in 5,311 / out 3,277 tokens
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
- schema_version: Input should be '1'
```

### 085-aws-lake-formation.pdf

- Status: **repaired**, 2 call(s), 204.7 s, in 9,727 / out 8,421 tokens
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

#### First answer rejected (repaired)

```text
- schema_version: Input should be '1'
```

### 033-amazon-kinesis-data-streams.pdf

- Status: **repaired**, 2 call(s), 194.2 s, in 9,863 / out 7,981 tokens
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

#### First answer rejected (repaired)

```text
- schema_version: Input should be '1'
```

### 007-amazon-bedrock-agentcore.pdf

- Status: **repaired**, 2 call(s), 104.4 s, in 7,302 / out 4,415 tokens
- Service: Amazon Bedrock AgentCore; quota table format: `none`

#### Endpoints (42)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (N. Virginia) | us-east-1 | bedrock-agentcore-control.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | bedrock-agentcore.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | bedrock-agentcore-control.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | bedrock-agentcore.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | bedrock-agentcore-control.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | bedrock-agentcore.us-west-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | bedrock-agentcore-control.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | bedrock-agentcore.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | bedrock-agentcore-control.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | bedrock-agentcore.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | bedrock-agentcore-control.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | bedrock-agentcore.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | bedrock-agentcore-control.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | bedrock-agentcore.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | bedrock-agentcore-control.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | bedrock-agentcore.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | bedrock-agentcore-control.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | bedrock-agentcore.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| US West (California) | us-west-1 | bedrock-agentcore-control.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (California) | us-west-1 | bedrock-agentcore.us-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | bedrock-agentcore-control.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | bedrock-agentcore.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | bedrock-agentcore-control.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | bedrock-agentcore.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | bedrock-agentcore-control.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | bedrock-agentcore.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | bedrock-agentcore-control.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | bedrock-agentcore.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | bedrock-agentcore-control.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | bedrock-agentcore.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | bedrock-agentcore-control.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | bedrock-agentcore.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | bedrock-agentcore-control.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | bedrock-agentcore.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | bedrock-agentcore-control.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | bedrock-agentcore.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | bedrock-agentcore-control.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | bedrock-agentcore.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | bedrock-agentcore-control.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | bedrock-agentcore.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | bedrock-agentcore-control.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | bedrock-agentcore.sa-east-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (0)

_none_

#### First answer rejected (repaired)

```text
- schema_version: Input should be '1'
```

### 066-aws-datasync.pdf

- Status: **repaired**, 2 call(s), 195.5 s, in 11,223 / out 7,636 tokens
- Service: AWS DataSync; quota table format: `standard`

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
| AWS GovCloud (US-West) | us-gov-west-1 | datasync-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | datasync-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | datasync.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (4)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Maximum number of tasks you can create | 100 | Yes | The maximum number of DataSync tasks that you can create in a specific AWS account and AWS Region. |
| Maximum number of (Enhanced mode tasks) source and destination objects that DataSync can work with per task execution | Virtually unlimited | No | The maximum number of source and destination objects that DataSync can work with per task execution in Enhanced mode. This quota is virtually unlimited. |
| Maximum number of (Basic mode tasks) source and destination files, objects, and directories that DataSync can work with per task execution between self-managed storage or other clouds and AWS services | 50 million | Yes | The maximum number of source and destination files, objects, and directories that DataSync can work with per task execution in Basic mode between self-managed storage or other clouds and AWS services. Important: If you transfer more than 20 million files, objects, or directories, make sure that you allocate a minimum of 64 GB of RAM to your DataSync agent. For more information, see agent requirements for transfers. Tip: For more information, see Filtering the data transferred by. |
| Maximum number of (Basic mode tasks) source and destination files, objects, and directories that DataSync can work with per task execution between AWS storage services | 25 million | Yes | The maximum number of source and destination files, objects, and directories that DataSync can work with per task execution in Basic mode between AWS storage services. Important: If you transfer more than 20 million files, objects, or directories, make sure that you allocate a minimum of 64 GB of RAM to your DataSync agent. For more information, see agent requirements for transfers. Tip: For more information, see Filtering the data transferred by. |

#### First answer rejected (repaired)

```text
- schema_version: Input should be '1'
- endpoints.0.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.us-east-2.amazonaws.com datasync-fips.us-east-2.api.aws datasync.us-east-2.api.aws datasync-fips.us-east-2.amazonaws.com'
- endpoints.1.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.us-east-1.amazonaws.com datasync-fips.us-east-1.api.aws datasync-fips.us-east-1.amazonaws.com datasync.us-east-1.api.aws'
- endpoints.2.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.us-west-1.amazonaws.com datasync-fips.us-west-1.api.aws datasync-fips.us-west-1.amazonaws.com datasync.us-west-1.api.aws'
- endpoints.3.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.us-west-2.amazonaws.com datasync-fips.us-west-2.api.aws datasync.us-west-2.api.aws datasync-fips.us-west-2.amazonaws.com'
- endpoints.4.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.af-south-1.amazonaws.com datasync.af-south-1.api.aws'
- endpoints.5.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ap-east-1.amazonaws.com datasync.ap-east-1.api.aws'
- endpoints.6.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ap-south-2.amazonaws.com datasync.ap-south-2.api.aws'
- endpoints.7.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ap-southeast-3.amazonaws.com datasync.ap-southeast-3.api.aws'
- endpoints.8.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ap-southeast-5.amazonaws.com datasync.ap-southeast-5.api.aws'
- endpoints.9.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ap-southeast-4.amazonaws.com datasync.ap-southeast-4.api.aws'
- endpoints.10.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ap-south-1.amazonaws.com datasync.ap-south-1.api.aws'
- endpoints.11.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ap-southeast-6.amazonaws.com datasync.ap-southeast-6.api.aws'
- endpoints.12.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ap-northeast-3.amazonaws.com datasync.ap-northeast-3.api.aws'
- endpoints.13.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ap-northeast-2.amazonaws.com datasync.ap-northeast-2.api.aws'
- endpoints.14.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ap-southeast-1.amazonaws.com datasync.ap-southeast-1.api.aws'
- endpoints.15.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ap-southeast-2.amazonaws.com datasync.ap-southeast-2.api.aws'
- endpoints.16.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ap-east-2.amazonaws.com datasync.ap-east-2.api.aws'
- endpoints.17.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ap-southeast-7.amazonaws.com datasync.ap-southeast-7.api.aws'
- endpoints.18.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ap-northeast-1.amazonaws.com datasync.ap-northeast-1.api.aws'
- endpoints.19.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ca-central-1.amazonaws.com datasync.ca-central-1.api.aws datasync-fips.ca-central-1.amazonaws.com datasync-fips.ca-central-1.api.aws'
- endpoints.20.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.ca-west-1.amazonaws.com datasync.ca-west-1.api.aws datasync-fips.ca-west-1.amazonaws.com datasync-fips.ca-west-1.api.aws'
- endpoints.21.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.eu-central-1.amazonaws.com datasync.eu-central-1.api.aws'
- endpoints.22.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.eu-west-1.amazonaws.com datasync.eu-west-1.api.aws'
- endpoints.23.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.eu-west-2.amazonaws.com datasync.eu-west-2.api.aws'
- endpoints.24.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.eu-south-1.amazonaws.com datasync.eu-south-1.api.aws'
- endpoints.25.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.eu-west-3.amazonaws.com datasync.eu-west-3.api.aws'
- endpoints.26.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.eu-south-2.amazonaws.com datasync.eu-south-2.api.aws'
- endpoints.27.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.eu-north-1.amazonaws.com datasync.eu-north-1.api.aws'
- endpoints.28.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.eu-central-2.amazonaws.com datasync.eu-central-2.api.aws'
- endpoints.29.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.il-central-1.amazonaws.com datasync.il-central-1.api.aws'
- endpoints.30.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.mx-central-1.amazonaws.com datasync.mx-central-1.api.aws'
- endpoints.31.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.me-south-1.amazonaws.com datasync.me-south-1.api.aws'
- endpoints.32.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.me-central-1.amazonaws.com datasync.me-central-1.api.aws'
- endpoints.33.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.sa-east-1.amazonaws.com datasync.sa-east-1.api.aws'
- endpoints.34.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.us-gov-east-1.amazonaws.com datasync.us-gov-east-1.api.aws datasync-fips.us-gov-east-1.amazonaws.com datasync-fips.us-gov-east-1.api.aws'
- endpoints.35.endpoint: Value error, not a single hostname (broken by a line wrap?): 'datasync.us-gov-west-1.amazonaws.com datasync-fips.us-gov-west-1.amazonaws.com datasync-fips.us-gov-west-1.api.aws datasync.us-gov-west-1.api.aws'
```

### 005-amazon-aurora.pdf

- Status: **repaired**, 2 call(s), 159.2 s, in 11,795 / out 6,289 tokens
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

#### First answer rejected (repaired)

```text
- schema_version: Input should be '1'
```

### 075-aws-glue.pdf

- Status: **failed**, 2 call(s), 324.3 s, in 15,743 / out 11,938 tokens

#### Error

```text
- schema_version: Input should be '1'
- endpoints.0.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.us-east-2.amazonaws.com glue-fips.us-east-2.api.aws glue-fips.us-east-2.amazonaws.com glue.us-east-2.api.aws'
- endpoints.1.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.us-east-1.amazonaws.com glue-fips.us-east-1.api.aws glue-fips.us-east-1.amazonaws.com glue.us-east-1.api.aws'
- endpoints.2.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.us-west-1.amazonaws.com glue-fips.us-west-1.api.aws glue-fips.us-west-1.amazonaws.com glue.us-west-1.api.aws'
- endpoints.3.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.us-west-2.amazonaws.com glue-fips.us-west-2.api.aws glue-fips.us-west-2.amazonaws.com glue.us-west-2.api.aws'
- endpoints.4.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.af-south-1.amazonaws.com glue.af-south-1.api.aws'
- endpoints.5.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ap-east-1.amazonaws.com glue.ap-east-1.api.aws'
- endpoints.6.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ap-south-2.amazonaws.com glue.ap-south-2.api.aws'
- endpoints.7.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ap-southeast-3.amazonaws.com glue.ap-southeast-3.api.aws'
- endpoints.8.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ap-southeast-5.amazonaws.com glue.ap-southeast-5.api.aws'
- endpoints.9.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ap-southeast-4.amazonaws.com glue.ap-southeast-4.api.aws'
- endpoints.10.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ap-south-1.amazonaws.com glue.ap-south-1.api.aws'
- endpoints.11.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ap-southeast-6.amazonaws.com glue.ap-southeast-6.api.aws'
- endpoints.12.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ap-northeast-3.amazonaws.com glue.ap-northeast-3.api.aws'
- endpoints.13.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ap-northeast-2.amazonaws.com glue.ap-northeast-2.api.aws'
- endpoints.14.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ap-southeast-1.amazonaws.com glue.ap-southeast-1.api.aws'
- endpoints.15.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ap-southeast-2.amazonaws.com glue.ap-southeast-2.api.aws'
- endpoints.16.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ap-east-2.amazonaws.com glue.ap-east-2.api.aws'
- endpoints.17.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ap-southeast-7.amazonaws.com glue.ap-southeast-7.api.aws'
- endpoints.18.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ap-northeast-1.amazonaws.com glue.ap-northeast-1.api.aws'
- endpoints.19.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ca-central-1.amazonaws.com glue-fips.ca-central-1.api.aws glue-fips.ca-central-1.amazonaws.com glue.ca-central-1.api.aws'
- endpoints.20.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.ca-west-1.amazonaws.com glue-fips.ca-west-1.api.aws glue-fips.ca-west-1.amazonaws.com glue.ca-west-1.api.aws'
- endpoints.21.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.eu-central-1.amazonaws.com glue.eu-central-1.api.aws'
- endpoints.22.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.eu-west-1.amazonaws.com glue.eu-west-1.api.aws'
- endpoints.23.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.eu-west-2.amazonaws.com glue.eu-west-2.api.aws'
- endpoints.24.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.eu-south-1.amazonaws.com glue.eu-south-1.api.aws'
- endpoints.25.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.eu-west-3.amazonaws.com glue.eu-west-3.api.aws'
- endpoints.26.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.eu-south-2.amazonaws.com glue.eu-south-2.api.aws'
- endpoints.27.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.eu-north-1.amazonaws.com glue.eu-north-1.api.aws'
- endpoints.28.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.eu-central-2.amazonaws.com glue.eu-central-2.api.aws'
- endpoints.29.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.il-central-1.amazonaws.com glue.il-central-1.api.aws'
- endpoints.30.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.mx-central-1.amazonaws.com glue.mx-central-1.api.aws'
- endpoints.31.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.me-south-1.amazonaws.com glue.me-south-1.api.aws'
- endpoints.32.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.me-central-1.amazonaws.com glue.me-central-1.api.aws'
- endpoints.33.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.sa-east-1.amazonaws.com glue.sa-east-1.api.aws'
- endpoints.34.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.us-gov-east-1.amazonaws.com glue-fips.us-gov-east-1.api.aws glue-fips.us-gov-east-1.amazonaws.com glue.us-gov-east-1.api.aws'
- endpoints.35.endpoint: Value error, not a single hostname (broken by a line wrap?): 'glue.us-gov-west-1.amazonaws.com glue-fips.us-gov-west-1.api.aws glue-fips.us-gov-west-1.amazonaws.com glue.us-gov-west-1.api.aws'
--- after repair:
- schema_version: Input should be '1'
```

### 048-amazon-simple-queue-service.pdf

- Status: **failed**, 2 call(s), 368.7 s, in 17,949 / out 12,842 tokens

#### Error

```text
- schema_version: Input should be '1'
- endpoints.0.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.us-east-2.amazonaws.com sqs-fips.us-east-2.api.aws sqs-fips.us-east-2.amazonaws.com sqs.us-east-2.api.aws'
- endpoints.3.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.us-east-1.amazonaws.com sqs-fips.us-east-1.api.aws sqs-fips.us-east-1.amazonaws.com sqs.us-east-1.api.aws'
- endpoints.6.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.us-west-2.amazonaws.com sqs-fips.us-west-2.api.aws sqs-fips.us-west-2.amazonaws.com sqs.us-west-2.api.aws'
- endpoints.9.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.af-south-1.amazonaws.com sqs.af-south-1.api.aws'
- endpoints.10.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-east-1.amazonaws.com sqs.ap-east-1.api.aws'
- endpoints.11.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-east-1.amazonaws.com sqs.ap-east-1.api.aws'
- endpoints.12.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-south-2.amazonaws.com sqs.ap-south-2.api.aws'
- endpoints.13.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-southeast-3.amazonaws.com sqs.ap-southeast-3.api.aws'
- endpoints.14.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-southeast-5.amazonaws.com sqs.ap-southeast-5.api.aws'
- endpoints.15.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-southeast-4.amazonaws.com sqs.ap-southeast-4.api.aws'
- endpoints.16.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-south-1.amazonaws.com sqs.ap-south-1.api.aws'
- endpoints.17.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-southeast-6.amazonaws.com sqs.ap-southeast-6.api.aws'
- endpoints.18.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-northeast-3.amazonaws.com sqs.ap-northeast-3.api.aws'
- endpoints.19.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-northeast-2.amazonaws.com sqs.ap-northeast-2.api.aws'
- endpoints.20.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-southeast-1.amazonaws.com sqs.ap-southeast-1.api.aws'
- endpoints.21.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-southeast-1.amazonaws.com sqs.ap-southeast-1.api.aws'
- endpoints.22.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-southeast-2.amazonaws.com sqs.ap-southeast-2.api.aws'
- endpoints.23.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-southeast-2.amazonaws.com sqs.ap-southeast-2.api.aws'
- endpoints.24.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-east-2.amazonaws.com sqs.ap-east-2.api.aws'
- endpoints.25.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-southeast-7.amazonaws.com sqs.ap-southeast-7.api.aws'
- endpoints.26.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ap-northeast-1.amazonaws.com sqs.ap-northeast-1.api.aws'
- endpoints.27.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ca-central-1.amazonaws.com sqs-fips.ca-central-1.api.aws sqs-fips.ca-central-1.amazonaws.com sqs.ca-central-1.api.aws'
- endpoints.31.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.ca-west-1.amazonaws.com sqs-fips.ca-west-1.api.aws sqs-fips.ca-west-1.amazonaws.com sqs.ca-west-1.api.aws'
- endpoints.35.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.eu-central-1.amazonaws.com sqs.eu-central-1.api.aws'
- endpoints.36.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.eu-central-1.amazonaws.com sqs.eu-central-1.api.aws'
- endpoints.37.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.eu-west-1.amazonaws.com sqs.eu-west-1.api.aws'
- endpoints.38.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.eu-west-1.amazonaws.com sqs.eu-west-1.api.aws'
- endpoints.39.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.eu-west-2.amazonaws.com sqs.eu-west-2.api.aws'
- endpoints.40.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.eu-west-2.amazonaws.com sqs.eu-west-2.api.aws'
- endpoints.41.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.eu-west-3.amazonaws.com sqs.eu-west-3.api.aws'
- endpoints.42.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.eu-west-3.amazonaws.com sqs.eu-west-3.api.aws'
- endpoints.43.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.eu-south-2.amazonaws.com sqs.eu-south-2.api.aws'
- endpoints.44.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.eu-south-2.amazonaws.com sqs.eu-south-2.api.aws'
- endpoints.45.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.eu-north-1.amazonaws.com sqs.eu-north-1.api.aws'
- endpoints.46.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.eu-north-1.amazonaws.com sqs.eu-north-1.api.aws'
- endpoints.47.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.eu-central-2.amazonaws.com sqs.eu-central-2.api.aws'
- endpoints.48.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.eu-central-2.amazonaws.com sqs.eu-central-2.api.aws'
- endpoints.49.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.il-central-1.amazonaws.com sqs.il-central-1.api.aws'
- endpoints.50.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.il-central-1.amazonaws.com sqs.il-central-1.api.aws'
- endpoints.51.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.mx-central-1.amazonaws.com sqs.mx-central-1.api.aws'
- endpoints.52.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.mx-central-1.amazonaws.com sqs.mx-central-1.api.aws'
- endpoints.53.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.me-south-1.amazonaws.com sqs.me-south-1.api.aws'
- endpoints.54.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.me-south-1.amazonaws.com sqs.me-south-1.api.aws'
- endpoints.55.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.me-central-1.amazonaws.com sqs.me-central-1.api.aws'
- endpoints.56.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.me-central-1.amazonaws.com sqs.me-central-1.api.aws'
- endpoints.57.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.sa-east-1.amazonaws.com sqs.sa-east-1.api.aws'
- endpoints.58.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.sa-east-1.amazonaws.com sqs.sa-east-1.api.aws'
- endpoints.59.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.us-gov-east-1.amazonaws.com sqs.us-gov-east-1.api.aws'
- endpoints.63.endpoint: Value error, not a single hostname (broken by a line wrap?): 'sqs.us-gov-west-1.amazonaws.com sqs.us-gov-west-1.api.aws'
--- after repair:
- schema_version: Input should be '1'
```

### 038-amazon-opensearch-service.pdf

- Status: **failed**, 1 call(s), 494.4 s, in 6,933 / out 18,432 tokens

#### Error

```text
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 1922 column 36
--- no repair call
```
