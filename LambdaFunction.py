import json
import boto3
import os
import traceback

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Table name
TABLE_NAME = "LogAnalysis"

table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        print("Full Event Received:")
        print(json.dumps(event))

        if "Records" not in event:
            print("No Records key in event.")
            return {"status": "no records"}

        for record in event["Records"]:
            if "s3" not in record:
                print("Record does not contain S3 data.")
                continue

            bucket_name = record["s3"]["bucket"]["name"]
            object_key = record["s3"]["object"]["key"]

            print(f"Processing file: {object_key} from bucket: {bucket_name}")

            response = table.put_item(
                Item={
                    "logId": object_key,
                    "bucket": bucket_name,
                    "status": "processed"
                }
            )

            print("DynamoDB PutItem Response:")
            print(response)

        return {"status": "success"}

    except Exception as e:
        print("ERROR OCCURRED:")
        print(str(e))
        print(traceback.format_exc())
        raise e
