from django.contrib import admin
from api.models import Livro, Autor, Genero
# Register your models here.

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Genero)
