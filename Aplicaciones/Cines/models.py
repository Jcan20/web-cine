from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    bandera = models.ImageField(upload_to='banderas/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Director(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    foto = models.ImageField(upload_to='directores/', blank=True, null=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, related_name='directores')

    def __str__(self):
        return self.nombre

class Protagonista(models.Model):
    nombre = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='protagonistas/', blank=True, null=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, related_name='protagonistas')

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_estreno = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='peliculas')  # Arreglado
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, related_name='peliculas')
    protagonistas = models.ManyToManyField(Protagonista, related_name='peliculas')
    pais_origen = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, related_name='peliculas')
    portada = models.ImageField(upload_to='portadas_peliculas/', blank=True, null=True)
    trailer = models.FileField(upload_to='trailers_peliculas/', blank=True, null=True)

    def __str__(self):
        return self.titulo
