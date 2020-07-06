from rest_framework import serializers
from .models import *


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id', 'name', 'active']


class ResourceSerializer(serializers.ModelSerializer):
    platform = PlatformSerializer()

    class Meta:
        model = Resource
        fields = ['id', 'name', 'platform', 'active']


class ConfigSerializer(serializers.ModelSerializer):
    reousrces = ResourceSerializer(many=True)
    platforms = PlatformSerializer(many=True)

    class Meta:
        model = Config
        fields = ['name', 'platforms', 'reousrces']


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id', 'name', 'active']


class ManifestSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True)
    total_crawled_records = serializers.SerializerMethodField()
    total_delivered_records = serializers.SerializerMethodField()

    class Meta:
        model = Manifest
        fields = ['id', 'keywords', 'resources', 'active', 'total_crawled_records', 'total_delivered_records']

    def get_total_crawled_records(self, obj):
        return obj.total_crawled_records()

    def get_total_delivered_records(self, obj):
        return obj.total_delivered_records()
