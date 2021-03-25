from django import forms
from .models import ImageUploadModel


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        fields = ("description", "document")
