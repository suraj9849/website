from django import forms
from .models import *
from django.forms import ModelForm


class ClothProductForm(ModelForm):
    class Meta:
        model = HamroShopCenter
        fields = '__all__'


class ComingsoonCloth(ModelForm):
    class Meta:
        model = ComingSoonProduct
        fields = '__all__'


class MenClothForm(ModelForm):
    class Meta:
        model = menClothes
        fields = '__all__'


class WomenClothForm(ModelForm):
    class Meta:
        model = womenClothes
        fields = '__all__'


class KidsClothForm(ModelForm):
    class Meta:
        model = kidsClothes
        fields = '__all__'


class OnsaleClothForm(ModelForm):
    class Meta:
        model = onsaleClothes
        fields = '__all__'
