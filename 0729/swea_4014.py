def height_back(j):
    cnt = 1
    while j!=0:
        if board[i][j] == board[i][j-1]:
            cnt += 1
        else:
            break
        j -= 1
    return cnt

def height_front(j):
    cnt = 1
    while j!=N-1:
        if board[i][j] == board[i][j+1]:
            cnt += 1
        else:
            break
        j += 1
    return cnt

def height_top(j):
    cnt = 1
    while j!=0:
        if board[j][i] == board[j-1][i]:
            cnt += 1
        else:
            break
        j -= 1
    return cnt

def height_down(j):
    cnt = 1
    while j!=N-1:
        if board[j][i] == board[j+1][i]:
            cnt += 1
        else:
            break
        j += 1
    return cnt

T = int(input())

for t in range(T):
    N, X = map(int,input().split())
    board = []
    # 지형 정보
    for i in range(N):
        board.append(list(map(int, input().split())))

    # 가로
    # 왼쪽부터 높아지면 수평 길이랑 램프 길이 비교
    ramp = [0 for i in range(N)]
    way = 0
    flag = 0
    for i in range(N):
        for j in range(N-1):
            if board[i][j+1] - board[i][j] == 1:
                if height_back(j) >= X:
                    for k in range(X):
                        ramp[j-k] = 1
                else:
                    flag = 1
                    break
            # 높이 차이 2 이상
            elif board[i][j+1] - board[i][j] > 1:
                flag = 1
                break
        for j in range(N-1, 0, -1):
            if board[i][j-1] - board[i][j] == 1:
                if height_front(j) >= X:
                    for k in range(X):
                        if ramp[j+k] != 0:
                            flag = 1
                            break
                        else:
                            ramp[j+k] = 1
                else:
                    flag = 1
                    break
            elif board[i][j-1] - board[i][j] > 1:
                flag = 1
                break

        ramp = [0 for i in range(N)]
        if flag == 0:
            way += 1
        flag = 0
    
    #세로    
    # 위에서 아래로 높아지면 수평 길이와 램프길이 비교
    ramp = [0 for i in range(N)]
    
    flag = 0
    for i in range(N):
        for j in range(N-1):
            if board[j+1][i] - board[j][i] == 1 :
                if height_top(j) >= X:
                    for k in range(X):
                        ramp[j-k] = 1
                else:
                    flag = 1
                    break
            elif board[j+1][i] - board[j][i] > 1 :
                flag = 1
                break
        for j in range(N-1, 0, -1):
            if board[j-1][i] - board[j][i] == 1 :
                if height_down(j) >= X:
                    for k in range(X):
                        if ramp[j+k] != 0:
                            flag = 1
                            break
                        else:
                            ramp[j+k] = 1
                else:
                    flag = 1
                    break
            elif board[j-1][i] - board[j][i] > 1 :
                flag = 1
                break
        ramp = [0 for i in range(N)]
        if flag == 0:
            way += 1
        flag = 0
    
    print(f'#{t+1} {way}')