from typing import List, Tuple, Callable
import math
import heapq

# 방향 벡터
d_row = (-1, 0, 1, 0)
d_col = (0, 1, 0, -1)

def a_star(
    matrix: List[List[int]], start: Coord, dest: Coord
) -> Tuple[int, List[Coord]]:
    global d_row
    global d_col

    h = len(matrix)
    w = len(matrix[0])

    # 휴리스틱 코스트 테이블
    heuristic_cost = [[float("inf")] * w for _ in range(h)]

    # 휴리스틱 코스트 구하기
    for i in range(h):
        for j in range(w):
            if matrix[i][j]:
                heuristic_cost[i][j] = round(get_euclidean_distance((i, j), dest))

    row, col = start
    dest_y, dest_x = dest

    vis = [[False] * w for _ in range(h)]

    heap = []
    heapq.heappush(heap, (heuristic_cost[row][col] + 0, row, col))

    total_cost = 0
    # 어떤 노드에서 어떤 노드로 이동하는지 저장할 리스트
    came_from = []

    """
    heap이 비거나 목적 지점에 도착할 때까지 반복:
        heap에서 cost가 최소인 값을 꺼내서 방문처리를 한 후,
        유효한 인접 노드가 있으면 코스트를 계산해 힙에 넣는다.
    """
    while heap and (row, col) != (dest_y, dest_x):
        total_cost, row, col = heapq.heappop(heap)

        # Total Cost 에서 휴리스틱 코스트를 빼면 시작 지점에서 현재 지점까지의 실제 거리를 구할 수 있음
        depth = total_cost - heuristic_cost[row][col]

        # 방문 처리
        vis[row][col] = True

        # 유효한 인접 노드가 있으면 코스트를 계산해 힙에 넣는다.
        for i in range(4):
            adjy = row + d_row[i]
            adjx = col + d_col[i]
            if is_vaild(matrix, vis, adjy, adjx):
                total_cost = heuristic_cost[adjy][adjx] + depth + 1
                came_from.append(((row, col), (adjy, adjx)))
                heapq.heappush(heap, (total_cost, adjy, adjx))

    # came_from을 역순으로 추적하여 최단 경로를 찾음
    from_y, from_x = came_from[-1][0]
    paths = []

    for i in range(len(came_from) - 1, -1, -1):
        from_coord, to_coord = came_from[i]
        to_y, to_x = to_coord

        if from_y == to_y and from_x == to_x:
            from_y, from_x = from_coord
            paths.insert(0, to_coord)

    return total_cost, paths, vis, heuristic_cost