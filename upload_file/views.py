from django.shortcuts import render

from services.s3_buckets import lists_bucket
from services.s3_buckets import lists_file_on_s3
from services.utils import get_bucket_name_date
from upload_file.forms import UploadForm


def upload_file_s3(request):
    msg = None
    form = UploadForm
    bucket = lists_bucket()
    bucket = get_bucket_name_date(bucket)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg = "File Upload Successfully."
        else:
            msg = "File Upload Unsuccessfully."
    return render(request, 'upload_file.html', {'page_name': 'Bucket', 'form': form, 'msg': msg, 'bucket': bucket})


def bucket_file(request, bucket_name):
    lists_file = lists_file_on_s3(bucket_name)
    return render(request, 'bucket_file.html', {'page_name': bucket_name, 'lists': lists_file})
