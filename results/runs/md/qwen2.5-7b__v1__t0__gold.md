# Run `qwen2.5-7b__v1__t0__gold`

Generated from the JSONL run file by `src/extract/report_md.py`; do not edit.

- Model: `qwen2.5:7b`
- Prompt version: `v1` (file sha `8a0da697aa92`)
- Schema sha: `e707d2e9616f`; validation version `1`
- Sampling: `t0` (temperature 0.0, top_p None)
- Documents: 10

## Summary

| # | Document | Group | Status | Calls | Latency, s | In tokens | Out tokens | Quota table | Endpoints | Quotas |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [006-amazon-aurora-dsql.pdf](#006-amazon-aurora-dsqlpdf) | short | repaired | 2 | 68.7 | 5,182 | 2,983 | standard | 25 | 4 |
| 2 | [076-aws-glue-databrew.pdf](#076-aws-glue-databrewpdf) | short | repaired | 2 | 78.4 | 5,311 | 3,277 | standard | 24 | 7 |
| 3 | [085-aws-lake-formation.pdf](#085-aws-lake-formationpdf) | short | repaired | 2 | 214.2 | 9,727 | 8,421 | none | 84 | 0 |
| 4 | [033-amazon-kinesis-data-streams.pdf](#033-amazon-kinesis-data-streamspdf) | short | repaired | 2 | 202.9 | 9,865 | 7,985 | standard | 76 | 1 |
| 5 | [007-amazon-bedrock-agentcore.pdf](#007-amazon-bedrock-agentcorepdf) | short | repaired | 2 | 78.9 | 6,682 | 3,175 | none | 30 | 0 |
| 6 | [066-aws-datasync.pdf](#066-aws-datasyncpdf) | short | repaired | 2 | 192.3 | 11,076 | 7,342 | standard | 88 | 4 |
| 7 | [005-amazon-aurora.pdf](#005-amazon-aurorapdf) | medium | repaired | 2 | 164.4 | 11,795 | 6,289 | standard | 35 | 25 |
| 8 | [075-aws-glue.pdf](#075-aws-gluepdf) | medium | repaired | 2 | 343.8 | 15,612 | 12,663 | standard | 74 | 46 |
| 9 | [048-amazon-simple-queue-service.pdf](#048-amazon-simple-queue-servicepdf) | medium | failed | 1 | 495.3 | 4,761 | 18,432 | — | — | — |
| 10 | [038-amazon-opensearch-service.pdf](#038-amazon-opensearch-servicepdf) | edge | repaired | 2 | 581.9 | 23,665 | 19,489 | standard | 153 | 38 |

## Documents

### 006-amazon-aurora-dsql.pdf

- Status: **repaired**, 2 call(s), 68.7 s, in 5,182 / out 2,983 tokens
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

- Status: **repaired**, 2 call(s), 78.4 s, in 5,311 / out 3,277 tokens
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

- Status: **repaired**, 2 call(s), 214.2 s, in 9,727 / out 8,421 tokens
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

- Status: **repaired**, 2 call(s), 202.9 s, in 9,865 / out 7,985 tokens
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

#### First answer rejected (repaired)

```text
- schema_version: Input should be '1'
```

### 007-amazon-bedrock-agentcore.pdf

- Status: **repaired**, 2 call(s), 78.9 s, in 6,682 / out 3,175 tokens
- Service: Amazon Bedrock AgentCore; quota table format: `none`

#### Endpoints (30)

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
| US West (N. California) | us-west-1 | bedrock-agentcore.us-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | bedrock-agentcore.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | bedrock-agentcore.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | bedrock-agentcore.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | bedrock-agentcore.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | bedrock-agentcore.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | bedrock-agentcore.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | bedrock-agentcore.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | bedrock-agentcore.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | bedrock-agentcore.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | bedrock-agentcore.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | bedrock-agentcore.sa-east-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (0)

_none_

#### First answer rejected (repaired)

```text
- schema_version: Input should be '1'
```

### 066-aws-datasync.pdf

- Status: **repaired**, 2 call(s), 192.3 s, in 11,076 / out 7,342 tokens
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
| Maximum number of tasks you can create | 100 | Yes | The maximum number of DataSync tasks you can create in a specific AWS account and AWS Region. |
| Maximum number of source and destination objects that DataSync can work with per task execution (Enhanced mode tasks) | Virtually unlimited | No | The maximum number of source and destination objects that DataSync can work with per task execution in Enhanced mode. |
| Maximum number of source and destination files, objects, and directories that DataSync can work with per task execution between self-managed storage or other clouds and AWS services (Basic mode tasks) | 50 million | Yes | The maximum number of source and destination files, objects, and directories that DataSync can work with per task execution in Basic mode. |
| Maximum number of source and destination files, objects, and directories that DataSync can work with per task execution between AWS storage services (Basic mode tasks) | 25 million | Yes | The maximum number of source and destination files, objects, and directories that DataSync can work with per task execution in Basic mode. |

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

- Status: **repaired**, 2 call(s), 164.4 s, in 11,795 / out 6,289 tokens
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

- Status: **repaired**, 2 call(s), 343.8 s, in 15,612 / out 12,663 tokens
- Service: AWS Glue; quota table format: `standard`

#### Endpoints (74)

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
| US West (Oregon) | us-west-2 | glue.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | glue-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | glue-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | glue.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | glue.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | glue.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | glue.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | glue.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | glue.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | glue.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | glue.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | glue.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | glue.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | glue.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | glue.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | glue.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | glue.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | glue.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | glue.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | glue.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | glue.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | glue.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | glue.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | glue.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | glue.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | glue-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | glue-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | glue.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | glue.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | glue-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Calgary) | ca-west-1 | glue-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada (Calgary) | ca-west-1 | glue.ca-west-1.api.aws | HTTPS | dual_stack |
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
| Concurrent compute capacity for Ray worker instances in M-DPUs per account | Each supported Region: 50 | No | The maximum number of data processing units that can be concurrently used by Ray jobs or interactive sessions in this account. The capacity provided by a Ray worker instance type is measured in memory optimized data processing units (M-DPUs). |
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
| Max spare compute capacity consumed in data processing units (DPUs) per account | Each supported Region: 4,000 | Yes | The maximum spare compute capacity in data processing units (DPUs) you can use concurrently in your account. |
| Max table versions per account | Each supported Region: 1,000,000 | Yes | The maximum number of table versions in your account. |
| Max table versions per table | Each supported Region: 100,000 | Yes | The maximum number of table versions per table. |
| Max tables per account | Each supported Region: 1,000,000 | Yes | The maximum number of tables in your account. |
| Max tables per database | Each supported Region: 200,000 | Yes | The maximum number of tables per database. |
| Max task DPUs per account | us-east-1: 1,000; us-east-2: 1,000; us-west-2: 1,000; ap-northeast-1: 1,000; ap-southeast-2: 1,000; eu-west-1: 1,000; Each of the other supported Regions: 500 | Yes | The maximum compute capacity in data processing units (DPUs) you can use concurrently in your account. |
| Max triggers per account | Each supported Region: 1,000 | Yes | The maximum number of triggers in your account. |
| Maximum number of in-flight completion requests allowed per account | Each supported Region: 10 | Yes | The maximum number of concurrent generative AI completion requests allowed per account in the current Region. These requests are used for code generation and Spark troubleshooting in AWS Glue. |
| Maximum number of queued job runs | Each supported Region: 1,000 | Yes | Orchestration: maximum number of queued job runs |
| Number of Schema Registries | Each supported Region: 100 | No | The maximum number of Schema Registries per AWS Region for this account. |
| Number of Schema Versions | Each supported Region: 10,000 | No | The maximum number of Schema Versions per AWS Region for this account. |
| Number of column statistics tasks running concurrently per account | Each supported Region: 50 | Yes | The maximum number of column statistics tasks running concurrently in your account. |
| Number of connection types | Each supported Region: 1,000 | Yes | The maximum number of connection types per AWS Region for this account. |
| Number of crawlers per account | Each supported Region: 1,000 | Yes | The maximum number of crawlers in your account. |
| Number of crawlers running concurrently per account | Each supported Region: 150 | Yes | The maximum number of crawlers running concurrently in your account. |
| Number of integrations | Each supported Region: 40 | Yes | The maximum number of integrations per AWS Region for this account. |
| Number of machine learning transforms | Each supported Region: 100 | Yes | The maximum number of machine learning transforms for this account. |
| Number of metadata key value pairs per Schema Version | Each supported Region: 10 | No | The maximum number of Schema Version metadata key value pairs per Schema Version. |
| Number of workflows | Each supported Region: 1,000 | Yes | The maximum number of workflows in your account. |
| The maximum number of concurrent materialized view refresh task runs | Each supported Region: 50 | Yes | The maximum number of concurrent materialized view refresh task runs. |

#### First answer rejected (repaired)

```text
- schema_version: Input should be '1'
```

### 048-amazon-simple-queue-service.pdf

- Status: **failed**, 1 call(s), 495.3 s, in 4,761 / out 18,432 tokens

#### Error

```text
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 1377 column 100
--- no repair call
```

### 038-amazon-opensearch-service.pdf

- Status: **repaired**, 2 call(s), 581.9 s, in 23,665 / out 19,489 tokens
- Service: Amazon OpenSearch Service; quota table format: `standard`

#### Endpoints (153)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| us-east-2 | us-east-2 | es.us-east-2.amazonaws.com | HTTPS | ipv4 |
| us-east-2 | us-east-2 | es-fips.us-east-2.amazonaws.com | HTTPS | fips |
| us-east-2 | us-east-2 | aos.us-east-2.api.aws | HTTPS | dual_stack |
| us-east-1 | us-east-1 | es.us-east-1.amazonaws.com | HTTPS | ipv4 |
| us-east-1 | us-east-1 | es-fips.us-east-1.amazonaws.com | HTTPS | fips |
| us-east-1 | us-east-1 | aos.us-east-1.api.aws | HTTPS | dual_stack |
| us-west-1 | us-west-1 | es.us-west-1.amazonaws.com | HTTPS | ipv4 |
| us-west-1 | us-west-1 | es-fips.us-west-1.amazonaws.com | HTTPS | fips |
| us-west-1 | us-west-1 | aos.us-west-1.api.aws | HTTPS | dual_stack |
| af-south-1 | af-south-1 | es.af-south-1.amazonaws.com | HTTPS | ipv4 |
| af-south-1 | af-south-1 | aos.af-south-1.api.aws | HTTPS | dual_stack |
| ap-east-1 | ap-east-1 | es.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| ap-east-1 | ap-east-1 | aos.ap-east-1.api.aws | HTTPS | dual_stack |
| ap-south-2 | ap-south-2 | es.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| ap-south-2 | ap-south-2 | aos.ap-south-2.api.aws | HTTPS | dual_stack |
| ap-southeast-3 | ap-southeast-3 | es.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-3 | ap-southeast-3 | aos.ap-southeast-3.api.aws | HTTPS | dual_stack |
| ap-southeast-5 | ap-southeast-5 | es.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-5 | ap-southeast-5 | aos.ap-southeast-5.api.aws | HTTPS | dual_stack |
| ap-southeast-4 | ap-southeast-4 | es.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-4 | ap-southeast-4 | aos.ap-southeast-4.api.aws | HTTPS | dual_stack |
| ap-south-1 | ap-south-1 | es.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| ap-south-1 | ap-south-1 | aos.ap-south-1.api.aws | HTTPS | dual_stack |
| ap-southeast-6 | ap-southeast-6 | es.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-6 | ap-southeast-6 | aos.ap-southeast-6.api.aws | HTTPS | dual_stack |
| ap-northeast-3 | ap-northeast-3 | es.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-3 | ap-northeast-3 | aos.ap-northeast-3.api.aws | HTTPS | dual_stack |
| ap-northeast-2 | ap-northeast-2 | es.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-2 | ap-northeast-2 | aos.ap-northeast-2.api.aws | HTTPS | dual_stack |
| ap-southeast-1 | ap-southeast-1 | es.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-1 | ap-southeast-1 | aos.ap-southeast-1.api.aws | HTTPS | dual_stack |
| ap-southeast-2 | ap-southeast-2 | es.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-2 | ap-southeast-2 | aos.ap-southeast-2.api.aws | HTTPS | dual_stack |
| ap-east-2 | ap-east-2 | es.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| ap-east-2 | ap-east-2 | aos.ap-east-2.api.aws | HTTPS | dual_stack |
| ap-southeast-7 | ap-southeast-7 | es.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-7 | ap-southeast-7 | aos.ap-southeast-7.api.aws | HTTPS | dual_stack |
| ap-northeast-1 | ap-northeast-1 | es.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-1 | ap-northeast-1 | aos.ap-northeast-1.api.aws | HTTPS | dual_stack |
| ca-central-1 | ca-central-1 | es.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| ca-central-1 | ca-central-1 | aos.ca-central-1.api.aws | HTTPS | dual_stack |
| ca-west-1 | ca-west-1 | es.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| ca-west-1 | ca-west-1 | aos.ca-west-1.api.aws | HTTPS | dual_stack |
| eu-central-1 | eu-central-1 | es.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| eu-central-1 | eu-central-1 | aos.eu-central-1.api.aws | HTTPS | dual_stack |
| eu-west-1 | eu-west-1 | es.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| eu-west-1 | eu-west-1 | aos.eu-west-1.api.aws | HTTPS | dual_stack |
| eu-west-2 | eu-west-2 | es.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| eu-west-2 | eu-west-2 | aos.eu-west-2.api.aws | HTTPS | dual_stack |
| eu-south-1 | eu-south-1 | es.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| eu-south-1 | eu-south-1 | aos.eu-south-1.api.aws | HTTPS | dual_stack |
| eu-west-3 | eu-west-3 | es.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| eu-west-3 | eu-west-3 | aos.eu-west-3.api.aws | HTTPS | dual_stack |
| eu-south-2 | eu-south-2 | es.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| eu-south-2 | eu-south-2 | aos.eu-south-2.api.aws | HTTPS | dual_stack |
| eu-north-1 | eu-north-1 | es.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| eu-north-1 | eu-north-1 | aos.eu-north-1.api.aws | HTTPS | dual_stack |
| eu-central-2 | eu-central-2 | es.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| eu-central-2 | eu-central-2 | aos.eu-central-2.api.aws | HTTPS | dual_stack |
| il-central-1 | il-central-1 | es.il-central-1.amazonaws.com | HTTPS | ipv4 |
| il-central-1 | il-central-1 | aos.il-central-1.api.aws | HTTPS | dual_stack |
| mx-central-1 | mx-central-1 | es.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| mx-central-1 | mx-central-1 | aos.mx-central-1.api.aws | HTTPS | dual_stack |
| me-south-1 | me-south-1 | es.me-south-1.amazonaws.com | HTTPS | ipv4 |
| me-south-1 | me-south-1 | aos.me-south-1.api.aws | HTTPS | dual_stack |
| me-central-1 | me-central-1 | es.me-central-1.amazonaws.com | HTTPS | ipv4 |
| me-central-1 | me-central-1 | aos.me-central-1.api.aws | HTTPS | dual_stack |
| sa-east-1 | sa-east-1 | es.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| sa-east-1 | sa-east-1 | aos.sa-east-1.api.aws | HTTPS | dual_stack |
| us-gov-east-1 | us-gov-east-1 | es.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| us-gov-east-1 | us-gov-east-1 | es-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| us-gov-east-1 | us-gov-east-1 | aos.us-gov-east-1.api.aws | HTTPS | dual_stack |
| us-gov-west-1 | us-gov-west-1 | es.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| us-gov-west-1 | us-gov-west-1 | es-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| us-gov-west-1 | us-gov-west-1 | aos.us-gov-west-1.api.aws | HTTPS | dual_stack |
| us-east-2 | us-east-2 | aoss.us-east-2.amazonaws.com | HTTPS | ipv4 |
| us-east-2 | us-east-2 | dashboards.us-east-2.aoss.amazonaws.com | HTTPS | ipv4 |
| us-east-2 | us-east-2 | dashboards.us-east-2.aoss-fips.amazonaws.com | HTTPS | fips |
| us-east-1 | us-east-1 | aoss.us-east-1.amazonaws.com | HTTPS | ipv4 |
| us-east-1 | us-east-1 | dashboards.us-east-1.aoss.amazonaws.com | HTTPS | ipv4 |
| us-east-1 | us-east-1 | dashboards.us-east-1.aoss-fips.amazonaws.com | HTTPS | fips |
| us-west-1 | us-west-1 | aoss.us-west-1.amazonaws.com | HTTPS | ipv4 |
| us-west-1 | us-west-1 | dashboards.us-west-1.aoss.amazonaws.com | HTTPS | ipv4 |
| us-west-1 | us-west-1 | dashboards.us-west-1.aoss-fips.amazonaws.com | HTTPS | fips |
| us-west-2 | us-west-2 | aoss.us-west-2.amazonaws.com | HTTPS | ipv4 |
| us-west-2 | us-west-2 | dashboards.us-west-2.aoss.amazonaws.com | HTTPS | ipv4 |
| us-west-2 | us-west-2 | dashboards.us-west-2.aoss-fips.amazonaws.com | HTTPS | fips |
| ap-east-1 | ap-east-1 | aoss.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| ap-east-1 | ap-east-1 | dashboards.ap-east-1.aoss.amazonaws.com | HTTPS | ipv4 |
| ap-south-2 | ap-south-2 | aoss.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| ap-south-2 | ap-south-2 | dashboards.ap-south-2.aoss.amazonaws.com | HTTPS | ipv4 |
| ap-south-2 | ap-south-2 | ap-south-2.aoss.amazonaws.com | HTTPS | ipv4 |
| ap-south-1 | ap-south-1 | aoss.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| ap-south-1 | ap-south-1 | dashboards.ap-south-1.aoss.amazonaws.com | HTTPS | ipv4 |
| ap-south-1 | ap-south-1 | ap-south-1.aoss.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-3 | ap-northeast-3 | aoss.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-3 | ap-northeast-3 | dashboards.ap-northeast-3.aoss.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-2 | ap-northeast-2 | aoss.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-2 | ap-northeast-2 | dashboards.ap-northeast-2.aoss.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-1 | ap-southeast-1 | aoss.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-1 | ap-southeast-1 | dashboards.ap-southeast-1.aoss.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-2 | ap-southeast-2 | aoss.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-2 | ap-southeast-2 | dashboards.ap-southeast-2.aoss.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-1 | ap-northeast-1 | aoss.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-1 | ap-northeast-1 | dashboards.ap-northeast-1.aoss.amazonaws.com | HTTPS | ipv4 |
| ca-central-1 | ca-central-1 | aoss.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| ca-central-1 | ca-central-1 | ca-central-1.aoss-fips.amazonaws.com | HTTPS | fips |
| ca-central-1 | ca-central-1 | dashboards.ca-central-1.aoss-fips.amazonaws.com | HTTPS | fips |
| ca-central-1 | ca-central-1 | dashboards.ca-central-1.aoss.amazonaws.com | HTTPS | ipv4 |
| ca-central-1 | ca-central-1 | ca-central-1.aoss.amazonaws.com | HTTPS | ipv4 |
| eu-central-1 | eu-central-1 | aoss.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| eu-central-1 | eu-central-1 | eu-central-1.aoss.amazonaws.com | HTTPS | ipv4 |
| eu-west-1 | eu-west-1 | aoss.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| eu-west-1 | eu-west-1 | eu-west-1.aoss.amazonaws.com | HTTPS | ipv4 |
| eu-west-2 | eu-west-2 | aoss.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| eu-west-2 | eu-west-2 | eu-west-2.aoss.amazonaws.com | HTTPS | ipv4 |
| eu-south-1 | eu-south-1 | aoss.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| eu-south-1 | eu-south-1 | eu-south-1.aoss.amazonaws.com | HTTPS | ipv4 |
| eu-west-3 | eu-west-3 | aoss.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| eu-west-3 | eu-west-3 | eu-west-3.aoss.amazonaws.com | HTTPS | ipv4 |
| eu-south-2 | eu-south-2 | aoss.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| eu-south-2 | eu-south-2 | eu-south-2.aoss.amazonaws.com | HTTPS | ipv4 |
| eu-north-1 | eu-north-1 | aoss.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| eu-north-1 | eu-north-1 | eu-north-1.aoss.amazonaws.com | HTTPS | ipv4 |
| eu-central-2 | eu-central-2 | aoss.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| eu-central-2 | eu-central-2 | eu-central-2.aoss.amazonaws.com | HTTPS | ipv4 |
| sa-east-1 | sa-east-1 | aoss.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| sa-east-1 | sa-east-1 | sa-east-1.aoss.amazonaws.com | HTTPS | ipv4 |
| sa-east-1 | sa-east-1 | dashboards.sa-east-1.aoss.amazonaws.com | HTTPS | ipv4 |
| us-gov-east-1 | us-gov-east-1 | aoss.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| us-gov-east-1 | us-gov-east-1 | aoss.us-gov-east-1.aoss-fips.amazonaws.com | HTTPS | fips |
| us-gov-east-1 | us-gov-east-1 | aoss.us-gov-east-1.aoss.amazonaws.com | HTTPS | ipv4 |
| us-gov-west-1 | us-gov-west-1 | aoss.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| us-gov-west-1 | us-gov-west-1 | aoss.us-gov-west-1.aoss-fips.amazonaws.com | HTTPS | fips |
| us-gov-west-1 | us-gov-west-1 | aoss.us-gov-west-1.aoss.amazonaws.com | HTTPS | ipv4 |
| us-east-2 | us-east-2 | osis.us-east-2.amazonaws.com | HTTPS | ipv4 |
| us-east-1 | us-east-1 | osis.us-east-1.amazonaws.com | HTTPS | ipv4 |
| us-west-1 | us-west-1 | osis.us-west-1.amazonaws.com | HTTPS | ipv4 |
| us-west-2 | us-west-2 | osis.us-west-2.amazonaws.com | HTTPS | ipv4 |
| ap-south-1 | ap-south-1 | osis.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-2 | ap-northeast-2 | osis.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-1 | ap-southeast-1 | osis.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| ap-southeast-2 | ap-southeast-2 | osis.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| ap-northeast-1 | ap-northeast-1 | osis.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| ca-central-1 | ca-central-1 | osis.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| eu-central-1 | eu-central-1 | osis.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| eu-west-1 | eu-west-1 | osis.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| eu-west-2 | eu-west-2 | osis.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| eu-west-3 | eu-west-3 | osis.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| eu-south-2 | eu-south-2 | osis.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| eu-north-1 | eu-north-1 | osis.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| eu-central-2 | eu-central-2 | osis.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| sa-east-1 | sa-east-1 | osis.sa-east-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (38)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Dedicated master instances per domain | Each supported Region: 5 | No | The maximum number of dedicated master instances in a single Amazon OpenSearch Service domain. |
| Domains per Region | Each supported Region: 500 | Yes | The maximum number of Amazon OpenSearch Service domains you can create in each AWS Region. |
| Instances per domain | Each supported Region: 200 | Yes | The maximum number of instances in a single Amazon OpenSearch Service domain. You can request an increase up to 1002 instances per domain. |
| Instances per domain (T2 instance type) | Each supported Region: 10 | No | The maximum number of T2 instances in a single Amazon OpenSearch Service domain. |
| Warm instances per domain | Each supported Region: 150 | No | The maximum number of warm nodes in a single Amazon OpenSearch Service cluster. |
| Total storage per domain | 3 PiB | No | This maximum is the sum of all data nodes and warm nodes. For example, your domain might have 45 r6gd.16xl large.search instances and 140 ultrawarm 1.large.search instances for a total of 2.88 PiB of storage. |
| Custom packages per Region | 25 | No | The maximum number of custom packages per Region. |
| Custom packages per domain | 20 | No | The maximum number of custom packages per domain. |
| Default indexing capacity (OCUs) | 10 | No | The default indexing capacity for OpenSearch Serverless resources. |
| Default search capacity (OCUs) | 10 | No | The default search capacity for OpenSearch Serverless resources. |
| Maximum indexing capacity (OCUs) | 1,700 | No | The maximum indexing capacity for OpenSearch Serverless resources. |
| Maximum search capacity (OCUs) | 1,700 | No | The maximum search capacity for OpenSearch Serverless resources. |
| Data access policies | 500 | No | The maximum number of data access policies. |
| Encryption policies | 150 | No | The maximum number of encryption policies. |
| Network policies | 500 | No | The maximum number of network policies. |
| SAML providers | 50 | No | The maximum number of SAML providers. |
| Data access policy size | 10,240 bytes | No | The maximum size of a data access policy. |
| Network policy size | 10,240 bytes | No | The maximum size of a network policy. |
| SAML provider size | 51,200 bytes | No | The maximum size of a SAML provider. |
| Encryption policy size | 10,240 bytes | No | The maximum size of an encryption policy. |
| Collection tags | 50 | No | The maximum number of collection tags. |
| Collections per collection group (Classic) | 1,500 | No | The maximum number of collections per Classic collection group. The actual number of collections can be further limited by MaxOCUs based on the size of collections. |
| Collections per collection group (NextGen) | 10,000 | Yes | The maximum number of collections per NextGen collection group. You can request an increase through the Service Quotas console. |
| Collections with unique KMS keys (not in a collection group) | Maximum OCU/2 | No | This limit only applies to collections that are not part of a collection group. It depends on the maximum number of OCUs you set and how many OCUs are already in use. Collections within a collection group have a separate limit of 1,500 collections per group, regardless of the number of unique KMS keys used. |
| OpenSearch Serverless-managed VPC endpoints | 50 | No | The maximum number of OpenSearch Serverless-managed VPC endpoints. It doesn't include OpenSearch Service-managed VPC endpoints. |
| Indexes per Amazon OpenSearch Serverless collection | 1000 | No | The maximum number of indexes per Amazon OpenSearch Serverless collection is 1000. |
| Index templates per Amazon OpenSearch Serverless collection | 500 | No | The maximum number of index templates per Amazon OpenSearch Serverless collection is 500. |
| Collection groups per account | 300 | No | The maximum number of collection groups per account. |
| Connected VPCs per pipeline | Each supported Region: 1 | No | The maximum number of connected VPCs per pipeline. |
| Pipelines connected to a single VPC domain | Each supported Region: 50 | No | The maximum number of pipelines connected to a single VPC domain. |
| Pipelines | Each supported Region: 50 | No | The maximum number of pipelines. |
| Characters per pipeline configuration | Each supported Region: 24000 | No | The maximum number of characters per pipeline configuration. |
| Sources per pipeline | Each supported Region: 100000 | No | The maximum number of sources per pipeline. This limit only applies to plugin sources, such as HTTP, OTel, or S3. You can still chain sub-pipelines together within a single OpenSearch Ingestion pipeline configuration. |
| Unique OpenSearch sinks per pipeline | Each supported Region: 1 | No | The maximum number of unique OpenSearch sinks per pipeline. This limit only applies to OpenSearch domain and collection sinks. You can still chain sub-pipelines together within a single OpenSearch Ingestion pipeline configuration. |
| Total OpenSearch sinks per pipeline | Each supported Region: 50 | No | The maximum number of times that you can specify the same OpenSearch sink within a pipeline configuration file. The number of non 'pipeline' sinks within the pipeline configurationBody must be between 1 and 20, inclusive. |
| Minimum Ingestion OCUs per pipeline | Each supported Region: 1 | No | The minimum number of Ingestion OCUs per pipeline. |
| Maximum Ingestion OCUs per stateless pipeline | Each supported Region: 96 | No | The maximum number of Ingestion OCUs per stateless pipeline. |
| Maximum Ingestion OCUs per stateful pipeline | Each supported Region: 48 | No | The maximum number of Ingestion OCUs per stateful pipeline. |

#### First answer rejected (repaired)

```text
- schema_version: Input should be '1'
```
