from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password")

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full py-4 px-6  rounded-xl",
                "placeholder": "Your username",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "py-4 px-6 w-full rounded-xl",
                "placeholder": "Your password",
            }
        )
    )


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full py-4 px-6  rounded-xl",
                "placeholder": "Your username",
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "py-4 px-6 w-full rounded-xl",
                "placeholder": "ex: email@server.com",
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "py-4 px-6 w-full rounded-xl",
                "placeholder": "Your password",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "py-4 px-6 w-full rounded-xl",
                "placeholder": "Repeat your password",
            }
        )
    )
