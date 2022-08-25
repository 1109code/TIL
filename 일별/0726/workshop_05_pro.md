# 1. 평균 점수 구하기

```python
students = {
    'python' : 80,
    'web' : 83,
    'algorithm' : 90,
    'django': 89,
}

total = 0
cnt = 0

for subject, score in students.items():
    total += score
    cnt += 1
print(total / cnt)
```



# 2. 혈액형 분류하기

```python
def count_blood(blood_types):
    blood_dict = {}
	for blood_type+s in blood_types:
		if blood_dict.get(blood_type):
			blood_dict[blood_type] += 1

        else :
			blood_dict[blood_type] = 1
    return blood_dict
```

