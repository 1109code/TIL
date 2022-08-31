# boj_2170 선긋기 문제풀이
# 2022-08-24
import sys

N = int(sys.stdin.readline())
a = []

for i in range(N):
    n, m = map(int, sys.stdin.readline().split())
    a.append((n, m))
a.sort(key=lambda x: (x[0], x[1]))

length = 0
cur = a[0][0]
end = a[0][1]

for i in range(len(a)-1):
    if end < a[i+1][0]:
        length += end - cur
        cur = a[i+1][0]
        end = a[i+1][1]
    if end >= a[i+1][0]:
        if end < a[i+1][1]:
            end = a[i+1][1]
length += end - cur

print(length)