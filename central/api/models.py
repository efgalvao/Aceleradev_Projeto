from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.core.validators import EmailValidator
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import validate_ipv4_address


LEVEL_CHOICES = [
    ('critical', 'critical'),
    ('debug', 'debug'),
    ('error', 'error'),
    ('warning', 'warning'),
    ('info', 'info'),
]

ENV_CHOICES = [
    ('Produção', 'Prod'),
    ('Dev', 'Devs'),
    ('homologação', 'homologação')
]
min_validator = MinLengthValidator(8, 'The password cant be smaller than 8')


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

        
class User(AbstractUser):
    username = None
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(validators=[EmailValidator], unique=True)
    password = models.CharField(max_length=50, validators=[MinLengthValidator(8)])
    last_login = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class Erro(models.Model):
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField("description", max_length=150)
    details = models.TextField(max_length=500)
    address = models.GenericIPAddressField(
        validators=[validate_ipv4_address], null=True)
    archived = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    env = models.CharField(max_length=20, choices=ENV_CHOICES)
    freq = models.PositiveIntegerField(blank=True)
   
    def __str__(self):
        return self.level + ' in ' + self.address

    class Meta:
        ordering = ['id']
    
    #@property
    #def frequency(self):
    #    return Erro.objects.filter(description=self.description).count()

    def archive(self):
        self.archived = True
        self.save()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
        
