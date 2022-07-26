from django.contrib import admin
from django.urls import path, include
from apps.libro.views import Inicio


urlpatterns = [
    path('admin/', admin.site.urls),
    path('libro/', include(('apps.libro.urls', 'libro'))),
    path('home/', Inicio.as_view(), name='index')
]
