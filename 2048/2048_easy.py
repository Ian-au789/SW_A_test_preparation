# https://www.acmicpc.net/problem/12100

import sys
sys.stdin = open("input.txt")


def game(size, matrix, level, large):
    global obj

    if level == 5:
        return

    if obj > large:
        return

    for k in range(4):
        if k < 2:
            for j in range(size - 1, -1, -1):
                for i in range(size - 1, -1, -1):
                    if not matrix[i][j]:
                        continue
                    else:
                        matrix = trial(i, j, k, size, matrix, obj)
                        if not matrix:
                            obj *= 2
                            return

            matrix_copy = [matrix[_][:] for _ in range(size)]
            game(size, matrix_copy, level + 1, large)

        else:
            for j in range(size):
                for i in range(size):
                    if not matrix[i][j]:
                        continue
                    else:
                        matrix = trial(i, j, k, size, matrix, obj)
                        if not matrix:
                            obj *= 2
                            return

            matrix_copy = [matrix[_][:] for _ in range(size)]
            game(size, matrix_copy, level + 1, large)


def trial(i, j, k, size, matrix, large):
    ci = i
    cj = j
    check = 0

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    # 다음 이동 위치가 배열의 범위를 벗어나지 않으며, 비어있다면 이동
    while 0 <= ci + di[k] < size and 0 <= cj + dj[k] < size and not matrix[ci + di[k]][cj + dj[k]]:
        ci += di[k]
        cj += dj[k]

    if not matrix[i][j][1]:  # 아직 합쳐진 적 없는 숫자면 다음 블록 확인
        if 0 <= ci + di[k] < size and 0 <= cj + dj[k] < size:
            ni = ci + di[k]
            nj = cj + dj[k]

            if matrix[ni][nj][0] == matrix[i][j][0] and not matrix[ni][nj][1]:
                new_block = matrix[i][j][0] * 2
                if new_block > large:
                    return 0
                matrix[ni][nj] = (new_block, 1)
                matrix[i][j] = 0
                check = 1

    if not check:
        if ci != i or cj != j:
            matrix[ci][cj] = matrix[i][j]
            matrix[i][j] = 0

    return matrix


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

obj = 0
for a in range(N):
    for b in range(N):
        if board[a][b] > 0:
            c = board[a][b]
            if c > obj:
                obj = c
            board[a][b] = (c, 0)

game(N, board, 0, obj)
print(obj)
