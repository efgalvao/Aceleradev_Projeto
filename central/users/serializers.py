from rest_framework import serializers
from users.models import CustomUser

class CadastroSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    def save(self):
        user = CustomUser(
                email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user

"""
class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs={
            'password' : {'write_only' : True}
        }
"""
