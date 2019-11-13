# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from .models import Materia, Novedad, RegistroMesaExamen


class NovedadListView(ListView):
	model = Novedad
	template_name = 'novedad/secretaria_novedad_list.html'
	context_object_name = 'novedades'


class NovedadDetailView(DetailView):
	model = Novedad
	template_name = 'novedad/secretaria_novedad_detail.html'
	context_object_name = 'novedad'


class MateriaView(ListView):
	model = Materia
	template_name = 'materia/listado.html'
	context_object_name = 'materias'


class MateriaDetail(DetailView):
	model = Materia
	template_name = 'materia/detalle.html'
	context_object_name = 'materia'


class AlumnoMesaExamenView(ListView):
	model = RegistroMesaExamen
	template_name = 'alumnos_mesas_examen/listado_alumnos.html'
	context_object_name = 'alumnos_registrados'
