import json
from pprint import pprint


def movie_info(movies, genres):
    movies_info = []
    for movie in movies:
        info = {
            'id' : movie['id'],
            'title' : movie['title'],
            'poster_path' : movie['poster_path'],
            'vote_average' : movie['vote_average'],
            'overview' : movie['overview'],
            'genre_names' : [],
        }
        
        for ids in movie['genre_ids']:
            for genre in genres:
                if genre['id'] == ids:
                    info['genre_names'].append(genre['name'])
        
        movies_info.append(info)
    
    return movies_info

        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))