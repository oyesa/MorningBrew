from django.urls import path,include
from .views import *
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('ratings', views.RatingsViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    
]