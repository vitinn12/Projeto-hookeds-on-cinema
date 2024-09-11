from django import forms
from core.models import *

class UsuarioRegistro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['apelido', 'email']
        labels = (
            'apelido', 'Nome :',
            'email' , 'E - mail'
        )
)