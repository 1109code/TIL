# 데이터 구조 활용

메서드(method)

ex)

List.append(10)

String.split()



### 파이썬 공식 문서의 표기법

* python 구문이 아니고 문법을 표현하기 위한 것

* str.replace(old,new [, count])
  * old, new는 필수 / [,count]는 선택적 인자

**=> 공식 문서 켜서 확인해보기**



### 문자열(String Type)

문자들의 나열(sequence of characters)

* 모든 문자는 str 타입(변경 불가능한 immutable)



### 문자열 조회/탐색 및 검증 메서드

**s.find(x)** : x의 **첫 번째 위치**를 반환. 없으면, **-1**을 반환 (**오류 X**)

**s.index(x)** : x의 **첫 번째 위치**를 반환. 없으면, **오류** 발생

**s.isalpha()** : **알파벳** 문자 여부

**s.isupper()** : **대문자** 여부

**s.islower()** : **소문자** 여부

**s.istitlle()** : **타이틀** 형식 여부 (타이틀 형식 = Hello , Hi 같이 대문자 + 소문자나열)



### 문자열 관련 검증 메서드 사용 예시

```python
print('abc'.isalpha()) # True
print('ㄱㄴㄷ'.isalpha()) # True
print('Ab'.isupper()) #False
print('ab'.islower()) # True
print('Title Title!'.istitle())
```



### 문자열 관련 검증 메서드

isdecimal() < isdigit < isnumeric

![image-20220725140023223](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220725140023223.png)



### 문자열 변경 메서드

s.replace(old, new[, count])

s. strip([chars])

s.split(sep=None, maxsplit=-1)

'separator'.join([iterable])

s.capitalize()

s.title()

s.upper()

s.lower()

s.swapcase()



### 문자열 변경

**.replace(old,new[, count])**

```python
print('coone'.replace('o', 'a')) # caane
print('wooooowoo'.replace,'o', '!', 2) # w!!ooowoo
```

**.strip([chars])**

```python
print('     와우!\n'.strip()) # '와우!'
print('     와우!\n'.lstrip()) # '와우!'
print('     와우!\n'.rstrip()) # '     와우!'
print('안녕하세요????'.rstrip('?')) # '안녕하세요'
```

**.split(sep=None, maxsplit=-1)**

```python
print('a,b,c'.split(',')) #['a', 'b', 'c']
print('a b c'.split()) # ['a', 'b', 'c']
print('서울시 강남구 00동'.split()[0]) # '서울시'
print('010-1234-1234'.split('-'))
```

**'separator'.join([iterable])**

```python
print('!'.join('ssafy')) #s!s!a!f!y'

print('  '.join['3', '5'])) # '3 5'
```



## 리스트

리스트는 대괄호([]) 혹은 list()를 통해 생성



**L.append(x)** : **마지막**에 항목 x 추가

**L.insert(i, x)**  : 인덱스 **i**에 항목 x 삽입

**L.remove(x)** : 첫 번째 x 제거

**L.pop()** : 리스트 가장 오른쪽 항목 반환 후 제거

**L.pop(i)** : 

**L.extend(m)** : += 과 같은 기능 (문자열 넣으면 한 글자씩 쪼개져서 들어감)

**L.index(x, start, end)** : 리스트 항목 중 가장 왼쪽에 있는 항목 x 인덱스 반환

**L.reverse** : 리스트 거꾸로 정렬

**L.sort()** : 

* sorted(numbers) 하면 원본은 그대로이고 얘만 정렬

**L.count(x)** : x 몇개 있는지 세기

**L.clear()** : 싹다 제거



## 튜플

여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용

* 리스트와의 차이점은 생성 후, 담고 있는 값 변경이 불가

### 튜플 관련 메서드

* 변경할 수 없기 때문에 값에 영향 미치지 않는 메서드만 지원
* 리스트 메서드 중 항목을 변경하는 메서드들을 제외하고 대부분 동일



### 멤버십 연산자

### 시퀀스형 연산자



## SET

중복되는 요소 없이 순서 상관 없는 데이터들의 묶음

* 인덱스 이용 접근 불가
* 중복 원소는 하나만 저장

집합

* 집합 연산 가능(여집합 제외)
* 중복된 값 존재 X

담고 있는 요소 삽입, 변경, 삭제 가능 ( 가변자료형, mutable)



### 셋 메서드

**s.copy()** : 셋의 **얕은 복사본** 반환

**s.add(x)** : x가 셋 s에 없다면 추가

**s. pop()** : 랜덤 항목 반환, 항목 제거, 비어있을 경우 KeyError

**s.remove(x)** : x를 셋 s에서 삭제, 항목 없을 경우 KeyError

**s.discard(x)** : x가 셋 s에 있는 경우, x를 셋 s에서 삭제 (없어도 에러 X)

**s.uppdate(t)** : 셋 t에 있는 모든 항목 중 셋 s에 없는 항목 추가

**s.clear()** : 모든 항목 제거

**s.isdisjoint(t)** : s가 셋 t의 서로 같은 항목을 하나도 갖고 있지 않는 경우 True

**s.issubset(t)** : s가 t의 하위 셋인 경우, True 반환

**s.issuperset(t)** : s가 t의 상위 셋인 경우, True 반환



주로 is~~ 는 True 나 False 반환

## 딕셔너리

3.7 부터는 ordered

### 딕셔너리 메서드

**d.clear()** : 모든 항목 제거

**d.copy()** : d의 얕은 복사본 반환

**d.keys()** : 

**d.values()** : 

**d.items()** :

**d.get(k)** : key를 통해 value를 가져옴 => None

**d.get(k, v)** :

**d.pop(k)** : 

**d.pop(k, v)** : 딕셔너리에 있으면 제거하고 해당 값 반환 그렇지 않으면 default반환 default 없으면 에러

**d.update([otehr])** :



## 얕은 복사와 깊은 복사

### 복사방법

할당 (assginment)

얕은 복사 (shallow copy) => 슬라이스 연산자로 복사 가능 but 2중 list 같은거는 리스트 안에 리스트는 주소가 그대로옴

깊은 복사 (deep copy) => 이때 import copy cop.deepcopy()하면 해결 가능

