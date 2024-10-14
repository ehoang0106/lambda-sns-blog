
### 1. SNS

1. Create an SNS topic with the `email` protocol
2. Copy the ARN of the SNS topic for use later

### 2. Lambda Function to Send Email

1. Create a Lambda function `NewPostSendEmail.py` to trigger SNS topic
2. In the function code, use AWS SDK `boto3` to integrate python with AWS services
3. Use `os` library to get the `env` the ARN from SNS. Go to `Lambda` -> `Configuration` -> `Environment variable` -> set `key` and `value`
4. Create a role for Lambda with SNS permission -> Attach a role 

### 3. S3

1. Setup S3 Event but make sure the Lambda function is working
2. Create a Event Notification with the all object create events
3. Choose Destination is a Lambda function


#### 4. Lambda Function to Send Subscription Confirmation

1. Create a Lambda function `SendSubConfirmation.py` to let the user subscribe to the SNS topic
2. The `email` variable to get the endpoint email

