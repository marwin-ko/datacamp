# Rekognition
  # A Computer Vision API

# Features
# - detecting objects
# - extracting text from images


# Init client
rekog = boto3.client('rekognition',
region_name = 'us-east-1',
aws_access_key_id = AWS_KEY_ID,
aws_secret_access_key = AWS_SECRET)
