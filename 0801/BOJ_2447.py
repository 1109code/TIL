N = int(input())
board = [[] for i in range(N)]
board[0].append('*'*3)
board[1].append('*' + ' ' + '*')
board[2].append('*'*3)
def draw(N):
    j = 3
    if  j < N:   
        for i in range(N//3):
            board[i].append(3*f'{draw[N//3]}')
            board[i+1].append(f'{draw[N//3]}')
            board[i+2].append(3*f'{draw[N//3]}')
        return draw(N//3)
print(draw(N))

# 첫째줄에 다 더하고
# 둘째줄에 1 0 1
# 막줄에 다 더하고