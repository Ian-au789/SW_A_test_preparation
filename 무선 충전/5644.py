# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWXRDL1aeugDFAUo&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")


def dfs(loc_a, loc_b, step, charge):
    global M
    delta = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]

    charge_a = field[loc_a[0]][loc_a[1]]
    charge_b = field[loc_a[0]][loc_a[1]]

    # A와 B가 같은 무선 충전 구역에 없는 경우
    if charge_a & charge_b == set():
        if len(charge_a) > 0:
            max_a = 0
            for a in charge_a:
                if max_a < chargers[a][3]:
                    max_a = chargers[a][3]
            charge += max_a

        if len(charge_b) > 0:
            max_b = 0
            for b in charge_b:
                if max_b < chargers[b][3]:
                    max_b = chargers[b][3]
            charge += max_b

    # A와 B가 같은 무선 충전 구역에 있는 경우
    else:
        max_c = 0
        for a in charge_a:
            for b in charge_b:
                if a == b:
                    c = chargers[a][3]
                else:
                    c = chargers[a][3] + chargers[b][3]

                if max_c < c:
                    max_c = c
        charge += max_c

    # 경로가 아직 끝나지 않았을 때 탐색 계속
    if step < M:
        next_a = [loc_a[0] + delta[route_a[step]][0], loc_a[1] + delta[route_a[step]][1]]
        next_b = [loc_b[0] + delta[route_b[step]][0], loc_a[1] + delta[route_b[step]][1]]
        return dfs(next_a, next_b, step+1, charge)

    # 모든 경로를 완주하면 지금까지의 충전량의 합 반환
    else:
        return charge


T = int(input())
for t in range(1, T+1):
    M, A = map(int, input().split())
    route_a = list(map(int, input().split()))
    route_b = list(map(int, input().split()))
    chargers = [list(map(int, input().split())) for _ in range(A)]


    # 10*10 배열 준비
    field = []
    for _ in range(10):
        input_list = []
        for __ in range(10):
            input_list.append(set())
        field.append(input_list)

    # 10*10 배열에 무선 충전 구역 표시
    idx = 0
    for charger in chargers:
        ci = charger[1] - 1
        cj = charger[0] - 1
        for di in range(-charger[2], charger[2] + 1):
            d = charger[2] - abs(di)
            for dj in range(-d, d + 1):
                if 0 <= ci + di < 10 and 0 <= cj + dj < 10:
                    field[ci+di][cj+dj].add(idx)
        idx += 1

    result = dfs([0, 0], [9, 9], 0, 0)

    print(f"#{t} {result}")
