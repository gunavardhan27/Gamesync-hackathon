from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User
from django.contrib.auth.models import AbstractUser
class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','option','password1','password2']

