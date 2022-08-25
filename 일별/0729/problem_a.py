import requests


def popular_count():
    #데이터를 요청할 URL 작성
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/movie/popular'
    # api_key, 언어, 지역 을 params에 입력
    params = {
        'api_key' : 'e67fd4cae34071117f73a8090324311b',
        'language' : 'ko',
        'region' : 'KR',
    }
    # 데이터 불러오기
    response = requests.get(BASE_URL + PATH, params = params).json()
    # 불러온 데이터 저장
    result = response.get('results')
    # 데이터의 길이 == 영화 개수 반환
    return len(result)
    # URL = 'https://api.themoviedb.org/3/movie/popular?api_key=e67fd4cae34071117f73a8090324311b&language=en-US&page=1'
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20