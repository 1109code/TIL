import requests
from pprint import pprint


def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/search/movie'
    params = {
    'api_key' : 'e67fd4cae34071117f73a8090324311b',
    'language' : 'ko',
    'region' : 'KR',
    'query' : title,
    }

    response = requests.get(BASE_URL + PATH, params = params).json()
    result = response.get('results')

    try:
        first_id = result[0]['id']
    except IndexError:
        return None
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = f'/movie/{first_id}/credits'
    params = {
        'api_key' : 'e67fd4cae34071117f73a8090324311b',
        'language' : 'ko',
    }
    response = requests.get(BASE_URL + PATH, params = params).json()
    cast_result = response.get('cast')
    crew_result = response.get('crew')
    cast_direct = {'cast' : [], 'directing' : []}

    for person in cast_result:
        if person['cast_id'] < 10:
            cast_direct['cast'].append(person['name'])
    for person in crew_result:
        if person['department'] == 'Directing':
            cast_direct['directing'].append(person['name'])
    
    return cast_direct
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
