from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Agent, Event, CustomUser, Group
from .forms import CustomUserCreationForm
# Register your models here.

admin.site.register(Agent)
admin.site.register(Group)
admin.site.register(Event)
admin.site.register(CustomUser)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('email', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active')}),
    )
        
    search_fields = ('email',)
    ordering = ('email',)

