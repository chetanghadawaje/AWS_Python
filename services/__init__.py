import boto3
from django.conf import settings

AWS_REGION_NAME = settings.AWS_REGION_NAME
AWS_SERVER_SECRET_KEY = settings.AWS_SERVER_SECRET_KEY
AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID

s3_arg = {'service_name': 's3', 'aws_access_key_id': AWS_ACCESS_KEY_ID, 'aws_secret_access_key': AWS_SERVER_SECRET_KEY,
          'region_name': AWS_REGION_NAME}

client_s3 = boto3.client(**s3_arg)

resource_s3 = boto3.resource(**s3_arg)
