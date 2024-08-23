from rest_framework import serializers
from .models import Exhibition, Slider, RentStand

class ExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibition
        fields = ['id', 'title', 'descriptions']

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'image', 'image_2']


class RentStandSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentStand
        fields = '__all__'