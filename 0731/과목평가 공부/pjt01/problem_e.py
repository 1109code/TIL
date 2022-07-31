import json


def dec_movies(movies):
    dec_list = []
    for movie in movies:
        movie_json = open(f'data/movies/{movie["id"]}.json', encoding = 'utf - 8')
        movie_info = json.load(movie_json)
        if movie_info['release_date'][5:7] == '12':
            dec_list.append(movie_info['title'])
    return dec_list
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
