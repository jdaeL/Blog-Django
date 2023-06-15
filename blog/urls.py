from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),

    path('', views.listar_articulos, name='listar'),
    path('crear/', views.crear_articulo, name='crear'),
    path('editar/<int:pk>/', views.editar_articulo, name='editar'),
    path('eliminar/<int:pk>/', views.eliminar_articulo, name='eliminar'),
    path('style.css', views.style)
]   
