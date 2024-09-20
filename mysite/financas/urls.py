from . import views
from django.urls import path

app_name = 'financas'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cadastro-balancete/', views.CadastroBalanceteView.as_view(), name='cadastro-balancete'),
    path('cadastro-usuario/', views.CadastroUsuarioView.as_view(), name='cadastro-usuario'),
    path('cadastro-receita/', views.CadastroReceitaView.as_view(), name='cadastro-receita'),
    path('cadastro-despesa/', views.CadastroDespesaView.as_view(), name='cadastro-despesa'),
    path('gerenciar-financas/', views.ListaBalancetesView.as_view(), name='gerenciar-financas'),
    path('detalhes-balancete/<int:pk>/', views.DetalhesBalanceteView.as_view(), name='detalhes-balancete'),
]