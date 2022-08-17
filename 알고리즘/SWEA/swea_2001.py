# swea_2001 파리퇴치 문제풀이
# 2022-08-16

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    # 파리들 있는 판
    board = [list(map(int, input().split())) for _ in range(N)]

    total_max = 0
    # 최대 N-M 인덱스 까지
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            # 파리채 크기만큼 파리 잡기
            for k in range(M):
                for l in range(M):
                    total += board[i+k][j+l]
            if total > total_max:
                total_max = total
    print('#{} {}'.format(t+1, total_max))