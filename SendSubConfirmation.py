import json
import boto3
import os

def lambda_handler(event, context):
    # TODO implement
    sns = boto3.client('sns')
    email = event['queryStringParameters']['email']
    topic_arn = os.getenv('SNS_TOPIC_ARN')
    
    message = f"Thank you for the subscription. The confirmation has been sent to {email}. Please check your email"
    try:
        response = sns.subscribe(
            TopicArn=topic_arn,
            Protocol='email',
            Endpoint=email
            )
        return {
            'statusCode': 200,
            'body': json.dumps(message)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error occured. Please check your email address again!')
        }