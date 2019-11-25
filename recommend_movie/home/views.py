from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  print(request)
  return HttpResponse("hello, django!")

def movie_list(request):
  movie_list = ['겨울왕국2', '블랙머니', '조커']
  return render(request, 'movie_list.html', {'movie_list': movie_list})