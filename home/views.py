from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("A view index funcionou, wow")

def sobre(request):
    return HttpResponse("<h1>Sistema 1.0 desenvolvido por mim</h1>")
    
def contato(request):
    return HttpResponse("<h1>Está pagina de contato</h1>")
