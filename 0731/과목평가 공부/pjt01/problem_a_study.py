import json
from pprint import pprint

def movie_info(movie):
    information = {
        'id' : movie.get('id'),
        'title' : movie['title'],
        'poster_path' : movie['poster_path'],
        'vote_average' : movie['vote_average'],
        'overview' : movie['overview'],
        'genre_ids' : movie['genre_ids'],
    }
    return information

if __name__=='__main__':
    movie_json = open('data/movie.json', encoding = 'utf-8')
    movie_dict = json.load(movie_json)
    pprint(movie_info(movie_dict))