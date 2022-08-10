# swea_1945_간단한_소인수분해 문제풀이
# 2022-08-09


T = int(input())
prime = [2, 3, 5, 7, 11]
for t in range(T):
    cnt = [0] * 5
    N = int(input())
    index = 0
    for i in prime:
        while N % i == 0:
            cnt[index] += 1
            N //= i
        index += 1
    print('#', t+1, end=' ', sep='')
    for i in range(5):
        print(cnt[i], end=' ' )
    print('')