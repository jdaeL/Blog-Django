from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),

    path('post/<int:pk>/', views.listar_articulos, name='listar_articulos'),
    path('post/new', views.crear_articulo, name='crear_articulo'),
    path('post/<int:pk>/edit/', views.editar_articulo, name='editar_articulo'),
    path('post/<int:pk>/delete/', views.eliminar_articulo, name='eliminar_articulo'),
    path('new/', views.crear_articulo, name='crear_articulo'),


    path('style.css', views.style)
]   
