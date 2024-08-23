from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Exhibition, Slider, RentStand
from apps.exhibition.translation import *

class ExhibitionAdmin(TranslationAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'descriptions',),
        }),
        ('Русская версия', {
            'fields': ('title_ru', 'descriptions_ru',),
        }),
        ('Английская версия', {
            'fields': ('title_en', 'descriptions_en',),
        }),
        ('Кыргызская версия', {
            'fields': ('title_ky', 'descriptions_ky',),
        }),
    )

class SliderAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ('image_ru', 'image_2_ru',),
        }),
        ('Английская версия', {
            'fields': ('image_en', 'image_2_en',),
        }),
        ('Кыргызская версия', {
            'fields': ('image_ky', 'image_2_ky',),
        }),
    )
    
admin.site.register(RentStand)
admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Slider, SliderAdmin)
