from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Novedad


class NovedadListView(ListView):
	model = Novedad
	template_name = 'novedad/novedad_list.html'
	context_object_name = 'novedades'


class NovedadDetailView(DetailView):
	model = Novedad
	template_name = 'novedad/novedad_detail.html'
	context_object_name = 'novedad'
