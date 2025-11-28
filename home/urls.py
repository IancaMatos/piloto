from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre,name='sobre'),
    # path('', views.sobre, name='sobre'),
]

