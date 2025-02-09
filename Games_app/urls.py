from django.urls import path, include
from rest_framework import routers
from . views import GameViewSet
from django.urls import path
from .views import register_view


router = routers.DefaultRouter()
router.register('games', GameViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('register/', register_view, name='register'),









]

