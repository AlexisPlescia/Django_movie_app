from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
#
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from .models import *
from .forms import *

# Create your views here.
class HomeView(TemplateView):
    template_name = "mvapp/home.html"

class GenderList(ListView):
    model = Gender

    def get_queryset(self):
        return Gender.objects.all().order_by('id').values()
        #return Gender.objects.filter(name__icontains='a').filter(name__icontains='i').order_by('id').values()

class CompanyList(ListView):
    model = Company
    #template_name = "mvapp/mis_companias.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = "Lista de Compañías de Películas"
        #contexto['generos'] = Gender.objects.all().values()
        return contexto

class MovieList(ListView):
    model = Movie

class MovieCreate(CreateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('movies')

class MovieUpdate(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
        return reverse_lazy('movie-update', args=[self.object.id])+'?ok'    
    
class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movies')    