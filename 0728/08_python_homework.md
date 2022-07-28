# 1. Circle 인스턴스 만들기

```python
class Circle:
    pi = 3.14

    def __init__(self,r,x,y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return Circle.pi*self.r*self.r

    def circumference(self):
        return 2*Circle.pi*self.r

    def center(self):
        return(self.x, self,y)

result = Circle(3, 2, 4)
print(result.area())
print(result.circumference())

# 결과값
# 28.259999999999998
# 18.84
```



# 2. Dog과 Bird는 Animal이다

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def run(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드덕!')

dog = Dog('꼽이')
dog.run()
dog.bark()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()

# 결과값
# 꼽이! 달린다!
# 꼽이! 짖는다!
# 구구! 걷는다!
# 구구! 먹는다!
# 구구! 푸드덕!
```



# 3. Module Import

> (a) : fibo
>
> (b) : fibo_recursion
>
> (c) : recursion