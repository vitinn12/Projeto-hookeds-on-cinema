from django.contrib import admin

# Register your models here.
from .models import *

class playlist(admin.ModelAdmin):
    ...
class CarroAdmin (admin.ModelAdmin):
    ...


admin.site.register (Playlists, playlist)

