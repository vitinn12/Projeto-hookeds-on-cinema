from django import forms
from core.models import Playlists



class PlaylistForm (forms.ModelForm):
    class Meta:
        model = Playlists
        fields = ['nome_filme', 'nome_musica', 'nome_artista', 'album_musica', 'ano', 'descricao', 'imagem', 'link']

        labels = {
            'nome_filme': 'Nome do Filme',
            'nome_musica': 'Nome da Música',
            'nome_artista': 'Nome do Artista',
            'album_musica': 'Nome do Álbum',
            'ano': 'Ano do Filme',
            'descricao': 'Descrição do Filme',
            'imagem': 'Imagem do Filme',
            'link': 'Link'
}

