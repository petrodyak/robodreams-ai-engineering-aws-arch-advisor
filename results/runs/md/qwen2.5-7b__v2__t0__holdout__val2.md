# Run `qwen2.5-7b__v2__t0__holdout__val2`

Generated from the JSONL run file by `src/extract/report_md.py`; do not edit.

- Model: `qwen2.5:7b`
- Prompt version: `v2` (file sha `a3adf0379524`)
- Schema sha: `d4010de95c65`; validation version `2`
- Sampling: `t0` (temperature 0.0, top_p None)
- Documents: 10

## Summary

| # | Document | Group | Status | Calls | Latency, s | In tokens | Out tokens | Quota table | Endpoints | Quotas |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [079-aws-iot-device-defender.pdf](#079-aws-iot-device-defenderpdf) | edge | ok | 1 | 80.5 | 6,241 | 2,766 | non_standard | 56 | 0 |
| 2 | [059-aws-clean-rooms.pdf](#059-aws-clean-roomspdf) | edge | failed | 2 | 438.1 | 21,196 | 15,091 | — | — | — |
| 3 | [016-amazon-comprehend.pdf](#016-amazon-comprehendpdf) | edge | failed | 2 | 418.6 | 20,704 | 14,169 | — | — | — |
| 4 | [069-aws-elemental-mediaconvert.pdf](#069-aws-elemental-mediaconvertpdf) | edge | ok | 1 | 170.6 | 6,320 | 6,287 | standard | 25 | 72 |
| 5 | [027-amazon-eventbridge-scheduler.pdf](#027-amazon-eventbridge-schedulerpdf) | medium | ok | 1 | 150.0 | 4,568 | 5,866 | standard | 88 | 14 |
| 6 | [068-aws-elastic-beanstalk.pdf](#068-aws-elastic-beanstalkpdf) | medium | ok | 1 | 107.3 | 5,174 | 4,066 | standard | 76 | 3 |
| 7 | [051-amazon-timestream.pdf](#051-amazon-timestreampdf) | medium | failed | 2 | 527.2 | 22,328 | 17,932 | — | — | — |
| 8 | [028-amazon-fsx.pdf](#028-amazon-fsxpdf) | medium | ok | 1 | 122.8 | 4,509 | 4,803 | standard | 53 | 28 |
| 9 | [073-aws-firewall-manager.pdf](#073-aws-firewall-managerpdf) | medium | failed | 2 | 257.6 | 13,351 | 9,539 | — | — | — |
| 10 | [046-amazon-simple-email-service.pdf](#046-amazon-simple-email-servicepdf) | medium | failed | 2 | 218.3 | 17,895 | 7,563 | — | — | — |

## Documents

### 079-aws-iot-device-defender.pdf

- Status: **ok**, 1 call(s), 80.5 s, in 6,241 / out 2,766 tokens
- Service: AWS IoT Device Defender; quota table format: `non_standard`

#### Endpoints (56)

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

### 059-aws-clean-rooms.pdf

- Status: **failed**, 2 call(s), 438.1 s, in 21,196 / out 15,091 tokens

#### Error

```text
- quotas.74.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListAnalysisLogExport requests'
- quotas.75.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListAnalysisTemplate requests'
- quotas.76.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationAnalysisTemplate requests'
- quotas.77.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationChangeRequest requests'
- quotas.78.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationConfiguredAudienceModelAssociation requests'
- quotas.79.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationIdNamespaceAssociation requests'
- quotas.80.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationPrivacyBudgetTemplate requests'
- quotas.81.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListConfiguredAudienceModelAssociation requests'
- quotas.82.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListConfiguredTableAssociation requests'
- quotas.83.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListConfiguredTable requests'
- quotas.84.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListIdMappingTable requests'
- quotas.85.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListIdNamespaceAssociation requests'
- quotas.86.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListMember requests'
- quotas.87.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListMembership requests'
- quotas.88.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListPrivacyBudgetTemplate requests'
- quotas.89.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListProtectedJob requests'
- quotas.90.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListProtectedQuery requests'
- quotas.91.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListSchema requests'
--- after repair:
- quotas.74.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListAnalysisLogExport requests'
- quotas.75.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListAnalysisTemplate requests'
- quotas.76.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationAnalysisTemplate requests'
- quotas.77.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationChangeRequest requests'
- quotas.78.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationConfiguredAudienceModelAssociation requests'
- quotas.79.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationIdNamespaceAssociation requests'
- quotas.80.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationPrivacyBudgetTemplate requests'
- quotas.81.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListConfiguredAudienceModelAssociation requests'
- quotas.82.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListConfiguredTableAssociation requests'
- quotas.83.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListConfiguredTable requests'
- quotas.84.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListIdMappingTable requests'
- quotas.85.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListIdNamespaceAssociation requests'
- quotas.86.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListMember requests'
- quotas.87.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListMembership requests'
- quotas.88.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListPrivacyBudgetTemplate requests'
- quotas.89.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListProtectedJob requests'
- quotas.90.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListProtectedQuery requests'
- quotas.91.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListSchema requests'
```

### 016-amazon-comprehend.pdf

- Status: **failed**, 2 call(s), 418.6 s, in 20,704 / out 14,169 tokens

#### Error

```text
- endpoints.34.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'comprehend-fips.us-gov-west-1.amazon'
--- after repair:
- endpoints.34.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'comprehend-fips.us-gov-west-1.amazon'
```

### 069-aws-elemental-mediaconvert.pdf

- Status: **ok**, 1 call(s), 170.6 s, in 6,320 / out 6,287 tokens
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
| Request rate for CreateResourceShare | Each supported Region: 0.1 | No | The maximum number of Share requests per second that you can send in this account in the current AWS Region. |
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

- Status: **ok**, 1 call(s), 150.0 s, in 4,568 / out 5,866 tokens
- Service: Amazon EventBridge Scheduler; quota table format: `standard`

#### Endpoints (88)

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
| Europe (Paris) | eu-west-3 | scheduler.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | scheduler.eu-west-3.api.aws | HTTPS | dual_stack |
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

- Status: **ok**, 1 call(s), 107.3 s, in 5,174 / out 4,066 tokens
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

- Status: **failed**, 2 call(s), 527.2 s, in 22,328 / out 17,932 tokens

#### Error

```text
- endpoints.3.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.8.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.13.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.17.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'ingest.timestream.ap-southeast-2.ama'
- endpoints.18.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.20.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'ingest.timestream.ap-northeast-1.ama'
- endpoints.21.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.23.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'ingest.timestream.eu-central-1.amazo'
- endpoints.24.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.28.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'ingest.timestream.us-gov-west-1.amaz'
- endpoints.29.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.33.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'query.timestream-fips.us-east-2.amaz'
- endpoints.34.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'onaws.com'
- endpoints.38.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'query.timestream-fips.us-east-1.amaz'
- endpoints.39.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'onaws.com'
- endpoints.43.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'query.timestream-fips.us-west-2.amaz'
- endpoints.44.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'onaws.com'
- endpoints.48.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'query.timestream.ap-southeast-2.amaz'
- endpoints.49.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'onaws.com'
- endpoints.51.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'query.timestream.ap-northeast-1.amaz'
- endpoints.52.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'onaws.com'
- endpoints.54.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'query.timestream.eu-central-1.amazo'
- endpoints.55.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.59.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'query.timestream.us-gov-west-1.amaz'
- endpoints.60.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.62.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.us-east-2.amazon'
- endpoints.65.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.us-east-1.amazon'
- endpoints.68.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.us-west-2.amazon'
- endpoints.71.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.af-south-1.amazo'
- endpoints.72.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.73.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-east-1.amazon'
- endpoints.74.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'aws.com'
- endpoints.77.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-south-2.amazo'
- endpoints.78.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.79.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-southeast-3.amazo'
- endpoints.80.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'mazonaws.com'
- endpoints.81.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-southeast-4.amazo'
- endpoints.82.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.83.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-south-1.amazo'
- endpoints.84.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.85.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-northeast-3.amazo'
- endpoints.86.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.87.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-northeast-2.amazo'
- endpoints.88.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.89.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-southeast-1.amazo'
- endpoints.90.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.91.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-southeast-2.amazo'
- endpoints.92.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.93.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-southeast-7.amazo'
- endpoints.94.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.95.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-northeast-1.amazo'
- endpoints.96.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.97.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ca-central-1.amazo'
- endpoints.98.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.101.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-central-1.amazo'
- endpoints.102.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.105.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-west-1.amazon'
- endpoints.106.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'aws.com'
- endpoints.109.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-west-2.amazon'
- endpoints.110.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'aws.com'
- endpoints.113.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-south-1.amazo'
- endpoints.114.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.117.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-west-3.amazon'
- endpoints.118.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'aws.com'
- endpoints.121.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-south-2.amazo'
- endpoints.122.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.125.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-north-1.amazo'
- endpoints.126.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.129.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-central-2.amazo'
- endpoints.130.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.133.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.il-central-1.amazo'
- endpoints.134.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.137.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ca-central-1.amazo'
- endpoints.138.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.141.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.sa-east-1.amazon'
- endpoints.142.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'aws.com'
--- after repair:
- endpoints.14.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'ingest.timestream.ap-southeast-2.ama'
- endpoints.15.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.17.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'ingest.timestream.ap-northeast-1.ama'
- endpoints.18.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.20.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'ingest.timestream.eu-central-1.amazo'
- endpoints.21.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.25.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'ingest.timestream.us-gov-west-1.amaz'
- endpoints.26.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.30.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'query.timestream-fips.us-east-2.amaz'
- endpoints.31.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'onaws.com'
- endpoints.35.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'query.timestream-fips.us-east-1.amaz'
- endpoints.36.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'onaws.com'
- endpoints.40.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'query.timestream-fips.us-west-2.amaz'
- endpoints.41.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'onaws.com'
- endpoints.45.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'query.timestream.ap-southeast-2.amaz'
- endpoints.46.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'onaws.com'
- endpoints.48.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'query.timestream.ap-northeast-1.amaz'
- endpoints.49.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'onaws.com'
- endpoints.51.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'query.timestream.eu-central-1.amazo'
- endpoints.52.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.56.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'query.timestream.us-gov-west-1.amaz'
- endpoints.57.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.59.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.us-east-2.amazon'
- endpoints.62.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.us-east-1.amazon'
- endpoints.65.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.us-west-2.amazon'
- endpoints.68.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.af-south-1.amazo'
- endpoints.69.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.70.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-east-1.amazon'
- endpoints.71.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'aws.com'
- endpoints.74.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-south-2.amazo'
- endpoints.75.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.76.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-southeast-3.amazo'
- endpoints.77.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'mazonaws.com'
- endpoints.78.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-southeast-4.amazo'
- endpoints.79.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.80.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-south-1.amazo'
- endpoints.81.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.82.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-northeast-3.amazo'
- endpoints.83.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.84.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-northeast-2.amazo'
- endpoints.85.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.86.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-southeast-1.amazo'
- endpoints.87.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.88.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-southeast-2.amazo'
- endpoints.89.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.90.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-southeast-7.amazo'
- endpoints.91.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.92.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ap-northeast-1.amazo'
- endpoints.93.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.94.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ca-central-1.amazo'
- endpoints.95.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.98.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-central-1.amazo'
- endpoints.99.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.102.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-west-1.amazon'
- endpoints.103.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'aws.com'
- endpoints.106.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-west-2.amazon'
- endpoints.107.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'aws.com'
- endpoints.110.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-south-1.amazo'
- endpoints.111.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.114.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-west-3.amazon'
- endpoints.115.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'aws.com'
- endpoints.118.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-south-2.amazo'
- endpoints.119.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.122.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-north-1.amazo'
- endpoints.123.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'naws.com'
- endpoints.126.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.eu-central-2.amazo'
- endpoints.127.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.130.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.il-central-1.amazo'
- endpoints.131.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.134.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.ca-central-1.amazo'
- endpoints.135.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.138.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'timestream-influxdb.sa-east-1.amazon'
- endpoints.139.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'aws.com'
```

### 028-amazon-fsx.pdf

- Status: **ok**, 1 call(s), 122.8 s, in 4,509 / out 4,803 tokens
- Service: Amazon FSx; quota table format: `standard`

#### Endpoints (53)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | fsx.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | fsx-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | fsx-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | fsx.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | fsx-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | fsx-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | fsx.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | fsx-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | fsx-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | fsx.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | fsx-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | fsx-fips.us-west-2.amazonaws.com | HTTPS | fips |
| Africa (Cape Town) | af-south-1 | fsx.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | fsx.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | fsx.ap-south-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Hong Kong) | ap-east-1 | fsx.ap-southeast-3.amazonaws.com | HTTPS | global |
| Asia Pacific (Hong Kong) | ap-east-1 | fsx.ap-southeast-5.amazonaws.com | HTTPS | global |
| Asia Pacific (Hong Kong) | ap-east-1 | fsx.ap-southeast-4.amazonaws.com | HTTPS | global |
| Asia Pacific (Hong Kong) | ap-east-1 | fsx.ap-south-1.amazonaws.com | HTTPS | global |
| Asia Pacific (Hong Kong) | ap-east-1 | fsx.ap-southeast-6.amazonaws.com | HTTPS | global |
| Asia Pacific (Hong Kong) | ap-east-1 | fsx.ap-northeast-3.amazonaws.com | HTTPS | global |
| Asia Pacific (Seoul) | ap-northeast-2 | fsx.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | fsx.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | fsx.ap-southeast-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Singapore) | ap-southeast-1 | fsx.ap-east-2.amazonaws.com | HTTPS | global |
| Asia Pacific (Singapore) | ap-southeast-1 | fsx.ap-southeast-7.amazonaws.com | HTTPS | global |
| Asia Pacific (Tokyo) | ap-northeast-1 | fsx.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | fsx.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | fsx-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | fsx-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | fsx-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Calgary) | ca-west-1 | fsx.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Calgary) | ca-west-1 | fsx-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada (Calgary) | ca-west-1 | fsx-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Europe (Frankfurt) | eu-central-1 | fsx.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | fsx.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | fsx.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | fsx.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | fsx.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | fsx.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | fsx.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | fsx.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | fsx.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | fsx.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | fsx.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | fsx.me-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | fsx.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | fsx.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | fsx-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | fsx-fips.us-gov-east-1.api.aws | HTTPS | fips_dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | fsx.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | fsx-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | fsx-fips.us-gov-west-1.api.aws | HTTPS | fips_dual_stack |

#### Quotas (28)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| Lustre Cache_1 caches | Each supported Region: 100 | Yes | The maximum number of Amazon File Cache caches with cache type Lustre and deployment type Cache_1 that you can create in this account. |
| Lustre Cache_1 storage capacity | Each supported Region: 100,800 | Yes | The maximum amount of storage capacity (in GiB) that you can configure in this account for all Amazon File Cache caches with cache type Lustre and deployment type Cache_1. |
| Lustre Persistent HDD storage capacity (per file system) | Each supported Region: 102,000 | Yes | The maximum amount of HDD storage capacity (in GiB) that you can configure for an Amazon FSx for Lustre persistent file system. |
| Lustre Persistent Intelligent-Tiering SSD read cache storage capacity | Each supported Region: 100,800 | Yes | The maximum amount of provisioned SSD read cache storage capacity (in GiB) that you can configure for all Amazon FSx for Lustre Intelligent-Tiering file systems in this account. |
| Lustre Persistent Intelligent-Tiering throughput capacity | Each supported Region: 100,000 | Yes | The total amount of throughput capacity (in MBps) allowed for all Amazon FSx for Lustre Intelligent-Tiering file systems in this account. |
| Lustre Persistent_1 file systems | Each supported Region: 100 | Yes | The maximum number of Amazon FSx for Lustre persistent_1 file systems that you can create in this account. |
| Lustre Persistent_1 storage capacity | Each supported Region: 100,800 | Yes | The maximum amount of storage capacity (in GiB) that you can configure for all Amazon FSx for Lustre persistent_1 file systems in this account. |
| Lustre Persistent_2 file systems | Each supported Region: 100 | Yes | The maximum number of Amazon FSx for Lustre persistent_2 file systems that you can create in this account. |
| Lustre Persistent_2 storage capacity | Each supported Region: 100,800 | Yes | The maximum amount of storage capacity (in GiB) that you can configure for all Amazon FSx for Lustre persistent_2 file systems in this account. |
| Lustre Scratch file systems | Each supported Region: 100 | Yes | The maximum number of Amazon FSx for Lustre scratch file systems that you can create in this account. |
| Lustre Scratch storage capacity | Each supported Region: 100,800 | Yes | The maximum amount of storage capacity (in GiB) that you can configure for all Amazon FSx for Lustre scratch file systems in this account. |
| Lustre backups | Each supported Region: 500 | Yes | The maximum number of user-initiated backups that you can have for all Amazon FSx for Lustre file systems in this account. |
| ONTAP SSD IOPS | Each supported Region: 2,000,000 | Yes | The total amount of SSD IOPS allowed for all Amazon FSx for NetApp ONTAP file systems in this account. |
| ONTAP SSD storage capacity | Each supported Region: 1,048,576 | Yes | The maximum amount of SSD storage capacity (in GiB) for all Amazon FSx for NetApp ONTAP file systems that you can have in this account. |
| ONTAP backups | Each supported Region: 10,000 | Yes | The maximum number of user-initiated backups for all Amazon FSx for NetApp ONTAP file systems that you can have in this account. |
| ONTAP file systems | Each supported Region: 100 | Yes | The maximum number of Amazon FSx for NetApp ONTAP file systems that you can create in this account. |
| ONTAP throughput capacity | Each supported Region: 10,240 | Yes | The total amount of throughput capacity (in MBps) allowed for all Amazon FSx for NetApp ONTAP file systems in this account. |
| OpenZFS SSD storage capacity | us-east-1: 262,144; us-east-2: 262,144; us-west-2: 262,144; Each of the other supported Regions: 65,536 | Yes | The maximum amount of SSD storage capacity (in GiB) that you can configure for all Amazon FSx for OpenZFS file systems in this account. |
| OpenZFS SSD storage capacity (per file system) | Each supported Region: 524,288 | Yes | The maximum amount of SSD storage capacity (in GiB) that you can configure for an Amazon FSx for OpenZFS file system. |
| OpenZFS backups | Each supported Region: 10,000 | Yes | The maximum number of user-initiated backups for all Amazon FSx for OpenZFS file systems that you can have in this account. |
| OpenZFS disk IOPS | Each supported Region: 400,000 | Yes | The total amount of disk IOPS allowed for all Amazon FSx for OpenZFS file systems in this account. |
| OpenZFS file systems | Each supported Region: 100 | Yes | The maximum number of Amazon FSx for OpenZFS file systems that you can create in this account. |
| OpenZFS provisioned SSD read cache storage capacity | us-east-1: 262,144; us-east-2: 262,144; us-west-2: 262,144; Each of the other supported Regions: 65,536 | Yes | The maximum amount of provisioned SSD read cache storage capacity (in GiB) that you can configure for all Amazon FSx for OpenZFS file systems in this account. |
| OpenZFS throughput capacity | Each supported Region: 10,240 | Yes | The total amount of throughput capacity (in MBps) allowed for all Amazon FSx for OpenZFS file systems in this account. |
| Windows HDD storage capacity | Each supported Region: 524,288 | Yes | The maximum amount of HDD storage capacity (in GiB) allowed for all Amazon FSx for Windows File Server file systems in this account. |
| Windows SSD storage capacity | Each supported Region: 524,288 | Yes | The maximum amount of SSD storage capacity (in GiB) for all Amazon FSx for Windows File Server file systems that you can have in this account. |
| Windows backups | Each supported Region: 500 | Yes | The maximum number of user-initiated backups for all Amazon FSx for Windows File Server file systems that you can have in this account. |
| Windows file systems | Each supported Region: 100 | Yes | The maximum number of Amazon FSx for Windows Server file systems that you can create in this account. |

### 073-aws-firewall-manager.pdf

- Status: **failed**, 2 call(s), 257.6 s, in 13,351 / out 9,539 tokens

#### Error

```text
- endpoints.19.endpoint: not printed in an endpoints table of the 'AWS Firewall Manager' chapter: 'fms-fips.ap-northeast-3.amazonaws.com'
--- after repair:
- endpoints.19.endpoint: not printed in an endpoints table of the 'AWS Firewall Manager' chapter: 'fms-fips.ap-northeast-3.amazonaws.com'
```

### 046-amazon-simple-email-service.pdf

- Status: **failed**, 2 call(s), 218.3 s, in 17,895 / out 7,563 tokens

#### Error

```text
- endpoints.37.endpoint: not printed in an endpoints table of the 'Amazon Simple Email Service' chapter: 'email-ca-central-1.api.aws'
- endpoints.41.endpoint: not printed in an endpoints table of the 'Amazon Simple Email Service' chapter: 'email-ca-west-1.api.aws'
--- after repair:
- endpoints.37.endpoint: not printed in an endpoints table of the 'Amazon Simple Email Service' chapter: 'email-ca-central-1.api.aws'
- endpoints.41.endpoint: not printed in an endpoints table of the 'Amazon Simple Email Service' chapter: 'email-ca-west-1.api.aws'
```
