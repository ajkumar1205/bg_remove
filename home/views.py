from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .forms import ImageForm, MyImageForm
from PIL import Image as PILImage
from django.views import View

from rembg import remove

def index(request: HttpRequest):
    
    try:
        if request.method == "GET":
            return render(request, 'index.html', {"form": MyImageForm(), "message": "Upload an image here!"})
        if request.method == "POST":
            form = MyImageForm(request.POST, request.FILES)
            # open PILImage with the form image data

            if form.is_valid():
                image = PILImage.open(form.files["image"])
                # img = PILImage.open("static/"+str(form.files["image"]))
                out = remove(image)
                name = "static/"+"no_bg_"+str(form.files["image"])
                out.save(name)
                return render(request, 'index.html', {"form": form, "message": "Image uploaded successfully!", "image": name})
            return render(request, 'index.html',{"form": MyImageForm(), "message": "Something went wrong!"})
    except Exception as e:
        return HttpResponse(f"Something unexpected happened! {e}")    