from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Incidences(models.Model):
  name = models.CharField(max_length=20)
  location= models.CharField(max_length=20)

  def __unicode__(self):
    return self.name
   
  class Meta:
    verbose_name_plural="Incidences"
