
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('portfolio.urls')),
    path('',include('ratings.urls')),
    path('', include('authapp.urls')),
    path('', include('profiles.urls'))

]
