from django import forms
from .models import *


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class MarkaForm(forms.ModelForm):
    class Meta:
        model = Marka
        fields = '__all__'