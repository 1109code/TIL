# BOJ_2075 N번째 큰 수제풀이
# 2022-08-21
import sys

N = int(sys.stdin.readline())
board = []
for i in range(N):
    board.extend(list(map(int, sys.stdin.readline().split())))

board.sort()

print(board[-5])
