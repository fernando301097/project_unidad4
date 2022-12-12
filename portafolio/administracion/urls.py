from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.AdministracionView.as_view(), name='index'),

    path('create/', views.CreateProyecto.as_view(), name="create"),

    path('delete/<int:id>', views.deleteProyecto, name="delete"),
   
]