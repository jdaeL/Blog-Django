from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from django.http import HttpResponse


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def style(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    response = HttpResponse(content_type='text/css')
    response['Content-Disposition'] = 'attachment; filename="style.css"'
    response.write(render(request, 'blog/style.css', {'posts': posts}).content)
    return response

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post

def listar_articulos(request):
    articulos = Post.objects.all()
    return render(request, 'blog/listar_articulos.html', {'articulos': articulos})

def crear_articulo(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        texto = request.POST['texto']
        autor = request.user  # Obtener el usuario actual (requiere autenticación)
        articulo = Post(author=autor, title=titulo, text=texto, created_date=timezone.now())
        articulo.save()
        return redirect('listar_articulos')
    return render(request, 'blog/crear_articulo.html')

def editar_articulo(request, pk):
    articulo = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        titulo = request.POST['titulo']
        texto = request.POST['texto']
        articulo.title = titulo
        articulo.text = texto
        articulo.save()
        return redirect('listar_articulos')
    return render(request, 'blog/editar_articulo.html', {'articulo': articulo})

def eliminar_articulo(request, pk):
    articulo = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        articulo.delete()
        return redirect('listar_articulos')
    return render(request, 'blog/eliminar_articulo.html', {'articulo': articulo})
