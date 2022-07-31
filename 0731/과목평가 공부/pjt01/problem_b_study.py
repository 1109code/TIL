import json
from pprint import pprint

def movie_info(movie, genre):
    information = {
        'id' : movie['id'],
        'title' : movie['title'],
        'poster_path' : movie['poster_path'],
        'vote_average' : movie['vote_average'],
        'overview' : movie['overview'],
    }
    information.update(genre_names = [])
    
    for i in movie['genre_ids']:
        for j in genre:
            if i == j['id']:
                information['genre_names'].append(j['name'])
    return information


if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding = 'utf - 8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding = 'utf - 8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))