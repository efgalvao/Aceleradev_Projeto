from django.core.validators import MinLengthValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_ipv4_address
from django.db import models

# Create your models here.

LEVEL_CHOICES = [
    ('critical', 'critical.'),
    ('debug', 'debug'),
    ('error', 'error'),
    ('warning', 'warning'),
    ('information', 'info'),
]

min_validator = MinLengthValidator(8, 'The password cant be smaller than 8')


class Group(models.Model):
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(validators=[EmailValidator], null=True)
    password = models.CharField(max_length=50, validators=[min_validator])
    last_login = models.DateField(auto_now_add=True)
    group = models.ManyToManyField(Group)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Agent(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    address = models.GenericIPAddressField(
        validators=[validate_ipv4_address], null=True)
    status = models.BooleanField(default=False)
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Event(models.Model):
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    data = models.TextField(max_length=500)
    agent = models.OneToOneField(Agent, on_delete=models.PROTECT)
    arquivado = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.level + ' in ' + self.agent.name

    class Meta:
        ordering = ['date']


"""
class Mae(models.Model):
    nome = models.CharField(max_length=10)
    teste = models.CharField(max_length=5)

class Filha(models.Model):
    nome = models.CharField(max_length=20)
    mae = models.ForeignKey(Mae, related_name="related",
                             on_delete=models.CASCADE)
"""
