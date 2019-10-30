from django.contrib import admin
from .models import Categoria, Novedad


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
