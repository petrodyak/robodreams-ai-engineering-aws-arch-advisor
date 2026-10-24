# Run `claude__v1__t0`

Generated from the JSONL run file by `src/extract/report_md.py`; do not edit.

- Model: `claude-haiku-4-5`
- Prompt version: `v1` (file sha `8a0da697aa92`)
- Schema sha: `e707d2e9616f`
- Sampling: `t0` (temperature 0.0, top_p None)
- Documents: 30

## Summary

| # | Document | Group | Status | Calls | Latency, s | In tokens | Out tokens | Quota table | Endpoints | Quotas |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [049-amazon-simple-storage-service.pdf](#049-amazon-simple-storage-servicepdf) | edge | ok | 1 | 78.1 | 20,001 | 16,589 | standard | 290 | 21 |
| 2 | [006-amazon-aurora-dsql.pdf](#006-amazon-aurora-dsqlpdf) | short | ok | 1 | 7.8 | 3,601 | 1,454 | standard | 25 | 4 |
| 3 | [076-aws-glue-databrew.pdf](#076-aws-glue-databrewpdf) | short | ok | 1 | 11.9 | 3,568 | 1,546 | standard | 24 | 7 |
| 4 | [085-aws-lake-formation.pdf](#085-aws-lake-formationpdf) | short | ok | 1 | 30.8 | 4,988 | 4,481 | none | 88 | 0 |
| 5 | [033-amazon-kinesis-data-streams.pdf](#033-amazon-kinesis-data-streamspdf) | short | ok | 1 | 20.4 | 5,097 | 4,125 | standard | 80 | 1 |
| 6 | [007-amazon-bedrock-agentcore.pdf](#007-amazon-bedrock-agentcorepdf) | short | ok | 1 | 16.4 | 4,462 | 2,236 | none | 39 | 0 |
| 7 | [037-amazon-managed-workflows-for-apache-airflow.pdf](#037-amazon-managed-workflows-for-apache-airflowpdf) | short | ok | 1 | 38.2 | 7,011 | 8,346 | standard | 163 | 1 |
| 8 | [055-aws-app-mesh.pdf](#055-aws-app-meshpdf) | short | ok | 1 | 44.5 | 6,754 | 6,515 | standard | 120 | 5 |
| 9 | [066-aws-datasync.pdf](#066-aws-datasyncpdf) | short | ok | 1 | 30.4 | 5,896 | 4,395 | non_standard | 88 | 0 |
| 10 | [091-aws-resource-groups-and-tagging.pdf](#091-aws-resource-groups-and-taggingpdf) | short | ok | 1 | 26.4 | 5,957 | 3,793 | non_standard | 76 | 0 |
| 11 | [018-amazon-ec2-auto-scaling.pdf](#018-amazon-ec2-auto-scalingpdf) | short | ok | 1 | 33.2 | 6,828 | 4,741 | standard | 84 | 9 |
| 12 | [005-amazon-aurora.pdf](#005-amazon-aurorapdf) | medium | ok | 1 | 23.8 | 6,951 | 3,091 | standard | 36 | 25 |
| 13 | [075-aws-glue.pdf](#075-aws-gluepdf) | medium | ok | 1 | 49.0 | 7,439 | 6,647 | standard | 88 | 46 |
| 14 | [042-amazon-redshift.pdf](#042-amazon-redshiftpdf) | medium | ok | 1 | 86.7 | 11,391 | 13,100 | none | 253 | 0 |
| 15 | [044-amazon-relational-database-service.pdf](#044-amazon-relational-database-servicepdf) | medium | ok | 1 | 39.0 | 9,180 | 5,268 | standard | 78 | 27 |
| 16 | [048-amazon-simple-queue-service.pdf](#048-amazon-simple-queue-servicepdf) | medium | ok | 1 | 38.0 | 8,102 | 5,317 | standard | 84 | 19 |
| 17 | [047-amazon-simple-notification-service.pdf](#047-amazon-simple-notification-servicepdf) | medium | ok | 1 | 27.1 | 8,020 | 3,898 | non_standard | 78 | 0 |
| 18 | [026-amazon-eventbridge.pdf](#026-amazon-eventbridgepdf) | medium | ok | 1 | 41.2 | 6,912 | 5,577 | standard | 84 | 17 |
| 19 | [092-aws-secrets-manager.pdf](#092-aws-secrets-managerpdf) | medium | ok | 1 | 25.6 | 7,107 | 3,343 | standard | 44 | 18 |
| 20 | [023-amazon-elastic-kubernetes-service.pdf](#023-amazon-elastic-kubernetes-servicepdf) | medium | ok | 1 | 31.2 | 6,947 | 4,359 | standard | 76 | 13 |
| 21 | [078-aws-iam-identity-center.pdf](#078-aws-iam-identity-centerpdf) | medium | ok | 1 | 30.0 | 9,989 | 4,208 | standard | 78 | 6 |
| 22 | [038-amazon-opensearch-service.pdf](#038-amazon-opensearch-servicepdf) | edge | ok | 1 | 60.7 | 10,864 | 9,074 | non_standard | 183 | 0 |
| 23 | [086-aws-lambda.pdf](#086-aws-lambdapdf) | edge | ok | 1 | 65.6 | 11,210 | 8,470 | standard | 78 | 73 |
| 24 | [004-amazon-athena.pdf](#004-amazon-athenapdf) | edge | ok | 1 | 57.9 | 11,605 | 8,129 | standard | 88 | 30 |
| 25 | [017-amazon-dynamodb.pdf](#017-amazon-dynamodbpdf) | edge | ok | 1 | 32.7 | 15,877 | 6,284 | standard | 94 | 13 |
| 26 | [095-aws-step-functions.pdf](#095-aws-step-functionspdf) | edge | ok | 1 | 86.7 | 13,824 | 12,474 | standard | 172 | 97 |
| 27 | [025-amazon-emr.pdf](#025-amazon-emrpdf) | edge | ok | 1 | 85.1 | 17,232 | 11,995 | standard | 78 | 106 |
| 28 | [010-amazon-cloudfront.pdf](#010-amazon-cloudfrontpdf) | edge | ok | 1 | 45.4 | 9,194 | 5,538 | standard | 4 | 97 |
| 29 | [074-aws-global-accelerator.pdf](#074-aws-global-acceleratorpdf) | edge | ok | 1 | 6.4 | 7,987 | 926 | standard | 2 | 16 |
| 30 | [019-amazon-ecr.pdf](#019-amazon-ecrpdf) | edge | ok | 1 | 85.7 | 10,763 | 12,373 | standard | 210 | 23 |

## Documents

### 049-amazon-simple-storage-service.pdf

- Status: **ok**, 1 call(s), 78.1 s, in 20,001 / out 16,589 tokens
- Service: Amazon Simple Storage Service; quota table format: `standard`

#### Endpoints (290)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | s3.us-east-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | s3.dualstack.us-east-2.amazonaws.com | HTTP and HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | s3-fips.dualstack.us-east-2.amazonaws.com | HTTP and HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | s3-fips.us-east-2.amazonaws.com | HTTP and HTTPS | fips |
| US East (N. Virginia) | us-east-1 | s3.us-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | s3.dualstack.us-east-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | s3-fips.us-east-1.amazonaws.com | HTTP and HTTPS | fips |
| US East (N. Virginia) | us-east-1 | s3-fips.dualstack.us-east-1.amazonaws.com | HTTP and HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | s3.us-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| US West (N. California) | us-west-1 | s3.dualstack.us-west-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| US West (N. California) | us-west-1 | s3-fips.dualstack.us-west-1.amazonaws.com | HTTP and HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | s3-fips.us-west-1.amazonaws.com | HTTP and HTTPS | fips |
| US West (Oregon) | us-west-2 | s3.us-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | s3.dualstack.us-west-2.amazonaws.com | HTTP and HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | s3-fips.dualstack.us-west-2.amazonaws.com | HTTP and HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | s3-fips.us-west-2.amazonaws.com | HTTP and HTTPS | fips |
| Africa (Cape Town) | af-south-1 | s3.af-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | s3.dualstack.af-south-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | s3.ap-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | s3.dualstack.ap-east-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | s3.ap-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | s3.dualstack.ap-south-2.amazonaws.com | HTTP and HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | s3.ap-southeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | s3.dualstack.ap-southeast-3.amazonaws.com | HTTP and HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | s3.ap-southeast-5.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | s3.dualstack.ap-southeast-5.amazonaws.com | HTTP and HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | s3.ap-southeast-4.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | s3.dualstack.ap-southeast-4.amazonaws.com | HTTP and HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | s3.ap-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | s3.dualstack.ap-south-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | s3.ap-southeast-6.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | s3.dualstack.ap-southeast-6.amazonaws.com | HTTP and HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | s3.ap-northeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | s3.dualstack.ap-northeast-3.amazonaws.com | HTTP and HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | s3.ap-northeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | s3.dualstack.ap-northeast-2.amazonaws.com | HTTP and HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | s3.ap-southeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | s3.dualstack.ap-southeast-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | s3.ap-southeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | s3.dualstack.ap-southeast-2.amazonaws.com | HTTP and HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | s3.ap-east-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | s3.dualstack.ap-east-2.amazonaws.com | HTTP and HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | s3.ap-southeast-7.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | s3.dualstack.ap-southeast-7.amazonaws.com | HTTP and HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | s3.ap-northeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | s3.dualstack.ap-northeast-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | s3.ca-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | s3.dualstack.ca-central-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | s3-fips.dualstack.ca-central-1.amazonaws.com | HTTP and HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | s3-fips.ca-central-1.amazonaws.com | HTTP and HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | s3.ca-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | s3.dualstack.ca-west-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | s3-fips.dualstack.ca-west-1.amazonaws.com | HTTP and HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | s3-fips.ca-west-1.amazonaws.com | HTTP and HTTPS | fips |
| Europe (Frankfurt) | eu-central-1 | s3.eu-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | s3.dualstack.eu-central-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | s3.eu-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | s3.dualstack.eu-west-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| Europe (London) | eu-west-2 | s3.eu-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (London) | eu-west-2 | s3.dualstack.eu-west-2.amazonaws.com | HTTP and HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | s3.eu-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | s3.dualstack.eu-south-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | s3.eu-west-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | s3.dualstack.eu-west-3.amazonaws.com | HTTP and HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | s3.eu-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | s3.dualstack.eu-south-2.amazonaws.com | HTTP and HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | s3.eu-north-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | s3.dualstack.eu-north-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | s3.eu-central-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | s3.dualstack.eu-central-2.amazonaws.com | HTTP and HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | s3.il-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | s3.dualstack.il-central-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | s3.mx-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | s3.dualstack.mx-central-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | s3.me-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | s3.dualstack.me-south-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | s3.me-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | s3.dualstack.me-central-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | s3.sa-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | s3.dualstack.sa-east-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | s3.us-gov-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | s3-fips.dualstack.us-gov-east-1.amazonaws.com | HTTPS | fips_dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | s3.dualstack.us-gov-east-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | s3-fips.us-gov-east-1.amazonaws.com | HTTP and HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | s3.us-gov-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | s3-fips.dualstack.us-gov-west-1.amazonaws.com | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | s3.dualstack.us-gov-west-1.amazonaws.com | HTTP and HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | s3-fips.us-gov-west-1.amazonaws.com | HTTP and HTTPS | fips |
| US East (Ohio) | us-east-2 | s3tables.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | s3tables.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | s3tables.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | s3tables.us-west-2.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | s3tables.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | s3tables.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | s3tables.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | s3tables.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | s3tables.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | s3tables.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | s3tables.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | s3tables.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | s3tables.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | s3tables.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | s3tables.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | s3tables.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | s3tables.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | s3tables.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | s3tables.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | s3tables.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | s3tables.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | s3tables.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | s3tables.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | s3tables.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | s3tables.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | s3tables.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | s3tables.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | s3tables.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | s3tables.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | s3tables.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | s3tables.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | s3tables.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | s3tables.me-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | s3tables.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | s3tables.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | s3tables.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | s3-accesspoint.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | s3-accesspoint-fips.dualstack.us-east-2.amazonaws.com | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | s3-accesspoint-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | s3-accesspoint.dualstack.us-east-2.amazonaws.com | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | s3-accesspoint.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | s3-accesspoint-fips.dualstack.us-east-1.amazonaws.com | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | s3-accesspoint-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | s3-accesspoint.dualstack.us-east-1.amazonaws.com | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | s3-accesspoint.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | s3-accesspoint-fips.dualstack.us-west-1.amazonaws.com | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | s3-accesspoint-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | s3-accesspoint.dualstack.us-west-1.amazonaws.com | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | s3-accesspoint.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | s3-accesspoint-fips.dualstack.us-west-2.amazonaws.com | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | s3-accesspoint-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | s3-accesspoint.dualstack.us-west-2.amazonaws.com | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | s3-accesspoint.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | s3-accesspoint.dualstack.af-south-1.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | s3-accesspoint.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | s3-accesspoint.dualstack.ap-east-1.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | s3-accesspoint.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | s3-accesspoint.dualstack.ap-south-2.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | s3-accesspoint.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | s3-accesspoint.dualstack.ap-southeast-3.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | s3-accesspoint.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | s3-accesspoint.dualstack.ap-southeast-5.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | s3-accesspoint.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | s3-accesspoint.dualstack.ap-southeast-4.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | s3-accesspoint.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | s3-accesspoint.dualstack.ap-south-1.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | s3-accesspoint.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | s3-accesspoint.dualstack.ap-southeast-6.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | s3-accesspoint.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | s3-accesspoint.dualstack.ap-northeast-3.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | s3-accesspoint.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | s3-accesspoint.dualstack.ap-northeast-2.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | s3-accesspoint.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | s3-accesspoint.dualstack.ap-southeast-1.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | s3-accesspoint.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | s3-accesspoint.dualstack.ap-southeast-2.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | s3-accesspoint.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | s3-accesspoint.dualstack.ap-east-2.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | s3-accesspoint.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | s3-accesspoint.dualstack.ap-southeast-7.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | s3-accesspoint.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | s3-accesspoint.dualstack.ap-northeast-1.amazonaws.com | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | s3-accesspoint.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | s3-accesspoint-fips.dualstack.ca-central-1.amazonaws.com | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | s3-accesspoint-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | s3-accesspoint.dualstack.ca-central-1.amazonaws.com | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | s3-accesspoint.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | s3-accesspoint-fips.dualstack.ca-west-1.amazonaws.com | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | s3-accesspoint-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | s3-accesspoint.dualstack.ca-west-1.amazonaws.com | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | s3-accesspoint.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | s3-accesspoint.dualstack.eu-central-1.amazonaws.com | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | s3-accesspoint.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | s3-accesspoint.dualstack.eu-west-1.amazonaws.com | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | s3-accesspoint.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | s3-accesspoint.dualstack.eu-west-2.amazonaws.com | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | s3-accesspoint.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | s3-accesspoint.dualstack.eu-south-1.amazonaws.com | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | s3-accesspoint.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | s3-accesspoint.dualstack.eu-west-3.amazonaws.com | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | s3-accesspoint.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | s3-accesspoint.dualstack.eu-south-2.amazonaws.com | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | s3-accesspoint.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | s3-accesspoint.dualstack.eu-north-1.amazonaws.com | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | s3-accesspoint.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | s3-accesspoint.dualstack.eu-central-2.amazonaws.com | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | s3-accesspoint.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | s3-accesspoint.dualstack.il-central-1.amazonaws.com | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | s3-accesspoint.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | s3-accesspoint.dualstack.mx-central-1.amazonaws.com | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | s3-accesspoint.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | s3-accesspoint.dualstack.me-south-1.amazonaws.com | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | s3-accesspoint.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | s3-accesspoint.dualstack.me-central-1.amazonaws.com | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | s3-accesspoint.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | s3-accesspoint.dualstack.sa-east-1.amazonaws.com | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | s3-accesspoint.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | s3-accesspoint-fips.dualstack.us-gov-east-1.amazonaws.com | HTTPS | fips_dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | s3-accesspoint-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | s3-accesspoint.dualstack.us-gov-east-1.amazonaws.com | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | s3-accesspoint.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | s3-accesspoint-fips.dualstack.us-gov-west-1.amazonaws.com | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | s3-accesspoint-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | s3-accesspoint.dualstack.us-gov-west-1.amazonaws.com | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | s3-control.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | s3-control.dualstack.us-east-2.amazonaws.com | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | s3-control-fips.dualstack.us-east-2.amazonaws.com | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | s3-control-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | s3-control.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | s3-control-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | s3-control.dualstack.us-east-1.amazonaws.com | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | s3-control-fips.dualstack.us-east-1.amazonaws.com | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | s3-control.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | s3-control.dualstack.us-west-1.amazonaws.com | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | s3-control-fips.dualstack.us-west-1.amazonaws.com | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | s3-control-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | s3-control.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | s3-control-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | s3-control.dualstack.us-west-2.amazonaws.com | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | s3-control-fips.dualstack.us-west-2.amazonaws.com | HTTPS | fips_dual_stack |
| Africa (Cape Town) | af-south-1 | s3-control.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | s3-control.dualstack.af-south-1.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | s3-control.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | s3-control.dualstack.ap-east-1.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | s3-control.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | s3-control.dualstack.ap-south-2.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | s3-control.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | s3-control.dualstack.ap-southeast-3.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | s3-control.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | s3-control.dualstack.ap-southeast-4.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | s3-control.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | s3-control.dualstack.ap-south-1.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | s3-control.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | s3-control.dualstack.ap-northeast-3.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | s3-control.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | s3-control.dualstack.ap-northeast-2.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | s3-control.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | s3-control.dualstack.ap-southeast-1.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | s3-control.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | s3-control.dualstack.ap-southeast-2.amazonaws.com | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | s3-control.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | s3-control.dualstack.ap-northeast-1.amazonaws.com | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | s3-control.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | s3-control.dualstack.ca-central-1.amazonaws.com | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | s3-control-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | s3-control-fips.dualstack.ca-central-1.amazonaws.com | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | s3-control.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | s3-control-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | s3-control.dualstack.ca-west-1.amazonaws.com | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | s3-control-fips.dualstack.ca-west-1.amazonaws.com | HTTPS | fips_dual_stack |
| Europe (Frankfurt) | eu-central-1 | s3-control.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | s3-control.dualstack.eu-central-1.amazonaws.com | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | s3-control.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | s3-control.dualstack.eu-west-1.amazonaws.com | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | s3-control.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | s3-control.dualstack.eu-west-2.amazonaws.com | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | s3-control.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | s3-control.dualstack.eu-south-1.amazonaws.com | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | s3-control.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | s3-control.dualstack.eu-west-3.amazonaws.com | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | s3-control.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | s3-control.dualstack.eu-south-2.amazonaws.com | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | s3-control.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | s3-control.dualstack.eu-north-1.amazonaws.com | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | s3-control.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | s3-control.dualstack.eu-central-2.amazonaws.com | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | s3-control.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | s3-control.dualstack.il-central-1.amazonaws.com | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | s3-control.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | s3-control.dualstack.me-south-1.amazonaws.com | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | s3-control.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | s3-control.dualstack.me-central-1.amazonaws.com | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | s3-control.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | s3-control.dualstack.sa-east-1.amazonaws.com | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | s3-control.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | s3-control-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | s3-control.dualstack.us-gov-east-1.amazonaws.com | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | s3-control-fips.dualstack.us-gov-east-1.amazonaws.com | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | s3-control.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | s3-control-fips.dualstack.us-gov-west-1.amazonaws.com | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | s3-control.dualstack.us-gov-west-1.amazonaws.com | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | s3-control-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |

#### Quotas (21)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Access Points | Each Account: 10,000 | Yes | The number of Amazon S3 Access Points that you can create per region in an account |
| Bucket policy | Each Account: 20 Kilobytes | No | The maximum size (in KB) of a bucket policy for an Amazon S3 bucket |
| Bucket tags | Each Account: 50 | No | The maximum number of tags you can assign to an Amazon S3 bucket |
| Directory buckets | Each Account: 100 | Yes | The number of Amazon S3 directory buckets that you can create in an account |
| Event notifications | Each Account: 100 | No | The maximum number of event notifications per Amazon S3 bucket |
| General purpose buckets | Each Account: 10,000 | Yes | The number of Amazon S3 general purpose buckets that you can create in an account |
| Lifecycle rules | Each Account: 1,000 | No | The maximum number of rules you can specify for an Amazon S3 lifecycle configuration |
| Maximum part size | Each Account: 5 Gigabytes | No | The maximum size (in GB) of an Amazon S3 object part in a Multipart upload using the API |
| Minimum part size | Each Account: 5 Megabytes | No | The minimum size (in MB) of an Amazon S3 object part in a Multipart upload using the API. The last part uploaded can be less than the stated minimum |
| Multi-Region Access Point Regions | Each Account: 20 | No | Maximum Regions per Multi-Region Access Point. |
| Multi-Region Access Points | Each Account: 100 | No | Multi-Region Access Points per Account. |
| Object size | Each Account: 48.828125 Terabytes | No | The maximum size (in TB) of an Amazon S3 object |
| Object size (Console upload) | Each Account: 160 Gigabytes | No | The maximum size (in GB) of an Amazon S3 object that you can upload using the console |
| Object tags | Each Account: 10 | No | The maximum number of tags you can assign to an Amazon S3 object |
| Parts | Each Account: 10,000 | No | The maximum number of Amazon S3 object parts per Multipart upload |
| Replication Destinations | Each Account: 28 | Yes | The number of destination S3 buckets you can add for each source S3 bucket across all replication rules. |
| Replication rules | Each Account: 1,000 | No | The maximum number of rules you can specify in an Amazon S3 Replication configuration |
| Replication transfer rate | Each Account: 1 Gigabits per second | Yes | The maximum Replication Time Control transfer rate that you can replicate from the source region in this account. |
| S3 Glacier: Number of random restore requests. | Each Account: 35 | No | The number of random restore requests from S3 Glacier storage class per PiB stored per day. |
| S3 Glacier: Provisioned capacity units | Each Account: 2 | No | The maximum number of S3 Glacier storage class provisioned capacity units available to purchase per account. |
| S3 Glacier: Retrieval request rate per second. | Each Account: 1,000 | No | The maximum number of retrieval requests per second allowed per account. |

### 006-amazon-aurora-dsql.pdf

- Status: **ok**, 1 call(s), 7.8 s, in 3,601 / out 1,454 tokens
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

- Status: **ok**, 1 call(s), 11.9 s, in 3,568 / out 1,546 tokens
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

- Status: **ok**, 1 call(s), 20.4 s, in 5,097 / out 4,125 tokens
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

- Status: **ok**, 1 call(s), 16.4 s, in 4,462 / out 2,236 tokens
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

### 037-amazon-managed-workflows-for-apache-airflow.pdf

- Status: **ok**, 1 call(s), 38.2 s, in 7,011 / out 8,346 tokens
- Service: Amazon Managed Workflows for Apache Airflow; quota table format: `standard`

#### Endpoints (163)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | api.airflow.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | env.airflow.us-east-2.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | ops.airflow.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | api.airflow.us-east-2.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | env.airflow-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | env.airflow-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | api.airflow-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | api.airflow-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | env.airflow.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | api.airflow.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | env.airflow.us-east-1.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | ops.airflow.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | api.airflow.us-east-1.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | env.airflow-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | env.airflow-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | api.airflow-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | api.airflow-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | env.airflow.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | api.airflow.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | env.airflow.us-west-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | api.airflow.us-west-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | env.airflow-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | env.airflow-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | api.airflow-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | api.airflow-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | env.airflow.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | api.airflow.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | env.airflow.us-west-2.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | ops.airflow.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | api.airflow.us-west-2.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | env.airflow-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | env.airflow-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | api.airflow-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | api.airflow-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | env.airflow.us-west-2.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | api.airflow.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | env.airflow.af-south-1.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | api.airflow.af-south-1.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | env.airflow.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | api.airflow.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | env.airflow.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | api.airflow.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | env.airflow.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | api.airflow.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | env.airflow.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | api.airflow.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | env.airflow.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | api.airflow.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | env.airflow.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | api.airflow.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | env.airflow.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | api.airflow.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | env.airflow.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | api.airflow.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | env.airflow.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | api.airflow.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | env.airflow.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | api.airflow.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | env.airflow.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | api.airflow.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | env.airflow.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | ops.airflow.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | api.airflow.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | env.airflow.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | api.airflow.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | env.airflow.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | api.airflow.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | env.airflow.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | api.airflow.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | env.airflow.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | ops.airflow.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | api.airflow.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | env.airflow.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | api.airflow.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | env.airflow.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | ops.airflow.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | api.airflow.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | env.airflow.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | api.airflow.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | env.airflow.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | ops.airflow.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | api.airflow.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | env.airflow.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | api.airflow.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | env.airflow.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | api.airflow.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | env.airflow.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | api.airflow.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | env.airflow.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | ops.airflow.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | api.airflow.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | env.airflow.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | api.airflow.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | env.airflow.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | ops.airflow.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | api.airflow.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | env.airflow-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | env.airflow-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | api.airflow-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | api.airflow-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | env.airflow.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | api.airflow.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | env.airflow.ca-west-1.api.aws | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | api.airflow.ca-west-1.api.aws | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | env.airflow-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | env.airflow-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | api.airflow-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | api.airflow-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | env.airflow.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | api.airflow.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | env.airflow.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | ops.airflow.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | api.airflow.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | env.airflow.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | api.airflow.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | env.airflow.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | ops.airflow.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | api.airflow.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | env.airflow.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | api.airflow.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | env.airflow.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | ops.airflow.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | api.airflow.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | env.airflow.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | api.airflow.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | env.airflow.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | api.airflow.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | env.airflow.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | api.airflow.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | env.airflow.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | ops.airflow.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | api.airflow.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | env.airflow.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | api.airflow.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | env.airflow.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | api.airflow.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | env.airflow.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | api.airflow.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | env.airflow.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | ops.airflow.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | api.airflow.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | env.airflow.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | api.airflow.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | env.airflow.eu-central-2.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | api.airflow.eu-central-2.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | env.airflow.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | api.airflow.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | env.airflow.il-central-1.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | api.airflow.il-central-1.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | env.airflow.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | api.airflow.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | env.airflow.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | api.airflow.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | env.airflow.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | api.airflow.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | env.airflow.me-central-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | api.airflow.me-central-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | env.airflow.me-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | api.airflow.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | env.airflow.sa-east-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | ops.airflow.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | api.airflow.sa-east-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | env.airflow.sa-east-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (1)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Environments per account per Region (small, medium, large) | Each supported Region: 10 | Yes | The maximum number of environments per account per Region. |

### 055-aws-app-mesh.pdf

- Status: **ok**, 1 call(s), 44.5 s, in 6,754 / out 6,515 tokens
- Service: AWS App Mesh; quota table format: `standard`

#### Endpoints (120)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | appmesh.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | appmesh-envoy-management-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | appmesh.us-east-2.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | appmesh-envoy-management-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | appmesh-envoy-management.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | appmesh-envoy-management.us-east-2.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | appmesh-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | appmesh-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | appmesh.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | appmesh-envoy-management.us-east-1.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | appmesh-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | appmesh-envoy-management-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | appmesh-envoy-management.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | appmesh.us-east-1.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | appmesh-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | appmesh-envoy-management-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | appmesh.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | appmesh-envoy-management.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | appmesh.us-west-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | appmesh-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | appmesh-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | appmesh-envoy-management.us-west-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | appmesh-envoy-management-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | appmesh-envoy-management-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | appmesh.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | appmesh-envoy-management.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | appmesh-envoy-management-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | appmesh-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | appmesh.us-west-2.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | appmesh-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | appmesh-envoy-management-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | appmesh-envoy-management.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | appmesh.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | appmesh-envoy-management.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | appmesh.af-south-1.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | appmesh-envoy-management.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | appmesh.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | appmesh.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | appmesh-envoy-management.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | appmesh-envoy-management.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | appmesh.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | appmesh-envoy-management.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | appmesh.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | appmesh-envoy-management.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | appmesh.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | appmesh.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | appmesh-envoy-management.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | appmesh-envoy-management.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | appmesh.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | appmesh-envoy-management.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | appmesh-envoy-management.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | appmesh.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | appmesh.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | appmesh-envoy-management.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | appmesh-envoy-management.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | appmesh.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | appmesh.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | appmesh-envoy-management.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | appmesh.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | appmesh-envoy-management.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | appmesh.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | appmesh-envoy-management.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | appmesh-envoy-management.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | appmesh.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | appmesh.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | appmesh-envoy-management.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | appmesh-envoy-management.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | appmesh.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | appmesh.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | appmesh-envoy-management-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | appmesh.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | appmesh-envoy-management.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | appmesh-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | appmesh-envoy-management.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | appmesh-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | appmesh-envoy-management-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Europe (Frankfurt) | eu-central-1 | appmesh.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | appmesh.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | appmesh-envoy-management.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | appmesh-envoy-management.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | appmesh.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | appmesh-envoy-management.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | appmesh-envoy-management.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | appmesh.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | appmesh.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | appmesh.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | appmesh-envoy-management.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | appmesh-envoy-management.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | appmesh.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | appmesh-envoy-management.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | appmesh-envoy-management.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | appmesh.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | appmesh.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | appmesh-envoy-management.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | appmesh-envoy-management.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | appmesh.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | appmesh.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | appmesh-envoy-management.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | appmesh.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | appmesh-envoy-management.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | appmesh.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | appmesh.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | appmesh-envoy-management.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | appmesh-envoy-management.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | appmesh.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | appmesh-envoy-management.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | appmesh-envoy-management.eu-central-2.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | appmesh.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | appmesh.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | appmesh-envoy-management.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | appmesh-envoy-management.il-central-1.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | appmesh.il-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | appmesh.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | appmesh-envoy-management.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | appmesh-envoy-management.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | appmesh.me-south-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | appmesh.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | appmesh.sa-east-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | appmesh-envoy-management.sa-east-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | appmesh-envoy-management.sa-east-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (5)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Backends per virtual node | Each supported Region: 50 | No | Number of backends per virtual node |
| Connected Envoy processes per virtual gateway | Each supported Region: 50 | Yes | Number of concurrently connected Envoy processes per virtual gateway |
| Connected Envoy processes per virtual node | Each supported Region: 50 | Yes | Number of concurrently connected Envoy processes per virtual node |
| Gateway routes per virtual gateway | Each supported Region: 10 | Yes | Number of gateway routes per virtual gateway |
| Meshes per account | Each supported Region: 15 | Yes | Number of meshes per account |

### 066-aws-datasync.pdf

- Status: **ok**, 1 call(s), 30.4 s, in 5,896 / out 4,395 tokens
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

### 091-aws-resource-groups-and-tagging.pdf

- Status: **ok**, 1 call(s), 26.4 s, in 5,957 / out 3,793 tokens
- Service: AWS Resource Groups and Tagging; quota table format: `non_standard`

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
| Canada West (Calgary) | ca-west-1 | resource-groups.ca-west-1.amazonaws.com | HTTPS | ipv4 |
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
| US East (Ohio) | us-east-2 | tagging.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | tagging.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | tagging.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | tagging.us-west-2.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | tagging.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | tagging.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | tagging.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | tagging.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | tagging.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | tagging.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | tagging.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | tagging.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | tagging.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | tagging.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | tagging.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | tagging.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | tagging.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | tagging.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | tagging.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | tagging.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | tagging.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | tagging.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | tagging.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | tagging.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | tagging.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | tagging.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | tagging.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | tagging.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | tagging.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | tagging.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | tagging.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | tagging.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | tagging.me-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | tagging.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | tagging.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | tagging.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (0)

_none_

### 018-amazon-ec2-auto-scaling.pdf

- Status: **ok**, 1 call(s), 33.2 s, in 6,828 / out 4,741 tokens
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
| Canada West (Calgary) | ca-west-1 | autoscaling.ca-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | autoscaling-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | autoscaling-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | autoscaling.ca-west-1.api.aws | HTTPS | dual_stack |
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
| AWS GovCloud (US-East) | us-gov-east-1 | autoscaling.us-gov-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | autoscaling.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | autoscaling.us-gov-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
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

- Status: **ok**, 1 call(s), 23.8 s, in 6,951 / out 3,091 tokens
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

- Status: **ok**, 1 call(s), 49.0 s, in 7,439 / out 6,647 tokens
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

### 042-amazon-redshift.pdf

- Status: **ok**, 1 call(s), 86.7 s, in 11,391 / out 13,100 tokens
- Service: Amazon Redshift; quota table format: `none`

#### Endpoints (253)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | redshift.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | redshift-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | redshift.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | redshift-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | redshift.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | redshift-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | redshift.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | redshift-fips.us-west-2.amazonaws.com | HTTPS | fips |
| Africa (Cape Town) | af-south-1 | redshift.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | redshift.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | redshift.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | redshift.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | redshift.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | redshift.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | redshift.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | redshift.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | redshift.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | redshift.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | redshift.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | redshift.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | redshift.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | redshift.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | redshift.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | redshift.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | redshift-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | redshift.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | redshift-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Europe (Frankfurt) | eu-central-1 | redshift.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | redshift.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | redshift.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | redshift.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | redshift.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | redshift.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | redshift.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | redshift.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | redshift.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | redshift.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | redshift.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | redshift.me-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | redshift.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | redshift.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | redshift-fips.us-gov-east-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | redshift.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | redshift-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | redshift-serverless.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | redshift-serverless-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | redshift-serverless-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | redshift-serverless.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | redshift-serverless.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | redshift-serverless-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | redshift-serverless-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | redshift-serverless.us-east-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | redshift-serverless.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | redshift-serverless-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | redshift-serverless-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | redshift-serverless.us-west-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | redshift-serverless.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | redshift-serverless-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | redshift-serverless-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | redshift-serverless.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | redshift-serverless.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | redshift-serverless.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | redshift-serverless.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | redshift-serverless.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | redshift-serverless.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | redshift-serverless.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | redshift-serverless.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | redshift-serverless.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | redshift-serverless.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | redshift-serverless.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | redshift-serverless.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | redshift-serverless.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | redshift-serverless.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | redshift-serverless.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | redshift-serverless.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | redshift-serverless.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | redshift-serverless.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | redshift-serverless.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | redshift-serverless.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | redshift-serverless.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | redshift-serverless.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | redshift-serverless.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | redshift-serverless.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | redshift-serverless.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | redshift-serverless.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | redshift-serverless.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | redshift-serverless.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | redshift-serverless.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | redshift-serverless.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | redshift-serverless.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | redshift-serverless.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | redshift-serverless-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | redshift-serverless-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | redshift-serverless.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | redshift-serverless.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | redshift-serverless-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | redshift-serverless-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | redshift-serverless.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | redshift-serverless.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | redshift-serverless.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | redshift-serverless.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | redshift-serverless.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | redshift-serverless.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | redshift-serverless.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | redshift-serverless.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | redshift-serverless.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | redshift-serverless.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | redshift-serverless.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | redshift-serverless.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | redshift-serverless.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | redshift-serverless.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | redshift-serverless.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | redshift-serverless.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | redshift-serverless.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | redshift-serverless.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | redshift-serverless.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | redshift-serverless.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | redshift-serverless.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | redshift-serverless.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | redshift-serverless.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | redshift-serverless.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | redshift-serverless.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | redshift-serverless.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | redshift-serverless-fips.us-gov-east-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | redshift-serverless-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | redshift-serverless.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | redshift-serverless.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | redshift-serverless-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | redshift-serverless-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | redshift-serverless.us-gov-west-1.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | redshift-data.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | redshift-data-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | redshift-data.us-east-2.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | redshift-data-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | redshift-data.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | redshift-data-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | redshift-data.us-east-1.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | redshift-data-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | redshift-data.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | redshift-data-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | redshift-data.us-west-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | redshift-data-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | redshift-data.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | redshift-data-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | redshift-data.us-west-2.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | redshift-data-fips.us-west-2.amazonaws.com | HTTPS | fips |
| Africa (Cape Town) | af-south-1 | redshift-data.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | redshift-data.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | redshift-data.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | redshift-data.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | redshift-data.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | redshift-data.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | redshift-data.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | redshift-data.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | redshift-data.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | redshift-data.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | redshift-data.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | redshift-data.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | redshift-data.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | redshift-data.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | redshift-data.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | redshift-data.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | redshift-data.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | redshift-data.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | redshift-data.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | redshift-data.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | redshift-data.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | redshift-data.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | redshift-data.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | redshift-data.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | redshift-data.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | redshift-data.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | redshift-data.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | redshift-data.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | redshift-data.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | redshift-data.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | redshift-data.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | redshift-data-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | redshift-data.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | redshift-data-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | redshift-data.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | redshift-data-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | redshift-data.ca-west-1.api.aws | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | redshift-data-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Europe (Frankfurt) | eu-central-1 | redshift-data.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | redshift-data.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | redshift-data.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | redshift-data.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | redshift-data.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | redshift-data.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | redshift-data.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | redshift-data.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | redshift-data.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | redshift-data.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | redshift-data.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | redshift-data.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | redshift-data.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | redshift-data.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | redshift-data.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | redshift-data.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | redshift-data.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | redshift-data.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | redshift-data.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | redshift-data.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | redshift-data.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | redshift-data.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | redshift-data.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | redshift-data.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | redshift-data.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | redshift-data.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | redshift-data.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | redshift-data-fips.us-gov-east-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | redshift-data.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | redshift-data-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | redshift-data.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | redshift-data-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | redshift-data.us-gov-west-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | redshift-data-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | api.sqlworkbench.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | api.sqlworkbench.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | api.sqlworkbench.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | api.sqlworkbench.us-west-2.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | api.sqlworkbench.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | api.sqlworkbench.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | api.sqlworkbench.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | api.sqlworkbench.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | api.sqlworkbench.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | api.sqlworkbench.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | api.sqlworkbench.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | api.sqlworkbench.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | api.sqlworkbench.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | api.sqlworkbench.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | api.sqlworkbench.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | api.sqlworkbench.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | api.sqlworkbench.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | api.sqlworkbench.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | api.sqlworkbench.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | api.sqlworkbench.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | api.sqlworkbench.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | api.sqlworkbench.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | api.sqlworkbench.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | api.sqlworkbench.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | api.sqlworkbench.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | api.sqlworkbench.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | api.sqlworkbench.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | api.sqlworkbench.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | api.sqlworkbench.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | api.sqlworkbench.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | api.sqlworkbench.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | api.sqlworkbench.me-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | api.sqlworkbench.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | api.sqlworkbench.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | api.sqlworkbench.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (0)

_none_

### 044-amazon-relational-database-service.pdf

- Status: **ok**, 1 call(s), 39.0 s, in 9,180 / out 5,268 tokens
- Service: Amazon Relational Database Service; quota table format: `standard`

#### Endpoints (78)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | rds.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | rds-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | rds.us-east-2.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | rds-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | rds.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | rds-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | rds-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | rds.us-east-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | rds.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | rds.us-west-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | rds-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | rds-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | rds.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | rds-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | rds.us-west-2.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | rds-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| Africa (Cape Town) | af-south-1 | rds.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | rds.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | rds.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | rds.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | rds.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | rds.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | rds.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | rds.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | rds.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | rds.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | rds.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | rds.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | rds.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | rds.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | rds.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | rds.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | rds.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | rds.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | rds.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | rds.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | rds.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | rds.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | rds.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | rds.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | rds.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | rds.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | rds.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | rds.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | rds.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | rds-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | rds-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | rds.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | rds-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Europe (Frankfurt) | eu-central-1 | rds.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | rds.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | rds.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | rds.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | rds.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | rds.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | rds.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | rds.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | rds.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | rds.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | rds.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | rds.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | rds.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | rds.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | rds.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | rds.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | rds.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | rds.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | rds.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | rds.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | rds.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | rds.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | rds.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | rds.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | rds.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | rds.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | rds.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | rds.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | rds.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (27)

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
| Security groups | ap-south-1: 20; Each of the other supported Regions: 25 | Yes | The maximum number of DB security groups |
| Subnets per DB subnet group | Each supported Region: 20 | No | The maximum number of subnets per DB subnet group |

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

### 047-amazon-simple-notification-service.pdf

- Status: **ok**, 1 call(s), 27.1 s, in 8,020 / out 3,898 tokens
- Service: Amazon Simple Notification Service; quota table format: `non_standard`

#### Endpoints (78)

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
| Africa (Cape Town) | af-south-1 | sns.af-south-1.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | sns.ap-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | sns.ap-east-1.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | sns.ap-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | sns.ap-south-2.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | sns.ap-southeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | sns.ap-southeast-3.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | sns.ap-southeast-5.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | sns.ap-southeast-5.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | sns.ap-southeast-4.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | sns.ap-southeast-4.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | sns.ap-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | sns.ap-south-1.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | sns.ap-southeast-6.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | sns.ap-southeast-6.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | sns.ap-northeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | sns.ap-northeast-3.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | sns.ap-northeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | sns.ap-northeast-2.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | sns.ap-southeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | sns.ap-southeast-1.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | sns.ap-southeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | sns.ap-southeast-2.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | sns.ap-east-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | sns.ap-east-2.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | sns.ap-southeast-7.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | sns.ap-southeast-7.api.aws | HTTP and HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | sns.ap-northeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | sns.ap-northeast-1.api.aws | HTTP and HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | sns.ca-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | sns-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | sns.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | sns.ca-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | sns-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | sns.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | sns.eu-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | sns.eu-central-1.api.aws | HTTP and HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | sns.eu-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | sns.eu-west-1.api.aws | HTTP and HTTPS | dual_stack |
| Europe (London) | eu-west-2 | sns.eu-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (London) | eu-west-2 | sns.eu-west-2.api.aws | HTTP and HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | sns.eu-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | sns.eu-south-1.api.aws | HTTP and HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | sns.eu-west-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | sns.eu-west-3.api.aws | HTTP and HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | sns.eu-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | sns.eu-south-2.api.aws | HTTP and HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | sns.eu-north-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | sns.eu-north-1.api.aws | HTTP and HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | sns.eu-central-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | sns.eu-central-2.api.aws | HTTP and HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | sns.il-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | sns.il-central-1.api.aws | HTTP and HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | sns.mx-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | sns.mx-central-1.api.aws | HTTP and HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | sns.me-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | sns.me-south-1.api.aws | HTTP and HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | sns.me-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | sns.me-central-1.api.aws | HTTP and HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | sns.sa-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | sns.sa-east-1.api.aws | HTTP and HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | sns.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | sns.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | sns.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | sns.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (0)

_none_

### 026-amazon-eventbridge.pdf

- Status: **ok**, 1 call(s), 41.2 s, in 6,912 / out 5,577 tokens
- Service: Amazon EventBridge; quota table format: `standard`

#### Endpoints (84)

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
| US West (N. California) | us-west-1 | events.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | events-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | events-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | events.us-west-1.api.aws | HTTPS | dual_stack |
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
| Canada West (Calgary) | ca-west-1 | events.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | events-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | events-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | events.ca-west-1.api.aws | HTTPS | dual_stack |
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
| Invocations throttle limit in transactions per second | us-east-1: 18,750 per second; us-east-2: 4,500 per second; us-west-1: 2,250 per second; us-west-2: 18,750 per second; ap-east-1: 1,100 per second; ap-northeast-1: 2,250 per second; ap-northeast-2: 1,100 per second; ap-south-1: 1,100 per second; ap-southeast-1: 2,250 per second; ap-southeast-2: 2,250 per second; ca-central-1: 1,100 per second; eu-central-1: 4,500 per second; eu-north-1: 1,100 per second; eu-south-2: 4,500 per second; eu-west-1: 18,750 per second; eu-west-2: 2,250 per second; eu-west-3: 1,100 per second; sa-east-1: 1,100 per second; Each of the other supported Regions: 750 per second | Yes | An invocation is an event matching a rule and being sent on to the rules targets. After the limit is reached, the invocations are throttled ; that is, they still happen but they are delayed. |
| Number of rules | af-south-1: 100; eu-south-1: 100; Each of the other supported Regions: 300 | Yes | Maximum number of rules an account can have per event bus |
| PutEvents throttle limit in transactions per second | us-east-1: 10,000 per second; us-east-2: 2,400 per second; us-west-1: 1,200 per second; us-west-2: 10,000 per second; ap-east-1: 600 per second; ap-northeast-1: 1,200 per second; ap-northeast-2: 600 per second; ap-south-1: 600 per second; ap-southeast-1: 1,200 per second; ap-southeast-2: 1,200 per second; ca-central-1: 600 per second; eu-central-1: 2,400 per second; eu-north-1: 600 per second; eu-south-2: 2,400 per second; eu-west-1: 10,000 per second; eu-west-2: 1,200 per second; eu-west-3: 600 per second; sa-east-1: 600 per second; Each of the other supported Regions: 400 per second | Yes | Maximum number of requests per second for PutEvents API. Additional requests are throttled. |
| Rate of invocations per API destination | Each supported Region: 300 per second | Yes | The maximum number of invocations per second to send to each API destination endpoint per account per Region. Once the quota is met, future invocations to that API endpoint are throttled. The invocations will still occur, but are delayed. |
| Targets per rule | Each supported Region: 5 | No | Maximum number of targets that can be associated with a rule |
| Throttle limit in transactions per second for control plane APIs | Each supported Region: 50 per second | No | Maximum number of requests per second for EventBridge control plane API operations. Additional requests are throttled. |
| UpdateEndpoint throttle limit in transactions per second | Each supported Region: 5 per second | No | The maximum number of requests per second for UpdateEndpoint API. Additional requests are throttled. |
| [EventsV2] Combined ingestion throughput and count per Event Group per second | Each supported Region: 1,500 per second | No | The maximum event throughput per Event Group per Second. Counted as the sum of (number of events) + (total size of those events in KB) delivered to a given event group within any one-second window. |
| [EventsV2] Event Buses | Each supported Region: 5 | Yes | The maximum number of V2 Event Buses owned by this account per Region. Does not include buses shared with this account. |

### 092-aws-secrets-manager.pdf

- Status: **ok**, 1 call(s), 25.6 s, in 7,107 / out 3,343 tokens
- Service: AWS Secrets Manager; quota table format: `standard`

#### Endpoints (44)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | secretsmanager.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | secretsmanager-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | secretsmanager.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | secretsmanager-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | secretsmanager.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | secretsmanager-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | secretsmanager.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | secretsmanager-fips.us-west-2.amazonaws.com | HTTPS | fips |
| Africa (Cape Town) | af-south-1 | secretsmanager.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | secretsmanager.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | secretsmanager.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | secretsmanager.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | secretsmanager.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | secretsmanager.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | secretsmanager.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | secretsmanager.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | secretsmanager.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | secretsmanager.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | secretsmanager.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | secretsmanager.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | secretsmanager.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | secretsmanager.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | secretsmanager.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | secretsmanager.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | secretsmanager-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | secretsmanager.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | secretsmanager-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Europe (Frankfurt) | eu-central-1 | secretsmanager.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | secretsmanager.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | secretsmanager.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | secretsmanager.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | secretsmanager.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | secretsmanager.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | secretsmanager.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | secretsmanager.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | secretsmanager.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | secretsmanager.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | secretsmanager.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | secretsmanager.me-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | secretsmanager.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | secretsmanager.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | secretsmanager-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | secretsmanager.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | secretsmanager-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |

#### Quotas (18)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Combined rate of DeleteResourcePolicy, GetResourcePolicy, PutResourcePolicy, and ValidateResourcePolicy API requests | Each supported Region: 50 per second | No | The maximum transactions per second for DeleteResourcePolicy, GetResourcePolicy, PutResourcePolicy, and ValidateResourcePolicy API requests combined. |
| Combined rate of PutSecretValue, RemoveRegionsFromReplication, ReplicateSecretToRegion, StopReplicationToReplica, UpdateSecret, and UpdateSecretVersionStage API requests | Each supported Region: 50 per second | No | The maximum transactions per second for PutSecretValue, RemoveRegionsFromReplication, ReplicateSecretToRegion, StopReplicationToReplica, UpdateSecret, and UpdateSecretVersionStage API requests combined. |
| Combined rate of RestoreSecret API requests | Each supported Region: 50 per second | No | The maximum transactions per second for RestoreSecret API requests. |
| Combined rate of RotateSecret and CancelRotateSecret API requests | Each supported Region: 50 per second | No | The maximum transactions per second for RotateSecret and CancelRotateSecret API requests combined. |
| Combined rate of TagResource and UntagResource API requests | Each supported Region: 50 per second | No | The maximum transactions per second for TagResource and UntagResource API requests combined. |
| Rate of BatchGetSecretValue API requests | Each supported Region: 100 per second | No | The maximum transactions per second for BatchGetSecretValue API requests. |
| Rate of CreateSecret API requests | Each supported Region: 50 per second | No | The maximum transactions per second for CreateSecret API requests. |
| Rate of DeleteSecret API requests | Each supported Region: 50 per second | No | The maximum transactions per second for DeleteSecret API requests. |
| Rate of DescribeSecret API requests | Each supported Region: 40,000 per second | No | The maximum transactions per second for DescribeSecret API requests. |
| Rate of GetRandomPassword API requests | Each supported Region: 50 per second | No | The maximum transactions per second for GetRandomPassword API requests. |
| Rate of GetSecretValue API requests | Each supported Region: 10,000 per second | No | The maximum transactions per second for GetSecretValue API requests. |
| Rate of ListSecretVersionIds API requests | Each supported Region: 50 per second | No | The maximum transactions per second for ListSecretVersionIds API requests. |
| Rate of ListSecrets API requests | Each supported Region: 100 per second | No | The maximum transactions per second for ListSecrets API requests. |
| Resource-based policy length | Each supported Region: 20,480 | No | The maximum number of characters in a resource-based permissions policy attached to a secret. |
| Secret value size | Each supported Region: 65,536 Bytes | No | The maximum size of an encrypted secret value. If the secret value is a string, then this is the number of characters permitted in the secret value. |
| Secrets | Each supported Region: 500,000 | No | The maximum number of secrets in each AWS Region of this AWS account. |
| Staging labels attached across all versions of a secret | Each supported Region: 20 | No | The maximum number of staging labels attached across all versions of a secret. |
| Versions per secret | Each supported Region: 100 | No | The maximum number of versions of a secret. |

### 023-amazon-elastic-kubernetes-service.pdf

- Status: **ok**, 1 call(s), 31.2 s, in 6,947 / out 4,359 tokens
- Service: Amazon Elastic Kubernetes Service; quota table format: `standard`

#### Endpoints (76)

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
| Canada West (Calgary) | ca-west-1 | eks.ca-west-1.amazonaws.com | HTTPS | ipv4 |
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
| US East (Ohio) | us-east-2 | eks-auth.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | eks-auth.us-east-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | eks-auth.us-west-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | eks-auth.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | eks-auth.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | eks-auth.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | eks-auth.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | eks-auth.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | eks-auth.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | eks-auth.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | eks-auth.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | eks-auth.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | eks-auth.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | eks-auth.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | eks-auth.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | eks-auth.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | eks-auth.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | eks-auth.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | eks-auth.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | eks-auth.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | eks-auth.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | eks-auth.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | eks-auth.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | eks-auth.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | eks-auth.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | eks-auth.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | eks-auth.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | eks-auth.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | eks-auth.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | eks-auth.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | eks-auth.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | eks-auth.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | eks-auth.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | eks-auth.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | eks-auth.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | eks-auth.us-gov-west-1.api.aws | HTTPS | dual_stack |

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

- Status: **ok**, 1 call(s), 30.0 s, in 9,989 / out 4,208 tokens
- Service: AWS IAM Identity Center; quota table format: `standard`

#### Endpoints (78)

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
| Canada West (Calgary) | ca-west-1 | sso.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | sso-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | sso.ca-west-1.api.aws | HTTPS | dual_stack |
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

- Status: **ok**, 1 call(s), 60.7 s, in 10,864 / out 9,074 tokens
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

### 086-aws-lambda.pdf

- Status: **ok**, 1 call(s), 65.6 s, in 11,210 / out 8,470 tokens
- Service: AWS Lambda; quota table format: `standard`

#### Endpoints (78)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | lambda.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | lambda-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | lambda.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | lambda.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | lambda-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | lambda.us-east-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | lambda.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | lambda-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | lambda.us-west-1.api.aws | HTTPS | dual_stack |
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
| Canada West (Calgary) | ca-west-1 | lambda.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | lambda.ca-west-1.api.aws | HTTPS | dual_stack |
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
| Asynchronous invocation request throughput on Lambda Managed Instances | Each supported Region: 5 Megabytes/ Second | Yes | The maximum invoke request throughput (MB/s) for asynchronous invocations on Lambda Managed Instances. Asynchronous invocations occur when Lambda functions are invoked by services such as Amazon S3 or Amazon SNS. |
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
| DynamoDB Event Source Mapping throughput on Lambda Managed Instances | Each supported Region: 10 Megabytes/ Second | Yes | The maximum data throughput (MB/s) per DynamoDB event source mapping on Lambda Managed Instances. |
| Elastic network interfaces per VPC | Each supported Region: 3,000 | Yes | The maximum number of network interfaces that Lambda creates for a VPC with functions attached. Lambda creates a network interface for each combination of subnet and security group that functions connect to. |
| Endpoints per Web Function | Each supported Region: 10 | No | The maximum number of endpoints allowed per Lambda Web Function. |
| Environment variable size | Each supported Region: 4 Kilobytes | No | The maximum combined size of environment variables that are configured on a function. |
| File descriptors | Each supported Region: 1,024 | No | The maximum number of file descriptors that a function can have open. |
| Function and layer storage | Each supported Region: 300 Gigabytes | Yes | The amount of storage thats available for deployment packages and layer archives in the current Region. |
| Function invocation rate to initiate durable executions | us-east-1: 6,000; us-west-2: 6,000; eu-west-1: 6,000; Each of the other supported Regions: 3,000 | Yes | The maximum number of new durable executions that you can initiate per second. |
| Function layers | Each supported Region: 5 | No | The maximum number of layers that you can add to your function. |
| Function resource-based policy | Each supported Region: 20 Kilobytes | No | The maximum combined size of resource-based policies that are configured on a function. |
| Function timeout | Each supported Region: 900 | No | The maximum timeout that you can configure for a function. |
| Function versions per capacity provider | Each supported Region: 100 | No | The maximum number of function versions per capacity provider. |
| Kafka Event Source Mappings in default mode on Lambda Managed Instances | Each supported Region: 100 | No | The maximum number of Kafka event source mappings in default mode on Lambda Managed Instances. |
| Kafka Stream Event Source Mapping throughput in non-provisioned mode | Each supported Region: 5 Megabytes/ Second | No | The maximum data throughput (MB/s) per Kafka Stream event source mapping in non-provisioned mode. |
| Kinesis Event Source Mapping throughput on Lambda Managed Instances | Each supported Region: 25 Megabytes/ Second | Yes | The maximum data throughput (MB/s) per Kinesis event source mapping on Lambda Managed Instances. |
| Max Execution Duration of a MicroVM (in Hours) | Each supported Region: 8 | No | The maximum execution duration of a MicroVM (in Hours). |
| Max allocated ARM_64 MicroVM memory | us-east-1: 1,024 Gigabytes; us-east-2: 1,024 Gigabytes; us-west-2: 1,024 Gigabytes; ap-northeast-1: 1,024 Gigabytes; Each of the other supported Regions: 400 Gigabytes | Yes | The maximum total configured baseline memory across all concurrently running ARM_64 MicroVMs, per account, per region. Individual MicroVMs can burst up to 4x their configured baseline memory. |
| Maximum number of durable operations per durable execution | Each supported Region: 30,000 | No | The maximum number of durable operations (including customer-initiated operations and automatic retries) that trigger state persistence within a single durable execution. |
| Maximum running durable executions | us-east-1: 10,000,000; us-west-2: 10,000,000; eu-west-1: 10,000,000; Each of the other supported Regions: 5,000,000 | Yes | The maximum number of durable executions that can be running simultaneously in the current region. |
| Network bandwidth per execution environment | Each supported Region: 625 Megabits/Second | Yes | The maximum sustained network bandwidth, in megabits per second, for a Lambda functions execution environment that is not attached to a VPC. |
| Network connectors | Each supported Region: 1,000 | No | Number of Network Connectors per account |
| Number of MicroVM images | Each supported Region: 100 Count | Yes | Number of MicroVM images per account per region |
| Number of concurrent MicroVM image builds | us-east-1: 10 Count; us-east-2: 10 Count; us-west-2: 10 Count; ap-northeast-1: 10 Count; Each of the other supported Regions: 5 Count | Yes | Number of concurrent MicroVM image builds per account per region |
| Processes and threads | Each supported Region: 1,024 | No | The maximum combined number of processes and threads that a function can have open. |
| RPS per 16 vCPU MicroVm | Each supported Region: 160 Count | No | Maximum number of requests per second per MicroVM with 16 vCPUs / 32 GB. |
| RPS per 4 vCPU MicroVm | Each supported Region: 40 Count | No | Maximum number of requests per second per MicroVM with 4 vCPUs / 8 GB. |
| Rate of CheckpointDurableExecution API requests | us-east-1: 20,000; us-west-2: 20,000; eu-west-1: 20,000; Each of the other supported Regions: 10,000 | Yes | The maximum number of CheckpointDurableExecution API requests per second. |
| Rate of CreateMicrovmAuthToken API requests | Each supported Region: 50 | Yes | The maximum number of CreateMicrovmAuthToken API requests per second. |
| Rate of CreateMicrovmShellAuthToken API requests | Each supported Region: 5 | Yes | The maximum number of CreateMicrovmShellAuthToken API requests per second in this account in the current Region. |
| Rate of GetDurableExecution API requests | Each supported Region: 30 | Yes | The maximum number of GetDurableExecution API requests per second. |
| Rate of GetDurableExecutionHistory API requests | Each supported Region: 15 | Yes | The maximum number of GetDurableExecutionHistory API requests per second. |
| Rate of GetDurableExecutionState API requests | us-east-1: 20,000; us-west-2: 20,000; eu-west-1: 20,000; Each of the other supported Regions: 10,000 | Yes | The maximum number of GetDurableExecutionState API requests per second. |
| Rate of GetFunction API requests | Each supported Region: 100 | No | The maximum number of GetFunction API requests per second. |
| Rate of GetMicrovm API requests | Each supported Region: 100 | Yes | The maximum number of GetMicrovm API requests per second. |
| Rate of GetPolicy API requests | Each supported Region: 15 | No | The maximum number of GetPolicy API requests per second. |
| Rate of ListDurableExecutionsByFunction API requests | Each supported Region: 15 | Yes | The maximum number of ListDurableExecutionsByFunction API requests per second. |
| Rate of ResumeMicrovm API requests | Each supported Region: 5 | Yes | The maximum number of ResumeMicrovm API requests per second. |
| Rate of RunMicrovm API requests | Each supported Region: 5 | Yes | The maximum number of RunMicrovm API requests per second |
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
| SQS Event Source Mapping throughput in default mode on Lambda Managed Instances | Each supported Region: 5 Megabytes/ Second | No | The maximum data throughput (MB/s) per SQS event source mapping in default mode on Lambda Managed Instances. |
| Synchronous payload | Each supported Region: 6 Megabytes | No | The maximum size of an incoming synchronous invocation request or outgoing response. |

### 004-amazon-athena.pdf

- Status: **ok**, 1 call(s), 57.9 s, in 11,605 / out 8,129 tokens
- Service: Amazon Athena; quota table format: `standard`

#### Endpoints (88)

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
| US West (N. California) | us-west-1 | athena.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | athena-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | athena-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | athena.us-west-1.api.aws | HTTPS | dual_stack |
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
| Asia Pacific (New Zealand) | ap-southeast-6 | athena.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | athena.ap-southeast-6.api.aws | HTTPS | dual_stack |
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
| Canada West (Calgary) | ca-west-1 | athena.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | athena-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | athena-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | athena.ca-west-1.api.aws | HTTPS | dual_stack |
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
| Burst multiplier quota for StartQueryExecution API | us-east-1: 5; us-east-2: 5; us-west-2: 5; ap-northeast-1: 5; eu-central-1: 5; eu-west-1: 5; Each of the other supported Regions: 4 | No | Multiplier factor to scale burst capacity for StartQueryExecution API based on the rate quota (Burst = Rate * BurstMultiplierQuota). StartQueryExecution Burst is the maximum number of StartQueryExecution API tokens you can accumulate in the account in the region |
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

- Status: **ok**, 1 call(s), 32.7 s, in 15,877 / out 6,284 tokens
- Service: Amazon DynamoDB; quota table format: `standard`

#### Endpoints (94)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | dynamodb.us-east-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | account-id.ddb.us-east-2.api.aws | HTTP and HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | dynamodb.us-east-2.api.aws | HTTP and HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | dynamodb-fips.us-east-2.api.aws | HTTP and HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | dynamodb-fips.us-east-2.amazonaws.com | HTTP and HTTPS | fips |
| US East (Ohio) | us-east-2 | account-id.ddb.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | dynamodb.us-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | dynamodb-fips.us-east-1.amazonaws.com | HTTP and HTTPS | fips |
| US East (N. Virginia) | us-east-1 | account-id.ddb.us-east-1.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | account-id.ddb.us-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | dynamodb.us-east-1.api.aws | HTTP and HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | dynamodb-fips.us-east-1.api.aws | HTTP and HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | dynamodb.us-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| US West (N. California) | us-west-1 | dynamodb.us-west-1.api.aws | HTTP and HTTPS | dual_stack |
| US West (N. California) | us-west-1 | dynamodb-fips.us-west-1.api.aws | HTTP and HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | dynamodb-fips.us-west-1.amazonaws.com | HTTP and HTTPS | fips |
| US West (N. California) | us-west-1 | account-id.ddb.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | account-id.ddb.us-west-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | dynamodb.us-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | account-id.ddb.us-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | dynamodb-fips.us-west-2.amazonaws.com | HTTP and HTTPS | fips |
| US West (Oregon) | us-west-2 | dynamodb.us-west-2.api.aws | HTTP and HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | account-id.ddb.us-west-2.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | dynamodb-fips.us-west-2.api.aws | HTTP and HTTPS | fips_dual_stack |
| Africa (Cape Town) | af-south-1 | dynamodb.af-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | account-id.ddb.af-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | dynamodb.ap-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | account-id.ddb.ap-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | dynamodb.ap-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | account-id.ddb.ap-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | dynamodb.ap-southeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | account-id.ddb.ap-southeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | dynamodb.ap-southeast-5.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | account-id.ddb.ap-southeast-5.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | dynamodb.ap-southeast-4.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | account-id.ddb.ap-southeast-4.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | dynamodb.ap-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | account-id.ddb.ap-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | dynamodb.ap-southeast-6.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | account-id.ddb.ap-southeast-6.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | dynamodb.ap-northeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | account-id.ddb.ap-northeast-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | dynamodb.ap-northeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | account-id.ddb.ap-northeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | dynamodb.ap-southeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | account-id.ddb.ap-southeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | dynamodb.ap-southeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | account-id.ddb.ap-southeast-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | dynamodb.ap-east-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | account-id.ddb.ap-east-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | dynamodb.ap-southeast-7.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | account-id.ddb.ap-southeast-7.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | dynamodb.ap-northeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | account-id.ddb.ap-northeast-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | dynamodb.ca-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | account-id.ddb.ca-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | dynamodb-fips.ca-central-1.amazonaws.com | HTTP and HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | dynamodb.ca-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | dynamodb-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | account-id.ddb.ca-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | dynamodb.eu-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | account-id.ddb.eu-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | dynamodb.eu-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | account-id.ddb.eu-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (London) | eu-west-2 | dynamodb.eu-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (London) | eu-west-2 | account-id.ddb.eu-west-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | dynamodb.eu-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | account-id.ddb.eu-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | dynamodb.eu-west-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | account-id.ddb.eu-west-3.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | dynamodb.eu-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | account-id.ddb.eu-south-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | dynamodb.eu-north-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | account-id.ddb.eu-north-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | dynamodb.eu-central-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | account-id.ddb.eu-central-2.amazonaws.com | HTTP and HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | dynamodb.il-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | account-id.ddb.il-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | dynamodb.mx-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | account-id.ddb.mx-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | dynamodb.me-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | account-id.ddb.me-south-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | dynamodb.me-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | account-id.ddb.me-central-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | dynamodb.sa-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | account-id.ddb.sa-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | dynamodb.us-gov-east-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | dynamodb-fips.us-gov-east-1.amazonaws.com | HTTP and HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | dynamodb.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | dynamodb-fips.us-gov-east-1.api.aws | HTTP and HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | dynamodb.us-gov-west-1.amazonaws.com | HTTP and HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | dynamodb-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | dynamodb.us-gov-west-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | dynamodb-fips.us-gov-west-1.amazonaws.com | HTTP and HTTPS | fips |

#### Quotas (13)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Account-level read throughput limit (Provisioned mode) | Each supported Region: 80,000 | Yes | The maximum number of read capacity units allocated for the account; applicable only for tables (including all associated global secondary indexes) in provisioned read/write capacity mode. For more information, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html#default-limits-throughput-capacity-modes |
| Account-level write throughput limit (Provisioned mode) | Each supported Region: 80,000 | Yes | The maximum number of write capacity units allocated for the account; applicable only for tables (including all associated global secondary indexes) in provisioned read/write capacity mode. For more information, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html#default-limits-throughput-capacity-modes |
| Concurrent control plane operations | Each supported Region: 500 | Yes | The maximum number of allowed concurrent control plane operations. For more information, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html#limits-api |
| Global Secondary Indexes per table | Each supported Region: 20 | Yes | The maximum number of global secondary indexes that can be created for a table. For more information, see, https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html#limits-secondary-indexes |
| Maximum Incremental Export concurrent data size | Each supported Region: 100 Terabytes | Yes | Maximum limit on size of in flight incremental export requests. For more information, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html#limits-table-export |
| Maximum Incremental Export concurrent requests | Each supported Region: 300 | Yes | Maximum limit on number of in flight incremental export requests. For more information, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html#limits-table-export |
| Maximum Incremental Export period window | Each supported Region: 24 | No | The limit on the maximum export period (in hours) for an incremental export request. For more information, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html#limits-table-export |
| Maximum number of tables | Each supported Region: 2,500 | Yes | The maximum number of tables that can be created per region. For more information, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html#limits-tables |
| Minimum Incremental Export period window | Each supported Region: 15 | No | The limit on the minimum export period (in minutes) for an incremental export request. For more information, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html#limits-table-export |
| Provisioned capacity decreases per day | Each supported Region: 27 | Yes | A decrease is allowed up to four times any time per day (GMT time zone). Also, if there was no decrease in the past hour, an additional decrease is allowed, effectively bringing the maximum number of decreases in a day to 27 times. For more information, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html |
| Table-level read throughput limit | Each supported Region: 40,000 | Yes | The maximum number of read throughput allocated for a table or global secondary index. For more information, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html#default-limits-throughput-capacity-modes |
| Table-level write throughput limit | Each supported Region: 40,000 | Yes | The maximum number of write throughput allocated for a table or global secondary index. For more information, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html#default-limits-throughput-capacity-modes |
| Write throughput limit for DynamoDB Streams (Provisioned mode) | Each supported Region: 40,000 | Yes | The maximum number of write capacity units allowed for a table with streams enabled; applicable only for tables in provisioned read/write capacity mode. Other quotas might also apply. For more information, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html#limits-dynamodb-streams |

### 095-aws-step-functions.pdf

- Status: **ok**, 1 call(s), 86.7 s, in 13,824 / out 12,474 tokens
- Service: AWS Step Functions; quota table format: `standard`

#### Endpoints (172)

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
| US West (N. California) | us-west-1 | states.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | sync-states.us-west-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | sync-states-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | sync-states-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | states-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | states-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | sync-states.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | states.us-west-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | states.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | sync-states.us-west-2.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | sync-states-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | sync-states-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | states-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | states-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | sync-states.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | states.us-west-2.api.aws | HTTPS | dual_stack |
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
| Canada West (Calgary) | ca-west-1 | states.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | sync-states.ca-west-1.api.aws | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | sync-states-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | sync-states-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | states-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | sync-states.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | states-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | states.ca-west-1.api.aws | HTTPS | dual_stack |
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
| AWS GovCloud (US-West) | us-gov-west-1 | sync-states-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | sync-states.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | states-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |

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
| DescribeActivity throttle token bucket size | Each supported Region: 200 | Yes | The maximum number of DescribeActivity calls that you can make per second. |
| DescribeActivity throttle token refill rate per second | Each supported Region: 20 | Yes | The token refill rate per second of DescribeActivity calls. |
| DescribeExecution throttle token bucket size | Each supported Region: 300 | Yes | The maximum number of DescribeExecution calls that you can make per second. |
| DescribeExecution throttle token refill rate per second | Each supported Region: 50 | Yes | The token refill rate per second of DescribeExecution calls. |
| DescribeMapRun throttle token bucket size | Each supported Region: 200 | Yes | The maximum number of DescribeMapRun calls that you can make per second. |
| DescribeMapRun throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for DescribeMapRun calls. |
| DescribeStateMachine throttle token bucket size | Each supported Region: 200 | Yes | The maximum number of DescribeStateMachine calls that you can make per second. |
| DescribeStateMachine throttle token refill rate per second | Each supported Region: 20 | Yes | The token refill rate per second of DescribeStateMachine calls. |
| DescribeStateMachineAlias throttle token bucket size | Each supported Region: 200 | Yes | The maximum number of DescribeStateMachineAlias calls that you can make per second. |
| DescribeStateMachineAlias throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for DescribeStateMachineAlias calls. |
| DescribeStateMachineForExecution throttle token bucket size | Each supported Region: 200 | Yes | The maximum number of DescribeStateMachineForExecution calls that you can make per second. |
| DescribeStateMachineForExecution throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second of DescribeStateMachineForExecution calls. |
| Execution history retention time | Each supported Region: 90 | Yes | The maximum time (in days) for which the execution history is stored after an execution completes. |
| Execution history size | Each supported Region: 25,000 | No | The maximum number of events in a state machines execution history. |
| Execution idle time | Each supported Region: 1 | No | The maximum amount of time (in years) a state machine execution can remain idle. |
| Execution time | Each supported Region: 1 | No | The maximum amount of time (in years) for which an execution can run. |
| GetActivityTask throttle token bucket size | us-east-1: 3,000; us-west-2: 3,000; eu-west-1: 3,000; Each of the other supported Regions: 1,500 | Yes | The maximum number of GetActivityTask calls that you can make per second. |
| GetActivityTask throttle token refill rate per second | us-east-1: 500; us-west-2: 500; eu-west-1: 500; Each of the other supported Regions: 300 | Yes | The token refill rate per second of GetActivityTask calls. |
| GetExecutionHistory throttle token bucket size | Each supported Region: 400 | Yes | The maximum number of GetExecutionHistory calls that you can make per second. |
| GetExecutionHistory throttle token refill rate per second | Each supported Region: 20 | Yes | The token refill rate per second of GetExecutionHistory calls. |
| Input file data size for a Map Run | Each supported Region: 10 Gigabytes | No | Input file data size for a Map Run |
| Input or result data size in task state or execution | Each supported Region: 262,144 Bytes | No | The maximum size of input or output data (in bytes) as a UTF-8 encoded string. This quota affects tasks (activity, Lambda function, or integrated service), state or execution output, and input data when scheduling a task, entering a state, or starting an execution. |
| ListActivities throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of ListActivities calls that you can make per second. |
| ListActivities throttle token refill rate per second | us-east-1: 10; us-west-2: 10; eu-west-1: 10; Each of the other supported Regions: 5 | Yes | The token refill rate per second of ListActivities calls. |
| ListExecutions throttle token bucket size | us-east-1: 200; us-west-2: 200; eu-west-1: 200; Each of the other supported Regions: 100 | Yes | The maximum number of ListExecutions calls that you can make per second. |
| ListExecutions throttle token refill rate per second | us-east-1: 5; us-west-2: 5; eu-west-1: 5; Each of the other supported Regions: 2 | Yes | The token refill rate per second of ListExecutions calls. |
| ListMapRuns throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of ListMapRuns calls that you can make per second. |
| ListMapRuns throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for ListMapRuns calls. |
| ListStateMachineAliases throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of ListStateMachineAliases calls that you can make per second. |
| ListStateMachineAliases throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for ListStateMachineAliases calls. |
| ListStateMachineVersions throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of ListStateMachineVersions calls that you can make per second. |
| ListStateMachineVersions throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for ListStateMachineVersions calls. |
| ListStateMachines throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of ListStateMachine calls that you can make per second. |
| ListStateMachines throttle token refill rate per second | Each supported Region: 5 | Yes | The token refill rate per second of ListStateMachines calls. |
| ListTagsForResource throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of ListTagsForResource calls that you can make per second. |
| ListTagsForResource throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second of ListTagsForResource calls. |
| Maximum Concurrency | Each supported Region: 10,000 | No | The maximum number of parallel Map Run child executions |
| Maximum Number of Items Read per Map Run | Each supported Region: 100,000,000 | No | Maximum Number of Items Read per Map Run |
| Maximum redrives of a Map Run | Each supported Region: 1,000 | No | Maximum redrives of a Map Run |
| Maximum size of CSV headers | Each supported Region: 10 Kilobytes | No | Maximum size of CSV headers |
| Open executions | Each supported Region: 1,000,000 | Yes | The maximum number of open executions per account in the current Region. |
| PublishStateMachineVersion throttle token bucket size | Each supported Region: 100 | Yes | The maximum number of PublishStateMachineVersion calls that you can make per second. |
| PublishStateMachineVersion throttle token refill rate per second | Each supported Region: 1 | Yes | The token refill rate per second for PublishStateMachineVersion calls. |
| Published state machine versions per state machine | Each supported Region: 1,000 | Yes | The maximum number of versions that can be published for a state machine. |
| RedriveExecution throttle token bucket size | Each supported Region: 800 | Yes | The maximum number of RedriveExecution calls that you can make per second. |
| RedriveExecution throttle token refill rate per second | Each supported Region: 150 | Yes | The token refill rate per second for RedriveExecution calls. |
| Registered activities | Each supported Region: 100,000 | Yes | The maximum number of activities that you can create in this account in the current Region. |
| Registered state machines | Each supported Region: 100,000 | Yes | The maximum number of state machines that you can create in this account in the current Region. |
| Request size | Each supported Region: 1 Megabytes | No | The total data size in Megabytes per Step Functions API request, including the request header and all other associated request data. |
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
| StartMapRun throttle token bucket size | Each supported Region: 25 | No | The maximum number of StartMapRun calls that you can make per second. |
| StartMapRun throttle token refill rate per second | Each supported Region: 25 | No | The token refill rate per second of StartMapRun calls |
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

### 025-amazon-emr.pdf

- Status: **ok**, 1 call(s), 85.1 s, in 17,232 / out 11,995 tokens
- Service: Amazon EMR; quota table format: `standard`

#### Endpoints (78)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | elasticmapreduce.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | elasticmapreduce-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | elasticmapreduce.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | elasticmapreduce.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | elasticmapreduce-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | elasticmapreduce.us-east-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | elasticmapreduce.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | elasticmapreduce-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | elasticmapreduce.us-west-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | elasticmapreduce.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | elasticmapreduce-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | elasticmapreduce.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | elasticmapreduce.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | elasticmapreduce.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | elasticmapreduce.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | elasticmapreduce.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | elasticmapreduce.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | elasticmapreduce.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | elasticmapreduce.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | elasticmapreduce.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | elasticmapreduce.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | elasticmapreduce.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | elasticmapreduce.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | elasticmapreduce.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | elasticmapreduce.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | elasticmapreduce.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | elasticmapreduce.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | elasticmapreduce.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | elasticmapreduce.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | elasticmapreduce.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | elasticmapreduce.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | elasticmapreduce.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | elasticmapreduce.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | elasticmapreduce.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | elasticmapreduce.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | elasticmapreduce.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | elasticmapreduce.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | elasticmapreduce.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | elasticmapreduce.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | elasticmapreduce.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | elasticmapreduce.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | elasticmapreduce.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | elasticmapreduce.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | elasticmapreduce-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | elasticmapreduce.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | elasticmapreduce.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | elasticmapreduce-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | elasticmapreduce.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | elasticmapreduce.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | elasticmapreduce.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | elasticmapreduce.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | elasticmapreduce.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | elasticmapreduce.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | elasticmapreduce.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | elasticmapreduce.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | elasticmapreduce.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | elasticmapreduce.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | elasticmapreduce.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | elasticmapreduce.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | elasticmapreduce.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | elasticmapreduce.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | elasticmapreduce.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | elasticmapreduce.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | elasticmapreduce.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | elasticmapreduce.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | elasticmapreduce.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | elasticmapreduce.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | elasticmapreduce.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | elasticmapreduce.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | elasticmapreduce.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | elasticmapreduce.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | elasticmapreduce.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | elasticmapreduce.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | elasticmapreduce.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | elasticmapreduce.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | elasticmapreduce.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | elasticmapreduce.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | elasticmapreduce.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (106)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| EMR WAL workspaces | Each supported Region: 20 | No | The maximum number of Amazon EMR write-ahead log (EMR WAL) workspaces that can be used at the same time in this account in the current Region. |
| Replenishment rate of AddInstanceFleet calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the AddInstanceFleet bucket |
| Replenishment rate of AddInstanceGroups calls | Each supported Region: 0.2 | Yes | The Rate at which tokens are added to the AddInstanceGroups bucket |
| Replenishment rate of AddJobFlowSteps calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the AddJobFlowSteps bucket |
| Replenishment rate of AddTags calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the AddTags bucket |
| Replenishment rate of CancelJobRun calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the CancelJobRun bucket |
| Replenishment rate of CancelSteps calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the CancelSteps bucket |
| Replenishment rate of CreateManagedCluster calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the CreateManagedCluster bucket |
| Replenishment rate of CreateSecurityConfiguration calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the CreateSecurityConfiguration bucket |
| Replenishment rate of DeleteSecurityConfiguration calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the DeleteSecurityConfiguration bucket |
| Replenishment rate of DescribeCluster calls | Each supported Region: 1 | Yes | The Rate at which tokens are added to the DescribeCluster bucket |
| Replenishment rate of DescribeJobFlows calls | Each supported Region: 0.2 | Yes | The Rate at which tokens are added to the DescribeJobFlows bucket |
| Replenishment rate of DescribeJobRun calls | Each supported Region: 2 | Yes | The Rate at which tokens are added to the DescribeJobRun bucket |
| Replenishment rate of DescribeManagedCluster calls | Each supported Region: 2 | Yes | The Rate at which tokens are added to the DescribeManagedCluster bucket |
| Replenishment rate of DescribeSecurityConfiguration calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the DescribeSecurityConfiguration bucket |
| Replenishment rate of DescribeStep calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the DescribeStep bucket |
| Replenishment rate of GetAutoTerminationPolicy calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the GetAutoTerminationPolicy bucket |
| Replenishment rate of GetBlockPublicAccessConfiguration calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the GetBlockPublicAccessConfiguration bucket |
| Replenishment rate of GetClusterSessionCredentials calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the GetClusterSessionCredentials bucket |
| Replenishment rate of GetJobRunQueryResults calls | Each supported Region: 2 | Yes | The Rate at which tokens are added to the GetJobRunQueryResults bucket |
| Replenishment rate of GetManagedScalingPolicy calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the GetManagedScalingPolicy bucket |
| Replenishment rate of GetResourceDashboard calls | Each supported Region: 2 | Yes | The Rate at which tokens are added to the GetResourceDashboard bucket |
| Replenishment rate of ListBootstrapActions calls | Each supported Region: 1 | Yes | The Rate at which tokens are added to the ListBootstrapActions bucket |
| Replenishment rate of ListClusters calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the ListClusters bucket |
| Replenishment rate of ListInstanceFleets calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the ListInstanceFleets bucket |
| Replenishment rate of ListInstanceGroups calls | Each supported Region: 1 | Yes | The Rate at which tokens are added to the ListInstanceGroups bucket |
| Replenishment rate of ListInstances calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the ListInstances bucket |
| Replenishment rate of ListJobRuns calls | Each supported Region: 1 | Yes | The Rate at which tokens are added to the ListJobRuns bucket |
| Replenishment rate of ListManagedClusters calls | Each supported Region: 1 | Yes | The Rate at which tokens are added to the ListManagedClusters bucket |
| Replenishment rate of ListReleaseLabels calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the ListReleaseLabels bucket |
| Replenishment rate of ListSecurityConfigurations calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the ListSecurityConfigurations bucket |
| Replenishment rate of ListSteps calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the ListSteps bucket |
| Replenishment rate of ListSupportedInstanceTypes calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the ListSupportedInstanceTypes bucket |
| Replenishment rate of ModifyCluster calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the ModifyCluster bucket |
| Replenishment rate of ModifyInstanceFleet calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the ModifyInstanceFleet bucket |
| Replenishment rate of ModifyInstanceGroups calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the ModifyInstanceGroups bucket |
| Replenishment rate of PutAutoScalingPolicy calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the PutAutoScalingPolicy bucket |
| Replenishment rate of PutAutoTerminationPolicy calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the PutAutoTerminationPolicy bucket |
| Replenishment rate of PutBlockPublicAccessConfiguration calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the PutBlockPublicAccessConfiguration bucket |
| Replenishment rate of PutManagedScalingPolicy calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the PutManagedScalingPolicy bucket |
| Replenishment rate of RemoveAutoScalingPolicy calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the RemoveAutoScalingPolicy bucket |
| Replenishment rate of RemoveAutoTerminationPolicy calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the RemoveAutoTerminationPolicy bucket |
| Replenishment rate of RemoveTags calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the RemoveTags bucket |
| Replenishment rate of RunJobFlow calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the RunJobFlow bucket |
| Replenishment rate of SetKeepJobFlowAliveWhenNoSteps calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the SetKeepJobFlowAliveWhenNoSteps bucket |
| Replenishment rate of SetKeepJobFlowAliveWhenNoSteps calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the RemoveManagedScalingPolicy bucket. |
| Replenishment rate of SetTerminationProtection calls | Each supported Region: 0.2 | Yes | The Rate at which tokens are added to the SetTerminationProtection bucket |
| Replenishment rate of SetVisibleToAllUsers calls | Each supported Region: 0.2 | Yes | The Rate at which tokens are added to the SetVisibleToAllUsers bucket |
| Replenishment rate of StartJobRun calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the StartJobRun bucket |
| Replenishment rate of TerminateJobFlows calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the TerminateJobFlows bucket |
| Replenishment rate of TerminateManagedCluster calls | Each supported Region: 0.5 | Yes | The Rate at which tokens are added to the TerminateManagedCluster bucket |
| The maximum number of API requests that you can make per second. | Each supported Region: 200 per second | Yes | The maximum number of requests per second that you can perform in this account in the current Region for all EMR operations. |
| The maximum number of AddInstanceFleet API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of AddInstanceFleet requests per second that you can perform in this account in the current Region. AddInstanceFleet adds an instance fleet to a running cluster. |
| The maximum number of AddInstanceGroups API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of AddInstanceGroups requests per second that you can perform in this account in the current Region. Adds one or more instance groups to a running cluster. |
| The maximum number of AddJobFlowSteps API requests that you can make per second. | Each supported Region: 10 per second | Yes | The maximum number of AddJobFlowSteps requests per second that you can perform in this account in the current Region. AddJobFlowSteps adds new steps to a running cluster. |
| The maximum number of AddTags API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of AddTags requests per second that you can perform in this account in the current Region. Adds tags to an Amazon EMR resource. |
| The maximum number of CancelJobRun API requests that you can make per second. | Each supported Region: 10 per second | Yes | The maximum number of CancelJobRun requests per second that you can perform in this account in the current Region. CancelJobRun cancels a running job run on a managed cluster. |
| The maximum number of CancelSteps API requests that you can make per second. | Each supported Region: 10 per second | Yes | The maximum number of CancelSteps requests per second that you can perform in this account in the current Region. |
| The maximum number of CreateManagedCluster API requests that you can make per second. | Each supported Region: 10 per second | Yes | The maximum number of CreateManagedCluster requests per second that you can perform in this account in the current Region. CreateManagedCluster creates and starts running a new managed cluster. |
| The maximum number of CreateSecurityConfiguration API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of CreateSecurityConfiguration requests per second that you can perform in this account in the current Region. CreateSecurityConfiguration creates a security configuration, which is stored in the service and can be specified when a cluster is created. |
| The maximum number of DeleteSecurityConfiguration API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of DeleteSecurityConfiguration requests per second that you can perform in this account in the current Region. DeleteSecurityConfiguration deletes a security configuration. |
| The maximum number of DescribeCluster API requests that you can make per second. | Each supported Region: 10 per second | Yes | The maximum number of DescribeCluster requests per second that you can perform in this account in the current Region. DescribeCluster provides cluster-level details including status, hardware and software configuration, VPC settings, and so on. |
| The maximum number of DescribeJobFlows API requests that you can make per second. | Each supported Region: 20 per second | Yes | The maximum number of DescribeJobFlows requests per second that you can perform in this account in the current Region. This API is deprecated and will eventually be removed. We recommend you use ListClusters, DescribeCluster, ListSteps, ListInstanceGroups and ListBootstrapActions instead. |
| The maximum number of DescribeJobRun API requests that you can make per second. | Each supported Region: 20 per second | Yes | The maximum number of DescribeJobRun requests per second that you can perform in this account in the current Region. DescribeJobRun provides job-run-level details including status. |
| The maximum number of DescribeManagedCluster API requests that you can make per second. | Each supported Region: 20 per second | Yes | The maximum number of DescribeManagedCluster requests per second that you can perform in this account in the current Region. DescribeManagedCluster provides managed-cluster-level details including status and configuration. |
| The maximum number of DescribeSecurityConfiguration API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of DescribeSecurityConfiguration requests per second that you can perform in this account in the current Region. DescribeSecurityConfiguration provides the details of a security configuration by returning the configuration JSON. |
| The maximum number of DescribeStep API requests that you can make per second. | Each supported Region: 10 per second | Yes | The maximum number of DescribeStep requests per second that you can perform in this account in the current Region. DescribeStep provides more detail about the cluster step. |
| The maximum number of GetAutoTerminationPolicy API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of GetAutoTerminationPolicy requests per second that you can perform in this account in the current Region. GetAutoTerminationPolicy returns the auto-termination policy for an Amazon EMR cluster. |
| The maximum number of GetBlockPublicAccessConfiguration API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of GetBlockPublicAccessConfiguration requests per second that you can perform in this account in the current Region. GetBlockPublicAccessConfiguration returns the Amazon EMR block public access configuration for the account in the current region. |
| The maximum number of GetClusterSessionCredentials API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of GetClusterSessionCredentials requests per second that you can perform in this account in the current Region. GetClusterSessionCredentials provides temporary, HTTP basic credentials that are associated with a given runtime IAM role and used by a cluster with fine-grained access control activated. |
| The maximum number of GetJobRunQueryResults API requests that you can make per second. | Each supported Region: 20 per second | Yes | The maximum number of GetJobRunQueryResults requests per second that you can perform in this account in the current Region. GetJobRunQueryResults retrieves query results for a job run. |
| The maximum number of GetManagedScalingPolicy API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of GetManagedScalingPolicy requests per second that you can perform in this account in the current Region. GetManagedScalingPolicy fetches the attached managed scaling policy for an Amazon EMR cluster. |
| The maximum number of GetResourceDashboard API requests that you can make per second. | Each supported Region: 20 per second | Yes | The maximum number of GetResourceDashboard requests per second that you can perform in this account in the current Region. GetResourceDashboard retrieves resource dashboard information for a managed cluster. |
| The maximum number of ListBootstrapActions API requests that you can make per second. | Each supported Region: 10 per second | Yes | The maximum number of ListBootstrapActions requests per second that you can perform in this account in the current Region. ListBootstrapActions provides information about the bootstrap actions associated with a cluster. |
| The maximum number of ListClusters API requests that you can make per second. | Each supported Region: 20 per second | Yes | The maximum number of ListClusters requests per second that you can perform in this account in the current Region. ListClusters provides the status of all clusters visible to this AWS account. |
| The maximum number of ListInstanceFleets API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of ListInstanceFleets requests per second that you can perform in this account in the current Region. ListInstanceFleets lists all available details about the instance fleets in a cluster. |
| The maximum number of ListInstanceGroups API requests that you can make per second. | Each supported Region: 10 per second | Yes | The maximum number of ListInstanceGroups requests per second that you can perform in this account in the current Region. ListInstanceGroups provides all available details about the instance groups in a cluster. |
| The maximum number of ListInstances API requests that you can make per second. | Each supported Region: 10 per second | Yes | The maximum number of ListInstances requests per second that you can perform in this account in the current Region. ListInstances provides information for all active EC2 instances and EC2 instances terminated in the last 30 days, up to a maximum of 2,000. |
| The maximum number of ListJobRuns API requests that you can make per second. | Each supported Region: 20 per second | Yes | The maximum number of ListJobRuns requests per second that you can perform in this account in the current Region. ListJobRuns provides the status of all job runs on a managed cluster. |
| The maximum number of ListManagedClusters API requests that you can make per second. | Each supported Region: 20 per second | Yes | The maximum number of ListManagedClusters requests per second that you can perform in this account in the current Region. ListManagedClusters provides the status of all managed clusters visible to this AWS account. |
| The maximum number of ListReleaseLabels API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of ListReleaseLabels requests per second that you can perform in this account in the current Region. ListReleaseLabels retrieves release labels of Amazon EMR services in the region. |
| The maximum number of ListSecurityConfigurations API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of ListSecurityConfigurations requests per second that you can perform in this account in the current Region. ListSecurityConfigurations lists all the security configurations visible to this account, providing their creation dates and times, and their names. |
| The maximum number of ListSteps API requests that you can make per second. | Each supported Region: 10 per second | Yes | The maximum number of ListSteps requests per second that you can perform in this account in the current Region. ListSteps provides a list of steps for the cluster in reverse order. |
| The maximum number of ListSupportedInstanceTypes API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of ListSupportedInstanceTypes requests per second that you can perform in this account in the current Region. ListSupportedInstanceTypes lists the instance types that Amazon EMR supports. |
| The maximum number of ModifyCluster API requests that you can make per second. | Each supported Region: 10 per second | Yes | The maximum number of ModifyCluster requests per second that you can perform in this account in the current Region. ModifyCluster modifies the number of steps that can be executed concurrently for the cluster specified using ClusterID. |
| The maximum number of ModifyInstanceFleet API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of ModifyInstanceFleet requests per second that you can perform in this account in the current Region. ModifyInstanceFleet modifies the target On-Demand and target Spot capacities for the instance fleet. |
| The maximum number of ModifyInstanceGroups API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of ModifyInstanceGroups requests per second that you can perform in this account in the current Region. ModifyInstanceGroups modifies the number of nodes and configuration settings of an instance group. |
| The maximum number of PutAutoScalingPolicy API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of PutAutoScalingPolicy requests per second that you can perform in this account in the current Region. PutAutoScalingPolicy creates or updates an automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. |
| The maximum number of PutAutoTerminationPolicy API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of PutAutoTerminationPolicy requests per second that you can perform in this account in the current Region. PutAutoTerminationPolicy creates or updates an auto-termination policy for an Amazon EMR cluster. |
| The maximum number of PutBlockPublicAccessConfiguration API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of PutBlockPublicAccessConfiguration requests per second that you can perform in this account in the current Region. PutBlockPublicAccessConfiguration creates or updates an Amazon EMR block public access configuration. |
| The maximum number of PutManagedScalingPolicy API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of PutManagedScalingPolicy requests per second that you can perform in this account in the current Region. PutManagedScalingPolicy creates or updates a managed scaling policy for an Amazon EMR cluster. |
| The maximum number of RemoveAutoScalingPolicy API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of RemoveAutoScalingPolicy requests per second that you can perform in this account in the current Region. RemoveAutoScalingPolicy removes an automatic scaling policy from a specified instance group within an EMR cluster. |
| The maximum number of RemoveAutoTerminationPolicy API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of RemoveAutoTerminationPolicy requests per second that you can perform in this account in the current Region. RemoveAutoTerminationPolicy removes an auto-termination policy from an Amazon EMR cluster. |
| The maximum number of RemoveManagedScalingPolicy API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of RemoveManagedScalingPolicy requests per second that you can perform in this account in the current Region. PutManagedScalingPolicy removes a managed scaling policy from a specified Amazon EMR cluster. |
| The maximum number of RemoveTags API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of RemoveTags requests per second that you can perform in this account in the current Region. Removes tags from an Amazon EMR resource. |
| The maximum number of RunJobFlow API requests that you can make per second. | Each supported Region: 10 per second | Yes | The maximum number of RunJobFlow requests per second that you can perform in this account in the current Region. RunJobFlow creates and starts running a new cluster (job flow). |
| The maximum number of SetKeepJobFlowAliveWhenNoSteps API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of SetKeepJobFlowAliveWhenNoSteps per second that you can perform in this account in the current Region |
| The maximum number of SetTerminationProtection API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of SetTerminationProtection requests per second that you can perform in this account in the current Region. SetTerminationProtection locks a cluster (job flow) so the EC2 instances in the cluster cannot be terminated. |
| The maximum number of SetVisibleToAllUsers API requests that you can make per second. | Each supported Region: 5 per second | Yes | The maximum number of SetVisibleToAllUsers requests per second that you can perform in this account in the current Region. Sets the VisibleToAllUsers value, which determines whether the cluster is visible to all IAM users of the AWS account associated with the cluster. |
| The maximum number of StartJobRun API requests that you can make per second. | Each supported Region: 10 per second | Yes | The maximum number of StartJobRun requests per second that you can perform in this account in the current Region. StartJobRun submits a new job run to a managed cluster. |
| The maximum number of TerminateJobFlows API requests that you can make per second. | Each supported Region: 10 per second | Yes | The maximum number of TerminateJobFlows requests per second that you can perform in this account in the current Region. TerminateJobFlows shuts a list of clusters (job flows) down. |
| The maximum number of TerminateManagedCluster API requests that you can make per second. | Each supported Region: 10 per second | Yes | The maximum number of TerminateManagedCluster requests per second that you can perform in this account in the current Region. TerminateManagedCluster shuts down a managed cluster. |
| The maximum number of active clusters can be run at the same time | Each supported Region: 500 | Yes | The maximum number of active clusters can be run at the same time. |
| The maximum number of active instances per instance group | Each supported Region: 2,000 | Yes | The maximum number of active instances per instance group. |
| The maximum rate at which your bucket replenishes for all EMR operations. | Each supported Region: 50 | Yes | The maximum rate at which your bucket replenishes for all EMR operations. |
| Write-ahead logs (EMR WAL) | Each supported Region: 20,000 | No | The maximum number of Amazon EMR write-ahead logs (EMR WAL) that can be used at the same time in this account in the current Region. |

### 010-amazon-cloudfront.pdf

- Status: **ok**, 1 call(s), 45.4 s, in 9,194 / out 5,538 tokens
- Service: Amazon CloudFront; quota table format: `standard`

#### Endpoints (4)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (N. Virginia) | us-east-1 | cloudfront.amazonaws.com | HTTPS | global |
| US East (N. Virginia) | us-east-1 | cloudfront-fips.amazonaws.com | HTTPS | global |
| US East (N. Virginia) | us-east-1 | cloudfront.global.api.aws | HTTPS | global |
| US East (N. Virginia) | us-east-1 | cloudfront-fips.global.api.aws | HTTPS | global |

#### Quotas (97)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Alternate domain names (CNAMEs) per distribution | Each supported Region: 100 | Yes | The maximum number of alternate domain names (CNAMEs) per distribution. |
| Anycast static IP lists per AWS account | Each supported Region: 0 | Yes | The maximum number of Anycast static IP lists per AWS account. |
| Cache behaviors per distribution | Each supported Region: 75 | Yes | The maximum number of cache behaviors per distribution. |
| Cache policies per AWS account | Each supported Region: 20 | Yes | The maximum number of cache policies per AWS account. |
| CloudFront Functions: Maximum number of distributions associated with a single function | Each supported Region: 100 | Yes | The maximum number of CloudFront distributions associated with a single CloudFront function. |
| Connection attempts per origin | Each supported Region: 3 | No | The number of connection attempts per origin (1-3). |
| Connection timeout per origin | Each supported Region: 10 Seconds | No | The connection timeout per origin (1-10 seconds). |
| Continuous deployment policies per AWS account | Each supported Region: 20 | Yes | The maximum number of continuous deployment policies that you can have for an AWS account. |
| Cookies per cache policy | Each supported Region: 10 | Yes | The maximum number of cookies per cache policy. |
| Cookies per origin request policy | Each supported Region: 10 | Yes | The maximum number of cookies per origin request policy. |
| Custom headers per response headers policy | Each supported Region: 10 | Yes | The maximum number of custom headers per response headers policy. |
| Custom headers: maximum length of a header name | Each supported Region: 256 | No | The maximum length of a header name in characters. |
| Custom headers: maximum length of a header value | Each supported Region: 1,783 | No | The maximum length of a header value in characters. |
| Custom headers: maximum length of all header values and names combined | Each supported Region: 10,240 | No | The maximum length of all header values and names combined. |
| Custom headers: maximum number of custom headers that you can configure CloudFront to add to origin requests | Each supported Region: 30 | Yes | The maximum number of custom headers that you can configure CloudFront to add to origin requests. |
| Data transfer rate per distribution | Each supported Region: 150 | Yes | The maximum data transfer rate (in Gbps) per distribution. |
| Distributions associated with a single key group | Each supported Region: 100 | Yes | The maximum number of distributions associated with a single key group. |
| Distributions associated with the same VPC origin | Each supported Region: 50 | No | The maximum number of distributions that can be associated with a single VPC origin. |
| Distributions associated with the same cache policy | Each supported Region: 100 | No | The maximum number of distributions associated with the same cache policy. |
| Distributions associated with the same origin access control | Each supported Region: 100 | Yes | The maximum number of distributions that you can associate with an origin access control. |
| Distributions associated with the same origin request policy | Each supported Region: 100 | No | The maximum number of distributions associated with the same origin request policy. |
| Distributions associated with the same response headers policy | Each supported Region: 100 | Yes | The maximum number of distributions that you can associate with the same response headers policy. |
| Distributions per AWS account that you can create triggers for | Each supported Region: 500 | Yes | The maximum number of distributions per AWS account that you can create triggers for. |
| File invalidation: maximum number of active wildcard invalidations allowed | Each supported Region: 15 | No | The maximum number of active wildcard invalidations allowed. |
| File invalidation: maximum number of files allowed in active invalidation requests, excluding wildcard invalidations | Each supported Region: 3,000 | No | The maximum number of files allowed in active invalidation requests, excluding wildcard invalidations. |
| Function memory size (Viewer request and response event) | Each supported Region: 128 Megabytes | No | The maximum function memory size (in MB). (Viewer request and response event) |
| Function timeout (Origin request and response event) | Each supported Region: 30 Seconds | No | The maximum function timeout (in seconds). (Origin request and response event) |
| Function timeout for a viewer request and response event | Each supported Region: 5 Seconds | No | The maximum function timeout (in seconds). (Viewer request and response event) |
| Headers per cache policy | Each supported Region: 10 | Yes | The maximum number of headers per cache policy. |
| Headers per origin request policy | Each supported Region: 10 | Yes | The maximum number of headers per origin request policy. |
| Keep-alive timeout for a custom origin associated with distribution | Each supported Region: 120 Seconds | Yes | How long (in seconds) CloudFront tries to maintain a connection to your distributions custom origin after it gets the last packet of a response. |
| Key groups associated with a single distribution | Each supported Region: 4 | Yes | The maximum number of key groups associated with a single distribution. |
| Key groups per AWS account | Each supported Region: 10 | Yes | The maximum number of key groups per AWS account. |
| Length of the content security policy value in a response headers policy | Each supported Region: 1,783 | Yes | The maximum length of the content security policy value in a response headers policy. |
| Maximum CA bundle size per trust store | Each supported Region: 64 Kilobytes | Yes | The maximum size (in KB) of a CA bundle that can be uploaded to a trust store. |
| Maximum certificate size in trust store CA bundle | Each supported Region: 16 Kilobytes | Yes | The maximum size (in KB) of an individual certificate within a trust stores CA bundle. |
| Maximum compressed size of a Lambda function and any included libraries. (Origin request and response event) | Each supported Region: 50 Megabytes | No | The maximum compressed size (in MB) of a Lambda function and any included libraries . (Origin request and response event) |
| Maximum compressed size of a Lambda function and any included libraries. (Viewer request and response event) | Each supported Region: 50 Megabytes | No | The maximum compressed size (in MB) of a Lambda function and any included libraries . (Viewer request and response event) |
| Maximum file size for HTTP GET, POST, and PUT requests | Each supported Region: 50 Gigabytes | No | The maximum file size (in GB) for HTTP GET, POST, and PUT requests. |
| Maximum length of a URL | Each supported Region: 8,192 Bytes | No | The maximum length of a URL (in bytes). |
| Maximum length of a field to encrypt | Each supported Region: 16 Kilobytes | No | The maximum length (in KB) of a field to encrypt. |
| Maximum length of a request body when field-level encryption is configured | Each supported Region: 1 Megabytes | No | The maximum length (in MB) of a request body when field-level encryption is configured. |
| Maximum length of a request, including headers and query strings, but not including the body content | Each supported Region: 20,480 Bytes | No | The maximum length of a request (in bytes), including headers and query strings, but not including the body content. |
| Maximum number of CloudFront distributions that can be associated with a field-level encryption configuration | Each supported Region: 20 | No | The maximum number of CloudFront distributions that can be associated with a field-level encryption configuration. |
| Maximum number of aliases per distribution tenant | Each supported Region: 100 | Yes | The maximum number of aliases that you can have for a distribution tenant. |
| Maximum number of associations per web ACL | Each supported Region: 100 | Yes | The maximum number of resources that can be associated with a single web ACL. |
| Maximum number of certificates per trust store | Each supported Region: 25 | Yes | The maximum number of certificates that you can have for a trust store. |
| Maximum number of characters in a whitelisted query string | Each supported Region: 128 | No | The maximum number of characters in a whitelisted query string. |
| Maximum number of characters total for all whitelisted query strings in the same parameter | Each supported Region: 512 | No | The maximum number of characters total for all whitelisted query strings in the same parameter. |
| Maximum number of connection functions per AWS account | Each supported Region: 0 | Yes | The maximum number of connection functions that you can have for an AWS account. |
| Maximum number of connection groups per AWS account | Each supported Region: 100 | Yes | The maximum number of connection groups that you can have for an AWS account. |
| Maximum number of connection groups per Anycast static IP list | Each supported Region: 5 | Yes | The maximum number of connection groups that can be associated with the same Anycast static IP list. |
| Maximum number of distribution tenants per AWS account | Each supported Region: 10,000 | Yes | The maximum number of distribution tenants that you can have for an AWS account. |
| Maximum number of distributions associated with the same trust store | Each supported Region: 25 | Yes | The maximum number of distributions that can be associated with a single trust store. |
| Maximum number of field-level encryption configurations that can be associated with one AWS account | Each supported Region: 10 | No | The maximum number of field-level encryption configurations that can be associated with one AWS account. |
| Maximum number of field-level encryption profiles that can be associated with one AWS account | Each supported Region: 10 | No | The maximum number of field-level encryption profiles that can be associated with one AWS account. |
| Maximum number of fields in a request body when field-level encryption is configured | Each supported Region: 10 | No | The maximum number of fields in a request body when field-level encryption is configured. |
| Maximum number of fields to encrypt that can be specified in one profile | Each supported Region: 10 | No | The maximum number of fields to encrypt that can be specified in one profile. |
| Maximum number of multi-tenant distributions per AWS account | Each supported Region: 20 | Yes | The maximum number of multi-tenant distributions that you can have for an AWS account. |
| Maximum number of parameters in a field in a multi-tenant distribution | Each supported Region: 2 | Yes | The maximum number of parameters that you can have in a field in a multi-tenant distribution. |
| Maximum number of parameters per distribution tenant | Each supported Region: 5 | Yes | The maximum number of parameters that you can have for a distribution tenant. |
| Maximum number of parameters per multi-tenant distribution | Each supported Region: 5 | Yes | The maximum number of parameters that you can have for a multi-tenant distribution. |
| Maximum number of public keys that can be added to one AWS account | Each supported Region: 10 | No | The maximum number of public keys that can be added to one AWS account. |
| Maximum number of query argument profile mappings that can be included in a field-level encryption configuration | Each supported Region: 5 | No | The maximum number of query argument profile mappings that can be included in a field-level encryption configuration. |
| Maximum number of trust stores per AWS account | Each supported Region: 20 | Yes | The maximum number of trust stores that you can have for an AWS account. |
| Origin access identities per account | Each supported Region: 100 | Yes | The maximum number of origin access identities per account. |
| Origin groups per distribution | Each supported Region: 10 | Yes | The maximum number of origin groups per distribution. |
| Origin request policies per AWS account | Each supported Region: 20 | Yes | The maximum number of origin request policies per AWS account. |
| Origin response timeout (idle timeout) | Each supported Region: 10 | No | The maximum origin response timeout (idle timeout) in minutes. If CloudFront hasn't detected any bytes sent from the origin to the client within the past 10 minutes, the connection is assumed to be idle and is closed. |
| Origins per distribution | Each supported Region: 100 | Yes | The maximum number of origins per distribution. |
| Public keys in a single key group | Each supported Region: 5 | Yes | The maximum number of public keys in a single key group. |
| Query strings per cache policy | Each supported Region: 10 | Yes | The maximum number of query strings per cache policy. |
| Query strings per origin request policy | Each supported Region: 10 | Yes | The maximum number of query strings per origin request policy. |
| Range of file sizes that CloudFront compresses | Each supported Region: 10,000,000 Bytes | No | The range of file sizes (in bytes) that CloudFront compresses (1,000 to 10,000,000). |
| Removing headers from a response headers policy | Each supported Region: 10 | Yes | The maximum number of headers that you can remove in a response headers policy. |
| Request body size for origin requests exposed to a Lambda@Edge function. | Each supported Region: 1 Megabytes | No | The maximum request body size (in MB) for origin requests exposed to a Lambda@Edge function. |
| Request body size for origin requests when returning from a Lambda function (base64 encoding) | Each supported Region: 1.33 Megabytes | No | The maximum request body size (in KB) for origin requests when returning from a Lambda function. (base64 encoding) |
| Request body size for origin requests when returning from a Lambda function (text encoding) | Each supported Region: 1 Megabytes | No | The maximum request body size (in KB) for origin requests when returning from a Lambda function. (text encoding) |
| Request body size for viewer requests exposed to a Lambda@Edge function. | Each supported Region: 40 Kilobytes | No | The maximum request body size (in KB) for viewer requests exposed to a Lambda@Edge function. |
| Request body size for viewer requests when returning from a Lambda function (base64 encoding) | Each supported Region: 53.2 Kilobytes | No | The maximum request body size (in KB) for viewer requests when returning from a Lambda function. (base64 encoding) |
| Request body size for viewer requests when returning from a Lambda function (text encoding) | Each supported Region: 40 Kilobytes | No | The maximum request body size (in KB) for viewer requests when returning from a Lambda function. (text encoding) |
| Requests per second per distribution | Each supported Region: 250,000 | Yes | The maximum number of requests per second per distribution. |
| Response headers policies | Each supported Region: 20 | Yes | The maximum number of response headers policies per AWS account. |
| Response timeout per origin | Each supported Region: 120 Seconds | Yes | The response timeout per origin (1-120 seconds). |
| SSL certificates per AWS account when serving HTTPS requests using dedicated IP addresses | Each supported Region: 2 | Yes | The maximum number of SSL certificates per AWS account when serving HTTPS requests using dedicated IP addresses (no quota when serving HTTPS requests using SNI). |
| SSL certificates that can be associated with a CloudFront web distribution | Each supported Region: 1 | No | The maximum number of SSL certificates that can be associated with a CloudFront web distribution. |
| Size of a response that is generated by a Lambda function, including headers and body (Origin request and response event) | Each supported Region: 1 Megabytes | No | The maximum size (in MB) of a response that is generated by a Lambda function, including headers and body. (Origin request and response event) |
| Size of a response that is generated by a Lambda function, including headers and body (Viewer request and response event) | Each supported Region: 40 Kilobytes | No | The maximum size (in KB) of a response that is generated by a Lambda function, including headers and body. (Viewer request and response event) |
| Staging distributions per AWS account | Each supported Region: 20 | Yes | The maximum number of staging distributions that you can have for an AWS account. |
| Tags that can be added to a distribution | Each supported Region: 50 | No | The maximum number of tags that can be added to a distribution. |
| Total length of the URI including query string in a Lambda@Edge function | Each supported Region: 8,192 | No | The maximum total length in characters of the URI including the query string in a Lambda@Edge function. |
| Total number of bytes in whitelisted cookie names (doesn't apply if you configure CloudFront to forward all cookies to the origin) | Each supported Region: 512 Bytes | No | The total number of bytes in whitelisted cookie names (doesn't apply if you configure CloudFront to forward all cookies to the origin). 512 minus the number of whitelisted cookies. |
| Triggers per distribution | Each supported Region: 100 | Yes | The maximum number of triggers per distribution. |
| VPC origins per AWS account | Each supported Region: 25 | Yes | The maximum number of VPC origins per AWS account. |
| Web distributions per AWS account | Each supported Region: 500 | Yes | The maximum number of web distributions per AWS account. |
| Whitelisted cookies per cache behavior | Each supported Region: 10 | Yes | The maximum number of whitelisted cookies per cache behavior. |
| Whitelisted headers per cache behavior | Each supported Region: 10 | Yes | The maximum number of whitelisted headers per cache behavior. |

### 074-aws-global-accelerator.pdf

- Status: **ok**, 1 call(s), 6.4 s, in 7,987 / out 926 tokens
- Service: AWS Global Accelerator; quota table format: `standard`

#### Endpoints (2)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US West (Oregon) | us-west-2 | globalaccelerator.amazonaws.com | HTTPS | global |
| US West (Oregon) | us-west-2 | globalaccelerator-fips.us-west-2.amazonaws.com | HTTPS | fips |

#### Quotas (16)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Cross-account attachments per AWS account | Each supported Region: 10 | Yes | The maximum number of cross-account attachments for each AWS account. |
| Custom routing accelerators per AWS account | Each supported Region: 10 | Yes | The maximum number of custom routing accelerators for each AWS account. |
| Endpoint groups per accelerator | Each supported Region: 42 | No | The maximum number of endpoint groups per accelerator. |
| Endpoint resources per cross-account attachment | Each supported Region: 500 | No | The maximum number of endpoint resources per cross-account attachment. |
| Endpoints per endpoint group - Application Load Balancers | Each supported Region: 10 | No | The maximum number of Application Load Balancers in an endpoint group containing only ALB endpoints. |
| Endpoints per endpoint group - EC2 instances | Each supported Region: 10 | Yes | The maximum number of EC2 instances in an endpoint group containing only EC2 instance endpoints. |
| Endpoints per endpoint group - Elastic IP addresses | Each supported Region: 10 | Yes | The maximum number of Elastic IP addresses in an endpoint group containing only Elastic IP address endpoints. |
| Endpoints per endpoint group - Network Load Balancers | Each supported Region: 10 | Yes | The maximum number of Network Load Balancers in an endpoint group containing only NLB endpoints. |
| Endpoints per endpoint group - VPC subnets | Each supported Region: 10 | Yes | The maximum number of VPC subnets in an endpoint group containing only subnet endpoints. |
| Endpoints per endpoint group - more than one endpoint type | Each supported Region: 10 | No | The maximum number of endpoints in an endpoint group containing more than one endpoint type. |
| Listeners per accelerator | Each supported Region: 10 | Yes | The maximum number of listeners for each accelerator. |
| Port overrides per endpoint group | Each supported Region: 10 | Yes | The maximum number of port overrides for each endpoint group. |
| Port ranges per listener | Each supported Region: 10 | No | The maximum number of port ranges for each listener. |
| Principals per cross-account attachment | Each supported Region: 10 | Yes | The maximum number of principals per cross-account attachment. |
| Standard accelerators per AWS account | Each supported Region: 20 | Yes | The maximum number of standard accelerators for each AWS account. |
| Tags per accelerator | Each supported Region: 50 | No | The maximum number of tags for each accelerator. |

### 019-amazon-ecr.pdf

- Status: **ok**, 1 call(s), 85.7 s, in 10,763 / out 12,373 tokens
- Service: Amazon ECR; quota table format: `standard`

#### Endpoints (210)

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
| US West (N. California) | us-west-1 | ecr.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | api.ecr-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | ecr.us-west-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | ecr-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | dkr-ecr.us-west-1.on.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | dkr-ecr-fips.us-west-1.on.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | dkr.ecr.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | dkr.ecr-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | api.ecr.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | ecr-fips.us-west-1.amazonaws.com | HTTPS | fips |
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
| Asia Pacific (Hong Kong) | ap-east-1 | ecr.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | api.ecr.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | ecr.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | api.ecr.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | dkr-ecr.ap-south-2.on.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | dkr.ecr.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | ecr.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | ecr.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | ecr.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | api.ecr.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | dkr-ecr.ap-southeast-3.on.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | dkr.ecr.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | ecr.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | api.ecr.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | dkr.ecr.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | ecr.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | dkr-ecr.ap-southeast-5.on.aws | HTTPS | dual_stack |
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
| Asia Pacific (Osaka) | ap-northeast-3 | api.ecr.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | dkr.ecr.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | ecr.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | dkr-ecr.ap-northeast-3.on.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | ecr.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | api.ecr.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | ecr.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | dkr.ecr.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | dkr-ecr.ap-northeast-2.on.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | ecr.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | api.ecr.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | dkr.ecr.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | ecr.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | dkr-ecr.ap-southeast-1.on.aws | HTTPS | dual_stack |
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
| Asia Pacific (Thailand) | ap-southeast-7 | dkr.ecr.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | ecr.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | api.ecr.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | ecr.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | dkr-ecr.ap-northeast-1.on.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | api.ecr.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | ecr.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | dkr.ecr.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | ecr.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | ecr.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | dkr-ecr.ca-central-1.on.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | dkr.ecr.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | api.ecr.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | ecr.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | ecr.ca-west-1.api.aws | HTTPS | dual_stack |
| Canada West (Calgary) | ca-west-1 | api.ecr.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | dkr.ecr.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | dkr-ecr.ca-west-1.on.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | ecr.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | ecr.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | dkr-ecr.eu-central-1.on.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | api.ecr.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | dkr.ecr.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | ecr.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | api.ecr.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | dkr-ecr.eu-west-1.on.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | dkr.ecr.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | ecr.eu-west-1.api.aws | HTTPS | dual_stack |
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
| Europe (Spain) | eu-south-2 | dkr-ecr.eu-south-2.on.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | api.ecr.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | dkr.ecr.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | ecr.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | dkr.ecr.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | api.ecr.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | ecr.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | dkr-ecr.eu-north-1.on.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | ecr.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | ecr.eu-central-2.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | dkr-ecr.eu-central-2.on.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | api.ecr.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | dkr.ecr.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | ecr.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | ecr.il-central-1.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | dkr-ecr.il-central-1.on.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | api.ecr.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | dkr.ecr.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | ecr.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | dkr.ecr.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | api.ecr.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | ecr.mx-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | dkr-ecr.mx-central-1.on.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | ecr.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | dkr.ecr.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | ecr.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | api.ecr.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | dkr-ecr.me-south-1.on.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | ecr.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | dkr.ecr.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | ecr.me-central-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | api.ecr.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | dkr-ecr.me-central-1.on.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | ecr.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | dkr-ecr.sa-east-1.on.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | dkr.ecr.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | ecr.sa-east-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | api.ecr.sa-east-1.amazonaws.com | HTTPS | ipv4 |
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
| AWS GovCloud (US-West) | us-gov-west-1 | dkr.ecr-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | ecr-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | api.ecr.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | dkr.ecr.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | api.ecr-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | ecr-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | ecr.us-gov-west-1.api.aws | HTTPS | dual_stack |
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
| Rules per lifecycle policy | Each supported Region: 50 | No | The maximum number of rules in a lifecycle policy |
| Rules per replication configuration | Each supported Region: 25 | No | The maximum number of rules in a replication configuration. |
| Tags per image | Each supported Region: 1,000 | No | The maximum number of tags per image. |
| Unique destinations across all rules in a replication configuration | Each supported Region: 25 | No | The maximum number of unique destinations across all rules in a replication configuration. |
