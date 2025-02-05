from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import AbsentTypeViewSet

app_name = 'absent'

router = DefaultRouter(trailing_slash=False)

router.register('absent', views.AbsentViewSet, basename='absent')

urlpatterns = [
                  path('type', AbsentTypeViewSet.as_view(), name='absenttypes'),
                  path('responder', views.ResponderView.as_view(), name='responder'),
              ] + router.urls