from distutils.command.upload import upload
from unicodedata import category
from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length=50)

    def save_service(self):
        self.save()
