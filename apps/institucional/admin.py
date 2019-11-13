from django.contrib import admin
from .models import (
	Profesor, Asignatura, Seguimiento 
)


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
	list_display = ['dni', 'nombre', 'apellido']
	list_filter = ['dni', 'nombre']
	search_fields = ['nombre__icontains', 'apellido', 'dni']

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
	list_display = ['codigo', 'nombre', 'año']
	list_filter = ['codigo']
	search_fields = ['nombre__icontains', 'codigo', 'año', 'nombre']


@admin.register(Seguimiento)
class SeguimientoAdmin(admin.ModelAdmin):
	list_display = ['fecha', 'profesor', 'get_turnos_turno', 'curso', 'division', 'get_nombre_asignatura', 'get_año_asignatura', 'get_codigo_asignatura', 'ausente', 'tarde']
	search_fields = ['asignatura__nombre__contains', 'profesor__dni__contains', 'fecha__icontains']


	def get_turnos_turno(self, obj):
		return obj.turno
	get_turnos_turno.short_description = 'tipo de turno'

	def get_codigo_asignatura(self, obj):
		return obj.asignatura.codigo
	get_codigo_asignatura.short_description = 'Código de la  Asignatura'

	def get_nombre_asignatura(self, obj):
		return obj.asignatura.nombre
	get_nombre_asignatura.short_description = 'nombre de la  Asignatura'

	def get_año_asignatura(self, obj):
		return obj.asignatura.codigo
	get_año_asignatura.short_description = 'año de la  Asignatura'
