# 07. 객체 지향 프로그래밍(workshop)

## 1. pip

> (1) faker 라는 패키지를 설치하기 위한 명령어
>
> (2) gti bash 터미널에 실행해 설치 가능

## 2. Basic Usages

```python
from faker import Faker # 1 Faker라는 클래스를 임포트 하기 위한 코드이다.
fake = Faker() # 2 Faker는 클래스, fake는 Faker의 인스턴스이다.
fake.name() # 3 name()은 fake의 메서드이다.
```

## 3. Localiztion

> (a) : init
>
> (b) : self
>
> (c) : locale

## 4. Seeding the Generator

```python
fake1 = Faker('ko_KR')
Faker.seed(87654321)

print(fake1.name())

fake2 = Faker('ko_KR')
print(fake2.name())

#출력 결과
#이진호
#강은주

```

> seed()는 클래스 메서드로 매 실행 결과마다 동일한 이름이 출력되는 것으로 보아 seed()에 입력한 값을 토대로 클래스 변수를 변경하는 것으로 보인다.
>
> ```python
> @classmethod
>     def seed(cls, seed: Optional[SeedType] = None) -> None:
>         """
>         Hashables the shared `random.Random` object across all factories
> 
>         :param seed: seed value
>         """
>         Generator.seed(seed)
> ```
>
> 

```python
fake1 = Faker('ko_KR')
fake1.seed_instance(87654321)

print(fake1.name())

fake2 = Faker('ko_KR')
print(fake2.name())

#출력 결과
#이진호
#강은주  (<- 매번 바뀜)
```

> seed_instance()는 인스턴스 메서드로서 재귀를 통해 첫 입력 이후 인스턴스 메서드를 계속해서 변화하는 것으로 보인다.
>
> ```python
> def seed_instance(self, seed: Optional[SeedType] = None) -> None:
>         """
>         Creates and seeds a new `random.Random` object for each factory
> 
>         :param seed: seed value
>         """
>         for factory in self._factories:
>             factory.seed_instance(seed)
> ```