# PizzaStoreDjangoProject

### This is a Django Project with REST API 
### Prerequisites - Python and MongoDB should be installed in system 

## Steps to run this project
  - Download or clone the project
  - After downloading the project open the project in your code editor
  - Now create the virtual environment
    - ```python -m venv venv```
    - ```.\venv\scripts\activate```
  - Now with the help of requirements.txt file Install the required libraries 
  - the run the following commands
    - ```pip install requirements.txt```
    - ```python manage.py makemigrations```
    - ```python manage.py migrate```
    - ```python manage.py runserver```
    
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


# Note:
    - The django project will run in http://127.0.0.1:8000/ only
    - It will not take the url http://localhost:8000/ 
    
 # API Documentation
 -  "Pizzalist": "/pizza-list/",   For displaying all the pizza orders
 -  "Detail View": "/pizza-detail/<int:pk>/",   For display a particular pizza order
 -  "Create": "/pizza-create/",  To create a new pizza order
 -  "Update": "/pizza-update/<int:pk>/", To update a pizza order
 -  "Delete": "/pizza-delete/<int:pk>/", To delete an order
    
