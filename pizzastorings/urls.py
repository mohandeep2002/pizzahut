from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="apioverview"),
    path('pizza-list/', views.pizzalist, name="pizzalist"),
    path('pizza-create/', views.createpizza, name="createpizza"),
    path('pizza-update/<int:id>/', views.updatepizza, name="updatepizza"),
    path('pizza-delete/<int:id>/', views.deletepizza, name="deletepizza"),
    path('pizza-detail/<int:id>', views.pizzadetail, name="detailview")
]