# swea_1859_백만장자프로젝트
# 2022-08-09

# def ahead_max(index):
#     max = board[index]
#     for i in board[(index+1):]:
#         if i > max:
#             max = i
#     return max-board[index]


# T = int(input())
# for t in range(T):
#     N = int(input())
#     board = list(map(int, input().split()))

#     sum = 0
#     for i in range(N-1):
#         sum += ahead_max(i)
    
#     print('#{0} {1}'.format(t+1, sum))

### 앞에서 부터 이중포문으로 돌리니깐 시간 초과


# 뒤에서부터 for문 한번만 도는 걸로 전략 변경
T = int(input())
for t in range(T):
    N = int(input())
    board = list(map(int, input().split()))
    
    # 뒤에서 2번째 값을 최대값으로 초기화
    max = board[N-1]
    # 차이를 더할 공간 초기화
    sum = 0
    # 뒤에서 2번째 부터 앞으로 오면서
    for i in range(N-2, -1, -1):
        # 값이 최대값 보다 작으면 빼서 sum에 더하기
        if board[i] < max:
            sum += max-board[i]
        # 값이 최대값 보다 크면 그 값을 최대값으로 초기화
        else:
            max = board[i]
    
    print('#{0} {1}'.format(t+1, sum))
