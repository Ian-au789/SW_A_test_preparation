# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5VwAr6APYDFAWu&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")

"""
문제 요약
1. 디저트 카페를 찾아 대각선으로만 이동
2. 어느 한 카페에서 출발하여 카페 투어 종착지로 출발점으로 돌아와야 한다
3. 카페 투어 중에 동일한 숫자의 디저트를 팔고 있는 카페를 2번 방문하지 않는다
4. 투어는 반드시 사각형 방향으로 이루어져야 한다.
5. 투어에 문제가 있으면 -1 출력, 투어를 마무리 한 다음에는 방문한 카페 수를 출력

해결 전략
1. 대각선 4 방향으로 배열을 벗어나지 않으며 델타 탐색
2. 지금까지 방문한 카페가 팔고 있던 디저트 숫자 저장하며 중복 피하기
3. 지금까지 방문한 카페 위치 저장하며 중복 피하기
4. 출발 지점 저장하고 있다가 돌아오면 탐색 중단하고 그 동안 지나온 카페 위치 반환하고 최댓값 갱신
5. 더 이상 진행이 불가하면 -1 반환
"""


def dfs(start, cur_loc, rotation, direction, turn, numbers, cnt):
    global result
    global N
    global dead_end

    # 시계방향
    if rotation == 0:
        di = [1, 1, -1, -1]
        dj = [1, -1, -1, 1]

    # 반시계방향
    else:
        di = [1, -1, -1, 1]
        dj = [1, 1, -1, -1]

    if turn == 4:
        if cur_loc == start:
            if cnt > result:
                result = cnt
        return

    k = direction // 4

    for _ in range(2):
        next_loc = (cur_loc[0] + di[k], cur_loc[1] + dj[k])

        if 0 <= next_loc[0] < N and 0 <= next_loc[1] < N and\
                next_loc not in dead_end and matrix[next_loc[0]][next_loc[1]] not in numbers:
            numbers.add(matrix[next_loc[0]][next_loc[1]])
            dfs(start, next_loc, rotation, k, turn, numbers, cnt + 1)
            numbers.remove(matrix[next_loc[0]][next_loc[1]])

        else:
            continue

        k = (k + 1)//4
        turn += 1

    return


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = []

    for _ in range(N):
        input_list = list(map(int, input().split()))
        matrix.append(input_list)

    result = -1

    dead_end = ((0, 0), (0, N - 1), (N - 1, 0), (N - 1, N - 1))
    for i in range(N):
        for j in range(N):
            if (i, j) in dead_end:
                continue

            else:
                for m in range(2):
                    for n in range(4):
                        dfs((i, j), (i, j), m, n, 0, {matrix[i][j]}, 1)

    print(f"#{t} {result}")
