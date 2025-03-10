import json
import boto3
import os

def lambda_handler(event, context):

    sns_client = boto3.client('sns')
    email = event.get('queryStringParameters', {}).get('email')
    
    topic_arn = os.getenv('SNS_TOPIC_ARN')
    if not topic_arn:
        return {
            'statusCode': 500,
            'body': json.dumps('SNS topic ARN is not configured.')
        }
    confirmation_message = (
        f"Thank you for the subscription. The confirmation has been sent to {email}. "
        "Please check your email!"
    )
    
    try:
        sns_client.subscribe(
            TopicArn=topic_arn,
            Protocol='email',
            Endpoint=email
        )
        return {
            'statusCode': 200,
            'body': json.dumps(confirmation_message)
        }
    except Exception as e:
        error_message = f'Error occurred: {str(e)}. Please check your email address and try again!'
        return {
            'statusCode': 500,
            'body': json.dumps(error_message)
        }
