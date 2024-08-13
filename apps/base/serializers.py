from rest_framework import serializers
from apps.base.models import Base, WhatWill, Slider, SliderTitle, Video, Banner, About_the_forum, What_will_title, SliderSponsors, SliderTitleSponsors, Button

class BaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ('id', 'logo', 'logo_2')
        
class WhatWillSerializers(serializers.ModelSerializer):
    class Meta:
        model = WhatWill
        fields = ('id', 'title', 'image')


class SliderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'image')
        
class SliderTitleSerializers(serializers.ModelSerializer):
    class Meta:
        model = SliderTitle
        fields = ('id', 'title')
        
        
class SliderSponsorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'image')
        
class SliderTitleSponsorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SliderTitle
        fields = ('id', 'title')
        
        
class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'url', 'title', 'descriptions')
        
class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('id', 'title', 'descriptions', 'image')
        
class About_the_forumSerializers(serializers.ModelSerializer):
    class Meta:
        model = About_the_forum
        fields = ('id', 'title', 'descriptions', )
        
class What_will_titleSerializers(serializers.ModelSerializer):
    class Meta:
        model = What_will_title
        fields = ('id', 'title', 'descriptions', )
        
class ButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Button
        fields = ('id', 'title',)
        
        
        
