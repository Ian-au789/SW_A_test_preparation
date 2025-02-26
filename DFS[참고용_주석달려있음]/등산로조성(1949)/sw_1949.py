# 기본
import sys
sys.stdin = open("sample_input.txt")


def dfs(cx, cy, depth, visited, is_hint):
    global res, arr

    # 현재 좌표 
    c_h = arr[cx][cy]
    # 여태까지 나온 등산로의 길이를 매번 갱신 (갱신 안되면 말고 )
    res = max(depth, res)

    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if visited[nx][ny]: continue

        next_h = arr[nx][ny]
 
        # 낮은 지형인 경우, 힌트를 사용하지 않고 그대로 진행
        if c_h > next_h:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, visited, is_hint)
            visited[nx][ny] = False

        # 높은 지형인데, 힌트가 남아있고, 깎을 수 있는 범위라면 ?
        if c_h <= next_h and is_hint and next_h - K < c_h:
            # 내려갈 수 있도록, 최소한만큼만 깍고 내려가기
            arr[nx][ny] = c_h - 1
            # 이때 힌트는 사용했으므로, False로 전달
            dfs(nx, ny, depth + 1, visited, False)
            # 기존 높이로 복구
            arr[nx][ny] = next_h


dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 방문 여부를 확인하기 위한 변수 
    _visited = [[False] * N for _ in range(N)]
    res = 0

    # 가장 높은 봉우리의 높이를 찾기 
    max_h = max(max(row) for row in arr)

    # 가장 높은 봉우리 목록 찾기 
    max_h_list = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_h:
                max_h_list.append([i, j])


    # max_h_list = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == max_h]

    # 가장 높은 봉우리 목록에서 DFS 탐색 시작 
    for max_h_x, max_h_y in max_h_list:
        # 시작 지점은 방문했다고 하기 
        _visited[max_h_x][max_h_y] = True
        """
        DFS 파라미터
        - 누적해서 가져가고 싶은 값
        => 현재 위치, 현재까지 만든 등산로의 길이, 공사 기회, 방문 여부
        (모르겠으면? 주어진 거 다 넣자.)
        """
        dfs(max_h_x, max_h_y, 1, _visited, True)
        # 다른 지점에서도 DFS를 시작해야하기 때문에 원상복구한다. 
        _visited[max_h_x][max_h_y] = False

    print(f"#{test_case} {res}")
