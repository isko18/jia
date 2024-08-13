# apps/base/translation.py
from modeltranslation.translator import translator, TranslationOptions
from apps.base.models import Slider, SliderTitle, WhatWill, Video, Banner, What_will_title, About_the_forum, SliderTitleSponsors, Button

class WhatWillTranslationOptions(TranslationOptions):
    fields = ('title',)
    
class ButtonTranslationOptions(TranslationOptions):
    fields = ('title', )
    
class SliderTitleTranslationOptions(TranslationOptions):
    fields = ('title', )

class SliderTitleSponsorsTranslationOptions(TranslationOptions):
    fields = ('title', )

class VideoTranslationOptions(TranslationOptions):
    fields = ('url', 'title', 'descriptions')
    
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')


class What_will_titleTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')
    

class About_the_forumTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')

translator.register(Button, ButtonTranslationOptions)
translator.register(SliderTitle, SliderTitleTranslationOptions)
translator.register(SliderTitleSponsors, SliderTitleSponsorsTranslationOptions)
translator.register(WhatWill, WhatWillTranslationOptions)
translator.register(Video, VideoTranslationOptions)
translator.register(Banner, BannerTranslationOptions)
translator.register(What_will_title, What_will_titleTranslationOptions)
translator.register(About_the_forum, About_the_forumTranslationOptions)



print("Translation options registered")  # Debug statement
