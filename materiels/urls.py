from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('materiel/<int:id>/', views.view_materiel, name='view_materiel'),
  path('add/', views.add, name='add'),
  path('edit/<int:id>/', views.edit, name='edit'),
  path('delete/<int:id>/', views.delete, name='delete'),
  path('bon/', views.bon, name='bon'),  # Ajoutez cette ligne
  path('panne/', views.panne, name='panne'), 
  path('diagnostique/', views.diagnostique, name='diagnostique'), 
]
