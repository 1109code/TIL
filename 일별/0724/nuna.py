# 스위치 한개 키고 끄는 함수
def sw_turn(idx):
    if sw_list[idx] == 0:
        sw_list[idx] = 1
    else:
        sw_list[idx] = 0

# sw_num : 스위치 갯수, sw_list : 스위치상태
sw_num = int(input())
sw_list = list(map(int, input().split()))

# st_num : 학생 수
st_num = int(input())

# 학생 수 만큼 스위치 바꾸기
for st in range(st_num):
    # gen : 성별, num : 스위치 번호
    gen, num = map(int, input().split())
    # 남자일 때
    if gen == 1:
        # 스위치 번호 비교해서 바꾸기
        for i in range(1, sw_num+1):
            if i % num == 0:
                sw_turn(i - 1)
    # 여자일 때
    else:
        idx = num - 1
        # 번호 받은 스위치 바꾸기
        sw_turn(idx)
        # 양쪽 대칭 비교하면서 같으면 바꾸기
        i = 1
        while num - i >= 1 and num + i <= sw_num:
            if sw_list[idx + i] == sw_list[idx - i]:
                sw_turn(idx + i)
                sw_turn(idx - i)
            
            else:
                break
            i += 1
    
for i in range(sw_num):
    print(sw_list[i], end=' ')
    if (i + 1) % 20 == 0: # 줄의 마지막일 때 19, 39 -> 줄바꿈
        print()