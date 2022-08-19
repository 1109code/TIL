# BOJ_9020 문제풀이
# 2022-08-18
def prime(n):
    prime_list = [2, 3]
    for i in range(2, n + 1):
        for j in range(2, int(i ** (1/2)) + 1):
            if i % j == 0:
                break
            else:
                if j == int(i **(1/2)):
                    prime_list.append(i)
                pass
        
    return prime_list

N = int(input())

even_list = []
for i in range(N):
    even_list.append(int(input()))

prime_list = prime(max(even_list))

for i in range(N):
    answer = []
    for number in prime_list:
        if (even_list[i] - number) in prime_list:
            answer. append([number, even_list[i] - number])
        if even_list[i] - number < number:
            break
    print(*answer[len(answer)//2])

# 해당 수 이하의 소수 구하고
# 합이 그 수 인거?
# 2 3 5 7