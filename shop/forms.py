from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов', widget=forms.TextInput(attrs={'class': 'checkout-coupon top log a-an l-contact'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'checkout-coupon top log a-an l-contact'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'checkout-coupon top log a-an l-contact'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'checkout-coupon top log a-an l-contact'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm (AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'checkout-coupon top log a-an l-contact'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'checkout-coupon top log a-an l-contact'}))