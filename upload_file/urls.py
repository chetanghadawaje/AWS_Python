from django.urls import path

from .views import upload_file_s3, bucket_file

urlpatterns = [
    path('upload/', upload_file_s3, name='upload_file'),
    path('bucket/<bucket_name>', bucket_file, name='bucket_file'),
]
