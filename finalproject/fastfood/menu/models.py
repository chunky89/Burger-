from django.db import models

# Create your models here.
class Pizza(models.Model):
    title = models.CharField(max_length=150)
    priceM = models.DecimalField(max_digits=4, decimal_places=2)
    priceL = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.URLField()
    
class Burger(models.Model):
    title = models.CharField(max_length=150)
    priceM = models.DecimalField(max_digits=4, decimal_places=2)
    priceL = models.DecimalField(max_digits=4, decimal_places=2)
    burgerImage = models.URLField()
    