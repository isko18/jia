from modeltranslation.translator import translator, TranslationOptions
from .models import Exhibition, Slider

class ExhibitionTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)

class SliderTranslationOptions(TranslationOptions):
    fields = ('image','image_2',)

translator.register(Exhibition, ExhibitionTranslationOptions)
translator.register(Slider, SliderTranslationOptions)
