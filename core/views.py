from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required


def login (request):
    return render (request, 'paginas/login.html')

def register(request):
    if request.method == "GET":
        return render(request, 'paginas/registro.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        # Verificar se o usuário já existe
        if User.objects.filter(username=usuario).exists():
            return HttpResponse('Já existe um usuário com esse username')

        # Criar o novo usuário
        try:
            User.objects.create_user(username=usuario, password=senha)
            return HttpResponse('Usuário cadastrado com sucesso')
        except Exception as e:
            return HttpResponse(f'Erro ao cadastrar usuário: {e}')
        
def login_user(request):
    if request.method == 'GET':
        return render(request, 'paginas/login.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=usuario, password=senha)

        if user is not None:
            auth_login(request, user)  # Inicia a sessão do usuário
            return redirect (home)  # Redireciona para uma URL após login bem-sucedido
        else:
            return HttpResponse('Usuário ou senha inválidos')


def index (request):
    return render (request, 'paginas/index.html')

def perfil_usuario(request):
    return render(request, 'paginas/perfil_usuario.html')

@login_required(login_url='/login/')
def home(request):
    return render(request, 'paginas/home.html')  