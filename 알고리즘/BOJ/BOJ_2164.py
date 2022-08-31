# BOJ_2164 카드2
# 2022-08-28

N = int(input())
q = []

front = -1
rear = -1
for i in range(1, N+1):
    q.append(i)
    rear += 1
while rear - front > 1:
    front += 1
    if rear-front == 1:
        break
    front += 1
    q.append(q[front])
    rear += 1

print(q[rear])