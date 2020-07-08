from . import models
from request import serializers
from rest_framework import response
from request.models import Platform
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework import authentication, permissions
from django.utils.translation import ugettext_lazy as _


# Create your views here.


class PlatformViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = models.Platform.objects.filter(active=True)
    serializer_class = serializers.PlatformSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]



class ResourceViewSet(viewsets.ModelViewSet):
    queryset = models.Resource.objects.filter(active=True)
    serializer_class = serializers.ResourceSerializer


class ConfigViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Config.objects.all()
    serializer_class = serializers.ConfigSerializer


class ManifestViewSet(viewsets.ModelViewSet):
    queryset = models.Manifest.objects.filter(active=True)
    serializer_class = serializers.ManifestSerializer
