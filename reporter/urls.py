from django.urls import re_path
from views import HomePageView, county_datasets,point_datasets

urlpatterns = [
	re_path(r'^$', HomePageView.as_view(), name = 'home'),
	re_path(r'^county_data/$', county_datasets, name = 'county'),
	re_path(r'^incidence_data/$', point_datasets, name = 'incidences'),
]