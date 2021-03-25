from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from django.conf import settings
from .detect import rewrite
from .models import ImageUploadModel


def home_view(request):
    return render(request, "home.html")


def dface(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # db delete
            if ImageUploadModel.objects.all().count() > 100:
                obs = ImageUploadModel.objects.all().first()
                if obs:
                    obs.delete()

            img_path = f"{settings.MEDIA_ROOT}/{form.instance.document.name}"
            rewrite(img_path)
            return render(request, "dface.html", {"form": form, "post": post})
    else:
        form = ImageUploadForm()
    return render(request, "dface.html", {"form": form})
