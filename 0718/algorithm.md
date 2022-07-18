# 파리잡기

```python
T = int(input())

# 회차
for i in range(T):
# N, M 입력 및 판 설정
    N, M = map(int,input().split())
    board = []
    sum = 0
    max = 0
    for j in range(N):
        board.append(list(map(int,input().split())))
        
# 파리채를 조금씩 움직이면서 범위 안 숫자 더하기
    for m in range(N-M+1):
        for n in range(N-M+1):
            for k in range(M):
                for q in range(M):
                    sum += board[m+k][n+q]
            if sum >= max:
                max = sum
            sum = 0
    print(f'#{i+1} {max}')
```



# 판 회전하기

```python
T = int(input())

#판 회전하는 함수
def turn(list,N):
    list_1 = [[0 for col in range(N)]for row in range(N)]
    for i in range(N):
        for j in range(N):
            list_1[i][j] = list[N-j-1][i]
    return list_1

# 기본 판, 90도, 180도, 270도 회전한 판
for k in range(T):
    board = []
    N = int(input())
    for i in range(N):
        board.append(list(map(int,input().split())))
    
    turn_1 = turn(board, N)
    turn_2 = turn(turn_1, N)
    turn_3 = turn(turn_2, N)

# 판 인쇄
    print(f'#{k+1}')
    for i in range(N):
        for j in range(N):
            print(turn_1[i][j], end='')
        print(' ',end = '')    
        for j in range(N):
            print(turn_2[i][j], end='')
        print(' ', end = '')
        for j in range(N):
            print(turn_3[i][j], end='')
        print('')
```



# 스도쿠 확인

```python
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
```

