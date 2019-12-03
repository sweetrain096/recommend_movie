import json
import pprint
import requests
import os

API_KEY = os.getenv("APIKEY")

# 영화 전체 데이터
with open("json_movie_list.json", "r", encoding="UTF-8") as file:
    json_movie_list = json.load(file)

# 영화 배우 데이터
with open("actor_list.json", "r", encoding="UTF-8") as file:
    actor_file = json.load(file)

# 영화 감독 데이터
with open("director_list.json", "r", encoding="UTF-8") as file:
    director_file = json.load(file)

# 장르 정보
with open("genres.json", "r", encoding="UTF-8") as file:
    genre_file = json.load(file)

# 영화 상세 정보
with open("movie_detail.json", "r", encoding="UTF-8") as file:
    detail_file = json.load(file)

def find_movie():
    url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={API_KEY}&targetDt=20191201"
    movie_list = dict()
    # 정보 requests로 가져오기
    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        # pprint.pprint(data)
        for movie in data['boxOfficeResult']['weeklyBoxOfficeList']:
            if not json_movie_list.get(movie['movieCd']):
                movie_list[movie['movieCd']] = movie['movieNm']
                # 하나 뽑은 영화의 디테일 저장
            # 영화 정보 없을때에는 초기에 그냥 하기
            get_movie_detail(movie['movieCd'])
    if movie_list:
        json_movie_list.update(movie_list)
        print(json_movie_list)


# 영화 상세 정보 조회
def get_movie_detail(movieCd):
    url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={API_KEY}&movieCd={movieCd}"
    movie_detail = dict()

    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        info = data['movieInfoResult']['movieInfo']
        pprint.pprint(info)


        # 영화 제목
        movie_detail['title'] = info['movieNm']
        movie_detail['titleEn'] = info['movieNmEn']

        # 개봉일
        movie_detail['openDt'] = info['openDt']
        movie_detail['prdtYear'] = int(info['prdtYear'])

        # 상영시간
        movie_detail['showTm'] = int(info['showTm'])

        # 영화 배우 정보
        actor_list = []
        for actor in info['actors']:
            actor_list.append(get_actors(actor))
        movie_detail['actors'] = actor_list

        # 영화 감독 정보
        director_list = []
        for director in info['directors']:
            director_list.append(get_directors(director))
        movie_detail['directors'] = director_list

        # 장르
        genre_list = []
        for genre in info['genres']:
            genre_list.append(get_genres(genre['genreNm']))
        movie_detail['genres'] = genre_list

        # 관람가
        movie_detail['audits'] = info['audits'][0]['watchGradeNm']

        print(movie_detail)

        detail_file.update({movieCd: movie_detail})
        print(detail_file)

# 영화 배우
def get_actors(people):
    peopleNm = people['peopleNm']
    people_id = actor_file.get(peopleNm)
    if people_id:
        return people_id
    if actor_file:
        people_id = max(actor_file.keys()) + 1
        actor_file.update({people_id: {'peopleNm': people['peopleNm'], 'peopleNmEn': people['peopleNmEn']}})
    else:
        people_id = 1
        actor_file.update({people_id: {'peopleNm': people['peopleNm'], 'peopleNmEn': people['peopleNmEn']}})
    # print(people_file)
    return people_id

# 영화 감독
def get_directors(people):
    peopleNm = people['peopleNm']
    people_id = director_file.get(peopleNm)
    if people_id:
        return people_id
    if director_file:
        people_id = max(director_file.keys()) + 1
        director_file.update({people_id: {'peopleNm': people['peopleNm'], 'peopleNmEn': people['peopleNmEn']}})
    else:
        people_id = 1
        director_file.update({people_id: {'peopleNm': people['peopleNm'], 'peopleNmEn': people['peopleNmEn']}})
    # print(people_file)
    return people_id

# 영화 장르
def get_genres(genreNm):
    genre_id = genre_file.get(genreNm)
    if genre_id:
        return genre_id
    if genre_file:
        genre_id = max(genre_file.keys()) + 1
        genre_file.update({genre_id: genreNm})
        return genre_id
    genre_id = 1
    genre_file.update({genre_id: genreNm})
    return genre_id




def save():
    # with open("json_movie_list.json", "w", encoding="UTF-8") as list_file:
        #     list_file.write(json.dumps(json_movie_list, ensure_ascii=False))

    # 영화 전체 데이터
    with open("json_movie_list.json", "w", encoding="UTF-8") as file:
        file.write(json.dumps(json_movie_list, ensure_ascii=False))

    # 영화 배우 데이터
    with open("actor_list.json", "w", encoding="UTF-8") as file:
        file.write(json.dumps(actor_file, ensure_ascii=False))

    # 영화 감독 데이터
    with open("director_list.json", "w", encoding="UTF-8") as file:
        file.write(json.dumps(director_file, ensure_ascii=False))

    # 장르 정보
    with open("genres.json", "w", encoding="UTF-8") as file:
        file.write(json.dumps(genre_file, ensure_ascii=False))

    # 영화 상세 정보
    with open("movie_detail.json", "w", encoding="UTF-8") as file:
        file.write(json.dumps(detail_file, ensure_ascii=False))

find_movie()
# save()
# get_movie_detail(20197803)