from modeltranslation.translator import translator, TranslationOptions
from .models import Financing, Reach, Sector, LegalName, NameInfo, ImageForm

class FinancingTranslationOptions(TranslationOptions):
    fields = ('title',)

class NameInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')

class ImageFormTranslationOptions(TranslationOptions):
    fields = ('image',)


class ReachTranslationOptions(TranslationOptions):
    fields = ('full_name', 'name_company', 'brief_description',)

class SectorTranslationOptions(TranslationOptions):
    fields = ('name',)

class LegalNameTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Financing, FinancingTranslationOptions)
translator.register(NameInfo, NameInfoTranslationOptions)
translator.register(ImageForm, ImageFormTranslationOptions)
translator.register(Reach, ReachTranslationOptions)
translator.register(Sector, SectorTranslationOptions)
translator.register(LegalName, LegalNameTranslationOptions)
