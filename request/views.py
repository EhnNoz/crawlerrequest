from rest_framework import viewsets, views, mixins
from django import views
from request.serializers import ManifestSerializer, PlatformSerializer, ResourceSerializer
from .models import Platform, Resource, Manifest

# Create your views here.


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ManifestViewSet(viewsets.ModelViewSet):
    queryset = Manifest.objects.all()
    serializer_class = ManifestSerializer
