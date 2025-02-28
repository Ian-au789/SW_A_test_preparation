def go(dy, dx, di, desert):
    global res, x, y
    # 사각형 만들고(방향 전환 3번) 출발 위치로 도착하면
    if di == 3 and x == dx and y == dy:
        res = max(res, len(desert))
        return

    # 벽을 벗어나지 않고, 이미 먹은 디저트가 아니면
    if (0 <= dx < N) and (0 <= dy < N) and (arr[dy][dx] not in desert):
        new_desert = desert + [arr[dy][dx]]
        ny = dy + direction[di][0]
        nx = dx + direction[di][1]

        go(ny, nx, di, new_desert)
        # 방향을 꺾어야 하면
        if di < 3:
            di += 1
            ny = dy + direction[di][0]
            nx = dx + direction[di][1]
            go(ny, nx, di, new_desert)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # 하우, 하좌, 상좌, 상우

    res = -1
    # 사각형으로 이동 가능한 위치만 시작위치로
    for y in range(0, N - 2):
        for x in range(1, N - 1):
            go(y, x, 0, [])
    print(f'#{tc} {res}')