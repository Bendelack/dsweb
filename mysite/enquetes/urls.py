from . import views
from django.urls import path

app_name = 'enquetes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetalhesView.as_view(), name='detalhes'),
    path('<int:pk>/resultado/', views.ResultadoView.as_view(), name='resultado'),
    path('<int:pergunta_id>/votacao/', views.votacao, name='votacao'),
]