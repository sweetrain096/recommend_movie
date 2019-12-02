import sys
import pprint
import requests

def find_movie():
    url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=20191201"
    movie_list = dict()
    # 정보 requests로 가져오기
    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        # pprint.pprint(data)
        for movie in data['boxOfficeResult']['weeklyBoxOfficeList']:
            # print(movie)
            movie_list[movie['movieCd']] = movie['movieNm']
    print(movie_list)
        # print(data['boxOfficeResult']['weeklyBoxOfficeList'])


find_movie()