from django.contrib import admin
from apps.about.models import About, AboutBanner, History, HistoryDetail, Statistics, Gallery, GalleryTitle
from modeltranslation.admin import TranslationAdmin
from apps.about.translation import AboutBannerTranslationOptions, AboutTranslationOptions, HistoryDetailTranslationOptions, HistoryTranslationOptions, GalleryTitleTranslationOptions

class AboutAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ('title_ru', 'descriptions_ru'),
        }),
        ('Английская версия', {
            'fields': ('title_en', 'descriptions_en'),
        }),
        ('Кыргызская версия', {
            'fields': ('title_ky', 'descriptions_ky'),
        }),
    )
    
class AboutBannerAdmin(TranslationAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('image',),
        }),
        ('Русская версия', {
            'fields': ('title_ru', 'descriptions_ru'),
        }),
        ('Английская версия', {
            'fields': ('title_en', 'descriptions_en'),
        }),
        ('Кыргызская версия', {
            'fields': ('title_ky', 'descriptions_ky'),
        }),
    )
    
class HistoryAdmin(TranslationAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('year_1', 'year_2', 'year_3', 'year_4', 'year_5'),
        }),
        ('Русская версия', {
            'fields': ('title_ru', 'descriptions_ru'),
        }),
        ('Английская версия', {
            'fields': ('title_en', 'descriptions_en'),
        }),
        ('Кыргызская версия', {
            'fields': ('title_ky', 'descriptions_ky'),
        }),
    )
    
class HistoryDetailAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ('title_ru', 'descriptions_ru', 'url_ru', 'amount_invest_ru','amount_projet_ru'),
        }),
        ('Английская версия', {
            'fields': ('title_en', 'descriptions_en', 'url_en','amount_invest_en'),
        }),
        ('Кыргызская версия', {
            'fields': ('title_ky', 'descriptions_ky', 'url_ky', 'amount_invest_ky', 'amount_projet_ky'),
        }),
    )
    
class StatisticsBannerAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ('title_ru', 'descriptions_ru'),
        }),
        ('Английская версия', {
            'fields': ('title_en', 'descriptions_en'),
        }),
        ('Кыргызская версия', {
            'fields': ('title_ky', 'descriptions_ky'),
        }),
    )
    
    
class GalleryTitleAdmin(TranslationAdmin):
    fieldsets = (
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
    
     
admin.site.register(About, AboutAdmin)
admin.site.register(AboutBanner, AboutBannerAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(HistoryDetail, HistoryDetailAdmin)
admin.site.register(Statistics, StatisticsBannerAdmin)
admin.site.register(GalleryTitle, GalleryTitleAdmin)
admin.site.register(Gallery)

