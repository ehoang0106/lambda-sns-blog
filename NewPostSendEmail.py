import json
import boto3
import os

sns_client = boto3.client('sns')

MESSAGE_TEMPLATE = "Hi there!\nA new blog post is published. Check it out on my blog!"
BLOG_URL = "\n<URL Blog URL>"
SUBJECT = 'New blog post just released!'

def lambda_handler(event, context):
    sns_topic_arn = os.getenv('SNS_TOPIC_ARN')
    if not sns_topic_arn:
        raise ValueError("SNS_TOPIC_ARN environment variable is not set")

    message = f"{MESSAGE_TEMPLATE}{BLOG_URL}"

    response = sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=message,
        Subject=SUBJECT
    )

    return {
        'body': json.dumps('Notification has been sent')
    }
