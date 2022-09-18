'''
정점 번호 V = 1~(E+1)
간선 수
부모 - 자식 순
4
1 2 1 3 3 4 3 5
4
2 1 2 3 1 4 1 5
'''

def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0: # 부모가 없으면 root
            return i


def preorder(n):
    if n:
        print(n, end=' ')    # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n): # 중위 순회
    if n:
        inorder(ch1[n])
        print(n, end=' ')
        inorder(ch2[n])


def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end=' ')

V = int(input())
arr = list(map(int, input().split()))
E = V - 1

# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V + 1)
ch2 = [0]*(V + 1)
# 자식을 인덱스로 부모 번호 저장
par = [0]*(V + 1)

# for j in range(0, E*2, 2):
#     p, c = arr[j], arr[j + 1]
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0: # 아직 자식이 없으면
        ch1[p] = c # 자식 1로 저장
    else:
        ch2[p] = c
    par[c] = p

for i in range(1, V+1):
    if par[i] == 0: # 부모가 없으면 root
        root = i
        break

root = find_root(V)

preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''