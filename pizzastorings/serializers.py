from rest_framework import serializers
from .models import Pizza


class PizzaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = "__all__"
