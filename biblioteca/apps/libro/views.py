from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor, Libro
from django.views.generic import TemplateView, ListView


class Inicio(TemplateView):
    template_name = 'index.html'


def crear_autor(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        nacionalidad = request.POST['nacionalidad']
        descripcion = request.POST['descripcion']
        
        autor = Autor.objects.create(
            nombre=nombre,
            apellidos=apellidos,
            nacionalidad=nacionalidad,
            descripcion=descripcion
        )
        return redirect('libro:listar_autor')
    
    return render(request, 'libro/crear_autor.html')


class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/listar_autor.html'
    queryset = Autor.objects.filter(estado=True).order_by('id')
    context_object_name = 'autores'
    
    
def editar_autor(request, id):
    autor_form = None
    error = None
    
    try:
        autor = Autor.objects.get(id=id)
        
        if request.method == 'POST':
            autor_form = AutorForm(
                request.POST, 
                instance=autor
            )
            
            if autor_form.is_valid():
                autor_form.save()
                return redirect('index')
        else:
            autor_form = AutorForm(instance=autor)
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request, 'libro/crear_autor.html', {
        'autor_form': autor_form, 
        'error': error
    })
    
    
def eliminar_autor(request, id):
    autor = Autor.objects.get(id=id)
    
    if request.method == 'POST':
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')
        
    
    return render(request, 'libro/eliminar_autor.html', {
        'autor': autor
    })