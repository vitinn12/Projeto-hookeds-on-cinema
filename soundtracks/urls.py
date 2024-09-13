
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
    path('perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),

]
 