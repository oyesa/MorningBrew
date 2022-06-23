from unicodedata import name
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
# phone number,category
class Service(models.Model):
    name = models.CharField(max_length=150)
    image = CloudinaryField('image',null=True)
    description = models.TextField()
    category = models.CharField(max_length=100,default='category')
    phone_number = models.IntegerField(default=0, null=True, blank=True)


    def save_service(self):
        self.save()

    def __str__(self):
        return self.name  

class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()

    def save_comment(self):
        self.save()

    def __str__(self):
        return self.comment

  
