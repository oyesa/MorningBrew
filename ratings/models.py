from django.db import models

# Create your models here.
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
    # service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='ratings', null=True)
    skills = models.IntegerField(choices=ratings, default=0, blank=True)
    time = models.IntegerField(choices=ratings, blank=True, default=0)
    affordability = models.IntegerField(choices=ratings, blank=True,default=0)
    overall_score = models.FloatField(default=0, blank=True)
    skills_avr = models.FloatField(default=0, blank=True)
    time_avr = models.FloatField(default=0, blank=True)
    affordability_avr = models.FloatField(default=0, blank=True)

    def save_ratings(self):
        self.save()

    def __str__(self):
        return f'{self.service} Ratings'

    @classmethod
    def get_ratings(cls, id):
        # ratings = Ratings.objects.filter(service_id=id).all()
        return ratings

