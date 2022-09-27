# swea_5204 병합 정렬 문제풀이
# 2022-09-27


def merge_sort(m: list) -> list:
    if len(m) == 1:
        return m

    middle = len(m) // 2                            # 중간 값
    left = m[:middle]                               # 왼쪽/ 오른쪽 나누기
    right = m[middle:]

    left = merge_sort(left)                         # 왼쪽/ 오른쪽 나눠 정렬 함수 재귀
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    global cnt

    result = []
    if left[-1] > right[-1]:                        # 왼쪽 끝값이 왼쪽 끝 값보다 크면 세기
        cnt += 1

    while len(left) > 0 or len(right) > 0:          # 왼쪽 오른쪽 중 하나라도 남아 있을때 계속 반복
        if len(left) > 0 and len(right) > 0:        # 둘다 남아 있으면
            if left[-1] >= right[-1]:               # 왼쪽값이 크거나 같으면 왼쪽에서 꺼내서 추가
                result.append(left.pop())
            else:                                   # 아니면 오른쪽에서 꺼내서 추가
                result.append(right.pop())

        elif len(left) > 0:                         # 왼쪽만 남아 있으면 꺼내서 추가
            result.append(left.pop())

        elif len(right) > 0:                        # 오른쪽만 남아 있으면 꺼내서 추가
            result.append(right.pop())
    return result[::-1]                             # pop(0) 안쓰려고 pop()했으므로 최대값 부터 들어갔으므로 역순 반환


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    cnt = 0

    print(f'#{tc} {merge_sort(ai)[N//2]} {cnt}')
