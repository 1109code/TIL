# swea_5432 문제풀이
# 2022-08-12

T = int(input())

for t in range(T):
    stick = input()
    num_stick = 0
    cnt = 0
    # '(' 와 ')'를 분석해 막대기를 추가할지 감소할지 레이저를 쏠 지 판단
    for i in range(len(stick)-1):
        # (( 이면 막대기 개수 하나 추가
        if stick[i] == '(' and stick [i+1] == '(':
            num_stick += 1
        # )) 이면 막대기가 잘리지 않고 끝난거니깐 막대기 하나 줄이고 한번 세기
        elif stick[i] == ')' and stick [i+1] == ')':
            cnt += 1
            num_stick -= 1
        # () 이면 레이저를 쏜 것이니깐 지금까지 쌓여있는 막대 개수 세기
        elif stick[i] == '(' and stick[i+1] == ')':
            cnt += num_stick
            
    
    print('#{0} {1}'.format(t+1, cnt))