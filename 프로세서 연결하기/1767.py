# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf&&

import sys
sys.stdin = open("sample_input.txt")

'''
1. 델타 탐색으로 전선 확보
2. 만약 테두리에 위치한다면 무시
3. 
'''


def connect_line(ci, cj, number):
    global N

    for k in range(4):
        line = []
        block = 0
        while ci not in range(N) or cj not in range(N):
            ni = ci + delta[k]
            nj = ci + delta[k]

            if matrix[ni][nj] > 0:
                block = 1
                break

            else:
                line.append((ni, nj))

        if block == 0:
            for l in line:
                matrix[l[0]][l[1]] = number


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    cores = []
    n = 2
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                if i == 0 or i == N-1 or j == 0 or j == N-1:
                    continue
                else:
                    matrix[i][j] = n
                    cores.append((i, j))
                    n += 1

    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    print(matrix)

    # print(f"#{t} {}")