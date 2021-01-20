#
# S3
#


# s3 client connection
s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET)

response = s3.list_buckets()

s3.head_object()

s3.upload_file(Filename = 'local_data.csv', # local path to data
               Bucket = 'my-bucket',
               Key = 'uploaded_test.csv',  # s3 filename
               )

s3.download_file(Filename = 'test.csv', # download name
                 Bucket = 'my-bucket',
                 Key = 'original_test.csv',
                 )
                 
s3.delete_object(Bucket = 'my-bucket',
                 Key = 'original_test.csv'
                 )
