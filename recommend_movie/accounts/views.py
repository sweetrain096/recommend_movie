from django.shortcuts import render, redirect
from .forms import UserCustomCreationForm

# Create your views here.
def signup(request):
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