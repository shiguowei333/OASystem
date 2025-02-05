from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Absent, AbsentType, AbsentStatusChoices
from .serializers import AbsentSerializer

class AbsentViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Absent.objects.all()
    serializer_class = AbsentSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
