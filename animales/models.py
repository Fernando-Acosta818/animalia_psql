from django.db import models

class Filo(models.Model):
    filo = models.CharField(max_length=255)

    def __str__(self):
        return self.filo

class Clase(models.Model):
    clase = models.CharField(max_length=255)
    nombreComun = models.CharField(max_length=255)

    def __str__(self):
        return self.clase

class Orden(models.Model):
    orden = models.CharField(max_length=255)

    def __str__(self):
        return self.orden

class Genero(models.Model):
    genero = models.CharField(max_length=255)

    def __str__(self):
        return self.genero

class Familia(models.Model):
    familia = models.CharField(max_length=255)

    def __str__(self):
        return self.familia

class Especie(models.Model):
    especie = models.CharField(max_length=255)

    def __str__(self):
        return self.especie

class Conservacion(models.Model):
    nivel = models.IntegerField()
    nombreNivel = models.CharField(max_length=255)

    def __str__(self):
        return self.nombreNivel

class Animal(models.Model):
    nombreAnimal = models.CharField(max_length=255)
    descripcion = models.TextField()
    foto1 = models.CharField(max_length=2000)
    foto2 = models.CharField(max_length=2000)
    foto3 = models.CharField(max_length=2000)
    foto4 = models.CharField(max_length=2000)
    foto5 = models.CharField(max_length=2000)
    habitat = models.TextField()
    
    filo = models.ForeignKey(Filo, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    conservacion = models.ForeignKey(Conservacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreAnimal