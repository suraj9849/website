from django.forms import ModelForm

from admin.models import AddSuggestedProducts
from hamrowatchshop.models import ComingSoonProduct, menClothes


class AddSuggestedProductsForm(ModelForm):
    class Meta:
        model = AddSuggestedProducts
        fields = '__all__'


class CommingSoonClothesForm(ModelForm):
    class Meta:
        model = ComingSoonProduct
        fields = '__all__'


class menClothesForm(ModelForm):
    class Meta:
        model = menClothes
        fields = '__all__'
