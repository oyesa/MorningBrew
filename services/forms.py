from django import forms
from .models import *

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = ['skills', 'time', 'affordability']