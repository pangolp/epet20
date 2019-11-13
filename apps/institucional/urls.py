from django.urls import path
from .views import (
	IndexView,
	SeguimientoDetail,
)

app_name = 'autoridades'
urlpatterns = [
	path('', IndexView.as_view(), name='index'),
    path('seguimiento/detalle/<int:pk>', SeguimientoDetail.as_view(), name='detalle'),
]
