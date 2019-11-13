from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Seguimiento


class IndexView(ListView):
	model = Seguimiento
	template_name = 'seguimiento/index.html'
	context_object_name = 'seguimientos'


class SeguimientoDetail(DetailView):
	model = Seguimiento
	template_name = 'seguimiento/detalle.html'
	context_object_name = 'seguimiento'
