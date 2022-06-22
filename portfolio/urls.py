from django.urls import path,include
from . import views
from django.conf.urls.static import static
from .views import *
from django.conf import settings
from rest_framework import routers


router = routers.DefaultRouter()
router.register('portfolios', views.PortfolioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)