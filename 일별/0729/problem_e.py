import requests
from pprint import pprint


def credits(title):
    # 데이터를 요청할 URL
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

    # 검색 결과 중 첫번째 영화의 id값 불러오기
    # 검색 결과가 없을 시 None을 반환하기 위해 try, except 활용
    try:
        first_id = result[0]['id']
    except:
        return None
    
    # 첫 번째 영화의 id를 활용해 credit 정보 불러오기
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = f'/movie/{first_id}/credits'
    params = {
        'api_key' : 'e67fd4cae34071117f73a8090324311b',
        'language' : 'ko',
    }
    
    response = requests.get(BASE_URL + PATH, params = params).json()
    
    # 출연진과 연출진 데이터를 담기
    cast_result = response.get('cast')
    crew_result = response.get('crew')

    # 출연진, 연출진 데이터 반환을 위한 딕셔너리 생성
    cast_direct = {'cast' : [], 'directing' : []}

    # 출연진 정보 중 cast_id가 10 이하이면 저장하기
    for person in cast_result:
        if person['cast_id'] < 10:
            cast_direct['cast'].append(person['name'])
    # 연출진 정보 중 'department'가 Directing'인 경우 담기
    for person in crew_result:        
        if person['department'] == 'Directing':
            cast_direct['directing'].append(person['name'])

    # 출연진, 연출진 정보 반환
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
