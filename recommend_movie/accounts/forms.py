from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCustomCreationForm(UserCreationForm):
  class Meta:
    model = get_user_model()
    fields = ['username', 'first_name', 'email', 'password1', 'password2']