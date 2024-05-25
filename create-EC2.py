import boto3

# Create an EC2 boto3 client
ec2 = boto3.client('ec2')

# Specify the instance configuration
image_id = 'ami-0c94755bb95c71c99'  
instance_type = 't2.micro'
key_name = 'my-key-pair'  
security_group_ids = ['sg-0123456789abcdef']

# Create the EC2 instance
response = ec2.run_instances(
    ImageId=image_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_group_ids,
    MinCount=1,
    MaxCount=1
)

# Get the ID of the created instance
instance_id = response['Instances'][0]['InstanceId']
print(f"Created EC2 instance with ID: {instance_id}")
