from django.contrib import admin

# Register your models here.

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','email','is_mvp')
    list_display_links = ('id','name')
    list_filter = ('is_mvp',)

admin.site.register(Realtor,RealtorAdmin)