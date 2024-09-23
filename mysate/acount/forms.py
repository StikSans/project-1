from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class RegisterUser(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "autocomplete": 'text',
                "placeholder": "Ведите логин",
            }
        ),
        required=True,
        validators=[RegexValidator(r'^[0-9а-яА-яёЁ]', "Ведите логин валидный")]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "autocomplete": 'email',
                "placeholder": "Введите адрес электронной почты",
            }
        ),
        required=True,
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Введите пароль",
            }
        ),
        required=True
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Подтвердите пароль",
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