# BOJ_2075 N번째 큰 수제풀이
# 2022-08-21
import heapq

N = int(input())
heap = []

# 처음 N개에 heap으로 저장해 놓기
for i in map(int, input().split()):
    heapq.heappush(heap, i)

# 이후 줄에 대해서 heap의 처음과 비교해(가장 작은것) a[j]가 더 크면
# pop 하고 a[j] 넣기
for i in range(1, N):
    a = list(map(int, input().split()))
    for j in range(N):
        if a[j] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, a[j])

# N번째 큰 수는 마지막 남은 거에서 가장 작은 수 이므로 출력
print(heapq.heappop(heap))