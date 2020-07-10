from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event, User
from .forms import UserCreationForm

admin.site.register(Event)
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

