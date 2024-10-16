![cover](https://blog.khoahoang.dev/images/sns.jpg)
### 1. Set Up SNS

1. Create an SNS topic using the `email` protocol.
2. Copy the ARN (Amazon Resource Name) of the SNS topic for later use.

![alt text](<images/lambda-sns- (3).png>)

### 2. Create Lambda Function for Email Notifications
In this case, I'm using Python as a runtime.
1. Develop a Lambda function named `NewPostSendEmail.py` that triggers the SNS topic.
2. Utilize the AWS SDK `boto3` to connect Python with AWS services in your function code.
3. Use the `os` library to retrieve the SNS ARN from environment variables. Navigate to `Lambda` -> `Configuration` -> `Environment variables` to set the `key` and `value`.
![alt text](<images/lambda-sns- (3).png>)
4. Create a role for the Lambda function that includes permissions for SNS, and then attach this role.

### 3. Configure S3

1. Set up an S3 event notification.
2. Create an event notification to capture all object creation events (this is a placeholder; improvements will be made in the future).
3. Set the destination for the event notification to be the Lambda function.

![alt text](<images/lambda-sns- (4).png>)

### 4. Create Lambda Function for Subscription Confirmation

1. Create a Lambda function called `SendSubConfirmation.py` to handle user subscriptions to the SNS topic.
2. Reuse the SNS ARN from earlier and set it as an environment variable, similar to the `NewPostSendEmail.py` function.
3. Use an `email` variable to specify the endpoint email address.

### 5. Set Up API Gateway

1. Create an API in API Gateway and choose the `HTTP API` type.
2. Define a route for the API using a `GET` method.
3. Integrate the API with the `SendSubConfirmation` Lambda function.

#### 6. Custom API Domain

1. Create a custom domain in API Gateway. Set up SSL or use an exist one in the ACM Certificate
2. Mapping the API in the `API Mappings`
![alt text](<images/lambda-sns- (5).png>)
3. Use `Route 53` and create an A record to route the traffic to our API.
![alt text](<images/lambda-sns- (1).png>)

### Conclusion

By following these steps, you have successfully set up a robust notification system using AWS services. You created SNS topics, Lambda functions for email notifications and subscription confirmations, configured S3 event notifications, and set up an API Gateway with a custom domain. This setup ensures that your application can handle notifications efficiently and securely, leveraging the scalability and reliability of AWS infrastructure.