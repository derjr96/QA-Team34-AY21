from django.forms import ModelForm
from django import forms
from .models import Product
from django.core.validators import MinValueValidator


class ProductForm(ModelForm):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(attrs={"placeholder": "your title.."}), max_length=15)

    itemname = forms.CharField(label='Product Name',
                            widget=forms.TextInput(attrs={"placeholder": "product name.."}), max_length=25)

    itemprice = forms.DecimalField(label='Item Price',initial=1, validators =[MinValueValidator(1.0)])

    content = forms.CharField(label='Content',
                               widget=forms.TextInput(attrs={"placeholder": "content.."}), max_length=55)

    class Meta:
        model = Product
        fields = [
            'title',
            'itemname',
            'itemprice',
            'content',
            'image'
        ]
