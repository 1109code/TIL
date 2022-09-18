# swea_1232 사칙연산
# 2022-09-15

def postorder(n):
    if n:
        postorder(int(ch1[n]))
        postorder(int(ch2[n]))
        cal.append(tree[n])


for t in range(10):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    ch1 = [0 for _ in range(N + 1)]
    ch2 = [0 for _ in range(N + 1)]

    cal = []

    for n in range(N):
        info = list(input().split())
        tree[int(info[0])] = info[1]

        if len(info) > 2:
            ch1[int(info[0])] = info[2]
            ch2[int(info[0])] = info[3]

    postorder(1)
    nums = []
    while cal:
        if cal[0] == '-':
            cal.pop(0)
            nums.append(-(nums.pop() - nums.pop()))
        elif cal[0] == '+':
            cal.pop(0)
            nums.append(nums.pop() + nums.pop())
        elif cal[0] == '*':
            cal.pop(0)
            nums.append(nums.pop() * nums.pop())
        elif cal[0] == '/':
            cal.pop(0)
            nums.append(1/(nums.pop() / nums.pop()))
        else:
            nums.append(int(cal.pop(0)))

    print('#{0} {1}'.format(t+1, round(nums[0])))