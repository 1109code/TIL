# BOJ_1991 트리 순회 문제풀이
# 2022-09-20
def pre(n):
    if n != '.' and n:
        print(n, end='')
        pre(ch1[n])
        pre(ch2[n])


def order(n):
    if n != '.' and n:
        order(ch1[n])
        print(n, end='')
        order(ch2[n])


def post(n):
    if n != '.' and n:
        post(ch1[n])
        post(ch2[n])
        print(n, end='')


N = int(input())

ch1 = dict()
ch2 = dict()

for i in range(N):
    info = list(input().split())
    ch1[info[0]] = info[1]
    ch2[info[0]] = info[2]

pre('A')
print()
order('A')
print()
post('A')
print()