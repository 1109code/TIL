N = int(input())
board = [['*']]
number = 3

def star(number):
    for j in range(2):
        for i in range(number//3):
            board.append(board[i])
    
    for i in range(number):
        if i // (number//3) == 0:
            board[i] = board[i]*3
        elif i // (number//3) == 2:
            board[i] = board[i]*3
        else:
            board[i] = board[i] + list(' '*(number//3)) + board[i]
    if number == N:
        return board
    else:
        return star(number*3)

star(number)
for i in range(N):
    print(''.join(board[i]))