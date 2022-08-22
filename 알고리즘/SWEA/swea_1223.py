# swea_1223_문제풀이
# 2022-08-22

for t in range(10):
    N = int(input())
    cal = input()
    stack = []
    answer = []
    level = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        '(': 0,
    }
    for number in cal:
        if number == '+' or number == '-' or number == '*' or number == '/':
            if (not stack) or level[stack[-1]] <= level[number]:
                stack.append(number)
            else:
                while level[stack[-1]] >= level[number]:
                    answer.append(stack.pop())
                    if not stack:
                        break
                stack.append(number)

        elif number == '(':
            stack.append(number)

        elif number == ')':
            while stack[-1] != '(':
                answer.append(stack.pop())
            stack.pop()

        else:
            answer.append(number)

    while stack:
        answer.append(stack.pop())

    cal_stack = []

    for i in answer:
        if i == '-':
            cal_stack.append(-(cal_stack.pop()-cal_stack.pop()))
        elif i == '+':
            cal_stack.append(cal_stack.pop() + cal_stack.pop())
        elif i == '*':
            cal_stack.append(cal_stack.pop() * cal_stack.pop())
        elif i == '/':
            cal_stack.append(1/(cal_stack.pop()/cal_stack.pop()))
        else:
            cal_stack.append(int(i))

    print('#{} {}'.format(t+1, cal_stack.pop()))