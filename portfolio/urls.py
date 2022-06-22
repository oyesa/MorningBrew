from django.urls import path
from . import views
from django.conf.urls.static import static
from .views import *
from django.conf import settings
from rest_framework import routers


router = routers.DefaultRouter()
router.register('portfolios', views.PortolioViewSet)

urlpatterns = [
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)