from rest_framework import serializers
from users.models import CustomUser

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwarGS={
            'password' : {'write_only' : True}
        }

    def save(self):
        user = CustomUser(
                email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user
