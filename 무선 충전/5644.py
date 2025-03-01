# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWXRDL1aeugDFAUo&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")

'''
문제 요약
1. A와 B는 주어진 경로를 따라 이동하며 해당 위치에서 이용 가능한 무선 충전기를 통해 충전
2. A와 B는 같은 위치에 있어도 되지만 같은 무선 충전기를 이용하면 충전량은 절반으로 감소
3. 해당 위치에 2개 이상의 무선 충전기를 이용할 수 있으면 원하는 것 선택 가능
4. A는 [0,0], B는 [9,9]에서 출발하여 주어진 경로를 이동하며 충전할 수 있는 최대치를 구해라
해결 전략
1. 10*10 배열을 만들고 각 위치에서 이용 가능한 무선 충전기 번호를 집합 형태로 저장
2. A와 B가 다음 경로로 이동할 때 마다 재귀 호출하는 DFS
3. 만약 A와 B의 사용 가능한 무선 충전기 번호의 교집합이 공집합이면 각자 이용가능한 무선 충전기의 충전량 중 최대치를 각자 충전
4. 교집합이 존재한다면 A와 B의 모든 조합을 시도해서 가장 큰 충전량의 합 저장
'''


def dfs(loc_a, loc_b, step, charge):
    global M
    delta = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]

    # 해당 위치에서 이용 가능한 무선 충전기 번호
    charge_a = field[loc_a[0]][loc_a[1]]
    charge_b = field[loc_b[0]][loc_b[1]]

    # A와 B가 같은 무선 충전 구역에 없는 경우
    if charge_a & charge_b == set():
        if len(charge_a) > 0:
            max_a = 0
            for a in charge_a:
                if max_a < chargers[a][3]:     # 각 사용자가 이용 가능한 최대 충전량 구하기
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
            for b in charge_b:                # 모든 조합 시도해보기
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
        next_b = [loc_b[0] + delta[route_b[step]][0], loc_b[1] + delta[route_b[step]][1]]
        return dfs(next_a, next_b, step+1, charge)

    # 경로 탐색이 끝나면 지금까지의 충전량 반환
    else:
        return charge


T = int(input())
for t in range(1, T+1):
    M, A = map(int, input().split())
    route_a = list(map(int, input().split()))
    route_b = list(map(int, input().split()))
    chargers = [list(map(int, input().split())) for _ in range(A)]


    # 10*10 공집합이 들어있는 배열 준비
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
