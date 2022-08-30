# BOJ_17298 문제풀이
# 2022-08-26

import sys
input = sys.stdin.readline

N = int(input())

board = list(map(int, input().split()))
stack = [-1]

for i in range(N-2, -1, -1):
    if board[i + 1] > board[i]:
        stack.append(board[i + 1])

    else:
        for k in range(len(stack)-1, -1, -1):
            if stack[k] > board[i]:
                stack.append(stack[k])
                break
            else:
                stack.append(-1)

print(*stack[::-1])