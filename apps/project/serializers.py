from rest_framework import serializers
from .models import Project, YearlyCatalog, Scroll, BusinessProject

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'descriptons']

class YearlyCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearlyCatalog
        fields = ['id', 'year', 'image']

class ScrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scroll
        fields = ['id', 'title', 'image']

class BusinessProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProject
        fields = ['id', 'title', 'descriptons', 'scroll']
