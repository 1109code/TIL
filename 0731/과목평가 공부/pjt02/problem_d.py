import requests
from pprint import pprint


def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/search/movie'
    params = {
    'api_key' : 'e67fd4cae34071117f73a8090324311b',
    'language' : 'ko',
    'region' : 'KR',
    'query' : title
    }

    response = requests.get(BASE_URL + PATH , params = params).json()
    result = response.get('results')
    
    try:
        movie_id = result[0]['id']
    except IndexError:
        return None

    params = {
        'api_key' : 'e67fd4cae34071117f73a8090324311b',
        'language' : 'ko',
    }

    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = f'/movie/{movie_id}/recommendations'
    response = requests.get(BASE_URL + PATH, params = params).json()
    result = response.get('results')
    movie_list = []
    
    for movie in result:
        movie_list.append(movie['title'])
    
    return movie_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
