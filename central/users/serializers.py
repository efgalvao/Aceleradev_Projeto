from rest_framework import serializers
from users.models import CustomUser
from rest_framework.validators import UniqueValidator


class CadastroSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(style={'input_type': 'password'})
    
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        user = CustomUser(
                email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user
        