from django.urls import path
from .views import crear_autor, editar_autor, eliminar_autor, ListadoAutor, ActualizarAutor, CrearAutor


urlpatterns = [
    path('crear_autor/', CrearAutor.as_view(), name='crear_autor'),
    path('listar_autor/', ListadoAutor.as_view(), name='listar_autor'),
    path('editar_autor/<int:pk>/', ActualizarAutor.as_view(), name='editar_autor'),
    path('eliminar_autor/<int:id>/', eliminar_autor, name='eliminar_autor')
]
