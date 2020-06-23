from django.db import models
from django.core import validators

# Create your models here.

class Agent(models.Model):
    name = models.CharField('Nome', max_length=50)
    status = models.BooleanField()
    env = models.CharField(max_length=20)
    version = models.CharField('Version', max_length=5)
    address = models.GenericIPAddressField('Origem', protocol="IPV4", default="0.0.0.0")

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField('Nome', max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):
    last_login = models.DateTimeField('Último login', auto_now_add=True)
    email = models.EmailField('E-mail', max_length=254, unique=True)
    password = models.CharField('Senha', max_length=50,
                                validators=[validators.MinLengthValidator(8)])


    def __str__(self):
        return self.email


class Event(models.Model):
    ERROR_LEVEL = [('CRITICAL', 'CRITICAL'), ('DEBUG', 'DEBUG'), ('ERROR', 'ERROR'),
                   ('WARNING', 'WARNING'), ('INFO', 'INFO'), ]
    level = models.CharField(max_length=20, choices=ERROR_LEVEL)
    title = models.CharField("Título", max_length=50)
    data = models.TextField("Dados")
    arquivado = models.BooleanField('Arquivado', default=False)
    date = models.DateTimeField('Data')
    user = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE, blank=True, \
                                                                                     null=True)
    agent = models.ForeignKey(Agent, related_name='events', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


"""
class Mae(models.Model):
    nome = models.CharField(max_length=10)
    teste = models.CharField(max_length=5)

class Filha(models.Model):
    nome = models.CharField(max_length=20)
    mae = models.ForeignKey(Mae, related_name="related", on_delete=models.CASCADE)
"""
