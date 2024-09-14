
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',views.index, name='paginaPrincipal'),
    path ('login/', views.login_user, name='login'),
    path ('home/', views.home, name='home'),
    path ('register/', views.register, name= 'registro'),
    path ('user/', views.User, name= 'areadousuario'),    
    path('redefinir/',views.redefinir_senha, name='redefinir_senha' ),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('addplaylist/', views.adicionarplaylist, name='adicionarplaylist'),
    path('create_playlist/', views.view_create_playlist, name='createplaylist'),
    path ('trilha/', views.areadatriha, name='areadatrilha'),
]
 