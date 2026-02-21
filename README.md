# ServerlessLogAnalyzer
AWS project that stores logs in S3 Automatically processes the results in DynamoDB. Visualizes results in CloudWatch.

Project Overview---------------------------------
This project implements an event-driven serverless log processing pipeline using AWS services. When a file is uploaded to Amazon S3, an AWS Lambda function is automatically triggered to process the event and store metadata in DynamoDB.
The architecture eliminates server management and scales automatically based on demand.

Services used-------------------------------------
Amazon S3 – Stores uploaded log files
AWS Lambda – Processes S3 events
Amazon DynamoDB – Stores processed log metadata
Amazon CloudWatch – Logs and monitoring
AWS Identity and Access Management – Secure role-based access

How it works--------------------------------------
A log file is uploaded to an S3 bucket.
The S3 PUT event triggers a Lambda function.
Lambda extracts file metadata.
Metadata is written to a DynamoDB table.
Execution logs are recorded in CloudWatch.

Implementation------------------------------------
1. Created S3 Bucket
Configure event notifications for PUT events.

2. Create DynamoDB Table
Table name: LogAnalysis
Partition key: logId (String)

3. Create IAM Role
Attach permissions:
DynamoDB PutItem
S3 Read Access
CloudWatch Logs access

4. Deploy Lambda Function
Runtime: Python 3.14
Add S3 trigger
Deploy code

🧪 Testing
Upload a new file to S3
Verify Lambda execution in CloudWatch
Scan DynamoDB table to confirm item insertion

Lessons Learned-------------------------------------------------
Importance of IAM permissions in serverless architectures
Region alignment between AWS services
Debugging using CloudWatch logs
Understanding S3 event payload structure
