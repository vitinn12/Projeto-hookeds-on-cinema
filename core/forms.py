from django import forms
from core.models import Playlists



class PlaylistForm (forms.ModelForm):
    class Meta:
        model = Playlists
        fields = ['nome_musica', 'nome_artista', 'album_musica', 'link']
        labels = {
            'nome_musica' : 'Nome da Musica',
            'nome_artista' : 'Nome do Artista',
            'album_musica' : 'Nome do Album',
            'link' : 'Link'
        }


