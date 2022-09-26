# swea_1949 등산로 조성 문제풀이
# 2022-09-25

def search(s):
    global d, path_length, map_info, max_length, K, dig, check

    if path_length >= max_length:
        max_length = path_length

    for i, j in d:
        if 0 <= s[0] + i < N and 0 <= s[1] + j < N:
            # 다음 탐색 위치의 높이가 현재 탐색 위치 보다 낮을 때
            if map_info[s[0]][s[1]] > map_info[s[0] + i][s[1] + j]:
                path_length += 1
                map_info[s[0]][s[1]] += 1000000000000

                check.append([s[0] + i, s[1] + j])
                search([s[0] + i, s[1] + j])

                check.pop()
                map_info[s[0]][s[1]] -= 1000000000000
                path_length -= 1

            # 다음 탐색 위치의 높이가 현재 탐색 위치 보다 높거나 같고 공사 가능일 때
            elif dig == 1 and map_info[s[0] + i][s[1] + j] - map_info[s[0]][s[1]] < K:
                cur_K = map_info[s[0] + i][s[1] + j] - map_info[s[0]][s[1]] + 1

                map_info[s[0]][s[1]] += 1000000000000
                dig = 0
                path_length += 1
                map_info[s[0] + i][s[1] + j] -= cur_K

                check.append([s[0] + i, s[1] + j])
                search([s[0] + i, s[1] + j])
                check.pop()

                map_info[s[0]][s[1]] -= 1000000000000
                dig = 1
                path_length -= 1
                map_info[s[0] + i][s[1] + j] += cur_K


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    map_info = [list(map(int, input().split())) for _ in range(N)]

    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    max_length = 0
    dig = 1
    # 가장 높은 봉우리 찾기
    highest = 0

    for i in range(N):
        for j in range(N):
            if map_info[i][j] >= highest:
                highest = map_info[i][j]

    # 길 찾기
    for i in range(N):
        for j in range(N):
            check = [[i, j]]
            path_length = 1
            if map_info[i][j] == highest:
                # 등산로 찾기 함수
                search([i, j])

    print(f'#{tc} {max_length}')