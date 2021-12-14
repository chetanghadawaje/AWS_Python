from django import forms
from django.core.exceptions import ValidationError


class BucketForm(forms.Form):
    bucket_name = forms.CharField(label='Bucket Name', max_length=20)

    # def clean_bucket_name(self):
    #     cleaned_data = super().clean()
    #     bucket_name = cleaned_data.get("bucket_name")
    #
    #     if bucket_name is None and bucket_name == '':
    #         msg = "Bucket name not pass empty."
    #         raise ValidationError(msg)
    #     return cleaned_data
