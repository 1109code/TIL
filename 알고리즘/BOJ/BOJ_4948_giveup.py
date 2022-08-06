# 21:58 시작
#n이 소수인지 판별
def prime(n):
    if n==1:
        return False
    for i in range(2, n//2+1):
        if n%i==0:
            return False
    return True

cnt = 0
while True:
    N=int(input())
    if N==0:
        break
    for i in range(N+1, 2*N+1):
        if prime(i):
            cnt +=1
    print(cnt)
    cnt=0