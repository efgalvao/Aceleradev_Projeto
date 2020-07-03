from rest_framework import serializers
from api.models import Agent, Event
from users.models import CustomUser, Group


"""
class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField('get_token')
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'token', )

    def get_token(self, user):
        token = token.key
        return token


class GroupSerializer(serializers.ModelSerializer):
        class Meta:
            model = Group
            fields = '__all__'
"""

class AgentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Agent
            fields = '__all__'


class EventViewSerializer(serializers.ModelSerializer):
    address = serializers.ReadOnlyField(source='agent.address')
    
    class Meta:
        model = Event
        fields = '__all__'

class EventDetailSerializer(serializers.ModelSerializer):
    address = serializers.ReadOnlyField(source='agent.address')
    
    class Meta:
        model = Event
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    address = serializers.ReadOnlyField(source='agent.address')

    class Meta:
        model = Event
        fields = '__all__'