import boto3
import json
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')

def lambda_handler (event, context):
    bucket = s3.Bucket('mysrcbucket')
    dest_bucket=s3.Bucket('mydestbucket')
    try:
        for obj in bucket.objects.filter:
            dest_key=obj.key
            s3.Object(dest_bucket,dest_key).copy_from(CopySource= { 'Bucket': obj.bucket_name , 'Key' : obj.key})
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print "User already exists"
        else:
            print "Unexpected error: %s" + str(e)
