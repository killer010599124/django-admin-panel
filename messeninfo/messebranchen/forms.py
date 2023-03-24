from django import forms
from .models import TradeFair


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = TradeFair
        fields = ('title', 'image1', 'image2')