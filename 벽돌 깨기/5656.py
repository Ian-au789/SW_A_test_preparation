# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWXRQm6qfL0DFAUo&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")
from copy import deepcopy


'''
문제 요약
1. 구슬은 위에서 떨어지면서 맞는 벽돌 하나를 꺤다. 벽돌은 깨질 때 가지고 있는 번호 만큼 옆에 가로, 세로로 벽돌을 동시에 부순다.
2. 벽돌이 부서지는 현상은 동시에 연쇄적으로 일어난다. 벽돌이 깨지면서 다른 벽돌을 부수면 그 벽돌도 가로 세로로 다른 벽돌을 부순다.
3. 벽돌이 모두 부서지면 남은 벽돌은 아래로 떨어진다. 
4. 구슬을 모두 발사하고 난 뒤 남아있는 벽돌의 개수 중 가능한 최소값을 반환한다.
해결 전략
1. 구슬이 떨어지면서 0이 아닌 첫 번째 벽돌에 부딪힘
2. 델타 탐색과 DFS로 벽돌 깨기의 연쇄 작용 구현
3. 남은 벽돌이 떨어지는 건 열보다 행이 더 쉬움 (전치)
'''


# 벽돌 깨기
def break_brick(ci, cj, number, matrix_bricks):
    global W
    global H
    di = [1, 0, -1, 0]             # 델타 탐색
    dj = [0, 1, 0, -1]
    matrix_bricks[ci][cj] = 0

    for k in range(4):
        for l in range(1, number):        # 상하좌우로 벽돌이 깨지는 범위
            ni = ci + l * di[k]           # 다음에 탐색할 좌표
            nj = cj + l * dj[k]
            if 0 <= ni < W and 0 <= nj < H:
                if matrix_bricks[ni][nj] == 0:         # 벽돌이 없는 빈 공간은 스킵
                    continue
                elif matrix_bricks[ni][nj] == 1:       # 벽돌 번호가 1인 경우 부수기
                    matrix_bricks[ni][nj] = 0
                else:                                  # 벽돌 번호가 2 이상인 경우 해당 연쇄 작용 탐색 (재귀호출)
                    break_brick(ni, nj, matrix_bricks[ni][nj], matrix_bricks)
    return


# 구슬 쏘기 및 남은 벽돌 세기
def bricks_left(number, bricks):
    global W
    global H
    global result

    if number == 0:                    # 구슬을 모두 쐈다면 남아있는 벽돌의 수 세서 최솟값 갱신
        cnt = 0
        for i in range(W):
            for j in range(H):
                if bricks[i][j] > 0:
                    cnt += 1
        if result > cnt:
            result = cnt

    else:
        for i in range(W):                  # 모든 행에서 구슬 한 번씩 쏘기
            idx = 0
            while bricks[i][idx] == 0:      # 맨 위의 벽돌 찾기
                idx += 1
                if idx == H:
                    break

            if idx == H:                          # 해당 행에 벽돌이 없으면 다음 구슬 쏘기
                bricks_left(number - 1, bricks)

            else:
                new_bricks = deepcopy(bricks)
                break_brick(i, idx, new_bricks[i][idx], new_bricks)     # 벽돌에 부딪히면 벽돌 깨기

                # 스택을 써서 남은 벽돌을 아래로 떨어뜨리기
                for row in new_bricks:
                    stack = []
                    for j in range(H):
                        if row[j] > 0:
                            stack.append(row[j])
                    top = H-1
                    while top >= 0:
                        if len(stack) > 0:
                            row[top] = stack.pop()
                        else:
                            row[top] = 0
                        top -= 1

                bricks_left(number - 1, new_bricks)        # 다음 구슬 쏘기


T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    matrix_t = list(map(list, zip(*matrix)))                     # 남아있는 벽돌을 떨어뜨릴 때 행과 열을 바꾸면 더 편함
    result = W*H
    bricks_left(N, matrix_t)

    print(f"#{t} {result}")
