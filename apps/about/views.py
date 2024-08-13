from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework import viewsets
from apps.about.serializers import AboutBannerSerializers, AboutSerializers, HistorySerializers, HistoryDetailSerializers, StatisticsSerializers, GallerySerializers, GalleryTitleSerializers
from apps.about.models import About, AboutBanner, History, HistoryDetail, Statistics, Gallery, GalleryTitle

# Create your views here.
class AboutMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = About.objects.all()
    serializer_class = AboutSerializers
    
class AboutBannerMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = AboutBanner.objects.all()
    serializer_class = AboutBannerSerializers
    
class HistoryMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = History.objects.all()
    serializer_class = HistorySerializers
    
class HistoryDetailMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = HistoryDetail.objects.all()
    serializer_class = HistoryDetailSerializers
    
class StatisticsMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializers
    
class GalleryMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers
    
class GalleryTitleMixins(CreateModelMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 DestroyModelMixin,
                 viewsets.GenericViewSet):
    
    queryset = GalleryTitle.objects.all()
    serializer_class = GalleryTitleSerializers