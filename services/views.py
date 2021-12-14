from django.shortcuts import render
from django.urls import reverse
from services.s3_buckets import lists_bucket, create_bucket
from services.utils import get_bucket_name_date
from services.forms import BucketForm


def services(request):
    services_list = {'S3': reverse('buckets'), "Test": "test"}
    return render(request, 'services.html', {'page_name': 'Services', 'services_list': services_list})


def buckets(request):
    form = BucketForm()
    bucket = lists_bucket()
    bucket = get_bucket_name_date(bucket)
    error_msg = None
    if request.method == 'POST':
        if form.is_valid():
            bucket_name = form.cleaned_data['bucket_name']
            response = create_bucket(bucket_name)
            error_msg = response['Message']
        else:
            error_msg = "Form is not valid."
    return render(request, 'buckets.html', {'page_name': 'Bucket', 'list': bucket, 'form': form, 'error_msg': error_msg})
