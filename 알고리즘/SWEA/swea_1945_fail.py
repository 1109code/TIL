# swea_1945_간단한_소인수분해 문제풀이
# 2022-08-09

def isprime(N):
    for i in range(2, int(N**(1/2))+1):
        if N % i == 0:
            return False
    return True

T = int(input())
for t in range(T):
    N = int(input())
    prime = []
    cnt = []
    for i in range(2, N+1):
        if isprime(i):
            prime.append(i)
            cnt.append(0) 
    
    index = 0
    for i in prime:
        
        while N % i == 0:
            cnt[index] += 1
            N //= i
        index += 1
    
    print(cnt)