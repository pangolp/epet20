from django.urls import path
from .views import (
	NovedadListView, MateriaView,
	MateriaDetail, AlumnoMesaExamenView
)

app_name = 'secretaria'
urlpatterns = [
	path('', NovedadListView.as_view(), name='novedades'),
	path('materias/', MateriaView.as_view(), name='materia_listado'),
	path('materia/detalle/<int:pk>/', MateriaDetail.as_view(), name='materia_detalle'),
	path('mesa-de-examen/listado-alumnos/', AlumnoMesaExamenView.as_view(), name='mesa_examen_listado_alumnos'),
]
