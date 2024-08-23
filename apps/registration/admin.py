from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Registration, Standart, Vip, SectorStandart, ReachStandart, SectorVip, ReachVip
from .translation import *

class RegistrationAdmin(TranslationAdmin):
    fieldsets = (
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

class StandartAdmin(TranslationAdmin):
    fieldsets = (
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

class VipAdmin(TranslationAdmin):
    fieldsets = (
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

class SectorStandartAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ReachStandartAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'name_company', 'sector', 'current', 'email', 'phone')
    list_filter = ('sector',)
    search_fields = ('full_name', 'name_company', 'email', 'phone')

class SectorVipAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ReachVipAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'name_company', 'sector', 'current', 'email', 'phone')
    list_filter = ('sector',)
    search_fields = ('full_name', 'name_company', 'email', 'phone')

admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Standart, StandartAdmin)
admin.site.register(Vip, VipAdmin)
admin.site.register(SectorStandart, SectorStandartAdmin)
admin.site.register(ReachStandart, ReachStandartAdmin)
admin.site.register(SectorVip, SectorVipAdmin)
admin.site.register(ReachVip, ReachVipAdmin)
