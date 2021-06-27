# PizzaStoreDjangoProject

### This is a Django Project with REST API (want to implement)
### Prerequisites - Python and MongoDB should be installed in system 

## Steps to run this project
  - Download or clone the project
  - After downloading the project open the project in your code editor
  - Now create the virtual environment
    - ```python -m venv venv```
    - ```.\venv\scripts\activate```
  - Now with the help of requirements.txt file Install the required libraries 
  - the run the following commands
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
      - [ ] Create an API endpoint to create regular pizza and a square pizza.
      - [ ] Create an API endpoint which lists the information about all the stored pizza, the response of this should also contain the information about the toppings, size and type of Pizza.
      - [ ] Allow filtering the list of pizza returned by the API based on Size & Type of Pizza.
      - [ ] Create an API endpoint that allows the user to edit or delete any pizza from the database. an API 