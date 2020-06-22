from rest_framework import serializers
from .models import User, Agent, Group, Event


class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = '__all__'
    
class AgentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Agent
            fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
        class Meta:
            model = Group
            fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    address = serializers.ReadOnlyField(source='agent.address')
    name = serializers.ReadOnlyField(source='agent.name')
    group = serializers.ReadOnlyField(source='user.group')

    class Meta:
        model = Event
        fields = ('id', 'level', 'title', 'data', 'arquivado', 'agent', 'date', 'name',
                  'address', 'user', 'group')
