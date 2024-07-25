from django.shortcuts import render

def login (request):
    return render (request, 'paginas/login.html')

def register (request):
    return render (request, 'paginas/registro.html')

def user (request):
    return render (request, 'paginas/perfil_usuario.html')

def index (request):
    return render (request, 'paginas/index.html')