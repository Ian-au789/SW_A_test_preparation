# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5V61LqAf8DFAWu&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")


def security_service(ci, cj, size):
    global max_h
    global houses
    global M
    global N

    cost = size ** 2 + (size - 1) ** 2
    cnt = 0

    # 탐색 범위가 최댓값보다 낮으면 탐색 중단
    if max_h > cost:
        return

    # 범위가 너무 커서 모든 집을 서비스해도 손해가 발생하면 탐색 불가
    if cost > houses * M:
        return

    for di in range(-(size - 1), size):
        for dj in range(-(size - 1 - abs(di)), (size - 1 - abs(di)) + 1):
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < N:
                if matrix[ni][nj] == 1:
                    cnt += 1

    if cnt * M >= cost:
        max_h = max(max_h, cnt)

    return


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_h = 0

    houses = 0
    for row in matrix:
        houses += sum(row)

    for i in range(N):
        for j in range(N):
            for k in range(N+1, 0, -1):
                security_service(i, j, k)

    print(f"#{t} {max_h}")
