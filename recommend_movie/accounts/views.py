from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def signup(request):
  context = {'user_form': UserForm()}
  return render(request, 'accounts/signup.html', context)