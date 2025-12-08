from django.shortcuts import render, HttpResponse
# from django.http import 


# Create your views here.

def index(request):
    context = {
        "data":"05/12/2025",
        "cidade":"Teresina"
    }
    return render(request, 'index.html',context)

def sobre(request):
    return render(request, 'sobre.html')
    
def contato(request):
    return render(request, 'contato.html')

def ajuda(request):
    return render(request, 'Ajuda.html')

def exibir_item(request, id):
    return render(request, 'exibir_item.html',{'id':id})

def perfil(request, usuario):
    return render(request, 'perfil.html', {'usuario': usuario})

def produtos(request):
    contexto = {
        'lista': [
            {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
            {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
            {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
            {'id': 4, 'nome': 'Mouse', 'preco': '40,00'},
            {'id': 5, 'nome': 'Impressora', 'preco': '600,00'},
            {'id': 6, 'nome': 'Scanner', 'preco': '700,00'},
            {'id': 7, 'nome': 'Câmera Web', 'preco': '150,00'},
            {'id': 8, 'nome': 'Headset', 'preco': '120,00'},
            {'id': 9, 'nome': 'Pendrive 32GB', 'preco': '30,00'},
            {'id': 10, 'nome': 'HD Externo 1TB', 'preco': '350,00'},
            {'id': 11, 'nome': 'Estabilizador', 'preco': '200,00'},
            {'id': 12, 'nome': 'Switch 8 portas', 'preco': '180,00'},
            {'id': 13, 'nome': 'Roteador Wi-Fi', 'preco': '220,00'},
        ],
    }
    return render(request, 'produtos/lista.html',contexto)


def dia_da_semana(request, dia):
    dias_semana = {
        "1":"Domingo",
        "2":"Segunda-Feira",
        "3":"Terça-Feira",
        "4":"Quarta-Feira",
        "5":"Quinta-Feira",
        "6":"Sexta-Feira",
        "7":"Sábado"
    }
    
    dia_nome = dias_semana.get(str(dia))
    
    if dia_nome:
        return render(request, 'dia_da_semana.html', {'dia': dia_nome})
    else:
        return render(request, 'dia_da_semana.html', {'dia': "é Dia inválido"})

def home(request):
    context = {
        'username': 'Ianca',
        'items': ['Lápis','Caneta','Borracha']
    }

    return render(request,'home.html',context)