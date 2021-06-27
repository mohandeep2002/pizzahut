from rest_framework import serializers
from pizzastorings.models import Pizza

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = (
            'id',
            'pizzatype',
            'pizzastyle',
            'ontoppings'
        )