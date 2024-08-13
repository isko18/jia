from modeltranslation.translator import translator, TranslationOptions
from .models import Project, YearlyCatalog, Scroll, BusinessProject

class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptons',)

class YearlyCatalogTranslationOptions(TranslationOptions):
    fields = ('image',)

class ScrollTranslationOptions(TranslationOptions):
    fields = ('title', 'image',)

class BusinessProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptons',)

translator.register(Project, ProjectTranslationOptions)
translator.register(YearlyCatalog, YearlyCatalogTranslationOptions)
translator.register(Scroll, ScrollTranslationOptions)
translator.register(BusinessProject, BusinessProjectTranslationOptions)
