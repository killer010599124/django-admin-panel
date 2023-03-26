from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = [
        'language_name',
    ]
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category_name',
    ]

@admin.register(models.TradeFair)
class TradeFairAdmin(admin.ModelAdmin):
    list_display = [
        'b_id',
        'image1',
        'image2'
    ]