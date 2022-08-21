# BOj_2751_수 정렬하기 2 문제풀이
# 2022-08-21

import sys
N = int(sys.stdin.readline())

a = []

for i in range(N):
    a.append(int(sys.stdin.readline()))

a.sort()

for i in range(N):
    print(a[i])

# import sys

# N = int(sys.stdin.readline())

# a = [0] * N
# for i in range(N):
#     a[i] = int(sys.stdin.readline())

# for i in range(N):
#     for j in range(1, N):
#         if a[j] < a[j-1]:
#             a[j], a[j-1] = a[j-1], a[j]

# for i in range(N):
#     print(a[i])

