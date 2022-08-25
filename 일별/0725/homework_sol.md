# 2. 가변 인자 리스트

```python
def my_avg(*args):
    count = 0
	total = 0
    for num in args:
        count += 1
        total += num
    return total / count
```



# 3. 반환값

```python
def my_func(a, b):
    c = a + b
    print(c)
result = my_func(3, 7)
```



# 4. 이름 공간(Namespace)

1. Local scope
2. Enclosed scope
3. Global scope
4. Built-in scope