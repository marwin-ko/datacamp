sns = boto3.client('sns'
region_name = 'us-east-1',
aws_access_key_id = AWS_KEY_ID,
aws_secret_access_key=AWS_SECRET)

# Create Topic


# subscribe phone
response = sns.subscribe(
TopicArn = 'arn:aws:sns:us-east-1:xxxxxxxxxxxx:<name>',
Protocol = 'sms',
Endpoint = '+1234567890'  #phone number
)

# subscribe email
response = sns.subscribe(
TopicArn = 'arn:aws:sns:us-east-1:xxxxxxxxxxxx:<name>',
Protocol = 'email',
Endpoint = 'somedude@gmail.com'
)

# View subscriptions by topics
response = sns.list_subscriptions_by_topic(TopicArn = 'arn')
subs = pd.DataFrame(response['Subscriptions'])

# unsubscribe
for sub in subs:
response = sns.unsubscribe(SubscriptionArn = sub['SubscriptionArn']

# publish to a topic
response = sns.publish(
TopicArn = 'arn',
Message = 'Body test of SMS or e-mail',
Subject = 'Subject Line for Email'
)





