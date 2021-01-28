# Rekognition
  # A Computer Vision API

# Features
# - detecting objects
#   - count instances of objects
# - extracting text from images
  # "TextDetections" can be 2 types: "LINE" or "WORD"
  # Line detection is a line of word (can span over multiple adjacent object)
  # Word detection is just the word by itself.


# Init client
rekog = boto3.client('rekognition',
region_name = 'us-east-1',
aws_access_key_id = AWS_KEY_ID,
aws_secret_access_key = AWS_SECRET)


# detect objects from image
response = rekog.detect_labels(
  Image = {'S3Object' : 
           {
             'Bucket': 'my-bucket',
             'Name': 'image.jpg'
           }
          },
  MaxLabels = 10,
  MinConfidence = 95  # min percent confidence
)


# extract text from image
response = rekog.detect_labels(
    Image = {'S3Object' :
             {
               'Bucket': 'my-bucket',
               'Name': 'image.jpg'
             }
            }
)
