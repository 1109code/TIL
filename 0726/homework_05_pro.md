# 1. 모음은 몇 개나 있을까?

```python
def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for vowel in vowels:
		for a in word:
	        if vowel == a:
    		    cnt += word.count(vowel)
    return cnt
```



# 2. 문자열 조작

**Answer : (4)**



# 3. 정사각형만 만들기

```python
def only_square_area(widths, heights):
    square_combination = []
    
    for width in widths:
        for height in heights:
            if width == height:
                square_combination.append(width ** 2)
    return square_combination
                
```

