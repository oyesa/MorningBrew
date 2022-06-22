from django.db import models

# Create your models here.
class Portfolio(models.Model):
    artisan = models.CharField(max_length=200, blank=True,null=True)
    phone_no = models.IntegerField(blank=True)
    description = models.TextField(blank=True, max_length=300)
