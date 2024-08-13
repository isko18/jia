# apps/base/admin.py
from django.contrib import admin
from apps.base.models import Base, WhatWill, Slider, SliderTitle, Video, Banner, What_will_title, About_the_forum,  SliderTitleSponsors, SliderSponsors, Button
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from apps.base.translation import *

class WhatWillInline(TranslationTabularInline):
    model = WhatWill
    extra = 1
    
class SliderInline(admin.TabularInline):
    model = Slider
    extra = 1

class SliderSponsorsInline(admin.TabularInline):
    model = SliderSponsors
    extra = 1

class SliderSponsorsAdmin(TranslationAdmin):
    inlines = [SliderSponsorsInline]
    fieldsets = (
        # ('Основное', {
        #     'fields': ('image',),
        # }),
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
# class WhatWillAdmin(TranslationAdmin):
#     fieldsets = (
#         ('Основное', {
#             'fields': ('image',),
#         }),
#         ('Русская версия', {
#             'fields': ('title_ru',),
#         }),
#         ('Английская версия', {
#             'fields': ('title_en',),
#         }),
#         ('Кыргызская версия', {
#             'fields': ('title_ky',),
#         }),
#     )

class BannerAdmin(TranslationAdmin):
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
    
class ButtonAdmin(TranslationAdmin):
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
    
class SliderAdmin(TranslationAdmin):
    inlines = [SliderInline]
    fieldsets = (
        # ('Основное', {
        #     'fields': ('image',),
        # }),
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
    
    
class VideoAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ('url_ru', 'title_ru', 'descriptions_ru'),
        }),
        ('Кыргызская версия', {
            'fields': ('url_ky', 'title_ky', 'descriptions_ky'),
        }),
    )
    
    
class About_the_forumAdmin(TranslationAdmin):
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
  
class what_will_titleAdmin(TranslationAdmin):
    inlines = [WhatWillInline]
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

admin.site.register(SliderTitle, SliderAdmin)
admin.site.register(SliderTitleSponsors, SliderSponsorsAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Base)
admin.site.register(Button, ButtonAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(About_the_forum, About_the_forumAdmin)
admin.site.register(What_will_title, what_will_titleAdmin)
