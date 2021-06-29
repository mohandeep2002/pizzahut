import json

from django.shortcuts import render

from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from .models import Pizza
from .serializers import PizzaSerializers
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Pizzalist': '/pizza-list/',
        'Detail View': '/pizza-detail/<int:pk>/',
        'Create': '/pizza-create/',
        'Update': '/pizza-update/<int:pk>/',
        'Delete': '/pizza-delete/<int:pk>/',
        'Detail': '/pizza-detail/<int:id>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def pizzalist(request):
    pizzas = Pizza.objects.all()
    serializer = PizzaSerializers(pizzas, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createpizza(request):
    serializer = PizzaSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updatepizza(request, id):
    pizza = Pizza.objects.get(id=id)
    serializer = PizzaSerializers(instance=pizza, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Updated successfully")

@api_view(['DELETE'])
def deletepizza(request, id):
    pizza = Pizza.objects.get(id=id)
    pizza.delete()
    return Response("Deleted successfully")

@api_view(['GET'])
def pizzadetail(request, id):
    pizza = Pizza.objects.get(id=id)
    serailzer = PizzaSerializers(pizza, many=False)
    return Response(serailzer.data)