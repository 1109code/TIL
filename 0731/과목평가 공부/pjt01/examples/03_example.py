# open 및 json 모듈 사용예시

import json
<<<<<<< HEAD

=======
from pprint import pprint
>>>>>>> 11ab27d979a0876ad907e7d582334034af92d566

movie = open('sample.json', encoding='utf-8')
movie_detail = json.load(movie)

<<<<<<< HEAD
print(movie_detail)
=======
pprint(movie_detail)
>>>>>>> 11ab27d979a0876ad907e7d582334034af92d566
