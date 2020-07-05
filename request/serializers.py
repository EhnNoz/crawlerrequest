from rest_framework import serializers
from .models import *


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id', 'name','active']


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name', 'platform', 'active']


class ManifestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manifest
        fields = ['id', 'keywords', 'resources','active']
