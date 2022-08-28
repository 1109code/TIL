# BOJ_13335 트럭
# 2022-08-27

n, w, L = map(int, input().split())
a = list(map(int, input().split()))

stack = []
i = 0
time = 0
weight = []
while True:
    while i < n and sum(weight) + a[i] <= L:
        stack.append(0)
        weight.append(a[i])
        i += 1
        for t in range(len(stack)):
            stack[t] += 1
        if stack[0] == w:
            time += temp - stack[0]
            temp = stack.pop(0)
            weight.pop(0)
            if stack:
                for t in range(len(stack)):
                    stack[t] = temp - stack[t]

    print(stack)
    while True:
        for k in range(len(stack)):
            stack[k] += 1
        print(stack)
        if stack[0] == w:
            time += stack[0]
            temp = stack.pop(0)
            weight.pop(0)
            if stack:
                for t in range(len(stack)):
                    stack[t] = temp-stack[t]

            break


    if i == n and not stack:
        break



print(time)