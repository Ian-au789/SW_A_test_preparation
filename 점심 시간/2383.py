# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5-BEE6AK0DFAVl&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")





T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                people.append((i, j))
            elif matrix[i][j] > 1:
                stairs.append((i, j, matrix[i][j]))

    route = [[] for _ in range(len(people))]
    idx = 0
    for man in people:
        for stair in stairs:
            route[idx].append([abs(man[0] - stair[0]) + abs(man[1] - stair[1]), stair[2]])
        idx += 1

    # print(f"#{t} {}")