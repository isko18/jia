from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Project, YearlyCatalog, Scroll, BusinessProject
from apps.project.translation import *

class ProjectAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ('title_ru', 'descriptons_ru',),
        }),
        ('Английская версия', {
            'fields': ('title_en', 'descriptons_en',),
        }),
        ('Кыргызская версия', {
            'fields': ('title_ky', 'descriptons_ky',),
        }),
    )

class YearlyCatalogAdmin(TranslationAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('year', 'image',),
        }),
    )

class ScrollAdmin(TranslationAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'image',),
        }),
        ('Русская версия', {
            'fields': ('title_ru', 'image_ru',),
        }),
        ('Английская версия', {
            'fields': ('title_en', 'image_en',),
        }),
        ('Кыргызская версия', {
            'fields': ('title_ky', 'image_ky',),
        }),
    )

class BusinessProjectAdmin(TranslationAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'descriptons', 'scroll',),
        }),
        ('Русская версия', {
            'fields': ('title_ru', 'descriptons_ru',),
        }),
        ('Английская версия', {
            'fields': ('title_en', 'descriptons_en',),
        }),
        ('Кыргызская версия', {
            'fields': ('title_ky', 'descriptons_ky',),
        }),
    )

admin.site.register(Project, ProjectAdmin)
admin.site.register(YearlyCatalog, YearlyCatalogAdmin)
admin.site.register(Scroll, ScrollAdmin)
admin.site.register(BusinessProject, BusinessProjectAdmin)
