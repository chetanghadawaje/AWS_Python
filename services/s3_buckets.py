import logging

import boto3
from botocore.exceptions import ClientError
from django.conf import settings

from services import client_s3

AWS_REGION_NAME = settings.AWS_REGION_NAME
AWS_SERVER_SECRET_KEY = settings.AWS_SERVER_SECRET_KEY
AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID


def create_bucket(bucket_name):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        location = {'LocationConstraint': AWS_REGION_NAME}
        client_s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return {"Message": e.response['Error']['Message'], "Code": e.response['ResponseMetadata']['HTTPStatusCode']}
    return {"Message": "Bucket created.", "Code": 200}


def lists_bucket():
    """
    Retrieve the list of existing buckets
    """
    response = dict()
    try:
        response = client_s3.list_buckets()
    except Exception as e:
        logging.exception(f"Exception in lists_bucket: {e}")

    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        logging.info(f"response in error: {response}")
        response = dict()

    logging.info(f"Bucket List: {response}")
    return response
