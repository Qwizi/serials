from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
