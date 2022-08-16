# swea_3143 문제풀이
# 2022-08-16

T = int(input())

for t in range(T):
    A, B = input().split()
    i = 0
    cnt = 0
    
    # A에서 최대 B 전까지 확인
    while i <= len(A) - len(B):
        flag = 0
        # A에서 B의 시작 문자와 같으면 검사
        if A[i] == B[0]:
            # B 전체와 A가 일치하면
            for j in range(len(B)):
                if A[i + j] == B[j]:
                    # 일치함을 나타내기 위해 flag on
                    flag = 1
                    pass
                # 한 번이라도 일치하지 않으면 flag 끄기
                else:
                    flag = 0
                    break

            # 끝까지 깃발이 안내려가면
            if flag == 1:
                # 한번 세고
                cnt += 1
                # B 길이만큼 뛰어 넘기
                i += len(B)
            
            # B가 일치 하지 않으면 그냥 하나 세고 다음칸으로
            else:
                cnt += 1
                i += 1
        # B가 일치할 껀덕지가 없으면 그냥 하나세고 다음 칸으로
        else:
            cnt += 1
            i += 1

    cnt += len(A) - i

    print('#{} {}'.format(t+1, cnt))