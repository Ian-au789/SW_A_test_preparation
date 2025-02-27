def dfs(cur_loc, path, work, cur_length, N, K, mountain):
    global result
    check = 0

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    for k in range(4):
        next_loc = (cur_loc[0] + di[k], cur_loc[1] + dj[k])
        if 0 <= next_loc[0] < N and 0 <= next_loc[1] < N and next_loc not in path:
            if mountain[cur_loc[0]][cur_loc[1]] > mountain[next_loc[0]][next_loc[1]]:
                path.add(next_loc)
                check += 1
                dfs(next_loc, path, work, cur_length + 1, N, K, mountain)
                path.remove(next_loc)

            elif work == 1 and mountain[cur_loc[0]][cur_loc[1]] > mountain[next_loc[0]][next_loc[1]] - K:
                path.add(next_loc)
                check += 1
                original_height = mountain[next_loc[0]][next_loc[1]]
                mountain[next_loc[0]][next_loc[1]] = mountain[cur_loc[0]][cur_loc[1]] - 1  # 깎아서 이동
                dfs(next_loc, path, 0, cur_length + 1, N, K, mountain)
                mountain[next_loc[0]][next_loc[1]] = original_height  # 복구
                path.remove(next_loc)

    if check == 0:
        result = max(result, cur_length)


T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 위치 찾기
    max_height = max(max(row) for row in mountain)
    top = [(i, j) for i in range(N) for j in range(N) if mountain[i][j] == max_height]

    result = 0
    for loc in top:
        dfs(loc, {loc}, 1, 1, N, K, mountain)

    print(f"#{t} {result}")

