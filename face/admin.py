from django.contrib import admin
from .models import ImageUploadModel


@admin.register(ImageUploadModel)
class FaceAdmin(admin.ModelAdmin):
    pass
