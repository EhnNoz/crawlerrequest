from django.shortcuts import render
from rest_framework import viewsets, views, mixins
from django import views
from request.serializers import RequestSerializer
from .models import Request

# Create your views here.



class RequestViewSet(viewsets.ModelViewSet):

#class PlatformViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
