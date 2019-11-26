from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('movie_list/', views.movie_list),
]