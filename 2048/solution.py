import sys
import copy
sys.stdin = open("input.txt")

def move_block(matrix, direction):
    N = len(matrix)
    merged = [[False]*N for _ in range(N)]
    moved = False

    def move(i, j, ni, nj):
        nonlocal moved
        matrix[ni][nj] = matrix[i][j] * 2
        matrix[i][j] = 0
        merged[ni][nj] = True
        moved = True

    if direction == 0:  # 위
        for j in range(N):
            for i in range(1, N):
                if matrix[i][j] == 0:
                    continue
                r = i
                while r > 0 and matrix[r - 1][j] == 0:
                    matrix[r - 1][j], matrix[r][j] = matrix[r][j], 0
                    r -= 1
                    moved = True
                if r > 0 and matrix[r - 1][j] == matrix[r][j] and not merged[r - 1][j]:
                    move(r, j, r - 1, j)
    elif direction == 1:  # 아래
        for j in range(N):
            for i in range(N - 2, -1, -1):
                if matrix[i][j] == 0:
                    continue
                r = i
                while r < N - 1 and matrix[r + 1][j] == 0:
                    matrix[r + 1][j], matrix[r][j] = matrix[r][j], 0
                    r += 1
                    moved = True
                if r < N - 1 and matrix[r + 1][j] == matrix[r][j] and not merged[r + 1][j]:
                    move(r, j, r + 1, j)
    elif direction == 2:  # 왼쪽
        for i in range(N):
            for j in range(1, N):
                if matrix[i][j] == 0:
                    continue
                c = j
                while c > 0 and matrix[i][c - 1] == 0:
                    matrix[i][c - 1], matrix[i][c] = matrix[i][c], 0
                    c -= 1
                    moved = True
                if c > 0 and matrix[i][c - 1] == matrix[i][c] and not merged[i][c - 1]:
                    move(i, c, i, c - 1)
    else:  # 오른쪽
        for i in range(N):
            for j in range(N - 2, -1, -1):
                if matrix[i][j] == 0:
                    continue
                c = j
                while c < N - 1 and matrix[i][c + 1] == 0:
                    matrix[i][c + 1], matrix[i][c] = matrix[i][c], 0
                    c += 1
                    moved = True
                if c < N - 1 and matrix[i][c + 1] == matrix[i][c] and not merged[i][c + 1]:
                    move(i, c, i, c + 1)
    return moved

max_block = 0

def dfs(board, depth):
    global max_block
    if depth == 5:
        for row in board:
            max_block = max(max_block, max(row))
        return

    for d in range(4):  # 0:위, 1:아래, 2:좌, 3:우
        copied = copy.deepcopy(board)
        moved = move_block(copied, d)
        if moved:
            dfs(copied, depth + 1)
        else:
            continue

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dfs(board, 0)
print(max_block)
