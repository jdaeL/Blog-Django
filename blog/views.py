from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from django.http import HttpResponse
from .form import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def style(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    response = HttpResponse(content_type='text/css')
    response['Content-Disposition'] = 'attachment; filename="style.css"'
    response.write(render(request, 'blog/style.css', {'posts': posts}).content)
    return response

def listar_articulos(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/listar_articulos.html', {'post': post})

def crear_articulo(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('listar_articulos', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'editar_articulo.html', {'form': form})

def editar_articulo(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('listar_articulos', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/editar_articulo.html', {'form': form})

def eliminar_articulo(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/eliminar_articulo.html', {'post': post})

def crear_articulo(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('listar_articulos', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/crear_articulo.html', {'form': form})
