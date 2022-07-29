import requests
from pprint import pprint


def recommendation(title):
    # 데이터를 요청할 URL, 기존과 다르게 path를 수정
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/search/movie'
    
    # query에 title 입력 해 영화 제목 검색
    params = {
        'api_key' : 'e67fd4cae34071117f73a8090324311b',
        'language' : 'ko',
        'region' : 'KR',
        'query' : title,
    }
    
    # 검색한 영화 정보 불러와 담기
    response = requests.get(BASE_URL + PATH, params = params).json()
    result = response.get('results')
    
    # 검색 내용이 없을 경우 None을 반환하기 위해 try, except 활용
    try:
        # 검색 영화중 첫 번째 id
        first_id = result[0]['id']

        # 검색한 첫 번째 id로 영화 정보 불러오기
        BASE_URL = 'https://api.themoviedb.org/3'
        PATH = f'/movie/{first_id}/recommendations'
        params = {
            'api_key' : 'e67fd4cae34071117f73a8090324311b',
            'language' : 'ko',
        }
        name_list = []
        response = requests.get(BASE_URL + PATH, params = params).json()
        result = response.get('results')
        
        # 불러온 영화 정보 제목 정리하기
        for movie in result:
            name_list.append(movie['title'])
    except:
        return None
    return name_list
    

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
