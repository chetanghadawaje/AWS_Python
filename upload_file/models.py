from django.db import models


class Upload(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    bucket_name = models.CharField(max_length=100, blank=True, null=True)
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d')
    upload_date = models.DateTimeField(auto_now_add=True)
