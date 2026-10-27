# Run `qwen2.5-7b__v2__t0__parts__holdout__val2`

Generated from the JSONL run file by `src/extract/report_md.py`; do not edit.

- Model: `qwen2.5:7b`
- Prompt version: `v2` (file sha `a3adf0379524`)
- Schema sha: `d4010de95c65`; validation version `2`
- Sampling: `t0` (temperature 0.0, top_p None)
- In parts: the endpoints part and the quotas part of each chapter in one call each, merged by code (step 13)
- Documents: 10

## Summary

| # | Document | Group | Status | Calls | Latency, s | In tokens | Out tokens | Quota table | Endpoints | Quotas |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [079-aws-iot-device-defender.pdf](#079-aws-iot-device-defenderpdf) | edge | failed | 2 | 561.3 | 6,942 | 21,299 | — | — | — |
| 2 | [059-aws-clean-rooms.pdf](#059-aws-clean-roomspdf) | edge | failed | 3 | 436.7 | 20,809 | 15,677 | — | — | — |
| 3 | [016-amazon-comprehend.pdf](#016-amazon-comprehendpdf) | edge | failed | 4 | 406.8 | 24,169 | 14,923 | — | — | — |
| 4 | [069-aws-elemental-mediaconvert.pdf](#069-aws-elemental-mediaconvertpdf) | edge | ok | 2 | 165.4 | 6,991 | 6,604 | standard | 26 | 72 |
| 5 | [027-amazon-eventbridge-scheduler.pdf](#027-amazon-eventbridge-schedulerpdf) | medium | ok | 2 | 148.5 | 5,250 | 6,330 | standard | 88 | 14 |
| 6 | [068-aws-elastic-beanstalk.pdf](#068-aws-elastic-beanstalkpdf) | medium | ok | 2 | 127.6 | 5,716 | 5,248 | standard | 76 | 3 |
| 7 | [051-amazon-timestream.pdf](#051-amazon-timestreampdf) | medium | failed | 3 | 426.6 | 16,142 | 16,445 | — | — | — |
| 8 | [028-amazon-fsx.pdf](#028-amazon-fsxpdf) | medium | failed | 3 | 184.6 | 10,091 | 7,674 | — | — | — |
| 9 | [073-aws-firewall-manager.pdf](#073-aws-firewall-managerpdf) | medium | failed | 3 | 226.7 | 10,418 | 9,463 | — | — | — |
| 10 | [046-amazon-simple-email-service.pdf](#046-amazon-simple-email-servicepdf) | medium | failed | 3 | 239.1 | 18,026 | 8,982 | — | — | — |

## Documents

### 079-aws-iot-device-defender.pdf

- Status: **failed**, 2 call(s), 561.3 s, in 6,942 / out 21,299 tokens
- Part `endpoints` (390 words): **ok**, 1 call(s), 65.4 s, in 2,085 / out 2,867 tokens, 58 rows
- Part `quotas` (2,005 words): **failed**, 1 call(s), 495.9 s, in 4,857 / out 18,432 tokens, —

#### Error

```text
[quotas]
- the answer was cut off at the max_tokens limit
- (document): Invalid JSON: EOF while parsing a value at line 1906 column 0
--- no repair call
```

### 059-aws-clean-rooms.pdf

- Status: **failed**, 3 call(s), 436.7 s, in 20,809 / out 15,677 tokens
- Part `endpoints` (240 words): **ok**, 1 call(s), 31.5 s, in 1,448 / out 1,420 tokens, 28 rows
- Part `quotas` (2,503 words): **failed**, 2 call(s), 405.2 s, in 19,361 / out 14,257 tokens, —

#### Error

```text
[quotas]
- quotas.76.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationAnalysisTemplate requests'
- quotas.77.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationChangeRequest requests'
- quotas.78.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationConfiguredAudienceModelAssociation requests'
- quotas.79.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationIdNamespaceAssociation requests'
- quotas.80.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationPrivacyBudgetTemplate requests'
- quotas.81.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationPrivacyBudget requests'
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
--- after repair:
- quotas.76.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationAnalysisTemplate requests'
- quotas.77.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationChangeRequest requests'
- quotas.78.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationConfiguredAudienceModelAssociation requests'
- quotas.79.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationIdNamespaceAssociation requests'
- quotas.80.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationPrivacyBudgetTemplate requests'
- quotas.81.name: not printed in a Standard Quota Table of the chapter: 'Rate of ListCollaborationPrivacyBudget requests'
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

- Status: **failed**, 4 call(s), 406.8 s, in 24,169 / out 14,923 tokens
- Part `endpoints` (280 words): **repaired**, 2 call(s), 87.7 s, in 5,153 / out 3,724 tokens, 36 rows
- Part `quotas` (2,459 words): **failed**, 2 call(s), 319.2 s, in 19,016 / out 11,199 tokens, —

#### Error

```text
[endpoints]
- endpoints.34.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'comprehend-fips.us-gov-west-1.amazon'
[quotas]
- quotas.0.name: not printed in a Standard Quota Table of the chapter: 'BatchDetectDominantLanguage'
- quotas.1.name: not printed in a Standard Quota Table of the chapter: 'BatchDetectEntities'
- quotas.2.name: not printed in a Standard Quota Table of the chapter: 'BatchDetectKeyPhrases'
- quotas.3.name: not printed in a Standard Quota Table of the chapter: 'BatchDetectSentiment'
- quotas.4.name: not printed in a Standard Quota Table of the chapter: 'BatchDetectSyntax'
- quotas.5.name: not printed in a Standard Quota Table of the chapter: 'BatchDetectTargetedSentiment'
- quotas.6.name: not printed in a Standard Quota Table of the chapter: 'ContainsPiiEntities'
- quotas.7.name: not printed in a Standard Quota Table of the chapter: 'CreateDocumentClassifier'
- quotas.8.name: not printed in a Standard Quota Table of the chapter: 'CreateEntityRecognizer'
- quotas.9.name: not printed in a Standard Quota Table of the chapter: 'CreateEntityRecognizer'
- quotas.10.name: not printed in a Standard Quota Table of the chapter: 'CreateFlywheel'
- quotas.11.name: not printed in a Standard Quota Table of the chapter: 'CreateFlywheel'
- quotas.12.name: not printed in a Standard Quota Table of the chapter: 'Datasets'
- quotas.13.name: not printed in a Standard Quota Table of the chapter: 'DeleteDocumentClassifier'
- quotas.14.name: not printed in a Standard Quota Table of the chapter: 'DeleteEntityRecognizer'
- quotas.15.name: not printed in a Standard Quota Table of the chapter: 'DescribeDocumentClassificationJob'
- quotas.16.name: not printed in a Standard Quota Table of the chapter: 'DescribeDocumentClassifier'
- quotas.17.name: not printed in a Standard Quota Table of the chapter: 'DescribeDominantLanguageDetectionJob'
- quotas.18.name: not printed in a Standard Quota Table of the chapter: 'DescribeEntitiesDetectionJob'
- quotas.19.name: not printed in a Standard Quota Table of the chapter: 'DescribeEntityRecognizer'
- quotas.20.name: not printed in a Standard Quota Table of the chapter: 'DescribeEventsDetectionJob'
- quotas.21.name: not printed in a Standard Quota Table of the chapter: 'DescribeKeyPhrasesDetectionJob'
- quotas.22.name: not printed in a Standard Quota Table of the chapter: 'DescribePiiEntitiesDetectionJob'
- quotas.23.name: not printed in a Standard Quota Table of the chapter: 'DescribeSentimentDetectionJob'
- quotas.24.name: not printed in a Standard Quota Table of the chapter: 'DescribeTargetedSentimentDetectionJob'
- quotas.25.name: not printed in a Standard Quota Table of the chapter: 'DescribeTopicsDetectionJob'
- quotas.26.name: not printed in a Standard Quota Table of the chapter: 'DetectDominantLanguage'
- quotas.27.name: not printed in a Standard Quota Table of the chapter: 'DetectEntities'
- quotas.28.name: not printed in a Standard Quota Table of the chapter: 'DetectKeyPhrases'
- quotas.29.name: not printed in a Standard Quota Table of the chapter: 'DetectPiiEntities'
- quotas.30.name: not printed in a Standard Quota Table of the chapter: 'DetectSentiment'
- quotas.31.name: not printed in a Standard Quota Table of the chapter: 'DetectSyntax'
- quotas.32.name: not printed in a Standard Quota Table of the chapter: 'DetectTargetedSentiment'
- quotas.33.name: not printed in a Standard Quota Table of the chapter: 'DetectToxicContent'
- quotas.34.name: not printed in a Standard Quota Table of the chapter: 'Endpoints'
- quotas.35.name: not printed in a Standard Quota Table of the chapter: 'Endpoints'
- quotas.36.name: not printed in a Standard Quota Table of the chapter: 'Endpoints'
- quotas.37.name: not printed in a Standard Quota Table of the chapter: 'ListDocumentClassificationJobs'
- quotas.38.name: not printed in a Standard Quota Table of the chapter: 'ListDocumentClassifiers'
- quotas.39.name: not printed in a Standard Quota Table of the chapter: 'ListDominantLanguageDetectionJobs'
- quotas.40.name: not printed in a Standard Quota Table of the chapter: 'ListEntitiesDetectionJobs'
- quotas.41.name: not printed in a Standard Quota Table of the chapter: 'ListEntityRecognizers'
- quotas.42.name: not printed in a Standard Quota Table of the chapter: 'ListEventsDetectionJobs'
- quotas.43.name: not printed in a Standard Quota Table of the chapter: 'ListKeyPhrasesDetectionJobs'
- quotas.44.name: not printed in a Standard Quota Table of the chapter: 'ListPiiEntitiesDetectionJobs'
- quotas.45.name: not printed in a Standard Quota Table of the chapter: 'ListSentimentDetectionJobs'
- quotas.46.name: not printed in a Standard Quota Table of the chapter: 'ListTagsForResource'
- quotas.47.name: not printed in a Standard Quota Table of the chapter: 'ListTargetedSentimentDetectionJobs'
- quotas.48.name: not printed in a Standard Quota Table of the chapter: 'ListTopicsDetectionJobs'
- quotas.51.name: not printed in a Standard Quota Table of the chapter: 'StartDocumentClassificationJob'
- quotas.52.name: not printed in a Standard Quota Table of the chapter: 'StartDocumentClassificationJob'
- quotas.53.name: not printed in a Standard Quota Table of the chapter: 'StartDominantLanguageDetectionJob'
- quotas.54.name: not printed in a Standard Quota Table of the chapter: 'StartDominantLanguageDetectionJob'
- quotas.55.name: not printed in a Standard Quota Table of the chapter: 'StartEntitiesDetectionJob'
- quotas.56.name: not printed in a Standard Quota Table of the chapter: 'StartEntitiesDetectionJob'
- quotas.57.name: not printed in a Standard Quota Table of the chapter: 'StartEventsDetectionJob'
- quotas.58.name: not printed in a Standard Quota Table of the chapter: 'StartEventsDetectionJob'
- quotas.59.name: not printed in a Standard Quota Table of the chapter: 'StartFlywheelIteration'
- quotas.60.name: not printed in a Standard Quota Table of the chapter: 'StartKeyPhrasesDetectionJob'
- quotas.61.name: not printed in a Standard Quota Table of the chapter: 'StartKeyPhrasesDetectionJob'
- quotas.62.name: not printed in a Standard Quota Table of the chapter: 'StartPiiEntitiesDetectionJob'
- quotas.63.name: not printed in a Standard Quota Table of the chapter: 'StartPiiEntitiesDetectionJob'
- quotas.64.name: not printed in a Standard Quota Table of the chapter: 'StartSentimentDetectionJob'
- quotas.65.name: not printed in a Standard Quota Table of the chapter: 'StartSentimentDetectionJob'
- quotas.66.name: not printed in a Standard Quota Table of the chapter: 'StartTargetedSentimentDetectionJob'
- quotas.67.name: not printed in a Standard Quota Table of the chapter: 'StartTargetedSentimentDetectionJob'
- quotas.68.name: not printed in a Standard Quota Table of the chapter: 'StartTopicsDetectionJob'
- quotas.69.name: not printed in a Standard Quota Table of the chapter: 'StartTopicsDetectionJob'
- quotas.70.name: not printed in a Standard Quota Table of the chapter: 'StopDominantLanguageDetectionJob'
- quotas.71.name: not printed in a Standard Quota Table of the chapter: 'StopEntitiesDetectionJob'
- quotas.72.name: not printed in a Standard Quota Table of the chapter: 'StopEventsDetectionJob'
- quotas.73.name: not printed in a Standard Quota Table of the chapter: 'StopKeyPhrasesDetectionJob'
- quotas.74.name: not printed in a Standard Quota Table of the chapter: 'StopPiiEntitiesDetectionJob'
- quotas.75.name: not printed in a Standard Quota Table of the chapter: 'StopSentimentDetectionJob'
- quotas.76.name: not printed in a Standard Quota Table of the chapter: 'StopTrainingDocumentClassifier'
- quotas.77.name: not printed in a Standard Quota Table of the chapter: 'StopTrainingEntityRecognizer'
- quotas.78.name: not printed in a Standard Quota Table of the chapter: 'TagResource'
--- after repair:
- quotas.0.name: not printed in a Standard Quota Table of the chapter: 'BatchDetectDominantLanguage'
- quotas.1.name: not printed in a Standard Quota Table of the chapter: 'BatchDetectEntities'
- quotas.2.name: not printed in a Standard Quota Table of the chapter: 'BatchDetectKeyPhrases'
- quotas.3.name: not printed in a Standard Quota Table of the chapter: 'BatchDetectSentiment'
- quotas.4.name: not printed in a Standard Quota Table of the chapter: 'BatchDetectSyntax'
- quotas.5.name: not printed in a Standard Quota Table of the chapter: 'BatchDetectTargetedSentiment'
- quotas.6.name: not printed in a Standard Quota Table of the chapter: 'ContainsPiiEntities'
- quotas.7.name: not printed in a Standard Quota Table of the chapter: 'CreateDocumentClassifier'
- quotas.8.name: not printed in a Standard Quota Table of the chapter: 'CreateEntityRecognizer'
- quotas.9.name: not printed in a Standard Quota Table of the chapter: 'CreateEntityRecognizer'
- quotas.10.name: not printed in a Standard Quota Table of the chapter: 'CreateFlywheel'
- quotas.11.name: not printed in a Standard Quota Table of the chapter: 'CreateFlywheel'
- quotas.12.name: not printed in a Standard Quota Table of the chapter: 'Datasets'
- quotas.13.name: not printed in a Standard Quota Table of the chapter: 'DeleteDocumentClassifier'
- quotas.14.name: not printed in a Standard Quota Table of the chapter: 'DeleteEntityRecognizer'
- quotas.15.name: not printed in a Standard Quota Table of the chapter: 'DescribeDocumentClassificationJob'
- quotas.16.name: not printed in a Standard Quota Table of the chapter: 'DescribeDocumentClassifier'
- quotas.17.name: not printed in a Standard Quota Table of the chapter: 'DescribeDominantLanguageDetectionJob'
- quotas.18.name: not printed in a Standard Quota Table of the chapter: 'DescribeEntitiesDetectionJob'
- quotas.19.name: not printed in a Standard Quota Table of the chapter: 'DescribeEntityRecognizer'
- quotas.20.name: not printed in a Standard Quota Table of the chapter: 'DescribeEventsDetectionJob'
- quotas.21.name: not printed in a Standard Quota Table of the chapter: 'DescribeKeyPhrasesDetectionJob'
- quotas.22.name: not printed in a Standard Quota Table of the chapter: 'DescribePiiEntitiesDetectionJob'
- quotas.23.name: not printed in a Standard Quota Table of the chapter: 'DescribeSentimentDetectionJob'
- quotas.24.name: not printed in a Standard Quota Table of the chapter: 'DescribeTargetedSentimentDetectionJob'
- quotas.25.name: not printed in a Standard Quota Table of the chapter: 'DescribeTopicsDetectionJob'
- quotas.26.name: not printed in a Standard Quota Table of the chapter: 'DetectDominantLanguage'
- quotas.27.name: not printed in a Standard Quota Table of the chapter: 'DetectEntities'
- quotas.28.name: not printed in a Standard Quota Table of the chapter: 'DetectKeyPhrases'
- quotas.29.name: not printed in a Standard Quota Table of the chapter: 'DetectPiiEntities'
- quotas.30.name: not printed in a Standard Quota Table of the chapter: 'DetectSentiment'
- quotas.31.name: not printed in a Standard Quota Table of the chapter: 'DetectSyntax'
- quotas.32.name: not printed in a Standard Quota Table of the chapter: 'DetectTargetedSentiment'
- quotas.33.name: not printed in a Standard Quota Table of the chapter: 'DetectToxicContent'
- quotas.34.name: not printed in a Standard Quota Table of the chapter: 'Endpoints'
- quotas.35.name: not printed in a Standard Quota Table of the chapter: 'Endpoints'
- quotas.36.name: not printed in a Standard Quota Table of the chapter: 'Endpoints'
- quotas.37.name: not printed in a Standard Quota Table of the chapter: 'ListDocumentClassificationJobs'
- quotas.38.name: not printed in a Standard Quota Table of the chapter: 'ListDocumentClassifiers'
- quotas.39.name: not printed in a Standard Quota Table of the chapter: 'ListDominantLanguageDetectionJobs'
- quotas.40.name: not printed in a Standard Quota Table of the chapter: 'ListEntitiesDetectionJobs'
- quotas.41.name: not printed in a Standard Quota Table of the chapter: 'ListEntityRecognizers'
- quotas.42.name: not printed in a Standard Quota Table of the chapter: 'ListEventsDetectionJobs'
- quotas.43.name: not printed in a Standard Quota Table of the chapter: 'ListKeyPhrasesDetectionJobs'
- quotas.44.name: not printed in a Standard Quota Table of the chapter: 'ListPiiEntitiesDetectionJobs'
- quotas.45.name: not printed in a Standard Quota Table of the chapter: 'ListSentimentDetectionJobs'
- quotas.46.name: not printed in a Standard Quota Table of the chapter: 'ListTagsForResource'
- quotas.47.name: not printed in a Standard Quota Table of the chapter: 'ListTargetedSentimentDetectionJobs'
- quotas.48.name: not printed in a Standard Quota Table of the chapter: 'ListTopicsDetectionJobs'
- quotas.51.name: not printed in a Standard Quota Table of the chapter: 'StartDocumentClassificationJob'
- quotas.52.name: not printed in a Standard Quota Table of the chapter: 'StartDocumentClassificationJob'
- quotas.53.name: not printed in a Standard Quota Table of the chapter: 'StartDominantLanguageDetectionJob'
- quotas.54.name: not printed in a Standard Quota Table of the chapter: 'StartDominantLanguageDetectionJob'
- quotas.55.name: not printed in a Standard Quota Table of the chapter: 'StartEntitiesDetectionJob'
- quotas.56.name: not printed in a Standard Quota Table of the chapter: 'StartEntitiesDetectionJob'
- quotas.57.name: not printed in a Standard Quota Table of the chapter: 'StartEventsDetectionJob'
- quotas.58.name: not printed in a Standard Quota Table of the chapter: 'StartEventsDetectionJob'
- quotas.59.name: not printed in a Standard Quota Table of the chapter: 'StartFlywheelIteration'
- quotas.60.name: not printed in a Standard Quota Table of the chapter: 'StartKeyPhrasesDetectionJob'
- quotas.61.name: not printed in a Standard Quota Table of the chapter: 'StartKeyPhrasesDetectionJob'
- quotas.62.name: not printed in a Standard Quota Table of the chapter: 'StartPiiEntitiesDetectionJob'
- quotas.63.name: not printed in a Standard Quota Table of the chapter: 'StartPiiEntitiesDetectionJob'
- quotas.64.name: not printed in a Standard Quota Table of the chapter: 'StartSentimentDetectionJob'
- quotas.65.name: not printed in a Standard Quota Table of the chapter: 'StartSentimentDetectionJob'
- quotas.66.name: not printed in a Standard Quota Table of the chapter: 'StartTargetedSentimentDetectionJob'
- quotas.67.name: not printed in a Standard Quota Table of the chapter: 'StartTargetedSentimentDetectionJob'
- quotas.68.name: not printed in a Standard Quota Table of the chapter: 'StartTopicsDetectionJob'
- quotas.69.name: not printed in a Standard Quota Table of the chapter: 'StartTopicsDetectionJob'
- quotas.70.name: not printed in a Standard Quota Table of the chapter: 'StopDominantLanguageDetectionJob'
- quotas.71.name: not printed in a Standard Quota Table of the chapter: 'StopEntitiesDetectionJob'
- quotas.72.name: not printed in a Standard Quota Table of the chapter: 'StopEventsDetectionJob'
- quotas.73.name: not printed in a Standard Quota Table of the chapter: 'StopKeyPhrasesDetectionJob'
- quotas.74.name: not printed in a Standard Quota Table of the chapter: 'StopPiiEntitiesDetectionJob'
- quotas.75.name: not printed in a Standard Quota Table of the chapter: 'StopSentimentDetectionJob'
- quotas.76.name: not printed in a Standard Quota Table of the chapter: 'StopTrainingDocumentClassifier'
- quotas.77.name: not printed in a Standard Quota Table of the chapter: 'StopTrainingEntityRecognizer'
- quotas.78.name: not printed in a Standard Quota Table of the chapter: 'TagResource'
```

### 069-aws-elemental-mediaconvert.pdf

- Status: **ok**, 2 call(s), 165.4 s, in 6,991 / out 6,604 tokens
- Part `endpoints` (307 words): **ok**, 1 call(s), 30.3 s, in 1,589 / out 1,336 tokens, 26 rows
- Part `quotas` (2,584 words): **ok**, 1 call(s), 135.1 s, in 5,402 / out 5,268 tokens, 72 rows, 5 ignored of the other kind
- Service: AWS Elemental MediaConvert; quota table format: `standard`

#### Endpoints (26)

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
| Asia Pacific (Mumbai) | ap-south-1 | mediaconvert.ap-south-1.amazonaws.com | HTTPS | ipv4 |
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
| Concurrent jobs per on-demand queue | us-east-1: 500; us-east-2: 250; us-west-2: 500; ap-northeast-1: 250; ap-south-1: 250 | Yes | The maximum number of concurrent jobs that are available when you configure an on-demand queue in the current AWS Region. For more information about configuring on-demand queues, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-on-demand-queues.html |
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

- Status: **ok**, 2 call(s), 148.5 s, in 5,250 / out 6,330 tokens
- Part `endpoints` (543 words): **ok**, 1 call(s), 100.8 s, in 2,639 / out 4,323 tokens, 88 rows
- Part `quotas` (706 words): **ok**, 1 call(s), 47.7 s, in 2,611 / out 2,007 tokens, 14 rows, 11 ignored of the other kind
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
| CreateSchedule request rate | us-east-1: 5,000; us-east-2: 5,000; us-west-2: 5,000 | Yes | Maximum CreateSchedule requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. This is adjustable to tens of thousands of requests per second. |
| CreateScheduleGroup request rate | Each supported Region: 10 | Yes | Maximum CreateScheduleGroup requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. |
| DeleteSchedule request rate | us-east-1: 1,000; us-east-2: 1,000; us-west-2: 1,000; ap-northeast-1: 1,000; ap-south-1: 1,000; ap-southeast-1: 1,000; ap-southeast-2: 1,000; eu-central-1: 1,000; eu-west-1: 1,000; eu-west-2: 1,000; sa-east-1: 1,000; Each of the other supported Regions: 250 | Yes | Maximum DeleteSchedule requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. This is adjustable to tens of thousands of requests per second. |
| DeleteScheduleGroup request rate | Each supported Region: 10 | Yes | Maximum DeleteScheduleGroup requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. |
| GetSchedule request rate | us-east-1: 1,000; us-east-2: 1,000; us-west-2: 1,000; ap-northeast-1: 1,000; ap-south-1: 1,000; ap-southeast-1: 1,000; ap-southeast-2: 1,000; eu-central-1: 1,000; eu-west-1: 1,000; eu-west-2: 1,000; sa-east-1: 1,000; Each of the other supported Regions: 250 | Yes | Maximum GetSchedule requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. This is adjustable to tens of thousands of requests per second. |
| GetScheduleGroup request rate | Each supported Region: 10 | Yes | Maximum GetScheduleGroup requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. |
| Invocations throttle limit in transactions per second | us-east-1: 1,000; us-east-2: 1,000; us-west-2: 1,000; ap-northeast-1: 1,000; ap-south-1: 1,000; ap-southeast-1: 1,000; ap-southeast-2: 1,000; eu-central-1: 1,000; eu-west-1: 1,000; eu-west-2: 1,000; sa-east-1: 1,000; Each of the other supported Regions: 500 | Yes | An invocation is a schedule payload being delivered to the defined target. After the limit is reached, the invocations are throttled; that is, they still happen but they are delayed. This is adjustable to tens of thousands of transactions per second. |
| ListScheduleGroups request rate | Each supported Region: 10 | Yes | Maximum ListScheduleGroups requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. |
| ListSchedules request rate | Each supported Region: 50 | Yes | Maximum ListSchedules requests per second. When you reach this quota, EventBridge Scheduler rejects requests for this operation for the remainder of the interval. |
| ListTagsForResource request rate | Each supported Region: 10 | Yes | Assigns one or more tags (key-value pairs) to the specified Scheduler resource. |
| Number of schedule groups | Each supported Region: 500 | Yes | The maximum number of schedule groups per region. |
| Number of schedules | Each supported Region: 10,000,000 | Yes | The maximum number of schedules per region. This quota includes one-time schedules that have completed running. We recommend configuring your schedules to automatically delete after completion using the ActionAfterCompletion feature. This is adjustable to billions of schedules. |
| TagResource request rate | Each supported Region: 1 | Yes | Assigns one or more tags (key-value pairs) to the specified Scheduler resource. |
| UntagResource request rate | Each supported Region: 1 | Yes | Removes one or more tags from the specified Scheduler resource. |

### 068-aws-elastic-beanstalk.pdf

- Status: **ok**, 2 call(s), 127.6 s, in 5,716 / out 5,248 tokens
- Part `endpoints` (1,095 words): **ok**, 1 call(s), 98.9 s, in 4,793 / out 3,885 tokens, 76 rows
- Part `quotas` (96 words): **ok**, 1 call(s), 28.8 s, in 923 / out 1,363 tokens, 3 rows, 22 ignored of the other kind
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

- Status: **failed**, 3 call(s), 426.6 s, in 16,142 / out 16,445 tokens
- Part `endpoints` (719 words): **failed**, 2 call(s), 351.0 s, in 14,040 / out 13,175 tokens, —
- Part `quotas` (689 words): **ok**, 1 call(s), 75.6 s, in 2,102 / out 3,270 tokens, 32 rows, 30 ignored of the other kind

#### Error

```text
[endpoints]
- endpoints.3.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.8.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.13.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.17.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'ingest.timestream.ap-southeast-2.ama'
- endpoints.18.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.20.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'ingest.timestream.ap-northeast-1.ama'
- endpoints.21.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.25.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'ingest.timestream.us-gov-west-1.amazonsaws.com'
- endpoints.30.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.35.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.40.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
--- after repair:
- endpoints.14.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'ingest.timestream.ap-southeast-2.ama'
- endpoints.15.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.17.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'ingest.timestream.ap-northeast-1.ama'
- endpoints.18.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.22.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'ingest.timestream.us-gov-west-1.amazonsaws.com'
- endpoints.27.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.32.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
- endpoints.37.endpoint: Value error, not a hostname on an AWS domain ('amazonaws.com', 'amazonaws.com.cn', 'api.aws', 'on.aws'): 'zonaws.com'
```

### 028-amazon-fsx.pdf

- Status: **failed**, 3 call(s), 184.6 s, in 10,091 / out 7,674 tokens
- Part `endpoints` (465 words): **failed**, 2 call(s), 125.8 s, in 7,247 / out 5,211 tokens, —
- Part `quotas` (991 words): **ok**, 1 call(s), 58.8 s, in 2,844 / out 2,463 tokens, 28 rows, 6 ignored of the other kind

#### Error

```text
[endpoints]
- endpoints.31.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-ca-west-1.amazonaws.com'
- endpoints.32.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-ca-west-1.api.aws'
--- after repair:
- endpoints.31.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-ca-west-1.amazonaws.com'
- endpoints.32.endpoint: not printed in an endpoints table of the 'Amazon FSx' chapter: 'fsx-ca-west-1.api.aws'
```

### 073-aws-firewall-manager.pdf

- Status: **failed**, 3 call(s), 226.7 s, in 10,418 / out 9,463 tokens
- Part `endpoints` (478 words): **failed**, 2 call(s), 149.4 s, in 7,982 / out 6,117 tokens, —
- Part `quotas` (997 words): **ok**, 1 call(s), 77.3 s, in 2,436 / out 3,346 tokens, 28 rows, 30 ignored of the other kind

#### Error

```text
[endpoints]
- endpoints.11.endpoint: not printed in an endpoints table of the 'AWS Firewall Manager' chapter: 'fms-fips.ap-southeast-3.amazonaws.com'
- endpoints.13.endpoint: not printed in an endpoints table of the 'AWS Firewall Manager' chapter: 'fms-fips.ap-southeast-5.amazonaws.com'
- endpoints.15.endpoint: not printed in an endpoints table of the 'AWS Firewall Manager' chapter: 'fms-fips.ap-southeast-4.amazonaws.com'
- endpoints.20.endpoint: not printed in an endpoints table of the 'AWS Firewall Manager' chapter: 'fms-fips.ap-northeast-3.amazonaws.com'
- endpoints.49.endpoint: not printed in an endpoints table of the 'AWS Firewall Manager' chapter: 'fms-fips.il-central-1.amazonaws.com'
--- after repair:
- endpoints.11.endpoint: not printed in an endpoints table of the 'AWS Firewall Manager' chapter: 'fms-fips.ap-southeast-3.amazonaws.com'
- endpoints.13.endpoint: not printed in an endpoints table of the 'AWS Firewall Manager' chapter: 'fms-fips.ap-southeast-5.amazonaws.com'
- endpoints.15.endpoint: not printed in an endpoints table of the 'AWS Firewall Manager' chapter: 'fms-fips.ap-southeast-4.amazonaws.com'
- endpoints.20.endpoint: not printed in an endpoints table of the 'AWS Firewall Manager' chapter: 'fms-fips.ap-northeast-3.amazonaws.com'
- endpoints.49.endpoint: not printed in an endpoints table of the 'AWS Firewall Manager' chapter: 'fms-fips.il-central-1.amazonaws.com'
```

### 046-amazon-simple-email-service.pdf

- Status: **failed**, 3 call(s), 239.1 s, in 18,026 / out 8,982 tokens
- Part `endpoints` (1,472 words): **failed**, 2 call(s), 198.9 s, in 17,080 / out 7,089 tokens, —
- Part `quotas` (112 words): **ok**, 1 call(s), 40.2 s, in 946 / out 1,893 tokens, 4 rows, 33 ignored of the other kind

#### Error

```text
[endpoints]
- endpoints.37.endpoint: not printed in an endpoints table of the 'Amazon Simple Email Service' chapter: 'email-ca-central-1.api.aws'
- endpoints.41.endpoint: not printed in an endpoints table of the 'Amazon Simple Email Service' chapter: 'email-ca-west-1.api.aws'
--- after repair:
- endpoints.37.endpoint: not printed in an endpoints table of the 'Amazon Simple Email Service' chapter: 'email-ca-central-1.api.aws'
- endpoints.41.endpoint: not printed in an endpoints table of the 'Amazon Simple Email Service' chapter: 'email-ca-west-1.api.aws'
```
