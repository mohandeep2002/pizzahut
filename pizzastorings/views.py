from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PizzaForm
from .models import Pizza
from django.contrib import messages
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from pizzastorings.serializers import PizzaSerializer
# Create your views here.

def success(request):
    return render(request, 'success.html')

def display(request):
    data = Pizza.objects.all()
    count = Pizza.objects.all().count()
    return render(request, 'display.html', {'data':data,'count': count})

def delete(request, id):
    Pizza.objects.filter(id=id).delete()
    messages.warning(request, "Order Deleted!!!! ID " + str(id))
    return redirect(display)

def update(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Pizza, id=id)
        form = PizzaForm(request.POST or None, instance= obj)
        if form.is_valid():
            obj = form.save(commit=False)
            #form.save()
            obj.save()
            return redirect(successupdate)
        else:
            return HttpResponse("Not stored")
    else:
        form = PizzaForm()
        #return render(request, 'index.html', {'form':form})
        data = Pizza.objects.filter(id=id)
        return render(request, 'update.html', {'data':data, 'form':form})

def index(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success)
        else:
            return HttpResponse("Not stored")
    else:
        form = PizzaForm()
    return render(request, 'index.html', {'form':form})

def cancelupdate(request):
    return render(request, 'cancelupdate.html')

def successupdate(request):
    return render(request, 'successupdate.html')
