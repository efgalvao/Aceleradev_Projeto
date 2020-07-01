from django.contrib import admin
from .models import Agent, Event
from users.models import Group

# Register your models here.

admin.site.register(Agent)
admin.site.register(Group)
admin.site.register(Event)
