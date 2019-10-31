from django.urls import path
from .views import (
	NovedadListView,
	NovedadDetailView,
	AsesoraListView,
)


app_name = 'asesoria'
urlpatterns = [
    path('', NovedadListView.as_view(), name='novedad_index'),
    path('novedad/<slug:slug>/', NovedadDetailView.as_view(), name='novedad_detail'),
    path('asesora/', AsesoraListView.as_view(), name='asesora_index'),
]
