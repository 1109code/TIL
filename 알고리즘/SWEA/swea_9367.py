# swea_9367 문제풀이
# 2022-08-12

T = int(input())

for t in range(T):
    N = int(input())
    carrot = list(map(int, input().split()))

    my_max = 1
    cnt = 1
    for i in range(N-1):
        if carrot[i+1]-carrot[i] == 1:
            cnt += 1
            if cnt > my_max:
                my_max = cnt
        else:
                cnt = 1
    print('#{0} {1}'.format(t+1, my_max))