# Run `qwen2.5-7b__v1__t0__holdout__val2`

Generated from the JSONL run file by `src/extract/report_md.py`; do not edit.

- Model: `qwen2.5:7b`
- Prompt version: `v1` (file sha `8a0da697aa92`)
- Schema sha: `d4010de95c65`; validation version `2`
- Sampling: `t0` (temperature 0.0, top_p None)
- Documents: 10

## Summary

| # | Document | Group | Status | Calls | Latency, s | In tokens | Out tokens | Quota table | Endpoints | Quotas |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [079-aws-iot-device-defender.pdf](#079-aws-iot-device-defenderpdf) | edge | repaired | 2 | 305.6 | 22,128 | 10,315 | non_standard | 58 | 0 |
| 2 | [059-aws-clean-rooms.pdf](#059-aws-clean-roomspdf) | edge | failed | 2 | 352.3 | 19,024 | 12,079 | — | — | — |
| 3 | [016-amazon-comprehend.pdf](#016-amazon-comprehendpdf) | edge | failed | 2 | 408.2 | 20,432 | 14,142 | — | — | — |
| 4 | [069-aws-elemental-mediaconvert.pdf](#069-aws-elemental-mediaconvertpdf) | edge | ok | 1 | 170.0 | 6,166 | 6,289 | standard | 25 | 72 |
| 5 | [027-amazon-eventbridge-scheduler.pdf](#027-amazon-eventbridge-schedulerpdf) | medium | ok | 1 | 150.7 | 4,414 | 5,916 | standard | 89 | 14 |
| 6 | [068-aws-elastic-beanstalk.pdf](#068-aws-elastic-beanstalkpdf) | medium | ok | 1 | 107.2 | 5,020 | 4,066 | standard | 76 | 3 |
| 7 | [051-amazon-timestream.pdf](#051-amazon-timestreampdf) | medium | failed | 1 | 510.8 | 4,733 | 18,432 | — | — | — |
| 8 | [028-amazon-fsx.pdf](#028-amazon-fsxpdf) | medium | failed | 2 | 296.8 | 14,573 | 10,817 | — | — | — |
| 9 | [073-aws-firewall-manager.pdf](#073-aws-firewall-managerpdf) | medium | failed | 2 | 253.4 | 13,103 | 9,395 | — | — | — |
| 10 | [046-amazon-simple-email-service.pdf](#046-amazon-simple-email-servicepdf) | medium | repaired | 2 | 205.8 | 17,371 | 7,131 | standard | 68 | 4 |

## Documents

### 079-aws-iot-device-defender.pdf

- Status: **repaired**, 2 call(s), 305.6 s, in 22,128 / out 10,315 tokens
- Service: AWS IoT Device Defender; quota table format: `non_standard`

#### Endpoints (58)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | iot.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | iot-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | iot-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | iot.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | iot.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | iot-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | iot-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | iot.us-east-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | iot.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | iot-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | iot-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | iot.us-west-2.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | iot.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | iot-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | iot-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | iot.us-west-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | iot.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | iot.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | iot.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | iot.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | iot.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | iot.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | iot.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | iot.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | iot.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | iot.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | iot.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | iot.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | iot.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | iot.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | iot.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | iot-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | iot-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | iot.ca-central-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | iot.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | iot.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | iot.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | iot.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | iot.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | iot.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | iot.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | iot.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | iot.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | iot.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | iot.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | iot.eu-north-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | iot.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | iot.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | iot.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | iot.me-central-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | iot.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | iot-fips.us-gov-east-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | iot-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | iot.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | iot.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | iot-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | iot-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | iot.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (0)

_none_

#### First answer rejected (repaired)

```text
- quotas.0.name: not printed in a Standard Quota Table of the chapter: 'Scheduled audits'
- quotas.1.name: not printed in a Standard Quota Table of the chapter: 'Simultaneous in progress on-demand audits'
- quotas.2.name: not printed in a Standard Quota Table of the chapter: 'Storage duration for audit findings'
- quotas.3.name: not printed in a Standard Quota Table of the chapter: 'Mitigation actions'
- quotas.4.name: not printed in a Standard Quota Table of the chapter: 'Number of audit mitigation action tasks running at the same time'
- quotas.5.name: not printed in a Standard Quota Table of the chapter: 'Retention period for audit mitigation action tasks'
- quotas.6.name: not printed in a Standard Quota Table of the chapter: 'Number of behavior metric value elements for each security profile'
- quotas.7.name: not printed in a Standard Quota Table of the chapter: 'Number of behaviors for each security profile'
- quotas.8.name: not printed in a Standard Quota Table of the chapter: 'Number of custom metrics'
- quotas.9.name: not printed in a Standard Quota Table of the chapter: 'Minimum delay between sending device metric reports'
- quotas.10.name: not printed in a Standard Quota Table of the chapter: 'Device metric peak reporting rate'
- quotas.11.name: not printed in a Standard Quota Table of the chapter: 'Metric dimensions'
- quotas.12.name: not printed in a Standard Quota Table of the chapter: 'Security profiles for each target (things or thing groups in the AWS account)'
- quotas.13.name: not printed in a Standard Quota Table of the chapter: 'Storage duration for detect metrics'
- quotas.14.name: not printed in a Standard Quota Table of the chapter: 'Storage duration for detect violations'
- quotas.15.name: not printed in a Standard Quota Table of the chapter: 'Number of detect metric dimensions'
- quotas.16.name: not printed in a Standard Quota Table of the chapter: 'Number of security profiles for each target (things or thing groups in the AWS account)'
- quotas.17.name: not printed in a Standard Quota Table of the chapter: 'Retention period for models (time after which models are expired)'
- quotas.18.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for AttachSecurityProfile API'
- quotas.19.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for CancelAuditMitigationActionTask API'
- quotas.20.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for CancelAuditTask API'
- quotas.21.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for CancelDetectMitigationActionTask API'
- quotas.22.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for CreateAuditSuppression API'
- quotas.23.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for CreateCustomMetric API'
- quotas.24.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for CreateMitigationAction API'
- quotas.25.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for CreateScheduledAudit API'
- quotas.26.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for CreateSecurityProfile API'
- quotas.27.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DeleteAccountAuditConfiguration API'
- quotas.28.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DeleteAuditSuppression API'
- quotas.29.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DeleteCustomMetric API'
- quotas.30.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DeleteMitigationAction API'
- quotas.31.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DeleteScheduledAudit API'
- quotas.32.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DeleteSecurityProfile API'
- quotas.33.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DescribeAccountAuditConfiguration API'
- quotas.34.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DescribeAuditFinding API'
- quotas.35.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DescribeAuditMitigationAction API'
- quotas.36.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DescribeAuditSuppression API'
- quotas.37.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DescribeAuditTask API'
- quotas.38.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DescribeCustomMetric API'
- quotas.39.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DescribeDetectMitigationAction API'
- quotas.40.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DescribeDimension API'
- quotas.41.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DescribeMitigationAction API'
- quotas.42.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DescribeScheduledAudit API'
- quotas.43.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DescribeSecurityProfile API'
- quotas.44.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for DetachSecurityProfile API'
- quotas.45.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListActiveViolations API'
- quotas.46.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListAuditFindings API'
- quotas.47.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListAuditMitigationActionExecutions API'
- quotas.48.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListAuditMitigationActionTasks API'
- quotas.49.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListAuditSuppressions API'
- quotas.50.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListAuditTasks API'
- quotas.51.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListCustomMetrics API'
- quotas.52.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListDetectMitigationActionExecutions API'
- quotas.53.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListDetectMitigationActionTasks API'
- quotas.54.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListDimensions API'
- quotas.55.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListMetricValues API'
- quotas.56.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListMitigationActions API'
- quotas.57.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListScheduledAudits API'
- quotas.58.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListSecurityProfiles API'
- quotas.59.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListSecurityProfilesForTarget API'
- quotas.60.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListTargetsForSecurityProfile API'
- quotas.61.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for ListViolationEvents API'
- quotas.62.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for PutVerificationStateOnViolation API'
- quotas.63.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for StartAuditMitigationActionTask API'
- quotas.64.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for StartDetectMitigationActionTask API'
- quotas.65.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for StartOnDemandAuditTask API'
- quotas.66.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for UpdateAccountAuditConfiguration API'
- quotas.67.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for UpdateAuditSuppression API'
- quotas.68.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for UpdateCustomMetric API'
- quotas.69.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for UpdateMitigationAction API'
- quotas.70.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for UpdateScheduledAudit API'
- quotas.71.name: not printed in a Standard Quota Table of the chapter: 'Number of transactions per second (TPS) for UpdateSecurityProfile API'
- quota_table_format: 'standard', but the chapter prints no table with the columns Name, Default, Adjustable, Description
```

### 059-aws-clean-rooms.pdf

- Status: **failed**, 2 call(s), 352.3 s, in 19,024 / out 12,079 tokens

#### Error

```text
- endpoints.0.endpoint: Value error, not a single hostname (broken by a line wrap?): 'cleanrooms.us-east-2.amazonaws.com cleanrooms-fips.us-east-2.api.aws cleanrooms.us-east-2.api.aws cleanrooms-fips.us-east-2.amazonaws.com'
- endpoints.1.endpoint: Value error, not a single hostname (broken by a line wrap?): 'cleanrooms.us-east-1.amazonaws.com cleanrooms-fips.us-east-1.api.aws cleanrooms-fips.us-east-1.amazonaws.com cleanrooms.us-east-1.api.aws'
- endpoints.2.endpoint: Value error, not a single hostname (broken by a line wrap?): 'cleanrooms.us-west-2.amazonaws.com cleanrooms-fips.us-west-2.api.aws cleanrooms.us-west-2.api.aws cleanrooms-fips.us-west-2.amazonaws.com'
- endpoints.3.endpoint: Value error, not a single hostname (broken by a line wrap?): 'cleanrooms.ap-northeast-2.amazonaws.com cleanrooms.ap-northeast-2.api.aws'
- endpoints.4.endpoint: Value error, not a single hostname (broken by a line wrap?): 'cleanrooms.ap-southeast-1.amazonaws.com cleanrooms.ap-southeast-1.api.aws'
- endpoints.5.endpoint: Value error, not a single hostname (broken by a line wrap?): 'cleanrooms.ap-southeast-2.amazonaws.com cleanrooms.ap-southeast-2.api.aws'
- endpoints.6.endpoint: Value error, not a single hostname (broken by a line wrap?): 'cleanrooms.ap-northeast-1.amazonaws.com cleanrooms.ap-northeast-1.api.aws'
- endpoints.7.endpoint: Value error, not a single hostname (broken by a line wrap?): 'cleanrooms.eu-central-1.amazonaws.com cleanrooms.eu-central-1.api.aws'
- endpoints.8.endpoint: Value error, not a single hostname (broken by a line wrap?): 'cleanrooms.eu-west-1.amazonaws.com cleanrooms.eu-west-1.api.aws'
- endpoints.9.endpoint: Value error, not a single hostname (broken by a line wrap?): 'cleanrooms.eu-west-2.amazonaws.com cleanrooms.eu-west-2.api.aws'
- endpoints.10.endpoint: Value error, not a single hostname (broken by a line wrap?): 'cleanrooms.eu-north-1.amazonaws.com cleanrooms.eu-north-1.api.aws'
--- after repair:
- quotas.74.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListAnalysisLogExport requests'
- quotas.75.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListAnalysisTemplate requests'
- quotas.76.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationAnalysisTemplate requests'
- quotas.77.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationChangeRequest requests'
- quotas.78.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationConfiguredAudienceModelAssociation requests'
- quotas.79.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationIdNamespaceAssociation requests'
- quotas.80.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationPrivacyBudgetTemplate requests'
- quotas.81.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationPrivacyBudget requests'
- quotas.82.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaboration requests'
- quotas.83.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListConfiguredAudienceModelAssociation requests'
- quotas.84.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListConfiguredTableAssociation requests'
- quotas.85.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListConfiguredTable requests'
- quotas.86.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListIdMappingTable requests'
- quotas.87.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListIdNamespaceAssociation requests'
- quotas.88.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListMember requests'
- quotas.89.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListMembership requests'
- quotas.90.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListPrivacyBudgetTemplate requests'
- quotas.91.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListPrivacyBudget requests'
- quotas.92.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListProtectedJob requests'
- quotas.93.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListProtectedQuery requests'
- quotas.94.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListSchema requests'
```

### 016-amazon-comprehend.pdf

- Status: **failed**, 2 call(s), 408.2 s, in 20,432 / out 14,142 tokens

#### Error

```text
- endpoints.7.region_code: Value error, not an AWS Region code like us-east-2: 'comprehend'
- endpoints.11.region_code: Value error, not an AWS Region code like us-east-2: 'comprehend'
- endpoints.34.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'comprehend-fips.us-gov-west-1.amazon'
--- after repair:
- quotas.12.name: not printed in a Standard Quota Table of the chapter: 'CreateFlywheel max concurrent flywheels'
```

### 069-aws-elemental-mediaconvert.pdf

- Status: **ok**, 1 call(s), 170.0 s, in 6,166 / out 6,289 tokens
- Service: AWS Elemental MediaConvert; quota table format: `standard`

#### Endpoints (25)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | mediaconvert.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | mediaconvert.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | mediaconvert.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | mediaconvert.us-west-2.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | mediaconvert.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | mediaconvert.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | mediaconvert.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | mediaconvert.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | mediaconvert.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | mediaconvert.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | mediaconvert.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | mediaconvert.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | mediaconvert.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | mediaconvert.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | mediaconvert.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | mediaconvert.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | mediaconvert.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | mediaconvert.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | mediaconvert.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | mediaconvert.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | mediaconvert.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | mediaconvert.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | mediaconvert.me-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | mediaconvert.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | mediaconvert.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (72)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Concurrent jobs per account | us-east-1: 2,000; us-west-2: 2,000; eu-west-1: 2,000; Each of the other supported Regions: 1,000 | No | The maximum number of jobs that MediaConvert can process at one time, across all of your on-demand queues in the current AWS Region. For more information about configuring on-demand queues, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-on-demand-queues.html |
| Concurrent jobs per on-demand queue | us-east-1: 500; us-east-2: 250; us-west-2: 500; ap-northeast-1: 250; ap-south-1: 250; eu-west-1: 500; eu-west-2: 250; Each of the other supported Regions: 100 | Yes | The maximum number of concurrent jobs that are available when you configure an on-demand queue in the current AWS Region. For more information about configuring on-demand queues, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-on-demand-queues.html |
| Concurrent jobs per on-demand queue, default | us-east-1: 200; us-west-2: 200; eu-west-1: 200; Each of the other supported Regions: 100 | No | The default value for concurrent jobs that MediaConvert applies to new on-demand queues in the current AWS Region. For more information about configuring on-demand queues, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-on-demand-queues.html |
| Concurrent jobs queries per account | Each supported Region: 10 | No | The maximum number of concurrent jobs queries you can create in this account in the current AWS Region. |
| Custom job templates | Each supported Region: 100 | Yes | The maximum number of custom job templates that you can create in this account in the current AWS Region. |
| Custom output presets | Each supported Region: 100 | Yes | The maximum number of custom output presets that you can create in this account in the current AWS Region. |
| Queues per AWS Region | Each supported Region: 10 | Yes | The maximum number of on-demand and reserved queues combined that you can create in the current AWS Region. |
| Request rate for AssociateCertificate | Each supported Region: 2 per second | No | The maximum number of AssociateCertificate requests per second that you can send in this account in the current AWS Region. |
| Request rate for AssociateCertificate, in a burst | Each supported Region: 100 | No | The maximum number of AssociateCertificate requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for CancelJob | Each supported Region: 2 per second | Yes | The maximum number of CancelJob requests per second that you can send in this account in the current AWS Region. |
| Request rate for CancelJob, in a burst | Each supported Region: 100 | Yes | The maximum number of CancelJob requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for CreateJob | Each supported Region: 5 per second | Yes | The maximum number of CreateJob requests per second that you can send in this account in the current AWS Region. |
| Request rate for CreateJob, in a burst | Each supported Region: 100 | Yes | The maximum number of CreateJob requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for CreateJobTemplate | Each supported Region: 2 per second | Yes | The maximum number of CreateJobTemplate requests per second that you can send in this account in the current AWS Region. |
| Request rate for CreateJobTemplate, in a burst | Each supported Region: 100 | Yes | The maximum number of CreateJobTemplate requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for CreatePreset | Each supported Region: 2 per second | Yes | The maximum number of CreatePreset requests per second that you can send in this account in the current AWS Region. |
| Request rate for CreatePreset, in a burst | Each supported Region: 100 | Yes | The maximum number of CreatePreset requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for CreateQueue | Each supported Region: 2 per second | Yes | The maximum number of CreateQueue requests per second that you can send in this account in the current AWS Region. |
| Request rate for CreateQueue, in a burst | Each supported Region: 100 | Yes | The maximum number of CreateQueue requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for CreateResourceShare | Each supported Region: 0.1 per second | No | The maximum number of Share requests per second that you can send in this account in the current AWS Region. |
| Request rate for CreateResourceShare, in a burst | Each supported Region: 10 | No | The maximum number of Share requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for DeleteJobTemplate | Each supported Region: 2 per second | Yes | The maximum number of DeleteJobTemplate requests per second that you can send in this account in the current AWS Region. |
| Request rate for DeleteJobTemplate, in a burst | Each supported Region: 100 | Yes | The maximum number of DeleteJobTemplate requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for DeletePolicy | Each supported Region: 2 per second | No | The maximum number of DeletePolicy requests per second that you can send in this account in the current AWS Region. |
| Request rate for DeletePolicy, in a burst | Each supported Region: 100 | No | The maximum number of DeletePolicy requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for DeletePreset | Each supported Region: 2 per second | Yes | The maximum number of DeletePreset requests per second that you can send in this account in the current AWS Region. |
| Request rate for DeletePreset, in a burst | Each supported Region: 100 | Yes | The maximum number of DeletePreset requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for DeleteQueue | Each supported Region: 2 per second | Yes | The maximum number of DeleteQueue requests per second that you can send in this account in the current AWS Region. |
| Request rate for DeleteQueue, in a burst | Each supported Region: 100 | Yes | The maximum number of DeleteQueue requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for DisassociateCertificate | Each supported Region: 2 per second | No | The maximum number of DisassociateCertificate requests per second that you can send in this account in the current AWS Region. |
| Request rate for DisassociateCertificate, in a burst | Each supported Region: 100 | No | The maximum number of DisassociateCertificate requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for GetJob | Each supported Region: 2 per second | Yes | The maximum number of GetJob requests per second that you can send in this account in the current AWS Region. |
| Request rate for GetJob, in a burst | Each supported Region: 100 | Yes | The maximum number of GetJob requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for GetJobTemplate | Each supported Region: 2 per second | Yes | The maximum number of GetJobTemplate requests per second that you can send in this account in the current AWS Region. |
| Request rate for GetJobTemplate, in a burst | Each supported Region: 100 | Yes | The maximum number of GetJobTemplate requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for GetJobsQueryResults | Each supported Region: 2 per second | No | The maximum number of GetJobsQueryResult s requests per second that you can send in this account in the current AWS Region. |
| Request rate for GetJobsQueryResults, in a burst | Each supported Region: 100 | No | The maximum number of GetJobsQueryResult s requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for GetPolicy | Each supported Region: 2 per second | No | The maximum number of GetPolicy requests per second that you can send in this account in the current AWS Region. |
| Request rate for GetPolicy, in a burst | Each supported Region: 100 | No | The maximum number of GetPolicy requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for GetPreset | Each supported Region: 2 per second | Yes | The maximum number of GetPreset requests per second that you can send in this account in the current AWS Region. |
| Request rate for GetPreset, in a burst | Each supported Region: 100 | Yes | The maximum number of GetPreset requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for GetQueue | Each supported Region: 2 per second | Yes | The maximum number of GetQueue requests per second that you can send in this account in the current AWS Region. |
| Request rate for GetQueue, in a burst | Each supported Region: 100 | Yes | The maximum number of GetQueue requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for ListJobTemplates | Each supported Region: 2 per second | Yes | The maximum number of ListJobTemplates requests per second that you can send in this account in the current AWS Region. |
| Request rate for ListJobTemplates, in a burst | Each supported Region: 100 | Yes | The maximum number of ListJobTemplates requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for ListJobs | Each supported Region: 2 per second | Yes | The maximum number of ListJobs requests per second that you can send in this account in the current AWS Region. |
| Request rate for ListJobs, in a burst | Each supported Region: 100 | Yes | The maximum number of ListJobs requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for ListPresets | Each supported Region: 2 per second | Yes | The maximum number of ListPresets requests per second that you can send in this account in the current AWS Region. |
| Request rate for ListPresets, in a burst | Each supported Region: 100 | Yes | The maximum number of ListPresets requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for ListQueues | Each supported Region: 2 per second | Yes | The maximum number of ListQueues requests per second that you can send in this account in the current AWS Region. |
| Request rate for ListQueues, in a burst | Each supported Region: 100 | Yes | The maximum number of ListQueues requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for ListTagsForResource | Each supported Region: 2 per second | Yes | The maximum number of ListTagsForResource requests per second that you can send in this account in the current AWS Region. |
| Request rate for ListTagsForResource, in a burst | Each supported Region: 100 | Yes | The maximum number of ListTagsForResource requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for ListVersions | Each supported Region: 2 per second | Yes | The maximum number of ListVersions requests per second that you can send in this account in the current AWS Region. |
| Request rate for ListVersions, in a burst | Each supported Region: 100 | Yes | The maximum number of ListVersions requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for Probe | Each supported Region: 5 per second | Yes | The maximum number of Probe requests per second that you can send in this account in the current AWS Region. |
| Request rate for Probe, in a burst | Each supported Region: 10 | Yes | The maximum number of Probe requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for PutPolicy | Each supported Region: 2 per second | No | The maximum number of PutPolicy requests per second that you can send in this account in the current AWS Region. |
| Request rate for PutPolicy, in a burst | Each supported Region: 100 | No | The maximum number of PutPolicy requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for SearchJobs | Each supported Region: 1 per second | No | The maximum number of SearchJobs requests per second that you can send in this account in the current AWS Region. |
| Request rate for SearchJobs, in a burst | Each supported Region: 20 | No | The maximum number of SearchJobs requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for StartJobsQuery | Each supported Region: 1 per second | No | The maximum number of StartJobsQuery requests per second that you can send in this account in the current AWS Region. |
| Request rate for StartJobsQuery, in a burst | Each supported Region: 10 | No | The maximum number of StartJobsQuery requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for TagResource | Each supported Region: 2 per second | Yes | The maximum number of TagResource requests per second that you can send in this account in the current AWS Region. |
| Request rate for TagResource, in a burst | Each supported Region: 100 | Yes | The maximum number of TagResource requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for UntagResource | Each supported Region: 2 per second | Yes | The maximum number of UntagResource requests per second that you can send in this account in the current AWS Region. |
| Request rate for UntagResource, in a burst | Each supported Region: 100 | Yes | The maximum number of UntagResource requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for UpdateJobTemplate | Each supported Region: 2 per second | Yes | The maximum number of UpdateJobTemplate requests per second that you can send in this account in the current AWS Region. |
| Request rate for UpdateJobTemplate, in a burst | Each supported Region: 100 | Yes | The maximum number of UpdateJobTemplate requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for UpdatePreset | Each supported Region: 2 per second | Yes | The maximum number of UpdatePreset requests per second that you can send in this account in the current AWS Region. |
| Request rate for UpdatePreset, in a burst | Each supported Region: 100 | Yes | The maximum number of UpdatePreset requests that you can send in one burst in this account in the current AWS Region. |
| Request rate for UpdateQueue | Each supported Region: 2 per second | Yes | The maximum number of UpdateQueue requests per second that you can send in this account in the current AWS Region. |

### 027-amazon-eventbridge-scheduler.pdf

- Status: **ok**, 1 call(s), 150.7 s, in 4,414 / out 5,916 tokens
- Service: Amazon EventBridge Scheduler; quota table format: `standard`

#### Endpoints (89)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | scheduler.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | scheduler-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | scheduler-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | scheduler.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | scheduler.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | scheduler-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | scheduler-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | scheduler.us-east-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-1 | scheduler.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-1 | scheduler-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-1 | scheduler-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-1 | scheduler.us-west-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | scheduler.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | scheduler-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | scheduler-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | scheduler.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | scheduler.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | scheduler.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | scheduler.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | scheduler.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | scheduler.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | scheduler.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | scheduler.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | scheduler.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | scheduler.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | scheduler.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | scheduler.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | scheduler.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | scheduler.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | scheduler.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | scheduler.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | scheduler.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | scheduler.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | scheduler.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | scheduler.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | scheduler.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | scheduler.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | scheduler.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | scheduler.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | scheduler.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | scheduler.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Taipei) | ap-east-2 | scheduler.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | scheduler.ap-east-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | scheduler.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | scheduler.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | scheduler.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | scheduler.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | scheduler.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | scheduler-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | scheduler-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | scheduler.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | scheduler.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | scheduler-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada (Calgary) | ca-west-1 | scheduler-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Calgary) | ca-west-1 | scheduler.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | scheduler.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | scheduler.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | scheduler.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | scheduler.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | scheduler.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | scheduler.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | scheduler.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | scheduler.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-3 | scheduler.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-3 | scheduler.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-2 | scheduler.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-2 | scheduler.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | scheduler.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | scheduler.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | scheduler.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | scheduler.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | scheduler.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | scheduler.il-central-1.api.aws | HTTPS | dual_stack |
| Mexico (Central) | mx-central-1 | scheduler.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | scheduler.mx-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | scheduler.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | scheduler.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | scheduler.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | scheduler.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | scheduler.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | scheduler.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | scheduler.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | scheduler-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | scheduler-fips.us-gov-east-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | scheduler.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | scheduler.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | scheduler-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | scheduler-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | scheduler.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (14)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| CreateSchedule request rate | us-east-1: 5,000; us-east-2: 5,000; us-west-2: 5,000; ap-northeast-1: 5,000; ap-south-1: 5,000; ap-southeast-1: 5,000; ap-southeast-2: 5,000; eu-central-1: 5,000; eu-west-1: 5,000; eu-west-2: 5,000; sa-east-1: 5,000; Each of the other supported Regions: 250 | Yes | Maximum CreateSchedule requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. This is adjustable to tens of thousands of requests per second. |
| CreateScheduleGroup request rate | Each supported Region: 10 | Yes | Maximum CreateScheduleGroup requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. |
| DeleteSchedule request rate | us-east-1: 1,000; us-east-2: 1,000; us-west-2: 1,000; ap-northeast-1: 1,000; ap-south-1: 1,000; ap-southeast-1: 1,000; ap-southeast-2: 1,000; eu-central-1: 1,000; eu-west-1: 1,000; eu-west-2: 1,000; sa-east-1: 1,000; Each of the other supported Regions: 250 | Yes | Maximum DeleteSchedule requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. This is adjustable to tens of thousands of requests per second. |
| DeleteScheduleGroup request rate | Each supported Region: 10 | Yes | Maximum DeleteScheduleGroup requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. |
| GetSchedule request rate | us-east-1: 1,000; us-east-2: 1,000; us-west-2: 1,000; ap-northeast-1: 1,000; ap-south-1: 1,000; ap-southeast-1: 1,000; ap-southeast-2: 1,000; eu-central-1: 1,000; eu-west-1: 1,000; eu-west-2: 1,000; sa-east-1: 1,000; Each of the other supported Regions: 250 | Yes | Maximum GetSchedule requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. This is adjustable to tens of thousands of requests per second. |
| GetScheduleGroup request rate | Each supported Region: 10 | Yes | Maximum GetScheduleGroup requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. |
| Invocations throttle limit in transactions per second | us-east-1: 1,000; us-east-2: 1,000; us-west-2: 1,000; ap-northeast-1: 1,000; ap-south-1: 1,000; ap-southeast-1: 1,000; ap-southeast-2: 1,000; eu-central-1: 1,000; eu-west-1: 1,000; eu-west-2: 1,000; sa-east-1: 1,000; Each of the other supported Regions: 500 | Yes | An invocation is a schedule payload being delivered to the defined target. After the limit is reached, the invocations are throttled; that is, they still happen but they are delayed. This is adjustable to tens of thousands of transactions per second. |
| ListScheduleGroups request rate | Each supported Region: 10 | Yes | Maximum ListScheduleGroups requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. |
| ListSchedules request rate | Each supported Region: 50 | Yes | Maximum ListSchedules requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. |
| ListTagsForResource request rate | Each supported Region: 10 | Yes | Assigns one or more tags (key-value pairs) to the specified Scheduler resource. |
| Number of schedule groups | Each supported Region: 500 | Yes | Maximum number of schedule groups per region. |
| Number of schedules | Each supported Region: 10,000,000 | Yes | The maximum number of schedules per region. This quota includes one-time schedules that have completed running. We recommend configuring your schedules to automatically delete after completion using the ActionAfterCompletion feature. This is adjustable to billions of schedules. |
| TagResource request rate | Each supported Region: 1 | Yes | Assigns one or more tags (key-value pairs) to the specified Scheduler resource. |
| UntagResource request rate | Each supported Region: 1 | Yes | Removes one or more tags from the specified Scheduler resource. |

### 068-aws-elastic-beanstalk.pdf

- Status: **ok**, 1 call(s), 107.2 s, in 5,020 / out 4,066 tokens
- Service: AWS Elastic Beanstalk; quota table format: `standard`

#### Endpoints (76)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | elasticbeanstalk.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | elasticbeanstalk-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | elasticbeanstalk-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | elasticbeanstalk.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | elasticbeanstalk.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | elasticbeanstalk-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | elasticbeanstalk-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | elasticbeanstalk.us-east-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | elasticbeanstalk.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | elasticbeanstalk-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | elasticbeanstalk-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | elasticbeanstalk.us-west-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | elasticbeanstalk.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | elasticbeanstalk-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | elasticbeanstalk-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | elasticbeanstalk.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | elasticbeanstalk.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | elasticbeanstalk.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hong Kong) | ap-east-1 | elasticbeanstalk.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | elasticbeanstalk.ap-east-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | elasticbeanstalk.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | elasticbeanstalk.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | elasticbeanstalk.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | elasticbeanstalk.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | elasticbeanstalk.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | elasticbeanstalk.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Melbourne) | ap-southeast-4 | elasticbeanstalk.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | elasticbeanstalk.ap-southeast-4.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | elasticbeanstalk.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | elasticbeanstalk.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (New Zealand) | ap-southeast-6 | elasticbeanstalk.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | elasticbeanstalk.ap-southeast-6.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | elasticbeanstalk.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | elasticbeanstalk.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | elasticbeanstalk.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | elasticbeanstalk.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | elasticbeanstalk.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | elasticbeanstalk.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | elasticbeanstalk.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | elasticbeanstalk.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Thailand) | ap-southeast-7 | elasticbeanstalk.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | elasticbeanstalk.ap-southeast-7.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | elasticbeanstalk.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | elasticbeanstalk.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | elasticbeanstalk.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | elasticbeanstalk.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Calgary) | ca-west-1 | elasticbeanstalk.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | elasticbeanstalk.ca-west-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | elasticbeanstalk.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | elasticbeanstalk.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | elasticbeanstalk.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | elasticbeanstalk.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | elasticbeanstalk.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | elasticbeanstalk.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Milan) | eu-south-1 | elasticbeanstalk.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | elasticbeanstalk.eu-south-1.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | elasticbeanstalk.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | elasticbeanstalk.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Spain) | eu-south-2 | elasticbeanstalk.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | elasticbeanstalk.eu-south-2.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | elasticbeanstalk.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | elasticbeanstalk.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | elasticbeanstalk.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | elasticbeanstalk.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | elasticbeanstalk.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | elasticbeanstalk.il-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | elasticbeanstalk.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | elasticbeanstalk.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | elasticbeanstalk.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | elasticbeanstalk.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | elasticbeanstalk.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | elasticbeanstalk.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | elasticbeanstalk.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | elasticbeanstalk.us-gov-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | elasticbeanstalk.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | elasticbeanstalk.us-gov-west-1.api.aws | HTTPS | dual_stack |

#### Quotas (3)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Application versions | Each supported Region: 1,000 | Yes | The maximum number of application versions that you can create in this account in the current Region. The limit applies across applications, not per application. |
| Applications | Each supported Region: 75 | Yes | The maximum number of applications that you can create in this account in the current Region. |
| Configuration templates | Each supported Region: 2,000 | Yes | The maximum number of configuration templates that you can create in this account in the current Region. |

### 051-amazon-timestream.pdf

- Status: **failed**, 1 call(s), 510.8 s, in 4,733 / out 18,432 tokens

#### Error

```text
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a string at line 1743 column 25
--- no repair call
```

### 028-amazon-fsx.pdf

- Status: **failed**, 2 call(s), 296.8 s, in 14,573 / out 10,817 tokens

#### Error

```text
- endpoints.42.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-central-1.amazonaws.com'
- endpoints.43.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-central-1.api.aws'
- endpoints.45.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-west-1.amazonaws.com'
- endpoints.47.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-west-2.amazonaws.com'
- endpoints.49.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-south-1.amazonaws.com'
- endpoints.51.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-west-3.amazonaws.com'
- endpoints.53.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-south-2.amazonaws.com'
- endpoints.55.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-north-1.amazonaws.com'
- endpoints.56.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-central-2.amazonaws.com'
- endpoints.57.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-central-2.amazonaws.com'
- endpoints.59.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.il-central-1.amazonaws.com'
- endpoints.60.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.il-central-1.api.aws'
--- after repair:
- endpoints.42.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-central-1.amazonaws.com'
- endpoints.43.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-central-1.api.aws'
- endpoints.45.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-west-1.amazonaws.com'
- endpoints.47.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-west-2.amazonaws.com'
- endpoints.49.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-south-1.amazonaws.com'
- endpoints.51.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-west-3.amazonaws.com'
- endpoints.53.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-south-2.amazonaws.com'
- endpoints.55.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-north-1.amazonaws.com'
- endpoints.56.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-central-2.amazonaws.com'
- endpoints.57.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.eu-central-2.amazonaws.com'
- endpoints.59.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.il-central-1.amazonaws.com'
- endpoints.60.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-fips.il-central-1.api.aws'
```

### 073-aws-firewall-manager.pdf

- Status: **failed**, 2 call(s), 253.4 s, in 13,103 / out 9,395 tokens

#### Error

```text
- endpoints.19.endpoint: not printed in an endpoints table of the 'AWS Firewall Manager' chapter: 'fms-fips.ap-northeast-3.amazonaws.com'
- quotas.7.name: not printed in a Standard Quota Table of the chapter: 'Custom managed application lists in any content audit security group policy'
- quotas.9.name: not printed in a Standard Quota Table of the chapter: 'Custom managed protocol lists in any content audit security group policy'
--- after repair:
- endpoints.19.endpoint: not printed in an endpoints table of the 'AWS Firewall Manager' chapter: 'fms-fips.ap-northeast-3.amazonaws.com'
```

### 046-amazon-simple-email-service.pdf

- Status: **repaired**, 2 call(s), 205.8 s, in 17,371 / out 7,131 tokens
- Service: Amazon Simple Email Service; quota table format: `standard`

#### Endpoints (68)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | email.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | email-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | email-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | email.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | email.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | email-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | email-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | email.us-east-1.api.aws | HTTPS | dual_stack |
| US West (N. California) | us-west-1 | email.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | email-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | email-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | email.us-west-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | email.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | email-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | email-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | email.us-west-2.api.aws | HTTPS | dual_stack |
| Africa (Cape Town) | af-south-1 | email.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | email.af-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Hyderabad) | ap-south-2 | email.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | email.ap-south-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Jakarta) | ap-southeast-3 | email.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | email.ap-southeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Malaysia) | ap-southeast-5 | email.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | email.ap-southeast-5.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | email.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | email.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Osaka) | ap-northeast-3 | email.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | email.ap-northeast-3.api.aws | HTTPS | dual_stack |
| Asia Pacific (Seoul) | ap-northeast-2 | email.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | email.ap-northeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Singapore) | ap-southeast-1 | email.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | email.ap-southeast-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | email.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | email.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | email.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | email.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | email.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | email.ca-central-1.api.aws | HTTPS | dual_stack |
| Canada (Central) | ca-central-1 | email-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | email-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (West) | ca-west-1 | email.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (West) | ca-west-1 | email.ca-west-1.api.aws | HTTPS | dual_stack |
| Canada (West) | ca-west-1 | email-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada (West) | ca-west-1 | email-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Europe (Frankfurt) | eu-central-1 | email.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | email.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | email.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | email.eu-west-1.api.aws | HTTPS | dual_stack |
| Europe (London) | eu-west-2 | email.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | email.eu-west-2.api.aws | HTTPS | dual_stack |
| Europe (Paris) | eu-west-3 | email.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | email.eu-west-3.api.aws | HTTPS | dual_stack |
| Europe (Stockholm) | eu-north-1 | email.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | email.eu-north-1.api.aws | HTTPS | dual_stack |
| Europe (Zurich) | eu-central-2 | email.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | email.eu-central-2.api.aws | HTTPS | dual_stack |
| Israel (Tel Aviv) | il-central-1 | email.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | email.il-central-1.api.aws | HTTPS | dual_stack |
| Middle East (Bahrain) | me-south-1 | email.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | email.me-south-1.api.aws | HTTPS | dual_stack |
| Middle East (UAE) | me-central-1 | email.me-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | email.me-central-1.api.aws | HTTPS | dual_stack |
| South America (São Paulo) | sa-east-1 | email.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | email.sa-east-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | email.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | email.us-gov-west-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-East) | us-gov-east-1 | email.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | email.us-gov-east-1.api.aws | HTTPS | dual_stack |

#### Quotas (4)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Configuration set count | Each supported Region: 10,000 | Yes | The maximum number of configuration sets that can exist within the current Region. |
| Sending quota | Each supported Region: 200 per 24 hours | Yes | The maximum number of emails that you can send in a 24-hour period for this account in the current Region. |
| Sending rate | Each supported Region: 1 per second | Yes | The maximum number of emails that Amazon SES can accept each second for this account in the current Region. |
| Tenant count | Each supported Region: 10,000 | Yes | The maximum number of tenants that can exist within the current Region. |

#### First answer rejected (repaired)

```text
- endpoints.37.endpoint: not printed in an endpoints table of the 'Amazon Simple Email Service' chapter: 'email-ca-central-1.api.aws'
- endpoints.41.endpoint: not printed in an endpoints table of the 'Amazon Simple Email Service' chapter: 'email-ca-west-1.api.aws'
```
