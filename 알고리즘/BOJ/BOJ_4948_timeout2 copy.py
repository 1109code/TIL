N = int(input())
flag = 0
cnt = 0
while N != 0:
    for i in range(N+1, 2*N+1):
        for j in range(2, i//2+1):
            if i%j==0:
                flag=1
                break

        if flag == 0:
            cnt += 1
        flag = 0
    print(cnt)
    cnt = 0
    N = int(input())
    