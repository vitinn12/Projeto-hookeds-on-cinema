from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import PlaylistForm


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
            return render(request, 'paginas/comfirmaregistro.html')
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
            return render(request, 'paginas/usuarioinvalido.html')


def index (request):
    Playlist = Playlists.objects.all()
    return render (request, 'paginas/index.html', {'Playlist':Playlist})

def areadatriha(request, id):
    playlist = Playlists.objects.get(id=id) 
    return render (request, 'paginas/areadatrilha.html', {'playlist': playlist})


def perfil_usuario(request):
    return render(request, 'paginas/perfil_usuario.html')

@login_required(login_url='/login/')

def redefinir_senha(request):
    return render (request, 'paginas/redefinir_senha.html')


def home(request):
    Playlist = Playlists.objects.all()
    return render(request, 'paginas/home.html', {'Playlist':Playlist})

def adicionarplaylist(request):
    form = PlaylistForm()
    return render (request ,'paginas/cadastrarplaylist.html', {'form': form})

def editarplaylist(request, id):
    playlist = Playlists.objects.get(id=id) 
    return render(request, 'paginas/editar.html', {'playlist': playlist})

def updateplaylist (request, id):
    vnomealbum = request.POST.get("album_musica")
    vnomemusica = request.POST.get ("nome_musica")
    vlink = request.POST.get ("link")

    playlist = Playlists.objects.get(id=id)

    playlist.album_musica = vnomealbum
    playlist.nome_musica = vnomemusica
    playlist.link = vlink
    playlist.save()

    return redirect(home)

def deleteplaylist(request,id):
    playlist = Playlists.objects.get(id=id) 
    playlist.delete()
    return redirect(home)


def view_create_playlist(request):
    form = PlaylistForm (request.POST)
    if form.is_valid():
        form.save()
        return render (request, 'paginas/playlistsalvo.html')
    
