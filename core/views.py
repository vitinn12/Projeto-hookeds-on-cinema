from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import PlaylistForm
from django.contrib.auth.decorators import user_passes_test




def login (request):
    return render (request, 'paginas/login.html')

def register(request):
    if request.method == "GET":
        return render(request, 'paginas/registro.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        if User.objects.filter(username=usuario).exists():
            return HttpResponse('Já existe um usuário com esse username')

        try:
            User.objects.create_user(username=usuario, password=senha)
            return render(request, 'paginas/confirmaregistro.html')
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
            auth_login(request, user)
            return redirect('home')  # Nome da URL da view home
        else:
            return render(request, 'paginas/usuarioinvalido.html')


def index (request):
    Playlist = Playlists.objects.all()
    return render (request, 'paginas/index.html', {'Playlist':Playlist})

def areadatriha(request, id):
    playlist = Playlists.objects.get(id=id) 
    return render (request, 'paginas/areadatrilha.html', {'playlist': playlist})

@login_required(login_url='/login/')
def perfil_usuario(request):
    return render(request, 'paginas/perfil_usuario.html', {'user': request.user})

@login_required(login_url='/login/')
def redefinir_senha(request):
    return render (request, 'paginas/redefinir_senha.html')

@login_required(login_url='/login/')
def home(request):
    playlists = Playlists.objects.all() 
    return render(request, 'paginas/home.html', {'playlists': playlists})

@login_required(login_url='/login/')
def adicionarplaylist(request):
    form = PlaylistForm()
    return render (request ,'paginas/cadastrarplaylist.html', {'form': form})

@login_required(login_url='/login/')
def editarplaylist(request, id):
    playlist = Playlists.objects.get(id=id) 
    return render(request, 'paginas/editar.html', {'playlist': playlist})

@login_required(login_url='/login/')
def updateplaylist(request, id):
    playlist = get_object_or_404(Playlists, id=id)

    if request.method == 'POST':
        form = PlaylistForm(request.POST, request.FILES, instance=playlist)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = PlaylistForm(instance=playlist)

    return render(request, 'paginas/editar.html', {'form': form, 'playlist': playlist})

@login_required(login_url='/login/')
def deleteplaylist(request,id):
    playlist = Playlists.objects.get(id=id) 
    playlist.delete()
    return redirect(home)

def is_superuser(user):
    return user.is_superuser


@login_required(login_url='/login/')
@user_passes_test(is_superuser)
def view_create_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print("Form errors:", form.errors)
    else:
        form = PlaylistForm()
    
    return render(request, 'paginas/cadastrarplaylist.html', {'form': form})