# swea_1216 회문 2 문제풀이
# 2022-08-16

for t in range(10):
    t = int(input())
    board = [input() for _ in range(100)]
    
    max = 0
    for k in range(1, 101):
        for i in range(100):
            for j in range(100):
                if j+k <= 100:
                    word = board[i][j:j+k]
                    if word[::] == word[::-1]:
                        if len(word) > max:
                            max = len(word)
    
    for k in range(1, 101):
        for j in range(100):
            for i in range(100):
                if i+k <= 100:
                    word = []
                    for m in range(k):
                        word.append(board[i+m][j])
                    if word[::] == word[::-1]:
                        if len(word) > max:
                            max = len(word)

    print('#{0} {1}'.format(t, max))