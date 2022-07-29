def height_back(j):
    cnt = 0
    while j!=0:
        if board[i][j] == board[i][j-1]:
            cnt += 1
        else:
            break
        j -= 1
    return cnt

def height_front():
    cnt = 0
    while j != N-2:
        if board[i][j] == board[i][j+1]:
            cnt += 1
        else:
            break
        j += 1

    return cnt

T = int(input())

N, X = map(int,input().split())
board = []
for i in range(T):
    for i in range(N):
        board.append(list(map(int, input().split())))

# 가로
# 문제가 되는곳은 높이가 변할때
# 높이 변화 후 경사로 만큼 이어져야됨
# 반대쪽 부터 다시 돌 때 경사로가 겹치면 안됨
for i in range(N):
    for j in range(N-1):
        if board[i][j] < board[i][j+1]:
            if height_back(j+1) < X:
                break
            else:
                pass
        elif board[i][j] > board[i][j+1]:
            if height_front(j) < X:
                break
            else:
                pass




# 세로