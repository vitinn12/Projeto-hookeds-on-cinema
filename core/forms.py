from django import forms
from core.models import Playlists



class PlaylistForm (forms.ModelForm):
    class Meta:
        model = Playlists
        fields = '__all__'
        labels = {
            'nome_musica' : 'Nome da Musica',
            'nome_artista' : 'Nome do Artista',
            'album_musica' : 'Nome do Album',
            'link' : 'Link'

        }


