from django.urls import path
from . import views

urlpatterns = [
    path('cv/', views.CvView.as_view(), name='cv'),
   
]