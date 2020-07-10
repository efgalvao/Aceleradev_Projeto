from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Erro, User
from .forms import UserCreationForm
# Register your models here.

admin.site.register(Erro)
admin.site.register(User)


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    model = User
    list_display = ('email', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active')}),
    )
        
    search_fields = ('email',)
    ordering = ('email',)

