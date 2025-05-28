from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('interesses/', views.interesses_view, name='interesses'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('contact/', views.contact_view, name='contact'),

    # ROTAS DE GESTÃO DE PROJETOS
    path('gerir_projetos/', views.gerir_projetos_view, name='gerir_projetos'),
    path('gerir_projetos/criar/', views.criar_projeto, name='criar_projeto'),
    path('gerir_projetos/<int:pk>/editar/', views.editar_projeto, name='editar_projeto'),
    path('gerir_projetos/<int:pk>/eliminar/', views.eliminar_projeto, name='eliminar_projeto'),

    # Rotas de autenticaçao
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registo/',views.registo_view, name='registo'),
    path('user/', views.login_view, name='user'),

    # ROTAS DO LINK MAGICO
    path('login-magico/', views.login_magico_view, name='login_magico'),
    path('pedido-link-magico/', views.pedido_link_magico_view, name='pedido_link_magico'),

    #ESTUDAR
    path('professores/', views.professor_view, name='professores'),

    #DEFESA
    path('interesses_defesa/', views.interesses_defesa_view, name='interesses_defesa'),
    path('interesses_defesa/criar/', views.criar_interesses_view, name='criar_interesse'),
    path('interesses_defesa/<int:pk>/editar/', views.editar_interesse_view, name='editar_interesse'),
    path('interesses_defesa/<int:pk>/', views.interesse_detalhe_view, name='interesse_detalhe'),




]
