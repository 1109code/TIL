# swea_5207 이진 탐색 문제풀이
# 2022-09-27
def binarySearch(n, S, key):
    low = 0
    high = n - 1
    flag = -1

    while low <= high:
        mid = low + (high - low) // 2

        if S[mid] == key:
            return mid

        elif S[mid] > key:
            if flag == 1:
                return -1
            else:
                flag = 1
                high = mid - 1

        else:
            if flag == 0:
                return -1
            else:
                flag = 0
                low = mid + 1
    return -1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()

    cnt = 0
    for b in B:
        check = binarySearch(len(A), A, b)
        if check != -1:
            cnt += 1

    print(f'#{tc} {cnt}')