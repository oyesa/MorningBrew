from .views import *
from django.urls import path

urlpatterns = [
  
  path('profiles/<str:username>/', UserProfileView.as_view(), name='profile'),
  path('profiles/update/<str:username>/',UpdateUserProfileView.as_view(), name='update_profile'),
  path('profiles/', UserListView.as_view(), name='list_users'),

]