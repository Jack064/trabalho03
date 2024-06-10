from django.contrib import admin
from django.urls import path, include
from .views import home, cadastro, salvar, editar, update, apagar
urlpatterns = [
    path('', home),
    path('cadastro.html', cadastro),
    path('salvar/', salvar, name = "salvar"),
    path('editar/<int:id>', editar, name = "editar"),
    path('update/<int:id>', update, name = "update"),
    path('apagar/<int:id>', apagar, name = "apagar")
]