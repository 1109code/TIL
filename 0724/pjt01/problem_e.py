import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    december = []
    for movie in movies:
        id = movie['id']
        movie_file = open(f'data/movies/{id}.json', encoding = 'utf-8')
        movie_info = json.load(movie_file)
        if movie_info['release_date'][5:7] == '12':
            december.append(movie_info['title'])
    return december

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
