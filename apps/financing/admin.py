from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import Financing, Reach, Sector, LegalName, Image, NameInfo, ImageForm
from apps.financing.translation import *



class NameInfoInline(TranslationTabularInline):
    model = NameInfo
    extra = 1

class ImageFormAdmin(TranslationAdmin):
    inlines = [NameInfoInline]
    fieldsets = (
        ('Основыне настройки', {
            'fields': ('image',),
        }),
    )
    
class FinancingAdmin(TranslationAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('image',),
        }),
        ('Русская версия', {
            'fields': ('title_ru',),
        }),
        ('Английская версия', {
            'fields': ('title_en',),
        }),
        ('Кыргызская версия', {
            'fields': ('title_ky',),
        }),
    )

admin.site.register(Image)

class ReachAdmin(TranslationAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('full_name', 'name_company', 'legal_name', 'brief_description', 'sector'),
        }),
        ('Русская версия', {
            'fields': ('full_name_ru', 'name_company_ru', 'brief_description_ru'),
        }),
        ('Английская версия', {
            'fields': ('full_name_en', 'name_company_en', 'brief_description_en'),
        }),
        ('Кыргызская версия', {
            'fields': ('full_name_ky', 'name_company_ky', 'brief_description_ky'),
        }),
    )

class SectorAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ('name_ru',),
        }),
        ('Английская версия', {
            'fields': ('name_en',),
        }),
        ('Кыргызская версия', {
            'fields': ('name_ky',),
        }),
    )

class LegalNameAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ('name_ru',),
        }),
        ('Английская версия', {
            'fields': ('name_en',),
        }),
        ('Кыргызская версия', {
            'fields': ('name_ky',),
        }),
    )

admin.site.register(ImageForm, ImageFormAdmin)
admin.site.register(Financing, FinancingAdmin)
admin.site.register(Reach, ReachAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(LegalName, LegalNameAdmin)
