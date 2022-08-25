def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for vowel in vowels:
	    for a in word:
	        if vowel == a:
                cnt += word.count(vowel)
    return cnt

print(count_vowels('apple'))