# swea_9020 문제풀이
# 2022-08-18
# 선준님 풀이 다시 풀기

import sys

input = sys.stdin.readline

def prime(n):
    prime_list = []
    for i in range(2, n):
        flag = 0
        for j in range(2, int(i ** (1/2)) + 1):
            if i % j == 0:
                flag =1
                break
            else:
                pass
        if flag == 0:
            prime_list.append(i)
    return prime_list


N = int(input())

even_list = []
for i in range(N):
    even_list.append(int(input()))

even_max = max(even_list)
prime_list = prime(even_max)

for i in even_list:
    answer = []
    end = 0
    start = 0
    while prime_list[start] < i//2 + 1:
        if prime_list[end] + prime_list[start] == i:
            answer.append([prime_list[start], prime_list[end]])
        end += 1
        if prime_list[end] > i or end == len(prime_list) - 1:
            start += 1
            end = start
    print(*answer[-1])