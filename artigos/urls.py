from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.listar_artigos, name='listar_artigos'),
    
    path('ver/<int:artigo_id>/', views.ver_artigo, name='ver_artigo'),

    # Gestão de artigos
    path('gerir_artigos/', views.gerir_artigos_view, name='gerir_artigos'),
    path('gerir_artigos/novo/', views.criar_artigo, name='criar_artigo'),
    path('gerir_artigos/<int:pk>/editar/', views.editar_artigo, name='editar_artigo'),
    path('gerir_artigos/<int:pk>/eliminar/', views.eliminar_artigo, name='eliminar_artigo'),
    path('avaliar/<int:artigo_id>/', views.avaliar_artigo, name='avaliar_artigo'),

]
