# 1. Download SSO Generator
# 2. Run the SSOGenerator on Command Line java -jar ssogenerator-2.1.0.jar
# 3. pip install boto3
# References:
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#bucket
# https://realpython.com/python-boto3-aws-s3/


import boto3
import os
import uuid
os.system('cls')

# Note that profile name can be fetched from ~/.aws/credentials file
session = boto3.Session(profile_name='profile_name_here')

# Specify s3 as the AWS resource to use
s3_resource = session.resource('s3')

# List Buckets in an account
buckets = s3_resource.buckets.all()
for bucket in buckets:
    print(bucket.name)

# List the contents of a specific bucket
my_bucket = s3_resource.Bucket('bucket_name_here')
for file in my_bucket.objects.all():
    print(file.key)

# Create a Bucket, Use uuid to append random characters for name to be unique
my_bucket_name = "python-training-" + str(uuid.uuid4())
bucket_name = my_bucket_name
bucket = s3_resource.Bucket(bucket_name)

# Create Bucket
response = bucket.create(ACL='private')

# Upload an Object
response = bucket.upload_file('dog.jpg', 'dog.jpg')
print(response)

# Download an Object
bucket.download_file(
    'dog.jpg', "Python Lessons/12_Boto3/my_downloaded_file.jpg")

# Delete an Object
response = bucket.delete_objects(
    Delete={
        'Objects': [
            {
                'Key': 'dog.jpg',
            }
        ]
    }
)
