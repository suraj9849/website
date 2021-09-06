from django.contrib import admin
from .models import HamroWatchShop


# Register your models here.

class HamroWatchShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(HamroWatchShop, HamroWatchShopAdmin)

