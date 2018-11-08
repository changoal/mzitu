from django.contrib import admin
from .models import Folder, ImageModel


class FolderAdmin(admin.ModelAdmin):
    fields = ['name', 'path', 'file_count']
    list_display = ('name', 'path', 'file_count')


class ImageAdmin(admin.ModelAdmin):
    fields = ['name', 'path', 'size']
    list_display = ('name', 'path', 'size')


# Register your models here.
admin.site.register(Folder, FolderAdmin)
admin.site.register(ImageModel, ImageAdmin)
