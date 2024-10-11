
### 1. SNS

1. Create an SNS topic with the `email` protocol
2. Copy the ARN of the SNS topic for use later

### 2. Lambda

1. Create a Lambda function to trigger SNS topic
2. Use AWS SDK `boto3` to integrate python with AWS services
3. Use `os` library to get the `env` the ARN from SNS. Go to Lambda -> Configuration -> Environment variable -> set key and value
4. Create a role for Lambda with SNS permission -> Attach a role 

### 3. S3

1. Setup S3 Event but make sure the Lambda function is working
2. Create a Event Notification with the all object create events
3. Choose Destination is a Lambda function


To continue with my cloud journey, I created another project that allow people can subscribe to my blog by using their email. To archive this, I use AWS SNS, AWS Lambda, API Gateway, Route 53 and S3 Event.

There are two main jobs. First, I create a Lambda function that trigger the SNS when I publish a new post to my hosted static website on S3

A second Lambda function integration with API gateway to send the confirmation subscription to the SNS topic. I also create a custom domain by using API Gateway and Route 53 to create a record for my new domain.

