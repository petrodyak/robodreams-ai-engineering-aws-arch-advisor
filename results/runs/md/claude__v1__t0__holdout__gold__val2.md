# Run `claude__v1__t0__holdout__gold__val2`

Generated from the JSONL run file by `src/extract/report_md.py`; do not edit.

- Model: `claude-haiku-4-5`
- Prompt version: `v1` (file sha `8a0da697aa92`)
- Schema sha: `d4010de95c65`; validation version `2`
- Sampling: `t0` (temperature 0.0, top_p None)
- Documents: 5

## Summary

| # | Document | Group | Status | Calls | Latency, s | In tokens | Out tokens | Quota table | Endpoints | Quotas |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [027-amazon-eventbridge-scheduler.pdf](#027-amazon-eventbridge-schedulerpdf) | medium | ok | 1 | 36.8 | 7,254 | 5,021 | standard | 88 | 14 |
| 2 | [068-aws-elastic-beanstalk.pdf](#068-aws-elastic-beanstalkpdf) | medium | ok | 1 | 29.4 | 8,138 | 4,225 | standard | 76 | 3 |
| 3 | [051-amazon-timestream.pdf](#051-amazon-timestreampdf) | medium | ok | 1 | 42.6 | 7,551 | 5,996 | standard | 84 | 32 |
| 4 | [028-amazon-fsx.pdf](#028-amazon-fsxpdf) | medium | ok | 1 | 21.4 | 7,107 | 4,037 | standard | 52 | 28 |
| 5 | [073-aws-firewall-manager.pdf](#073-aws-firewall-managerpdf) | medium | ok | 1 | 35.1 | 6,879 | 4,634 | standard | 58 | 28 |

## Documents

### 027-amazon-eventbridge-scheduler.pdf

- Status: **ok**, 1 call(s), 36.8 s, in 7,254 / out 5,021 tokens
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
| US West (N. California) | us-west-1 | scheduler.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | scheduler-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | scheduler-fips.us-west-1.api.aws | HTTPS | fips_dual_stack |
| US West (N. California) | us-west-1 | scheduler.us-west-1.api.aws | HTTPS | dual_stack |
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
| Canada West (Calgary) | ca-west-1 | scheduler.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | scheduler-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | scheduler-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | scheduler.ca-west-1.api.aws | HTTPS | dual_stack |
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
| Europe (Spain) | eu-south-2 | scheduler.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | scheduler.eu-south-2.api.aws | HTTPS | dual_stack |
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
| ListTagsForResource request rate | Each supported Region: 10 | Yes | Lists the tags associated with the Scheduler resource. |
| Number of schedule groups | Each supported Region: 500 | Yes | Maximum number of schedule groups per region. |
| Number of schedules | Each supported Region: 10,000,000 | Yes | The maximum number of schedules per region. This quota includes one-time schedules that have completed running. We recommend configuring your schedules to automatically delete after completion using the ActionAfterCompletion feature. This is adjustable to billions of schedules. |
| TagResource request rate | Each supported Region: 1 | Yes | Assigns one or more tags (key-value pairs) to the specified Scheduler resource. |
| UntagResource request rate | Each supported Region: 1 | Yes | Removes one or more tags from the specified Scheduler resource. |

### 068-aws-elastic-beanstalk.pdf

- Status: **ok**, 1 call(s), 29.4 s, in 8,138 / out 4,225 tokens
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
| Canada West (Calgary) | ca-west-1 | elasticbeanstalk.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | elasticbeanstalk.ca-west-1.api.aws | HTTPS | dual_stack |
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

- Status: **ok**, 1 call(s), 42.6 s, in 7,551 / out 5,996 tokens
- Service: Amazon Timestream; quota table format: `standard`

#### Endpoints (84)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | ingest.timestream.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | timestream-ingest-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | ingest.timestream-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | timestream-ingest.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | ingest.timestream.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | timestream-ingest-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | ingest.timestream-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | timestream-ingest.us-east-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | ingest.timestream.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | timestream-ingest-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | ingest.timestream-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | timestream-ingest.us-west-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | ingest.timestream.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | timestream-ingest.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | ingest.timestream.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | timestream-ingest.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | ingest.timestream.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | timestream-ingest.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | ingest.timestream.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | timestream-ingest.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | ingest.timestream.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | timestream-ingest.eu-west-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | ingest.timestream.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | timestream-ingest.us-gov-west-1.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | query.timestream.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | timestream-query-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | query.timestream-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (Ohio) | us-east-2 | timestream-query.us-east-2.api.aws | HTTPS | dual_stack |
| US East (N. Virginia) | us-east-1 | query.timestream.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | timestream-query-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | query.timestream-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | timestream-query.us-east-1.api.aws | HTTPS | dual_stack |
| US West (Oregon) | us-west-2 | query.timestream.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | timestream-query-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | query.timestream-fips.us-west-2.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | timestream-query.us-west-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Mumbai) | ap-south-1 | query.timestream.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | timestream-query.ap-south-1.api.aws | HTTPS | dual_stack |
| Asia Pacific (Sydney) | ap-southeast-2 | query.timestream.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | timestream-query.ap-southeast-2.api.aws | HTTPS | dual_stack |
| Asia Pacific (Tokyo) | ap-northeast-1 | query.timestream.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | timestream-query.ap-northeast-1.api.aws | HTTPS | dual_stack |
| Europe (Frankfurt) | eu-central-1 | query.timestream.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | timestream-query.eu-central-1.api.aws | HTTPS | dual_stack |
| Europe (Ireland) | eu-west-1 | query.timestream.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | timestream-query.eu-west-1.api.aws | HTTPS | dual_stack |
| AWS GovCloud (US-West) | us-gov-west-1 | query.timestream.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | timestream-query.us-gov-west-1.api.aws | HTTPS | dual_stack |
| US East (Ohio) | us-east-2 | timestream-influxdb.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | timestream-influxdb-fips.us-east-2.api.aws | HTTPS | fips_dual_stack |
| US East (Ohio) | us-east-2 | timestream-influxdb-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | timestream-influxdb.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | timestream-influxdb-fips.us-east-1.api.aws | HTTPS | fips_dual_stack |
| US East (N. Virginia) | us-east-1 | timestream-influxdb-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | timestream-influxdb.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | timestream-influxdb-fips.us-west-2.api.aws | HTTPS | fips_dual_stack |
| US West (Oregon) | us-west-2 | timestream-influxdb-fips.us-west-2.amazonaws.com | HTTPS | fips |
| Africa (Cape Town) | af-south-1 | timestream-influxdb.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | timestream-influxdb.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hyderabad) | ap-south-2 | timestream-influxdb.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | timestream-influxdb.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | timestream-influxdb.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | timestream-influxdb.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | timestream-influxdb.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | timestream-influxdb.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | timestream-influxdb.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | timestream-influxdb.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | timestream-influxdb.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | timestream-influxdb.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | timestream-influxdb.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | timestream-influxdb-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada (Central) | ca-central-1 | timestream-influxdb-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Europe (Frankfurt) | eu-central-1 | timestream-influxdb.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | timestream-influxdb.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | timestream-influxdb.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | timestream-influxdb.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | timestream-influxdb.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Spain) | eu-south-2 | timestream-influxdb.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | timestream-influxdb.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | timestream-influxdb.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | timestream-influxdb.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | timestream-influxdb.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (UAE) | me-central-1 | timestream-influxdb.me-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | timestream-influxdb.sa-east-1.amazonaws.com | HTTPS | ipv4 |

#### Quotas (32)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| CreateBatchLoadTask request rate | Each supported Region: 1 per second | No | Maximum number of CreateBatchLoadTask requests per second. |
| CreateDatabase request rate | Each supported Region: 1 per second | No | Maximum number of CreateDatabase requests per second. |
| CreateScheduledQuery request rate | Each supported Region: 1 per second | No | Maximum number of CreateScheduledQuery requests per second. |
| CreateTable request rate | Each supported Region: 1 per second | No | Maximum number of CreateTable requests per second. |
| Databases per account | Each supported Region: 500 | No | The maximum number of databases you can create per AWS account. |
| DeleteDatabase request rate | Each supported Region: 1 per second | No | Maximum number of DeleteDatabase requests per second. |
| DeleteScheduledQuery request rate | Each supported Region: 1 per second | No | Maximum number of DeleteScheduledQuery requests per second. |
| DeleteTable request rate | Each supported Region: 1 per second | No | Maximum number of DeleteTable requests per second. |
| DescribeAccountSettings request rate | Each supported Region: 1 per second | No | Maximum number of DescribeAccountSettings requests per second. |
| DescribeBatchLoadTask request rate | Each supported Region: 5 per second | No | Maximum number of DescribeBatchLoadTask requests per second. |
| DescribeDatabase request rate | Each supported Region: 5 per second | No | Maximum number of DescribeDatabase requests per second. |
| DescribeScheduledQuery request rate | Each supported Region: 5 per second | No | Maximum number of DescribeScheduledQuery requests per second. |
| DescribeTable request rate | Each supported Region: 5 per second | No | Maximum number of DescribeTable requests per second. |
| Dimensions per table | Each supported Region: 128 | No | The maximum number of dimensions per table. |
| ExecuteScheduledQuery request rate | Each supported Region: 5 per second | No | Maximum number of ExecuteScheduledQuery requests per second. |
| ListBatchLoadTasks request rate | Each supported Region: 5 per second | No | Maximum number of ListBatchLoadTasks requests per second. |
| ListDatabases request rate | Each supported Region: 5 per second | No | Maximum number of ListDatabases requests per second. |
| ListScheduledQueries request rate | Each supported Region: 5 per second | No | Maximum number of ListScheduledQueries requests per second. |
| ListTables request rate | Each supported Region: 5 per second | No | Maximum number of ListTables requests per second. |
| Max allowed MaxQueryTCU | Each supported Region: 1,000 | No | The maximum allowed MaxQueryTCU in your account |
| Max allowed ProvisionedQueryTCU | Each supported Region: 1,000 | No | The maximum allowed ProvisionedQueryTCU in your account |
| Maximum count of active magnetic store partitions per database | Each supported Region: 250 | No | Maximum number of active magnetic store partitions per database. A partition may remain active for up to 6 hours after receiving ingestion. |
| Measures per table | Each supported Region: 8,192 | No | The maximum number of measures per table. |
| PrepareQuery request rate | Each supported Region: 5 per second | No | Maximum number of PrepareQuery requests per second. |
| ResumeBatchLoadTask request rate | Each supported Region: 1 per second | No | Maximum number of ResumeBatchLoadTask requests per second. |
| Scheduled queries per account | Each supported Region: 10,000 | No | The maximum number of scheduled queries you can create per AWS account. |
| Tables per account | Each supported Region: 50,000 | No | The maximum number of tables you can create per AWS account. |
| Unique measures across multi-measure records per table | Each supported Region: 1,024 | No | The unique measures in all the multi-measure records defined in a single table. A single multi-measure record can have MaximumMeasureAttributesPerRecord unique measures, and a table can have MaximumMeasureAttributesPerTable unique measures defined across multi-measure records. |
| UpdateAccountSettings request rate | Each supported Region: 1 per second | No | Maximum number of UpdateAccountSettings requests per second. |
| UpdateDatabase request rate | Each supported Region: 1 per second | No | Maximum number of UpdateDatabase requests per second. |
| UpdateScheduledQuery request rate | Each supported Region: 1 per second | No | Maximum number of UpdateScheduledQuery requests per second. |
| UpdateTable request rate | Each supported Region: 1 per second | No | Maximum number of UpdateTable requests per second. |

### 028-amazon-fsx.pdf

- Status: **ok**, 1 call(s), 21.4 s, in 7,107 / out 4,037 tokens
- Service: Amazon FSx; quota table format: `standard`

#### Endpoints (52)

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
| Asia Pacific (Hyderabad) | ap-south-2 | fsx.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | fsx.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | fsx.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | fsx.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | fsx.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (New Zealand) | ap-southeast-6 | fsx.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | fsx.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | fsx.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | fsx.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | fsx.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Taipei) | ap-east-2 | fsx.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | fsx.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | fsx.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | fsx.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | fsx-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | fsx-fips.ca-central-1.api.aws | HTTPS | fips_dual_stack |
| Canada West (Calgary) | ca-west-1 | fsx.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | fsx-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | fsx-fips.ca-west-1.api.aws | HTTPS | fips_dual_stack |
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
| Lustre Persistent_1 file systems | Each supported Region: 100 | Yes | The maximum number of Amazon FSx for Lustre persistent_1 file systems that you can create in this account |
| Lustre Persistent_1 storage capacity | Each supported Region: 100,800 | Yes | The maximum amount of storage capacity (in GiB) that you can configure for all Amazon FSx for Lustre persistent_1 file systems in this account. |
| Lustre Persistent_2 file systems | Each supported Region: 100 | Yes | The maximum number of Amazon FSx for Lustre persistent_2 file systems that you can create in this account |
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

- Status: **ok**, 1 call(s), 35.1 s, in 6,879 / out 4,634 tokens
- Service: AWS Firewall Manager; quota table format: `standard`

#### Endpoints (58)

| Region name | Region | Endpoint | Protocol | Type |
|---|---|---|---|---|
| US East (Ohio) | us-east-2 | fms.us-east-2.amazonaws.com | HTTPS | ipv4 |
| US East (Ohio) | us-east-2 | fms-fips.us-east-2.amazonaws.com | HTTPS | fips |
| US East (N. Virginia) | us-east-1 | fms.us-east-1.amazonaws.com | HTTPS | ipv4 |
| US East (N. Virginia) | us-east-1 | fms-fips.us-east-1.amazonaws.com | HTTPS | fips |
| US West (N. California) | us-west-1 | fms.us-west-1.amazonaws.com | HTTPS | ipv4 |
| US West (N. California) | us-west-1 | fms-fips.us-west-1.amazonaws.com | HTTPS | fips |
| US West (Oregon) | us-west-2 | fms.us-west-2.amazonaws.com | HTTPS | ipv4 |
| US West (Oregon) | us-west-2 | fms-fips.us-west-2.amazonaws.com | HTTPS | fips |
| Africa (Cape Town) | af-south-1 | fms.af-south-1.amazonaws.com | HTTPS | ipv4 |
| Africa (Cape Town) | af-south-1 | fms-fips.af-south-1.amazonaws.com | HTTPS | fips |
| Asia Pacific (Hong Kong) | ap-east-1 | fms.ap-east-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Hong Kong) | ap-east-1 | fms-fips.ap-east-1.amazonaws.com | HTTPS | fips |
| Asia Pacific (Hyderabad) | ap-south-2 | fms.ap-south-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Jakarta) | ap-southeast-3 | fms.ap-southeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Malaysia) | ap-southeast-5 | fms.ap-southeast-5.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Melbourne) | ap-southeast-4 | fms.ap-southeast-4.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | fms.ap-south-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Mumbai) | ap-south-1 | fms-fips.ap-south-1.amazonaws.com | HTTPS | fips |
| Asia Pacific (New Zealand) | ap-southeast-6 | fms.ap-southeast-6.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Osaka) | ap-northeast-3 | fms.ap-northeast-3.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | fms.ap-northeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Seoul) | ap-northeast-2 | fms-fips.ap-northeast-2.amazonaws.com | HTTPS | fips |
| Asia Pacific (Singapore) | ap-southeast-1 | fms.ap-southeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Singapore) | ap-southeast-1 | fms-fips.ap-southeast-1.amazonaws.com | HTTPS | fips |
| Asia Pacific (Sydney) | ap-southeast-2 | fms.ap-southeast-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Sydney) | ap-southeast-2 | fms-fips.ap-southeast-2.amazonaws.com | HTTPS | fips |
| Asia Pacific (Taipei) | ap-east-2 | fms.ap-east-2.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Thailand) | ap-southeast-7 | fms.ap-southeast-7.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | fms.ap-northeast-1.amazonaws.com | HTTPS | ipv4 |
| Asia Pacific (Tokyo) | ap-northeast-1 | fms-fips.ap-northeast-1.amazonaws.com | HTTPS | fips |
| Canada (Central) | ca-central-1 | fms.ca-central-1.amazonaws.com | HTTPS | ipv4 |
| Canada (Central) | ca-central-1 | fms-fips.ca-central-1.amazonaws.com | HTTPS | fips |
| Canada West (Calgary) | ca-west-1 | fms.ca-west-1.amazonaws.com | HTTPS | ipv4 |
| Canada West (Calgary) | ca-west-1 | fms-fips.ca-west-1.amazonaws.com | HTTPS | fips |
| Europe (Frankfurt) | eu-central-1 | fms.eu-central-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Frankfurt) | eu-central-1 | fms-fips.eu-central-1.amazonaws.com | HTTPS | fips |
| Europe (Ireland) | eu-west-1 | fms.eu-west-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Ireland) | eu-west-1 | fms-fips.eu-west-1.amazonaws.com | HTTPS | fips |
| Europe (London) | eu-west-2 | fms.eu-west-2.amazonaws.com | HTTPS | ipv4 |
| Europe (London) | eu-west-2 | fms-fips.eu-west-2.amazonaws.com | HTTPS | fips |
| Europe (Milan) | eu-south-1 | fms.eu-south-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Milan) | eu-south-1 | fms-fips.eu-south-1.amazonaws.com | HTTPS | fips |
| Europe (Paris) | eu-west-3 | fms.eu-west-3.amazonaws.com | HTTPS | ipv4 |
| Europe (Paris) | eu-west-3 | fms-fips.eu-west-3.amazonaws.com | HTTPS | fips |
| Europe (Spain) | eu-south-2 | fms.eu-south-2.amazonaws.com | HTTPS | ipv4 |
| Europe (Stockholm) | eu-north-1 | fms.eu-north-1.amazonaws.com | HTTPS | ipv4 |
| Europe (Zurich) | eu-central-2 | fms.eu-central-2.amazonaws.com | HTTPS | ipv4 |
| Israel (Tel Aviv) | il-central-1 | fms.il-central-1.amazonaws.com | HTTPS | ipv4 |
| Mexico (Central) | mx-central-1 | fms.mx-central-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | fms.me-south-1.amazonaws.com | HTTPS | ipv4 |
| Middle East (Bahrain) | me-south-1 | fms-fips.me-south-1.amazonaws.com | HTTPS | fips |
| Middle East (UAE) | me-central-1 | fms.me-central-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | fms.sa-east-1.amazonaws.com | HTTPS | ipv4 |
| South America (São Paulo) | sa-east-1 | fms-fips.sa-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-East) | us-gov-east-1 | fms.us-gov-east-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-East) | us-gov-east-1 | fms-fips.us-gov-east-1.amazonaws.com | HTTPS | fips |
| AWS GovCloud (US-West) | us-gov-west-1 | fms.us-gov-west-1.amazonaws.com | HTTPS | ipv4 |
| AWS GovCloud (US-West) | us-gov-west-1 | fms-fips.us-gov-west-1.amazonaws.com | HTTPS | fips |

#### Quotas (28)

| Name | Default | Adjustable | Description |
|---|---|---|---|
| AWS WAF Classic rule groups per AWS WAF Classic policy | Each supported Region: 2 | No | The maximum number of AWS WAF Classic rule groups that you can use in a Firewall Manager AWS WAF Classic policy. |
| Accounts per Firewall Manager admin | Each supported Region: 10,000 | Yes | The maximum number of accounts that you can be managed by Firewall Manager under a single FMS admin. |
| Admins per organization in Firewall Manager | Each supported Region: 10 | No | The maximum number of admin accounts that you can onboard under a single organization in Firewall Manager |
| Amazon VPC instances in scope of a common security group policy | Each supported Region: 100 | Yes | The maximum number of Amazon VPC instances that you can have in scope per Firewall Manager common security group policy per account. This number represents the combined count of VPCs that you own and VPCs that are shared with you. |
| Applications per application list | Each supported Region: 50 | Yes | The maximum number of applications that you can define in an application list. |
| Audit security groups per security group content audit policy | Each supported Region: 1 | Yes | The maximum number of audit security groups that you can use in a Firewall Manager content audit security group policy. |
| Custom managed application lists for rules that allow all traffic | Each supported Region: 1 | Yes | The maximum number of managed application lists for rules that allow all traffic in a Firewall Manager content audit security group policy. |
| Custom managed application lists in any content audit security group policy setting | Each supported Region: 1 | Yes | The maximum number of custom managed application lists that you can use in any setting in a Firewall Manager content audit security group policy. |
| Custom managed application lists per account | Each supported Region: 10 | Yes | The maximum number of custom managed application lists that you can define for an account. |
| Custom managed protocol lists in any content audit security group policy setting | Each supported Region: 1 | Yes | The maximum number of custom managed protocol lists that you can use in any setting in a Firewall Manager content audit security group policy. |
| Custom managed protocol lists per account | Each supported Region: 10 | Yes | The maximum number of custom managed protocol lists that you can define for an account. |
| Explicitly included or excluded accounts per policy per Region | Each supported Region: 200 | Yes | The maximum number of accounts per Region that you can explicitly include in scope or explicitly exclude from scope for a Firewall Manager policy. |
| Firewall Manager policies per organization per Region | Each supported Region: 50 | Yes | The maximum number of Firewall Manager policies for any pair of Region and organization in AWS Organizations. |
| IPV4 CIDRs for a Network Firewall policy | Each supported Region: 50 | Yes | The maximum number of IPV4 CIDR ranges that you can provide in a single Firewall Manager Network Firewall policy, for use in firewall endpoint management. |
| Inbound/outbound rules per network ACL policy | Each supported Region: 5 | Yes | The maximum number of inbound/outbound rules that you can use in a Firewall Manager Network ACL policy. |
| Organizational units in scope per policy per Region | Each supported Region: 20 | Yes | The maximum number of organizational units that can be in scope of a Firewall Manager policy for any Region. |
| Partner rule groups per AWS WAF policy | Each supported Region: 1 | Yes | The maximum number of partner rule groups that can be applied to a single policy, limited by Web Application Firewall WebACL limits. |
| Primary security groups per common security group policy | Each supported Region: 3 | Yes | The maximum number of primary security groups that you can use in a Firewall Manager common security group policy. |
| Protocols per protocol list | Each supported Region: 5 | Yes | The maximum number of protocols that you can define in a protocol list. |
| Resource sets per Firewall Manager admin account | Each supported Region: 20 | Yes | The maximum number of resource sets that you can create under a single Firewall Manager admin account. |
| Resources per resource set | Each supported Region: 100 | Yes | The maximum number of resources that a single resource set can contain. |
| Route 53 Resolver DNS Firewall rule groups per DNS Firewall policy | Each supported Region: 2 | Yes | The maximum number of Route 53 Resolver DNS Firewall rule groups that you can use in a Firewall Manager DNS Firewall policy. |
| Rule groups per AWS WAF policy | Each supported Region: 50 | Yes | The maximum number of rule groups that you can use in a Firewall Manager AWS WAF policy. |
| Stateful rule group capacity per Network Firewall policy | Each supported Region: 30,000 | Yes | The maximum number of rules that can be included in a stateful rule group within a Firewall Manager Network Firewall policy. |
| Stateful rule groups per Network Firewall policy | Each supported Region: 20 | No | The maximum number of stateful rule groups that you can use in a Firewall Manager Network Firewall policy. |
| Stateless rule group capacity per Network Firewall policy | Each supported Region: 30,000 | No | The maximum number of rules that can be included in a stateless rule group within a Firewall Manager Network Firewall policy. |
| Stateless rule groups per Network Firewall policy | Each supported Region: 20 | No | The maximum number of stateless rule groups that you can use in a Firewall Manager Network Firewall policy. |
| Tags to include or exclude resources per policy | Each supported Region: 8 | Yes | The maximum number of tags that you can use to include or exclude resources for a Firewall Manager policy. |
