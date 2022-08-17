# swea_1974 스도쿠 검증 문제풀이
# 2022-08-16

T = int(input())
for k in range(T):
    board = []
    count = [0 for i in range(9)]
    check = 1
    
    for i in range(9):
        board.append(list(map(int, input().split())))
    # 가로줄 check
    for i in range(9):
        for j in range(9):
            count[board[i][j]-1] += 1
        for j in range(9):
            if count[j] != 1:
                check = 0
        count = [0 for i in range(9)]
    
    # 세로줄 check
    for i in range(9):
        for j in range(9):
            count[board[j][i]-1] += 1
        for j in range(9):
            if count[j] != 1:
                check = 0
        count = [0 for i in range(9)]
    
    # 3*3 check
    for g in range(0,9,3):
        for i in range(0,9,3):
            for j in range(3):
                for h in range(3):
                    count[board[i+j][g+h]-1] += 1
            for j in range(9):
                if count[j] != 1:
                    check = 0
            count = [0 for i in range(9)]
    
    print(f'#{k+1} {check}')