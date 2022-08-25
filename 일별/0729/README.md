# PJT 02

### 이번 pjt 를 통해 배운 내용

* requests 라이브러리 사용하기

* URL 정보를 통해 정보 불러오기

* URL, PATH, params에 대해 알게 됨

* API 활용하는법

* 정보를 불러오기 위해 api_key가 필요하다는 것

  

## A. problem_a

* 요구 사항 : TMDB에서 인기 영화 목록을 응답 받아 개수 출력하기

* 결과 :

  * 문제 접근 방법 및 코드 설명

    ```python
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
        
    # 아래의 코드는 수정하지 않습니다.
    if __name__ == '__main__':
        """
        popular 영화목록의 개수 반환
        """
        print(popular_count())
        # 20
    ```
  
    
  
  * 이 문제에서 어려웠던 점

    * api_key라는 것을 처음 보아 가져오는 법이 생소했다.
    * URL을 불러와 작업을 하는 것이 아직은 익숙하지 않았다.
  
    
  
  * 내가 생각하는 이 문제의 포인트
  
    * api_key, language 등의 값을  BASE_URL에 추가해 데이터를 불러오고 활용할 수 있는가

## B. problem_b

* 요구 사항 : TMDB에서 현재 인기있는영화 목록 데이터를 가져와 평점 8이상의 영화 반환하기

* 결과 :

  * 문제 접근 방법 및 코드 설명

    ```python
    import requests
    from pprint import pprint
    
    
    def vote_average_movies():
        #데이터를 요청할 URL
        BASE_URL = 'https://api.themoviedb.org/3'
        PATH = '/movie/popular'
        params = {
            'api_key' : 'e67fd4cae34071117f73a8090324311b',
            'language' : 'ko',
            'region' : 'KR',
        }
        
        # 불러온 데이터 담기
        response = requests.get(BASE_URL + PATH, params = params).json()
        result = response.get('results')
        
        # result에 있는 movie 목록들 중 'vote_average'키 값이 8 이상이면 답안에 append
        answer = []
        for movie in result:
          if movie['vote_average'] >= 8:
            answer.append(movie)
        return answer
    # 아래의 코드는 수정하지 않습니다.
    if __name__ == '__main__':
        """
        popular 영화목록중 vote_average가 8 이상인 영화목록 반환
        (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
        """
        pprint(vote_average_movies())
        """
        [{'adult': False,
          'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
          'genre_ids': [28, 12, 878],
          'id': 634649,
          'original_language': 'en',
          'original_title': 'Spider-Man: No Way Home',
          'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                      '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                      '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                      '사상 최악의 위기를 맞게 되는데…',
          'popularity': 1842.592,
          'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
          'release_date': '2021-12-15',
          'title': '스파이더맨: 노 웨이 홈',
          'video': False,
          'vote_average': 8.1,
          'vote_count': 13954},
        ..생략..,
        }]
        """
    ```
  
    
  
  * 이 문제에서 어려웠던 점
  
    * 해당 문제의 경우 a번 문제를 수월하게 풀 수있으면 큰 어려움이 없었다.
    
  * 내가 생각하는 이 문제의 포인트
  
    * 데이터를 요청해 가져온 후 데이터를 활용해 원하는 자료만 걸러낼 수 있는가

## C. problem _c

* 요구 사항 : TMDB에서 현재 인기 있는 영화 목록을 가져와 평점이 높은 순으로 5개 영화 데이터 반환하기

* 결과 :

  * 문제 접근 방법 및 코드 설명

    ```python
    import requests
    from pprint import pprint
    
    
    def ranking():
        #데이터를 요청할 URL
        BASE_URL = 'https://api.themoviedb.org/3'
        PATH = '/movie/popular'
        params = {
            'api_key' : 'e67fd4cae34071117f73a8090324311b',
            'language' : 'ko',
            'region' : 'KR',
        }
        
        # 불러온 데이터 담기
        response = requests.get(BASE_URL + PATH, params = params).json()
        result = response.get('results')
    
        # 불러온 데이터 중 'vote_average'의  value값을 내림차순으로 정렬
        result.sort(key = lambda x:x['vote_average'], reverse = True)
        
        # 정렬된 값 중 처음 5번째 까지 반환
        top_5 = []
        for i in range(5):
          top_5.append(result[i])
        return top_5
    
    # 아래의 코드는 수정하지 않습니다.
    if __name__ == '__main__':
        """
        popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
        (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
        """
        pprint(ranking())
        """
        [{'adult': False,
          'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
          'genre_ids': [28, 18],
          'id': 361743,
          'original_language': 'en',
          'original_title': 'Top Gun: Maverick',
          'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                      '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                      '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                      '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
          'popularity': 911.817,
          'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
          'release_date': '2022-06-22',
          'title': '탑건: 매버릭',
          'video': False,
          'vote_average': 8.4,
          'vote_count': 1463},
        ..생략..,
        }]
        """
    ```
  
    
  
  * 이 문제에서 어려웠던 점
  
    * 영화 데이터를 sort 할 때 특정 키의 value값을 기준으로 반환하는 법을 몰랐어서 헤맸다(이번에 알게 됨)
    * 그 외에는 이전의 문제들과 유사해 큰 어려움은 없었다.
  
    
  
  * 내가 생각하는 이 문제의 포인트
  
    * 딕셔너리의 value값을 기준으로 정렬할 수 있는가?

## D. problem_d

* 요구 사항 : TMDB에서 영화를 검색해 첫번째 영화의 id값을 찾아 해당 영화의 추천 목록 가져오기

* 결과 :

  * 문제 접근 방법 및 코드 설명

    ```python
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
    
    ```
  
    
  
  * 이 문제에서 어려웠던 점
  
    * 'query'에 영화 제목을 입력해 검색할 수 있다는 점을 몰라 처음에 해메었다.
    * 검색 결과가 없을 경우 try, except문을 활용할 수 있다는 점이 흥미로웠다.
    * 데이터를 두번 요청해야 해서 복잡했다.
  
    
  
  * 내가 생각하는 이 문제의 포인트
  
    * 처음 요청한 데이터를 기반으로 정보를 추출해 새로운 데이터를 요청할 수 있는가
    * tyr, except문을 활용할 수 있는가

## E. problem_e

* 요구 사항 : 제공된 영화 제목을 검색해 첫번째 영화의 정보에서 출연진과 스태프 목록 걸러 가져오기

* 결과 :

  * 문제 접근 방법 및 코드 설명

    ```python
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
    
    ```
  
    
  
  * 이 문제에서 어려웠던 점
  
    * 출연진과 연출진의 데이터가 있는 credits의 자료 구성을 이해하기 힘들었다. (눈의 피로도 상승)
  
    
  
  * 내가 생각하는 이 문제의 포인트
  
    * 자유자재로 데이터를 요청해 원하는 정보만 추출해 정리할 수 있는가
    * try except문의 활용을 유연하게 할 수 있는가

## 후기

* 첫 주와 마찬가지로 관통 프로젝트는 이전의 학습 내용을 모두 활용해 해결해야 하기 때문에 복습을 하기 위한 최고의 수단이라고 생각되었다.
* 또한 단순 복습이 아닌 실제로 이론을 적용해 봄으로써 1석 2조의 이득을 얻을 수 있었다.
* requests 라이브러리를 제대로 활용할 수 있게 되어 유의미한 시간이었다.
* requests 로 할 수 있는 더 많은 내용들을 학습하고 싶은 욕구가 생긴다.
* 정보를 처리함에 있어 상당히 효율적인 툴이지 않을수 없었다.

