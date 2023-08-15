from django.contrib import admin
from django.urls import path,include

from .views import index, UserViewSet

from rest_framework import routers

router = routers.DefaultRouter('')
router.register(r'users', UserViewSet,basename="user")
urlpatterns = [
    path('', include(router.urls)),
]
