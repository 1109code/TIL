from faker import Faker # 1 Faker라는 클래스를 임포트 하기 위한 코드이다.
fake = Faker() # 2 Faker는 클래스, fake는 Faker의 인스턴스이다.
# print(fake.name()) # 3 name()은 fake의 메서드이다.

# fake1 = Faker('ko_KR')
# Faker.seed(87654321)

# print(fake1.name())

# fake2 = Faker('ko_KR')
# print(fake2.name())

fake1 = Faker('ko_KR')
fake1.seed_instance(87654321)

print(fake1.name())

fake2 = Faker('ko_KR')
print(fake2.name())