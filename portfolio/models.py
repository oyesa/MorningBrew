from django.db import models

# Create your models here.
class Portfolio(models.Model):
    artisan = models.CharField(max_length=200, blank=True,null=True)
    phone_no = models.IntegerField(blank=True)
    description = models.TextField(blank=True, max_length=300)

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
