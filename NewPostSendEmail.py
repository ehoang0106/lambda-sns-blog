import json
import boto3
import os

sns_client = boto3.client('sns')

def lambda_handler(event, context):
    
    sns_topic_arn  = os.getenv('SNS_TOPIC_ARN')
    message = "Hi there!\nA new blog post is published. Check it out on my blog!"
    blog_url = "\nhttps://blog.khoahoang.dev/"
    
    response = sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=message+blog_url,
        Subject='New blog post just released!')
    
    return {
        'body': json.dumps('Noti has been sent')
    }
