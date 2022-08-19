# SWEA_5658 보물상자 비밀번호 문제풀이
# 2022-08-19

def htod(number):
    number_change = {
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        'A' : 10,
        'B' : 11,
        'C' : 12,
        'D' : 13,
        'E' : 14,
        'F' : 15,
    }
    change = number_change[number]
    return change

def rot(numbers):
    new_numbers = numbers[1:] + numbers[0]
    return new_numbers

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    numbers = input()

    answer = []

    n_sum = 0

    for i in range(N//4):
        numbers = rot(numbers)
        
        k = N//4 - 1
        for j in range(N):
            number = (16 ** k) * htod(numbers[j])
            n_sum += number
            k -= 1

            if j % 3 == 2:
                if n_sum != 0:
                    answer.append(n_sum)
                n_sum = 0
                k = N//4 - 1
            
    answer = set(answer)
    answer = list(answer)
    answer.sort()

    print('#{} {}'.format(t+1, answer[-K]))