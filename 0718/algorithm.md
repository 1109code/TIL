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

