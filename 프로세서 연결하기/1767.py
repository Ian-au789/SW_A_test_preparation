# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf&&

import sys
sys.stdin = open("sample_input.txt")

'''
1. 델타 탐색으로 전선 확보
2. 만약 테두리에 위치한다면 무시
3. 각 프로세서를 연결 안하는 경우, 그리고 연결 가능한 방향으로 연결하는 경우 전부 시도
4. 각 시도마다 다음 프로세서를 대상으로 재귀 호출
5. 프로세서 연결 성공 카운트, 연결할 때 마다 전선의 길이 카운트
6. 모든 리스트의 프로세서 탐색 종료 시 연결 성공이 최대치 갱신하면 갱신
7. 프로세서 개수는 동일하지만 전선 길이 줄어들면 최소치 갱신
'''


def connect_line(cores, success, length, field):
    size = len(cores)
    global connected
    global lines

    # 모든 프로세서 탐색 종료 시
    if size == 0:
        if success == connected:                 # 연결한 프로세서 개수가 동일하면
            lines = min(length, lines)           # 전선 최소 길이 갱신
        elif connected < success:                # 연결한 프로세서 개수가 늘었으면
            connected = success                  # 모든 값 갱신
            lines = length
        return

    if size + success < connected:               # 백트래킹 (남은 프로세서 개수를 다 연결해도 현재 최댓값에 못 미치면 탐색 의미 없음)
        return

    global N
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    core = cores[size-1]
    number = core[0]
    ci = core[1][0]
    cj = core[1][1]

    temp = cores.pop()
    connect_line(cores, success, length, field)   # 해당 프로세서를 연결않는 경우
    cores.append(temp)

    for k in range(4):
        line = []
        block = 0
        ni = ci + di[k]
        nj = cj + dj[k]

        # 4가지 방향으로 테두리에 연결 가능한지 탐색
        while ni in range(N) and nj in range(N):
            if matrix[ni][nj] > 0:
                block = 1                        # 막혀 있으면 표시
                break

            else:
                line.append((ni, nj))

            ni += di[k]
            nj += dj[k]

        if block == 0:                           # 막혀 있지 않으면 해당 경로에 전선 표시
            cnt = 0
            for loc in line:
                field[loc[0]][loc[1]] = number
                cnt += 1

            temp = cores.pop()                   # 탐색 완료한 프로세서 제거
            connect_line(cores, success + 1, length + cnt, field)           # 다음 프로세서 탐색
            cores.append(temp)                   # 해당 경로 탐색 이전으로 초기화

            for loc in line:
                field[loc[0]][loc[1]] = 0

    return


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    check_list = []
    n = 2
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                if i == 0 or i == N-1 or j == 0 or j == N-1:
                    continue
                else:
                    matrix[i][j] = n
                    check_list.append([n, (i, j)])
                    n += 1

    connected = 0
    lines = N**2

    connect_line(check_list, 0, 0, matrix)

    print(f"#{t} {lines}")
