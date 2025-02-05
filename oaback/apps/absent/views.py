from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Absent, AbsentType, AbsentStatusChoices

class AbsentViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = AbsentType.objects.all()
    serializer_class = None
