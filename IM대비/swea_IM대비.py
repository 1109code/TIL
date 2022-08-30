def order(o):
    global password
    if o == 'I':
        a = int(secret.pop(0))
        add_list = []
        for i in range((int(secret.pop(0)))):
            add_list.append(secret.pop(0))
        password = password[:a] + add_list + password[a:]

    elif o == 'D':
        a = int(secret.pop(0))
        password = password[:a] + password[a + int(secret.pop(0)):]
    elif o == 'A':
        a = int(secret.pop(0))
        for i in range(a):
            password.append(secret.pop(0))
    return

for t in range(10):
    N = int(input())
    password = list(map(int, input().split()))
    M = int(input())

    secret = list(input().split())

    for i in range(M):
        order(secret.pop(0))
    print('#{} '.format(t+1), end= '')

    print(*password[:10], sep= ' ')