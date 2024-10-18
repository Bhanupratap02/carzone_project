from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(selft,object):
        return format_html('<img src="{}" width="40" style="border-radius:50%" />'.format(object.car_photo.url))
    thumbnail.short_description = 'Photo'
    list_display = ('id','thumbnail','car_title','state','model','body_style','passengers','fuel_type','is_featured',)
    list_display_links = ('id','thumbnail','car_title')
    list_editable = ('is_featured',)
    search_fields = ('id','car_title','model','body_style','fuel_type')
    list_filter = ('model','body_style','fuel_type','state',)
admin.site.register(Car,CarAdmin)
