# import django_filters
# from .models import *
# from django_filters import CharFilter


# class HamroshopCenterFilter(django_filters.FilterSet):
#     name_contains = CharFilter(field_name='name',
#                                lookup_expr='icontains')
#     class Meta:
#         model = HamroShopCenter
#         fields = ""
import django_filters
from .models import HamroShopCenter
from django_filters import CharFilter
 
class ShadesFilter(django_filters.FilterSet):
    name_contains = CharFilter(field_name='name',
                                   lookup_expr='icontains')
    class Meta:
        model = HamroShopCenter
        fields = ""
        # exclude = ['firstname', 'lastname', 'phone']