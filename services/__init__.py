import boto3
from django.conf import settings

AWS_REGION_NAME = settings.AWS_REGION_NAME
AWS_SERVER_SECRET_KEY = settings.AWS_SERVER_SECRET_KEY
AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID

s3_arg = {'service_name': 's3', 'aws_access_key_id': AWS_ACCESS_KEY_ID, 'aws_secret_access_key': AWS_SERVER_SECRET_KEY,
          'region_name': AWS_REGION_NAME}

"""
is a low level class object. For each client call, you need to explicitly specify the targeting resources, the designated
service target name must be pass long. You will lose the abstraction ability.
"""
client_s3 = boto3.client(**s3_arg)

"""
This is the high-level service class recommended to be used. This allows you to tied particular AWS resources and passes
it along, so you just use this abstraction than worry which target services are pointed to. As you notice from the 
session part, if you have a custom session, you just pass this abstract object than worrying about all custom regions,
etc to pass along
"""
resource_s3 = boto3.resource(**s3_arg)
