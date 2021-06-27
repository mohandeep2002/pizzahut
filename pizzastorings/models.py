from django.db import models

# Create your models here.
class Pizza(models.Model):
    type = models.CharField(max_length=20, blank=False, verbose_name="Type of Pizza", default=" ")
    sizes = models.CharField(max_length=50, blank=False, verbose_name="Size of Pizza", default=" ")
    toppings = models.CharField(max_length=200, blank=False, verbose_name="Toppings", default=" ")

