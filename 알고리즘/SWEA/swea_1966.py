# swea_1966_숫자를정렬하자 문제풀이
# 2022-08-11

T = int(input())
for t in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))

    
    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[min_idx], numbers[i] = numbers[i], numbers[min_idx]
    # answer = ''
    # for i in range(N):
    #     answer += str(numbers[i])
    #     answer += ' '
    # print('#{} {}'.format(t+1, answer))
    print('#{}'.format(t+1), *numbers)
    
