from django.contrib import admin
from api.models import User, Agent, Group, Erro, GroupUser
# Register your models here.

admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Group)
admin.site.register(Erro)
admin.site.register(GroupUser)