# BOJ_5430 문제풀이
# 2022-08-09
def R(board):
    return list(reversed(board))

def D(board):
    if len(board) == 0:
        return 'error'
    board.pop(0)
    return board

T = int(input())
for t in range(T):
    func = input()
    N = int(input())
    board = []
    arr = input()
    new_arr = []
    cnt = 0
    for i in range(len(arr)):
        if arr[i].isdigit():
            if arr[i-1].isdigit():
                new_arr.append(int(arr[i-1]) * 10 + int(arr[i]))
            else:
                board.append(arr[i])
    
    for i in range(len(func)):
        if func[i] == 'R':
            board = R(board)
        elif func[i] == 'D':
            if len(board) == 0:
                print('error')
                break
            board = D(board)
    
    result = list(map(int, board))
    print(result)
