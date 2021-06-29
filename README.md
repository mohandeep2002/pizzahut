# Django REST framework

# Overview
Django REST framework is a powerful and flexible toolkit for building Web API's.

## **ALL API's**

1. Overview of the created API
	
	```
	@api_view(['GET'])
	def apiOverview(request):
		api_urls = {
			'Pizzalist': '/pizza-list/',
			'Detail View': '/pizza-detail/<int:pk>/',
			'Create': '/pizza-create/',
			'Update': '/pizza-update/<int:pk>/',
			'Delete': '/pizza-delete/<int:pk>/',
		}
		return Response(api_urls)
	```

	![image](https://user-images.githubusercontent.com/63908290/123760234-482a4080-d8de-11eb-8037-cc2b95151dd8.png)
	
2. Creating a pizza order api
		
	```
	@api_view(['POST'])
	def createpizza(request):
		serializer = PizzaSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)
	```

	![image](https://user-images.githubusercontent.com/63908290/123760614-a8b97d80-d8de-11eb-8a74-f8f447c6acca.png)


3. Getting a single pizza order detail api
	```
	@api_view(['GET'])
	def pizzadetail(request, id):
		pizza = Pizza.objects.get(id=id)
		serailzer = PizzaSerializers(pizza, many=False)
		return Response(serailzer.data)
	```
	
	
	![image](https://user-images.githubusercontent.com/63908290/123765193-24b5c480-d8e3-11eb-96ff-22ba9fa046ad.png)




4. Updating a pizza order api
	```
	@api_view(['POST'])
	def updatepizza(request, id):
		pizza = Pizza.objects.get(id=id)
		serializer = PizzaSerializers(instance=pizza, data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response("Updated successfully")
	```
	
	![image](https://user-images.githubusercontent.com/63908290/123765300-3e570c00-d8e3-11eb-8c8d-d72073778a5e.png)



5. Deleting a pizza order api
	```
	@api_view(['DELETE'])
	def deletepizza(request, id):
		pizza = Pizza.objects.get(id=id)
		pizza.delete()
		return Response("Deleted successfully")
	```
	
	
	![image](https://user-images.githubusercontent.com/63908290/123765396-5464cc80-d8e3-11eb-9f8c-fcbb64911bb8.png)



6. Displaying all the pizza orders api
	```
	@api_view(['GET'])
	def pizzalist(request):
		pizzas = Pizza.objects.all()
		serializer = PizzaSerializers(pizzas, many=True)
		return Response(serializer.data)
	```
	
	![image](https://user-images.githubusercontent.com/63908290/123765614-85dd9800-d8e3-11eb-9516-fd63833f1e61.png)

# Serializers and Models

- serializers.py


	```
	from rest_framework import serializers
	from .models import Pizza
	
	class PizzaSerializers(serializers.ModelSerializer):
		class Meta:
		model = Pizza
		fields = "__all__"

	```

- models.py

	
	```
	from django.db import models
	
	class Pizza(models.Model):
		type = models.CharField(max_length=20, blank=False, verbose_name="Type of Pizza", default=" ")
		sizes = models.CharField(max_length=50, blank=False, verbose_name="Size of Pizza", default=" ")
		toppings = models.CharField(max_length=200, blank=False, verbose_name="Toppings", default=" ")
	```


# Steps to run this project

* clone or download the project from <a href="https://github.com/mohandeep2002/pizzahut">here</a>
* after downloading the zip file, unzip the project and open in your code editor.
* Now, Create a virtual environment.

	```
	python -m venv venv
	```	
	
* Now run the following commands to run this project
	```
	.\venv\scritps\activate  
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver
	```

* Note:
	```
	This Project will open in http://127.0.0.1:8000/ and not in http://localhost:8000/
	Because of CORS is disabled.
	MongoDB should be installed in your system.
	```
	

### Given tasks
  - Completed Taks
    - [x] A Pizza can be of multiple types: Regular or Square
    - [x] A Pizza can be of multiple sizes: Small, Medium, Large, etc. 
    - [x] A Pizza can consist of many toppings out of the following (Onion, Tomato, Corn, Capsicum, Cheese, Jalapeno etc.), the choice of toppings should not be limited to the ones 
	  mentioned above, the user should be allowed to add any type of topping at any point of time)
  - Want to do
    - API
      - [x] Create an API endpoint to create regular pizza and a square pizza.
      - [x] Create an API endpoint which lists the information about all the stored pizza, the response of this should also contain the information about the toppings, size and type of Pizza.
      - [ ] Allow filtering the list of pizza returned by the API based on Size & Type of Pizza.
      - [x] Create an API endpoint that allows the user to edit or delete any pizza from the database.


