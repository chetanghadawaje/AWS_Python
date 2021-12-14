import logging

import boto3
from botocore.exceptions import ClientError
from django.conf import settings

AWS_REGION_NAME = settings.AWS_REGION_NAME
AWS_SERVER_SECRET_KEY = settings.AWS_SERVER_SECRET_KEY
AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID


def create_bucket(bucket_name, region=AWS_REGION_NAME):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SERVER_SECRET_KEY)
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SERVER_SECRET_KEY,
                                     region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return {"Message": e.response['Error']['Message'], "Code": e.response['ResponseMetadata']['HTTPStatusCode']}
    return {"Message": "Bucket created.", "Code": 200}


def lists_bucket():
    # Retrieve the list of existing buckets
    response = dict()
    try:
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SERVER_SECRET_KEY,
                          region_name=AWS_REGION_NAME)
        response = s3.list_buckets()
    except Exception as e:
        logging.exception(f"Exception in lists_bucket: {e}")

    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        logging.info(f"response in error: {response}")
        response = dict()

    logging.info(f"Bucket List: {response}")
    return response
