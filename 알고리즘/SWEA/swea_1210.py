# swea_1210_ladder1 문제풀이
# 2022-08-11

def l_end(ladder, s):
    lad = ladder
    di = [1, 0, 0]
    dj = [0, -1, 1]
    
    now = [0, s]
    
    flag_r = 0
    flag_l = 0
    while now[0] != 100:
        # 좌
        if -1 < now[1] + dj[1]:
            if (lad[now[0]][now[1]+dj[1]] == 1) and (flag_r != 1):
                now[1] += dj[1]
                flag_l = 1
                continue
        flag_r = 0
        # 우
        if now[1] + dj[2] < 100:
            if (lad[now[0]][now[1]+dj[2]] == 1) and (flag_l != 1):
                now[1] += dj[2]
                flag_r = 1
                continue
        flag_l = 0
        
        now[0] += di[0]
    
    return ladder[99][now[1]]


for t in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    for s in range(100):
        if ladder[0][s] == 1:
            if l_end(ladder, s) == 2:
                print('#{0} {1}'.format(T, s))
                break