from django.contrib import admin
from .models import Juego
from .models import Usuario
from .models import Genero

admin.site.register(Juego)
admin.site.register(Usuario)
admin.site.register(Genero)
