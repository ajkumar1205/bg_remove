from django.forms import ModelForm
from django import forms

from .models import Image

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']

class MyImageForm(forms.Form):
    image = forms.ImageField()

