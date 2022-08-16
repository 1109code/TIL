# swea_4864 문자열- 비교 문제풀이
# 2022-08-16

T = int(input())
for t in range(T):
    word = input()
    sentance = input()
    
    for i in range(len(sentance) - len(word) + 1):
        flag = 1
        for j in range(len(word)):
            if word[j] == sentance[i + j]:
                pass
            else:
                flag = 0
        if flag == 1:
            print('#{} 1'.format(t+1))
            break

    if flag == 0:
        print('#{} 0'.format(t+1))