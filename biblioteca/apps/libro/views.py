from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from .forms import AutorForm
from .models import Autor, Libro
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy


class Inicio(TemplateView):
    template_name = 'index.html'
    
    
class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/listar_autor.html'
    queryset = Autor.objects.filter(estado=True).order_by('id')
    context_object_name = 'autores'
    
    
class ActualizarAutor(UpdateView):
    model = Autor
    template_name = 'libro/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')
    
    
class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')
    
    
class EliminarAutor(DeleteView):
    model = Autor
    success_url: Optional[str]


def crear_autor(request):
    autor_form = AutorForm()
    
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        
        if autor_form.is_valid():
            print(autor_form.cleaned_data)
            autor_form.save()
        
        return redirect('libro:listar_autor')
    
    return render(request, 'libro/crear_autor.html', {
        'autor_form': autor_form
    })
    
    
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