from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    clasificacion = models.CharField(max_length=10)
    anio_estreno = models.IntegerField()
    duracion = models.IntegerField(help_text="Duración en minutos")
    genero = models.CharField(max_length=50, choices=[
        ('Comedia', 'Comedia'),
        ('Romance', 'Romance'),
        ('Aventura', 'Aventura'),
        ('Terror', 'Terror'),
        ('Acción', 'Acción'),
        ('Otro', 'Otro'),
    ])

    def __str__(self):
        return self.titulo
