from django.shortcuts import render, redirect
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework import viewsets
from apps.base.serializers import BaseSerializers, WhatWillSerializers, SliderSerializers,SliderTitleSerializers, VideoSerializers, BannerSerializers, What_will_titleSerializers, About_the_forumSerializers, SliderTitleSponsorsSerializers, SliderSponsorsSerializers, ButtonSerializer
from apps.base.models import Base, WhatWill, Slider, Video, Banner, About_the_forum, What_will_title, SliderTitle, SliderTitleSponsors, SliderSponsors, Button

# Create your views here.

def index(request, path='index'):
    # Ваш код здесь
    # if request:
    #     return redirect("https://biforum.kg/")
    return render(request, 'index.html')

class BaseMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = Base.objects.all()
    serializer_class = BaseSerializers
    
class ButtonMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = Button.objects.all()
    serializer_class = ButtonSerializer
    
class BannerMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = Banner.objects.all()
    serializer_class = BannerSerializers
    
class What_willMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = WhatWill.objects.all()
    serializer_class = WhatWillSerializers


class SliderMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = Slider.objects.all()
    serializer_class = SliderSerializers
    
class SliderTitleMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = SliderTitle.objects.all()
    serializer_class = SliderTitleSerializers
    
class VideoMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
  
class What_will_titleMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = What_will_title.objects.all()
    serializer_class = What_will_titleSerializers
    
class About_the_forumMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = About_the_forum.objects.all()
    serializer_class = About_the_forumSerializers  
    
    
class SliderSponsorsMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = SliderSponsors.objects.all()
    serializer_class = SliderSponsorsSerializers
    
class SliderTitleSponsorsMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = SliderTitleSponsors.objects.all()
    serializer_class = SliderTitleSponsorsSerializers


