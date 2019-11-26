from django.db import models

# Create your models here.
class Genre(models.Model):
  genre = models.CharField(max_length=10)

class Director(models.Model):
  director = models.CharField(max_length=20)

class Actor(models.Model):
  actor = models.CharField(max_length=20)

class Movie(models.Model):
  # 영화 정보
  # 제목, 내용, 개봉일, 포스터
  # foreignkey 묶을것
  # 감독, 배우, 장르, 댓글, 좋아요, 싫어요
  # 점수는 따로 뺄 것. => 계산 쉽게
  title = models.CharField(max_length=50)
  content = models.TextField()
  poster = models.TextField()
  opened_at = models.DateTimeField()

  genres = models.ManyToManyField(Genre, related_name="movies")
  directors = models.ManyToManyField(Director, related_name="filmo")
  actors = models.ManyToManyField(Actor, related_name="filmo")

# class Score(models.Model):
#   score = models.IntegerField()
#   movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # 삭제 시 같이 삭제
  
