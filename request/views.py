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

    @action(detail=True, methods=['delete'])
    def custom_delete(self, request):
        if 'platform_id' not in request.data:
            return response.Response(_("Bad request"), status=400)

        platform_id = request.data['platform_id']
        p = Platform.objects.filter(name=platform_id)
        if p.count():
            p[0].delete()
            return response.Response(_("Platform deleted successfully"), status=200)
        else:
            return response.Response(_("Platform not found"), status=404)


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = models.Resource.objects.filter(active=True)
    serializer_class = serializers.ResourceSerializer


class ConfigViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Config.objects.all()
    serializer_class = serializers.ConfigSerializer


class ManifestViewSet(viewsets.ModelViewSet):
    queryset = models.Manifest.objects.filter(active=True)
    serializer_class = serializers.ManifestSerializer
