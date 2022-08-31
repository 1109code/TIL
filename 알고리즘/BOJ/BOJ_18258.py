# BOJ_18258 큐2
# 2022-08-28
import sys

input = sys.stdin.readline

N = int(input())
q = []
front = -1
back = -1
for n in range(N):
    order = list(input().split())
    if order[0] == 'push':
        q.append(order[1])
        back += 1
    elif order[0] == 'pop':
        if front < back:
            print(q[front+1])
            front += 1
        else:
            print(-1)
    elif order[0] == 'size':
        print(back-front)
    elif order[0] == 'empty':
        if front == back:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if front < back:
            print(q[front + 1])
        else:
            print(-1)
    else:
        if front != back:
            print(q[back])
        else:
            print(-1)