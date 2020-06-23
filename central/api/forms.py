from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import password_validation
#from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import User

class SignUpForm(forms.ModelForm):
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))
    password = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                help_text=password_validation.password_validators_help_text_html())

    class Meta:
        model = User
        fields = ('email', 'password',)