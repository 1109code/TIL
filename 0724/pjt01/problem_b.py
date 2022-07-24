import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.
    genre_names = []
    for i in range(len(movie.get('genre_ids'))):
        for names in genres:
            id = movie.get('genre_ids')[i]
            if id == names['id']:
                genre_names.append(names['name'])

    new_info = {
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_names' : genre_names
    }
    return new_info    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
