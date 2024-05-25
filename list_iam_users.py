import boto3

iam = boto3.client('iam')
print(iam.list_users())