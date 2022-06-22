from django.contrib import admin
from .models import Incidences
from leaflet.admin import LeafletGeoAdmin


#ADMIN=MorningBrew 
#Password=SEMBERUA
# email:kevin.kipkemoi@student.moringaschool.com 
# Register your models here.
class IncidencesAdmin(LeafletGeoAdmin):
    list_display=('name', 'location')


admin.site.register(Incidences, IncidencesAdmin)
