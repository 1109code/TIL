# BOJ_2491 문제풀이
# 2022-08-14

N = int(input())
board = list(map(int, input().split()))

cnt = 1
cnt_max = 1
# 커지는 것 중 최대값 찾기
for i in range(len(board)-1):
    if board[i] <= board[i+1]:
        cnt += 1
        if cnt > cnt_max:
            cnt_max = cnt
    else:
        cnt = 1

# cnt 1로 초기화 하고 작아지는 것 중 최대값 찾기
cnt = 1
for i in range(len(board)-1):
    if board[i] >= board[i+1]:
        cnt += 1
        if cnt > cnt_max:
            cnt_max = cnt
    else:
        cnt = 1

print(cnt_max)