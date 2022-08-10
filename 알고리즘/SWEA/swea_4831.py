# swea_4831_전기버스 문제풀이
# 2022-08-09
# import sys
# sys.stdin = open('swea_4831_input.txt', 'r')

T = int(input())


for t in range(T): # 테스트 케이스 입력
    K, N, M = map(int, input().split()) #K, N, M 입력
    board = [0 for i in range(N+1)] # 충전소를 표시할 판
    charger = list(map(int, input().split())) # 충전소 입력
    for i in charger:
        board[i] = 1 # board에 충전소 저장
    
    now = 0 # 이동 후 현재 위치 저장할 공간
    cnt = 0 # 충전 횟수 저장 고악ㄴ

    while now+K < N: # 종점에 도착할 떄 까지
        flag = 0 # 종점에 도착할 수 없는 경우 확인을 위한 flag
        for i in range(now+K, now, -1): # 최대 이동거리부터 역으로 검사
            if board[i] == 1: # 가장 먼 곳에 충전소가 있으면
                cnt += 1 # 충전횟수 +1
                now = i # 충전 위치로 현재 위치 변경
                flag = 1 # 종점 도착 불가 아님을 표시
                break
        if flag == 0: # 최대 거리 내에 충전할 곳이 없으면 flag가 안켜짐
            cnt = 0 # 0 반환을 위해 
            break

    print('#{} {}'.format(t+1, cnt))

