from django.contrib import admin

# Register your models here.

from .models import Listings

class ListingsAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','realtor')
    list_display_links = ('id','title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    list_per_page = 25

admin.site.register(Listings,ListingsAdmin)

