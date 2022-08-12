# swea_1221 문제풀이
# 2022-08-12
# import sys
# sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())
board = {
        'ZRO' : 0,
        'ONE' : 1,
        'TWO' : 2,
        'THR' : 3,
        'FOR' : 4,
        'FIV' : 5,
        'SIX' : 6,
        'SVN' : 7,
        'EGT' : 8,
        'NIN' : 9,
    }
for t in range(T):
    case = list(input().split())
    numbers = input().split()

    i_numbers = []
    for number in numbers:
        i_numbers.append(board[number])
    
    i_numbers = sorted(i_numbers)

    print('#{}'.format(t+1))
    for number in i_numbers:
        for key, val in board.items():
            if number == val:
                print(key, end = ' ')