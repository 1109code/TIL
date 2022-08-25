import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    max = 0
    for movie in movies:
        id = movie['id']
        movie_detail = open(f'data/movies/{id}.json', encoding = 'utf-8')
        movie_info = json.load(movie_detail)
        if movie_info['revenue'] > max:
            max = movie_info['revenue']
            max_movie = movie_info['title']
        
    return max_movie

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
