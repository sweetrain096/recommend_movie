from django.shortcuts import render, redirect
# 로그인 form, 로그인 유지
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import UserCustomCreationForm

# Create your views here.
def signup(request):
  # 만약 이미 로그인 되어있으면 메인으로 redirect
  if request.user.is_authenticated:
    return redirect('movies:index')
  # 만약 form 으로 요청이 올 경우
  if request.method == "POST":
    user_form = UserCustomCreationForm(request.POST)
    # 만약 들어온 값이 유효하면 저장
    if user_form.is_valid():
      user_form.save()
      return redirect('movies:index')
  else:
    user_form = UserCustomCreationForm()
  context = {'user_form': user_form}
  return render(request, 'accounts/signup.html', context)

def signin(request):
  # 만약 이미 로그인 되어있으면 메인으로 redirect
  if request.user.is_authenticated:
    return redirect('movies:index')
  # POST요청으로 들어올 경우 유효하면 로그인
  if request.method == 'POST':
    signin_form = AuthenticationForm(request, request.POST)
    if signin_form.is_valid():
      auth_login(request, signin_form.get_user())
      return redirect('movies:index')
    else:
      signin_form = AuthenticationForm()
  context = {'signin_form': signin_form}
  return render(request, 'accounts/signin.html', context)