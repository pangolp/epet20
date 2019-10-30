from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('asesoria/', include('apps.asesoria.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
