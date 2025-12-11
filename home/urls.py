from django.urls import path
# from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre,name='sobre'),
    path('contato/', views.contato,name='contato'),
    path('ajuda/', views.ajuda,name='ajuda'),

    path('item/<int:id>/', views.exibir_item,name='exibir_item'),
    path('perfil/<str:usuario>/', views.perfil,name='perfil'),
    path('dia_da_semana/<int:dia>/', views.dia_da_semana, name='dia_da_semana'),
    path('produtos/', views.produtos, name='produtos'),
    path('page/', views.home, name='page'),
    path('produtos/form', views.form_produto, name='form_produto'),
    # Rota: /produtos/detalhes/10
    path('detalhe/<int:id>', views.detalhe_produto, name='detalhe_produto'),

    # Rota: /produtos/editar/10
    path('editar/<int:id>', views.editar_produto, name='editar_produto'),

    # Rota: /produtos/excluir/10
    path('excluir/<int:id>', views.excluir_produto, name='excluir_produto'),
   
]

