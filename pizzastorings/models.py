from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Pizza(models.Model):
    types = (
        ('Regular', 'Regular'),
        ('Square', 'Square')
    )
    toppings =(
        ('Onion', 'Onion'),
        ('Tomato', 'Tomato'),
        ('Corn', 'Corn'),
        ('Capsicum', 'Capsicum'),
        ('Cheese', 'Cheese'),
        ('Jalapeno', 'Jalapeno')
    )
    sizes = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large')
    )
    pizzatype = models.CharField(max_length=10, choices=types, verbose_name="Pizza Type")
    pizzasize = models.CharField(max_length=10, choices=sizes, verbose_name="Size of Pizza")
    #ontoppings = models.CharField(max_length=20, choices=toppings, verbose_name="Toppings")
    ontoppings = MultiSelectField(choices=toppings)