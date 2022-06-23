from django import urls
from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path,include
from . import views

router = DefaultRouter()
router.register('service',ServiceViewSet)
router.register('ratings',RatingsViewSet)

urlpatterns = [
    # path('api/service/',views.ServiceList.as_view()),
    path('api/',include(router.urls)),
    path('api/',include(router.urls)),
    path('api/service/<int:pk>', views.showservice, name='service'),
]


