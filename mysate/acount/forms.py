from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class RegisterUser(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "autocomplete": 'text',
                "placeholder": "Ведите логин",
                 "class": "MyInput"
            }
        ),
        required=True,
        validators=[RegexValidator(r'^[0-9а-яА-яёЁ]', "Ведите логин валидный")]
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "autocomplete": 'email',
                "placeholder": "Введите адрес электронной почты",
                 "class": "MyInput"
            }
        ),
        required=True,
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Введите пароль",
                 "class": "MyInput"
            }
        ),
        required=True
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Подтвердите пароль",
                 "class": "MyInput"
            }
        ),
        required=True
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise forms.ValidationError("Введите логин", code='invalid')
        return username

    def clean_password(self) :
        password = self.cleaned_data['password']
        if password == '':
            raise forms.ValidationError("Введите пароль", code='invalid')
        return password

    def clean_email(self) :
        email = self.cleaned_data['email']
        if email == '':
            raise forms.ValidationError("Введите адрес электронной почты", code='invalid')
        return email
    
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'password1', 'password2')
    


class LoginUser(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "autocomplete": 'text',
                "placeholder": "Введите логин",
                "class": "MyInput"
            }
        ),
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Введите пароль",
                 "class": "MyInput"
            }
        ),
        required=True
    )
    error_messages = {
        'invalid_login': ("Ведите логин и пароль")
    }

    def clean_password(self):
        password = self.changed_data['password']
        if password == '':
            raise forms.ValidationError("Введите пароль", code='invalid')
        return password
    
    def clean_username(self):
        username = self.changed_data['username']
        if username == '':
            raise forms.ValidationError("Введите логин", code='invalid')
        if not User.objects.filter(username=username):
            raise forms.ValidationError("Пользователь с таким логином не найден", code='invalid')

        return username