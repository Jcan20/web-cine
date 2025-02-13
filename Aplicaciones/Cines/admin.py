from django.contrib import admin
from .models import Genero, Pais, Director, Protagonista, Pelicula

# Register your models here.
admin.site.register (Genero)
admin.site.register (Pais)
admin.site.register (Director)
admin.site.register (Protagonista)
admin.site.register (Pelicula)