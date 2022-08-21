# BOJ_9012 괄호
# 2022-08-19

# 괄호의 모양이 바르게 구성된 문자열 = VPS


# 괄호를 담을 빈 stack
stack = []



# 테스트 케이스
T = int(input())

letter_dict = {
    ')' : '(',
    '(' : ')',
}

for t in range(T):
    # 테스트 케이스 입력 받을 공간 - str
    letters = input()
    for letter in letters:
        if letter == '(':
            stack.append(letter)
        else:
            if stack[-1] == 