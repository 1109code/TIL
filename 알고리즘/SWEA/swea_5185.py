# swea_5185 문제풀이
# 2022-09-20
def h_to_b(num):
    sheet = {                     # 16진수 알파벳 정수로
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }
    if num in sheet:                # 문자면 sheet에 따라 정수 변환
        num = sheet[num]
    else:                           # 숫자면 int화
        num = int(num)

    bi = [0 for _ in range(4)]

    for i in range(3, -1, -1):      # 뒤에서부터 bi에 입력
        bi[i] = str(num % 2)        # 나머지는 입력
        num = num // 2              # 몫은 다시 num으로 초기화
    return bi


T = int(input())

for t in range(T):
    N, numbers = input().split()
    result = ""
    for n in range(int(N)):         # 입력 수 만큼 순회하며
        for let in h_to_b(numbers[n]):      # 문자들을 h_to_b 함수로 변환하여
            result += let                   # 결과에 더하기

    print(f'#{t+1} {result}')