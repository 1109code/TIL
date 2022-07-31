def gcd(a,b):
    if b == 0:
        return a
    else:
        return b, a%b

N, S = map(int, input().split())
A = list(map(int, input().split()))
ans = abs(S-A[0])

if S == 1:
    print(ans)
else:
    for i in range(1, N):
        ans = gcd(ans, abs(S-A[i]))
    print(ans)