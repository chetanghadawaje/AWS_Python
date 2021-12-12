from django.urls import path

from .views import buckets

urlpatterns = [
    path('buckets/', buckets, name='buckets'),
]
