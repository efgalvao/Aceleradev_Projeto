from django.db import models

# Create your models here.

class Genero(models.Model):
    genero = models.CharField("Genêro", max_length= 20)
    teste = models.CharField("teste", max_length=5, default="teste")

    def __str__(self):
        return self.genero

class Autor(models.Model):
    nome = models.CharField("Nome", max_length=100)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField("Título", max_length=150)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    paginas = models.IntegerField("Páginas")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return self.titul0

class Mae(models.Model):
    nome = models.CharField(max_length=10)
    teste = models.CharField(max_length=5)

class Filha(models.Model):
    nome = models.CharField(max_length=20)
    mae = models.ForeignKey(Mae, related_name="related", on_delete=models.CASCADE)
