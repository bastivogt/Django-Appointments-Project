from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",

            "email",
            "password1",
            "password2"
        ]
        

class SignInForm(AuthenticationForm):
    pass