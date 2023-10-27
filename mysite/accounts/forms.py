from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="ユーザーネーム",
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    password1 = forms.CharField(
        label="パスワード作成",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    password2 = forms.CharField(
        label="パスワード再確",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')
