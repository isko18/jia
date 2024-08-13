from rest_framework import serializers
from .models import About, AboutBanner, History, HistoryDetail, Statistics, Gallery, GalleryTitle

class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class AboutBannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutBanner
        fields = '__all__'

class HistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class HistoryDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = HistoryDetail
        fields = '__all__'

class StatisticsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'
        
class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
        
class GalleryTitleSerializers(serializers.ModelSerializer):
    class Meta:
        model = GalleryTitle
        fields = '__all__'