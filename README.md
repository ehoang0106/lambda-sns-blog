### 1. Set Up SNS

1. Create an SNS topic using the `email` protocol.
2. Copy the ARN (Amazon Resource Name) of the SNS topic for later use.

### 2. Create Lambda Function for Email Notifications
In this case, I'm using Python as a runtime.
1. Develop a Lambda function named `NewPostSendEmail.py` that triggers the SNS topic.
2. Utilize the AWS SDK `boto3` to connect Python with AWS services in your function code.
3. Use the `os` library to retrieve the SNS ARN from environment variables. Navigate to `Lambda` -> `Configuration` -> `Environment variables` to set the `key` and `value`.
4. Create a role for the Lambda function that includes permissions for SNS, and then attach this role.

### 3. Configure S3

1. Set up an S3 event notification.
2. Create an event notification to capture all object creation events (this is a placeholder; improvements will be made in the future).
3. Set the destination for the event notification to be the Lambda function.

### 4. Create Lambda Function for Subscription Confirmation

1. Create a Lambda function called `SendSubConfirmation.py` to handle user subscriptions to the SNS topic.
2. Reuse the SNS ARN from earlier and set it as an environment variable, similar to the `NewPostSendEmail.py` function.
3. Use an `email` variable to specify the endpoint email address.

### 5. Set Up API Gateway

1. Create an API in API Gateway and choose the `HTTP API` type.
2. Define a route for the API using a `GET` method.
3. Integrate the API with the `SendSubConfirmation` Lambda function.
