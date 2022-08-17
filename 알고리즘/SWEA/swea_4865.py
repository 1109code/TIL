# swea_4865.py 문제풀이
# 2022-08-16

T = int(input())

for t in range(T):
    word = input()
    word_dict = {}
    for i in range(len(word)):
        word_dict[word[i]] = 0
    
    sentance = input()
    for letter in word_dict:
        for i in range(len(sentance)):
            if sentance[i] == letter:
                word_dict[letter] += 1
    cnt_max = 0
    for cnt in word_dict.values():
        if cnt > cnt_max:
            cnt_max = cnt
    
    print('#{0} {1}'.format(t+1, cnt_max))