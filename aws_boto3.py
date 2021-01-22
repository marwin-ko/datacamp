#
# S3
#

# AWS Permissions
# - IAM (resource level)
# - Bucket Policy (bucket level)
# - ACL (object level)
# - Presigned URL (temporary object level)

# URL format
url = f'https://{bucket}.s3.amazonaws.com/{key}'

# s3 client connection
s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET)

response = s3.list_buckets()

s3.head_object()

s3.upload_file(
  Filename = 'local_data.csv', # local path to data
  Bucket = 'my-bucket',
  Key = 'uploaded_test.csv',  # s3 filename
)

s3.download_file(
  Filename = 'test.csv', # download name
  Bucket = 'my-bucket',
  Key = 'original_test.csv',
)
                 
s3.delete_object(
  Bucket = 'my-bucket',
  Key = 'original_test.csv'
)

s3.download_file(
  Filename = 'test.csv',
  Bucket = 'my-bucket',
  Key = 'original_test.csv'
)

# read streaming object 
obj = s3.get_object(
  Bucket = 'my-bucket',
  Key = 'original_test.csv'
)
df = pd.read_csv(obj['Body'])

s3.generate_presigned_url(
  ClientMethod = 'get_method',
  ExpiresIn = '3600', # 1 hr expiration
  Params = {'Bucket' = 'my-bucket', 'Key' = 'path'}
)
 
 
# Example of pulling multiple files and concat them
df_list =  [ ] 
for file in response['Contents']:
    # For each file in response load the object from S3
    obj = s3.get_object(Bucket='gid-requests', Key=file['Key'])
    # Load the object's StreamingBody with pandas
    obj_df = pd.read_csv(obj['Body'])
    # Append the resulting DataFrame to list
    df_list.append(obj_df)
# Concat all the DataFrames with pandas
df = pd.concat(df_list)



