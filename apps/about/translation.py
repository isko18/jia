# apps/base/translation.py
from modeltranslation.translator import translator, TranslationOptions
from apps.about.models import About, AboutBanner, History, HistoryDetail, Statistics, Gallery, GalleryTitle

class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')
    
class AboutBannerTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')

class HistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')
    
class HistoryDetailTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'url', 'amount_invest', 'amount_projet')
    
class StatisticsTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')

class GalleryTitleTranslationOptions(TranslationOptions):
    fields = ('title', )

translator.register(About, AboutTranslationOptions)
translator.register(AboutBanner, AboutBannerTranslationOptions)
translator.register(History, HistoryTranslationOptions)
translator.register(HistoryDetail, HistoryDetailTranslationOptions)
translator.register(Statistics, StatisticsTranslationOptions)
translator.register(GalleryTitle, GalleryTitleTranslationOptions)





print("Translation options registered")  # Debug statement
