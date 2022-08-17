# swea_9489 문제풀이
# 2022-08-12

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    cnt_max = 0
    #  가로 1 연속으로 나오면 세기
    for i in range(N):
        cnt = 1
        for j in range(M-1):
            if board[i][j] == 1 and board[i][j+1] == 1:
                    cnt += 1
										# cnt가 최대면 최대값 초기화
                    if cnt > cnt_max:
                        cnt_max = cnt
						# 1이 연속으로 나오는게 아니면 cnt 초기화
            else:
                cnt = 1

    # 세로 : 가로와 동일한 방식이나 인덱스 비교가 행으로만 바뀜
    for j in range(M):
        cnt = 1
        for i in range(N-1):
            if board[i][j] == 1 and board[i+1][j] == 1:
                    cnt += 1
                    if cnt > cnt_max:
                        cnt_max = cnt
                
            else:
                cnt = 1
    
    print('#{0} {1}'.format(t+1, cnt_max))