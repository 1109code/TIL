# swea_5178 노드의 합 문제풀이
# 2022-09-15
def post(n):
    post()


T = int(input())

for t in range(T):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        tree[a] = b

    k = N - M
    while k > 0:
        if 2 * k + 1 <= N:
            tree[k] = tree[2 * k] + tree[2 * k +1]
        else:
            tree[k] = tree[2 * k]
        k -= 1
    print('#{0} {1}'.format(t+1, tree[L]))
