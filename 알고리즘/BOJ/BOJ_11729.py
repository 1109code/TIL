# BOJ_11729 하노이 탑 이동 순서 문제풀이
# 2022-08-17
def hanoi(n, a, b, c):
    if n == 1:
        print('{} {}'.format(a, c))
    else:
        hanoi(n-1, a, c, b)
        print('{} {}'.format(a, c))
        hanoi(n-1, b, a, c)
        
        return

N = int(input())
a , b, c = 1, 2, 3

print(2 ** N -1)
hanoi(N, a, b, c)

#1
#2
#4
#8