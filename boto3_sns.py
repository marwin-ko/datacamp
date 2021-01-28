sns = boto3.client('sns'
region_name = 'us-east-1',
aws_access_key_id = AWS_KEY_ID,
aws_secret_access_key=AWS_SECRET)


# Summary
# create topic, add subscribers to that topic, leverage that topic to mass send (publish) messages.

# Create Topic
topic_arn = sns.create_topic(Name = 'topic_notification')['TopicArn']

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
response = sns.unsubscribe(SubscriptionArn = sub['SubscriptionArn'])

# publish to a topic
response = sns.publish(
TopicArn = 'arn',
Message = 'Body text of SMS or e-mail',
Subject = 'Subject Line for Email'  # not visible for texts
)
                           
# sending single SMS message
# (no need for topicArn or subscription)
# good for one-off message (not good for maintainability)
response = sns.publish(
  PhoneNumber  = '+1234567890',
  Message = 'Body text')





