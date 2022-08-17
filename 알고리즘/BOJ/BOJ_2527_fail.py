# BOJ_2527 문제풀이
# 2022-08-14

# 0 1 2 3 4 5 6 7
# x y p q x y p q

board = []
for i in range(4):
    board.append(list(map(int, input().split())))

result = []
for i in range(4):
    # 공
    if (board[i][6] < board[i][0]) or (board[i][4] > board[i][2]) or (board[i][7] < board[i][1]) or (board[i][5] > board[i][3]):
        result.append('d')
    
    # 한 점
    elif ((board[i][6] == board[i][0]) and ((board[i][7] == board[i][1]) or (board[i][5] == board[i][3]))) or ((board[i][4] == board[i][2]) and ((board[i][7] == board[i][1]) or (board[i][5] == board[i][3]))):
        result.append('c')

    # 직선
    elif (board[i][0] < board[i][6] < board[i][2]) and (board[i][7] == board[i][1] or board[i][5] == board[i][3]):
        result.append('b')
    elif (board[i][0] < board[i][4] < board[i][2]) and (board[i][7] == board[i][1] or board[i][5] == board[i][3]):
        result.append('b')
    elif (board[i][1] < board[i][7] < board[i][3]) and (board[i][0] == board[i][6] or board[i][2] == board[i][4]):
        result.append('b')
    elif (board[i][1] < board[i][5] < board[i][3]) and (board[i][0] == board[i][6] or board[i][2] == board[i][4]):
        result.append('b')
    
    else:
        result.append('a')

for i in range(4):
    print(result[i])



    
        # 이걸 다 나누라고?
        # 아닐거 같은데
        # 일단 ㄱ


# 겹칠 때
# x, y 중 하나라도 사이에 있을 때

# 직선
# 사이에 없고 x, y 중 하나가 같을 때

# 점
# 사이에 없고 하나의 x, y 가 완전 동일

# 공
# else