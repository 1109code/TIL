# swea_5186 이진수2 문제풀이
# 2022-09-21
def d_to_b(n):
    i = 0
    ans = ''
    while n:
        i += 1

        if i == 13:
            print(f'#{t + 1} overflow')
            break

        a = n - 2 ** (-i)
        if a >= 0:
            n = a
            ans += '1'
        else:
            ans += '0'


    if i <= 12:
        print(f'#{t + 1} {ans}')


T = int(input())

for t in range(T):
    N = float(input())
    d_to_b(N)