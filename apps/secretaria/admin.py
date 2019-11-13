# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Materia, Categoria, Novedad, RegistroMesaExamen


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Novedad)
class NovedadAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'user', 'fecha_alta', 'fecha_modificado')
	list_filter = ('user', 'fecha_alta', 'fecha_modificado')

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):

	list_display = [
		'id', 'nombre','año',
		'fecha_hora', 'aula', 'profesores'
	]

	list_filter = ['nombre', 'año', 'aula']

	search_fields = ['nombre__icontains', 'año']


@admin.register(RegistroMesaExamen)
class RegistroMesaExamenAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'apellido', 'dni', 'get_nombre_materia','get_año_materia', 'correo_electronico']
	list_filter = ['materia__nombre', 'materia__año']
	search_fields = ['dni']

	def get_nombre_materia(self, obj):
		return obj.materia.nombre
	get_nombre_materia.short_description = 'Nombre de la materia'

	def get_año_materia(self, obj):
		return obj.materia.año
	get_año_materia.short_description = 'Año de la materia'
