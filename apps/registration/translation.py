from modeltranslation.translator import translator, TranslationOptions
from .models import Registration, Standart, Vip

class RegistrationTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')

class StandartTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')
    
class VipTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')

translator.register(Registration, RegistrationTranslationOptions)
translator.register(Standart, StandartTranslationOptions)
translator.register(Vip, VipTranslationOptions)


