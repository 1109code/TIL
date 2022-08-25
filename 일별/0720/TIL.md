# 내장 함수 최소한으로 사용하기

* 리스트 중간값 뽑아오기

```python
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,
]

def count(list):
    c = 0
    for i in numbers:
        c+=1
    return c

def order(list):
    length = count(list)
    for i in range(1, length):
        change = list[i]
        k = i
        while change < list[k-1]:
            k -= 1

        temp = list[i]
        list[i] = list[k]
        list[k] = temp

for i in range(count(numbers)):
    order(numbers)
    
print(numbers[count(numbers)//2])
```

---

bubble sort 란?

* 서로 인접한 두 원소를 검사하여 정렬
* 1회전 수행하고 나면 가장 큰 자료가 맨 뒤로 이동 ing

---

len 함수 구현하기 (더 좋은 방법이 있을지도)

```python
c = 0
for i in numbers:
    c+=1
print(c)
```



# for - else 문

for 끝나고 else문 실력

but 중간에 break 하면 else 실행 안됨

---

* Decomposition

* Abstraction

* LEGB
  * Local
  * Enclosed function locals
  * Global
  * Built-in
