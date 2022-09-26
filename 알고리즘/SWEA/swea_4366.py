# swea_4366 정식이의 은행업무 문제풀이
# 2022-09-21
def b_to_d(n):
    dec = 0
    for i in range(len(n)-1, -1, -1):
        dec += n[i] * 2 ** (len(n) - i - 1)
    return dec

def t_to_d(n):
    tri = 0
    for i in range(len(n)-1, -1, -1):
        tri += n[i] * 3 ** (len(n) -i -1)
    return tri

T = int(input())

for tc in range(1, T+1):
    flag = 0
    b = list(map(int, list(input())))
    t = list(map(int, list(input())))

    for i in range(len(b)):
        b[i] = b[i] ^ 1

        for j in range(len(t)):
            for k in range(3):
                tmp = t[:]
                tmp[j] = k
                if b_to_d(b) == t_to_d(tmp):
                    print(f'#{tc} {b_to_d(b)}')
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 1:
            break
        b[i] = b[i] ^ 1