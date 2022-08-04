# 21:58 시작
#n이 소수인지 판별
def prime(n):
    flag = 0
    if n==1:
        return False
    for i in range(2, n//2+1):
        if n%i==0:
            flag = 1
            break
        else:
            pass
    if flag==0:
        return True
    else:
        return False

cnt = 0
N=int(input())
while N!=0:
    for i in range(N+1, 2*N+1):
        if prime(i) == True:
            cnt +=1
    print(cnt)
    cnt=0
    N=int(input())