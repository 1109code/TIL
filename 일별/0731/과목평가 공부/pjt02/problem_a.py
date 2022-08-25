import requests


def popular_count():
    cnt = 0
    
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/movie/popular'
    params = {
        'api_key' : 'e67fd4cae34071117f73a8090324311b',
        'language' : 'ko',
        'region' : 'KR'
    }
    
    response = requests.get(BASE_URL + PATH , params = params).json()
    result = response.get('results')
    
    for movie in result:
        cnt+=1
        
    return cnt

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
