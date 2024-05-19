#######################
# This script assume that there are buckets crearted in s3 service with the porefix gim
# Like: gim-bucket1 , gim-bucket2 , gim-bucket3
# Using boto3 we will replace the buckets with another ones with the prefix gid instead of gim
########################

import boto3

# Create the s3 boto3 client
s3 = boto3.client('s3')

# Get the list all buckets in the account
response = s3.list_buckets()

# Check if each bucket name of the response list has the prefix gim in it's name
for bucket in response['Buckets']:
    if 'gim' in bucket['Name']:
        s3.delete_bucket(Bucket=bucket['Name'])

# Create the buckets with the new 
s3.crearte_bucket(Bucket='gid-bucket1')
s3.crearte_bucket(Bucket='gid-bucket2')

# List the buckets after modifying it's name
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])