from django.shortcuts import render

from .forms import UploadForm


def home(request):
    msg = None
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg = "File Upload Successfully."
        else:
            msg = "File Upload Unsuccessfully."
        return render(request, 'home.html', {'form': form, 'msg': msg})
    else:
        form = UploadForm
    return render(request, 'home.html', {'form': form, 'msg': msg})
