def low_and_up(word):
    a = list(word.upper())
    for i in range(0, len(word), 2):
        a[i] = a[i].lower()
    ''.join(a)
    
    return a

word = 'Apple'
print(low_and_up(word))

word = ['A', 'P', 'P', 'L', 'E']
