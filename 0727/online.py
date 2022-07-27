class dog():
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, type):
        self.name = name
        self.type = type
        dog.num_of_dogs += 1
        dog.birth_of_dogs += 1
        f'{self.name}(이)가 태어났습니다.'
    
    def bark(self):
        return f'{self.name} : 왈왈'
    
    def __del__(self):
        dog.num_of_dogs -= 1
        return f'{self.name}(이)가 무지개 다리를 건넜습니다.'
        
    
    @classmethod
    def get_status(cls):
        return f'총 탄생한 강이지는 {cls.birth_of_dogs}마리 입니다.\n현재 있는 강아지는 {cls.num_of_dogs}마리 입니다.'