from django.contrib import admin
from .models import Categoria, Novedad, Asesora, Horario


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


@admin.register(Asesora)
class AsesoraAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellido', 'email')


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
	list_display = ('asesora', 'dia', 'horario_inicio', 'horario_fin')
	list_filter = ('asesora', 'dia', 'horario_inicio', 'horario_fin')
	