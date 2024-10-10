from django.contrib import admin
from images.models import LottiImage
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

# Register your models here.
@admin.register(LottiImage)
class LottiImageAdmin(admin.ModelAdmin):
    pass