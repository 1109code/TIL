class Dog1:
    kind = 'canine'

    def __init__(self, name):
        self.name = name

print('-Dog1-')
chanbin_dog = Dog1('Atto')
ej_dog = Dog1('ZzangA')
print(chanbin_dog.name)
print(ej_dog.name)

class Cat:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

hb_cat_1 = Cat('milk')
hb_cat_2 = Cat('Cream')
print(hb_cat_1.name) # type
print(hb_cat_2.name) # type

hb_cat_1.add_trick('hi')
hb_cat_2.add_trick('hello')
print(hb_cat_1.tricks)
print(hb_cat_2.tricks)

class Tiger:
    
    def __init__(self, name):
        self.name = name
        self.tricks = []
    
    def add_trick(self, trick):
        self.tricks.append(trick)

my_tiger = Tiger('Ccobi')
your_tiger = Tiger('싸버지')
print(my_tiger)
print(your_tiger)

print(my_tiger.name)
print(your_tiger.name)

my_tiger.add_trick('어흥')
your_tiger.add_trick('크항')

print(my_tiger.tricks)
print(your_tiger.tricks)

fruit ='apple'
print(fruit.upper())
print(str.upper('apple'))

def greeting(name):
    return f'hello, {name}'

print(greeting('youjin'))

class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'hello, {self.name}'

my_name = Person('승환')
print(my_name)
print(my_name.name)
print(my_name.greeting()) # hello jihye

class Greeting:

    def __init__(self, name):
        self.name = name

    
    def hello(self):
        return f'hello, {self.name}'

    def hihi(self):
        return f'hihi, {self.name}'
    def bye(self):
        return f'bye, {self.name}'

my_name = Greeting('jihye')
print(my_name.name)
print(my_name.hello())
print(my_name.hihi())
print(my_name.bye())

# 객체 지향
# 개발자의 눈에서 (관점에서) 편리하게 프로그래밍 하는
# SRP (Single Responsibility Principle) = 단일 책임원칙
# cordla <- 분리해서 관리하기 편리