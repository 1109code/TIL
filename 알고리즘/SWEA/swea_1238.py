# swea_1238 Contact 문제풀이
# 2022-09-13

for t in range(10):

    visited = [0 for _ in range(101)]
    call_list = [[] for _ in range(101)]
    N, s = map(int, input().split())
    info = list(map(int, input().split()))
    for i in range(0, N, 2):
        if info[i+1] not in call_list[info[i]]:
            call_list[info[i]].append(info[i+1])
    next_num = [s]

    while True:
        flag = 0
        for i in next_num:
            if visited[i] != 1:
                visited[i] = 1

        tmp = next_num
        next_num = []
        for i in tmp:
            for j in call_list[i]:
                if visited[j] != 1:
                    next_num.append(j)
                    flag = 1

        if flag == 0 :
            print('#{} {}'.format(t+1, max(tmp)))
            break