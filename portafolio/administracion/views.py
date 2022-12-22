from django.shortcuts import render, redirect
from .models import Proyecto
from django.views.generic import View, TemplateView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProyectoForm
from django.contrib.auth.decorators import login_required

class AdministracionView(LoginRequiredMixin, TemplateView):
    template_name = "administracion/index.html"
    extra_context = {"proyectos": Proyecto.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["proyectos"] = Proyecto.objects.all()
        return context


class CreateProyecto(LoginRequiredMixin, FormView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "administracion/create.html"
    

    def form_valid(self, form):
        Proyecto.objects.create(**form.cleaned_data)
        return redirect('index')

@login_required
def deleteProyecto(request, id):
    project = Proyecto.objects.get(id=id)
    project.delete()
    return redirect("index")
    



