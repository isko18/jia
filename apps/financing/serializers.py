from rest_framework import serializers
from .models import Financing, Image, Reach, Sector, LegalName, NameInfo, ImageForm

class FinancingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financing
        fields = ['id', 'title', 'image']
        
class NameInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameInfo
        fields = ['id', 'title', 'descriptions']

class ImageFormSerializer(serializers.ModelSerializer):
    name_infos = NameInfoSerializer(many=True, read_only=True)

    class Meta:
        model = ImageForm
        fields = ['id', 'image', 'name_infos']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financing
        fields = ['id', 'image']

class ReachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reach
        fields = ['id', 'full_name', 'name_company', 'legal_name', 'brief_description', 'sector']

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['id', 'name']

class LegalNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalName
        fields = ['id', 'name']
