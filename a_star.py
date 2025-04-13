from typing import List, Tuple, Dict
import heapq

Coord = Tuple[int, int]

d_row = (-1, 0, 1, 0)
d_col = (0, 1, 0, -1)

def get_manhattan_distance(a: Coord, b: Coord) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def is_valid(matrix: List[List[int]], vis: List[List[bool]], y: int, x: int) -> bool:
    return (
        0 <= y < len(matrix) and
        0 <= x < len(matrix[0]) and
        not vis[y][x] and
        matrix[y][x] == 0
    )

def a_star(matrix: List[List[int]], start: Coord, dest: Coord) -> Tuple[int, List[Coord], List[List[bool]], List[List[int]]]:
    h, w = len(matrix), len(matrix[0])

    heuristic_cost = [[float('inf')] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 0:
                heuristic_cost[i][j] = get_manhattan_distance((i, j), dest)

    row, col = start
    dest_y, dest_x = dest

    vis = [[False] * w for _ in range(h)]
    came_from: Dict[Coord, Coord] = {}

    heap = []
    heapq.heappush(heap, (heuristic_cost[row][col], row, col))

    while heap:
        current_cost, row, col = heapq.heappop(heap)

        if (row, col) == (dest_y, dest_x):
            break

        if vis[row][col]:
            continue

        vis[row][col] = True
        g = current_cost - heuristic_cost[row][col]

        for i in range(4):
            adjy, adjx = row + d_row[i], col + d_col[i]
            if is_valid(matrix, vis, adjy, adjx):
                new_cost = g + 1 + heuristic_cost[adjy][adjx]
                heapq.heappush(heap, (new_cost, adjy, adjx))
                came_from[(adjy, adjx)] = (row, col)

    # 경로 복원
    path = []
    current = dest
    while current in came_from:
        path.insert(0, current)
        current = came_from[current]
    if path:
        path.insert(0, start)

    total_cost = len(path) - 1
    return total_cost, path, vis, heuristic_cost

# ----------------------
# ✅ 테스트 실행 예제
# ----------------------
if __name__ == "__main__":
    # 0 = 이동 가능, 1 = 장애물
    test_map = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]

    start = (0, 0)
    dest = (4, 4)

    total_cost, path, vis, heuristics = a_star(test_map, start, dest)

    print(f"최단 거리: {total_cost}")
    print(f"경로: {path}")
    print("맵 위에 경로 표시:")
    for i in range(len(test_map)):
        row = ""
        for j in range(len(test_map[0])):
            if (i, j) == start:
                row += "S "
            elif (i, j) == dest:
                row += "D "
            elif (i, j) in path:
                row += "* "
            elif test_map[i][j] == 1:
                row += "# "
            else:
                row += ". "
        print(row)
