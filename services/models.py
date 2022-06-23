from django.utils import timezone
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

# class Comment(models.Model):
#     # portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=100)
#     comment = models.TextField()
#     created_at = models.DateTimeField(default=timezone.now)

#     def save_comment(self):
#         self.save()

#     def __str__(self):
#         return self.comment

class Ratings(models.Model):
    ratings=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10',)
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='ratings', null=True)
    skills = models.IntegerField(choices=ratings, default=0, blank=True)
    time = models.IntegerField(choices=ratings, blank=True, default=0)
    affordability = models.IntegerField(choices=ratings, blank=True,default=0)
    
    def save_ratings(self):
        self.save()
    def __str__(self):
        return f'{self.service} Ratings'
    @classmethod
    def get_ratings(cls, id):
        ratings = Ratings.objects.filter(service_id=id).all()
        return ratings

  
