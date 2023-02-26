# BOJ_2075 N번째 큰 수제풀이
# 2022-08-21
import sys

N = int(sys.stdin.readline())
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

i = N-1
while i != -1:
    board[i].sort()
    if max(board[i-1]) 
    i -= 1

print(board[-1][-5])
