from django.db import models
from django.utils import timezone


# Create your models here.
class Portfolio(models.Model):
    artisan = models.CharField(max_length=200, blank=True,null=True)
    phone_no = models.IntegerField(blank=True)
    description = models.TextField(blank=True, max_length=300)
    image=models.ImageField(upload_to = 'images/', default='no image')


    def __str__(self):
        return self.artisan

    def create_portfolio(self):
        """
        A method that creates a portfolio
        """
        self.save()

    @classmethod
    def find_portfolio(cls, portfolio_id):
        """
        A method that finds a neighbourhood using its id
        """

         
        portfolios=Portfolio.objects.filter(id=portfolio_id) 
        return portfolios

class Comment(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)

    def save_comment(self):
        self.save()

    def __str__(self):
        return self.comment