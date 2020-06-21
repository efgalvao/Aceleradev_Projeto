from rest_framework import serializers
from api.models import User, Agent, Group, Event, Groupuser


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
        class Meta:
            model = Event
            fields = '__all__'

    class GroupuserSerializer(serializers.ModelSerializer):
        class Meta:
            model = Groupuser
            fields = '__all__'