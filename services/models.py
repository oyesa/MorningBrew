from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    artisan_category = models.ForeignKey('Category',on_delete=models.CASCADE,default='')


    def save_service(self):
        self.save()

    def __str__(self):
        return self.name  

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def save_category_name(self):
        self.save()

    def delete_category_name(self):
        self.delete()

    def __str__(self):
        return self.category_name  
