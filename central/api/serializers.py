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
    
    class Meta:
        model = Event
        fields = ('level', 'data', 'arquivado', 'date', 'address', 'agent')
