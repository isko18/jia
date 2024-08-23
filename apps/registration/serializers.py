from rest_framework import serializers
from .models import Registration, Standart, Vip, SectorStandart, ReachStandart, SectorVip, ReachVip

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'title', 'descriptions']

class StandartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standart
        fields = ['id', 'title', 'descriptions']

class VipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vip
        fields = ['id', 'title', 'descriptions']

class SectorStandartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorStandart
        fields = ['id', 'name']

class ReachStandartSerializer(serializers.ModelSerializer):
    sector = serializers.CharField(source='sector.name')

    class Meta:
        model = ReachStandart
        fields = ['id', 'full_name', 'name_company', 'sector', 'current', 'email', 'phone']

    def create(self, validated_data):
        sector_name = validated_data.pop('sector')['name']
        sector, created = SectorStandart.objects.get_or_create(name=sector_name)
        validated_data['sector'] = sector
        return ReachStandart.objects.create(**validated_data)

    def update(self, instance, validated_data):
        sector_name = validated_data.pop('sector')['name']
        sector, created = SectorStandart.objects.get_or_create(name=sector_name)
        instance.sector = sector

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

class SectorVipSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorVip
        fields = ['id', 'name']

class ReachVipSerializer(serializers.ModelSerializer):
    sector = serializers.CharField(source='sector.name')

    class Meta:
        model = ReachVip
        fields = ['id', 'full_name', 'name_company', 'sector', 'current', 'email', 'phone']

    def create(self, validated_data):
        sector_name = validated_data.pop('sector')['name']
        sector, created = SectorVip.objects.get_or_create(name=sector_name)
        validated_data['sector'] = sector
        return ReachVip.objects.create(**validated_data)

    def update(self, instance, validated_data):
        sector_name = validated_data.pop('sector')['name']
        sector, created = SectorVip.objects.get_or_create(name=sector_name)
        instance.sector = sector

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
