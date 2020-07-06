from rest_framework import viewsets, views, mixins
from django import views
from request import serializers
from . import models


# Create your views here.


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = models.Platform.objects.filter(active=True)
    serializer_class = serializers.PlatformSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = models.Resource.objects.filter(active=True)
    serializer_class = serializers.ResourceSerializer


class ConfigViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Config.objects.all()
    serializer_class = serializers.ConfigSerializer


class ManifestViewSet(viewsets.ModelViewSet):
    queryset = models.Manifest.objects.filter(active=True)
    serializer_class = serializers.ManifestSerializer
