
from django.urls import path
from .views import index, success, display, delete, update, cancelupdate, successupdate

urlpatterns = [
    path('', index, name="index"),
    path('success/', success, name="success"),
    path('display/', display, name="display"),
    path('delete/<int:id>', delete, name="delete"),
    path('update/<int:id>', update, name="update"),
    path('cancelUpdate/', cancelupdate, name="cancelupdate"),
    path('successupdate/', successupdate, name="successupdate")

]
