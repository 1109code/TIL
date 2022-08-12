# swea_1213_string 문제풀이
# 2022-08-12

for t in range(10):
    T = int(input())
    letter = input()
    sentance = input()    
    cnt = 0
    M = len(letter)
		
		# 슬라이싱으로 letter와 동일한지 확인
    for i in range(len(sentance)):
        if sentance[i:i+M] == letter:
            cnt += 1
    
    print('#{} {}'.format(t+1, cnt))