
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',views.index, name='paginaPrincipal'),
    path ('login/', views.login, name='login'),
    path ('register/', views.register, name= 'registro'),
    path ('user/', views.user, name= 'areadousuario'),    
    path('redefinir/',views.redefinir_senha, name='redefinir_senha' ),
    path('master/',views.master, name='master' ),

]
 