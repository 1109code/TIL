# swea_10726 이진수 표현 문제풀이
# 2022-09-21
def d_to_b(m):
    global ans

    while m:
        ans += str(m % 2)
        m = m//2


TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    ans = ''

    d_to_b(M)

    if ans[:N] == '1' * N:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')

