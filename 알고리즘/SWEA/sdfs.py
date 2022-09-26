def dfs(x,y):
    global summ
    global sum_list
    summ += arr[x][y]   # 해당 위치를 summ에 더해주고

    if x!=N-1 and y!=N-1:   # 만약, 인덱스가 끝에 도달하지 않았다면
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N:    # 인덱스가 범위 내에 있다면
                dfs(nx,ny)
    elif x==N-1 and y==N-1:
        sum_list.append(summ[:])
        return