from django.contrib import admin
from .models import Incidences


#ADMIN=MorningBrew 
#Password=SEMBERUA
# email:kevin.kipkemoi@student.moringaschool.com 
# Register your models here.
class IncidencesAdmin(admin.ModelAdmin):
    list_display=('name', 'location')


admin.site.register(Incidences, IncidencesAdmin)
