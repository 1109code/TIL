# swea_1242 암호코드 스캔 문제풀이
# 2022-09-20
def h_to_b(s):
    dic = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

    if s in dic:
        s = dic[s]
    else:
        s = int(s)

    bi = [0 for _ in range(4)]

    for i in range(3, -1, -1):
        bi[i] = (s % 2)
        s = s//2
    return bi


def decode(r):
    global secret
    for i in range(2):
        r.pop(0)
        r.pop()
    a = len(r) # 암호 길이
    b = a//56 # 이진 하나가 찾하는 길이

    cnt = 1
    for k in range(7):
        if r[k * b] == r[(k + 1) * b]:
            cnt += 1
            if k == 6:
                secret.append(cnt)
                cnt = 1

        elif r[k * b] != r[(k + 1) * b] and k == 6:
            secret.append(cnt)
            secret.append(1)
            cnt = 1

        else:
            secret.append(cnt)
            cnt = 1



T = int(input())

# answer_sheet = {
#     [3, 2, 1, 1]: 0,
#     [2, 2, 2, 1]: 1,
#     [2, 1, 2, 2]: 2,
#     [1, 4, 1, 1]
# }
for t in range(T):
    secret = []
    N, M = map(int, input().split())
    board = []
    for n in range(N):
        board.append(input())

    result = []
    password = []
    flag = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != '0':
                result.extend(h_to_b(board[i][j]))
                flag = 1
            elif board[i][j] == '0' and flag == 1:
                decode(result)
                result = []
                flag = 0
    print(secret)