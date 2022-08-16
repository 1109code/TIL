# swea_4864 문자열- 비교 문제풀이
# 2022-08-16

def skip_list(word):
    m = len(word)
    skip = [m for i in range(m)]
    for i in range(m):
        skip[i] = m - i - 1
    return skip

def search(letter, word, skip):
    if letter in word:
        idx = word.index(letter)
        return skip[idx]
    else:
        return len(word)

T = int(input())

for t in range(T):
    word = input()
    sentance = input()
    skip = skip_list(word)
    
    i = 0
    flag = 0

    while i <= len(sentance) - len(word):
        for j in range(len(word) - 1, -1, -1):
            if sentance[i + j] == word[j]:
                if j == 0:
                    flag = 1
                
            else:
                s = search(sentance[i+j], word, skip)
                i += s
                flag = 0
                break
                
        if flag == 1:
            print('#{0} 1'.format(t+1))
            break
    if flag == 0:
        print('#{0} 0'.format(t+1))