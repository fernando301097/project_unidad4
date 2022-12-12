from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, FormView

class CvView(TemplateView):
    template_name = "home/index.html"
    
