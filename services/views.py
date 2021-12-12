from django.shortcuts import render
from django.urls import reverse
from services.s3_buckets import lists_bucket


def services(request):
    services_list = {'S3': reverse('buckets'), "a": "a"}
    return render(request, 'services.html', {'page_name': 'Services', 'services_list': services_list})


def buckets(request):
    bucket = lists_bucket()
    bucket_list = {}
    return render(request, 'services.html', {'page_name': 'Bucket', 'services_list': bucket_list})
