from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('service',ServiceViewSet)

urlpatterns = [
    path('api/service/',views.ServiceList.as_view()),
    path('add/',include(router.urls))
]


