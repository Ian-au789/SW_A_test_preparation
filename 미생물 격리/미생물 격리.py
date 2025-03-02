# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV597vbqAH0DFAVl&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")


def cells_left(time, cells):

    if time == 0:
        result = 0
        for cell in cells:
            result += cell[2]
        return result

    locations = {}                               # 딕셔너리의 key를 좌표로 가지고 value를 미생물 개수와 방향으로 저장
    new_cells = []                               # 다음 재귀 호출에 넘겨줄 배열
    for cell in cells:
        cell[0] += dc[cell[3]][0]                # 다음 좌표로 이동
        cell[1] += dc[cell[3]][1]

        if field[cell[0]][cell[1]] == 1:         # 약품 칠해진 칸에 들어가면 방향 반대 및 미생물 절반 감소
            cell[2] //= 2
            if cell[3] % 2 == 1:
                cell[3] += 1
            else:
                cell[3] -= 1

        if (cell[0], cell[1]) not in locations:                     # 어떤 미생물도 가지 않은 위치라면 새로 저장
            locations[(cell[0], cell[1])] = [(cell[2], cell[3])]
        else:
            locations[(cell[0], cell[1])].append((cell[2], cell[3]))  # 어떤 미생물이 이미 갔다면 기존 key에 같이 저장

    for key in locations:
        # 해당 좌표에 미생물이 하나만 있으면 정보들을 다시 new_cell에 저장
        if len(locations[key]) == 1:
            new_cells.append([key[0], key[1], locations[key][0][0], locations[key][0][1]])

        # 같은 좌표에 있는 미생물은 크기를 비교해서 방향 설정 후 미생물의 총합과 함께 new_cell에 저장
        else:
            cell_max = 0
            group = 0
            for value in locations[key]:
                group += value[0]
                if cell_max < value[0]:
                    cell_max = value[0]
                    direction = value[1]

            new_cells.append([key[0], key[1], group, direction])

    return cells_left(time - 1, new_cells)


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    cell_list = [list(map(int, input().split())) for _ in range(K)]
    dc = {1:[-1, 0], 2:[1, 0], 3:[0, -1], 4:[0, 1]}

    field = [[0]*N for _ in range(N)]
    for k in range(N):
        field[0][k] = 1
        field[N-1][k] = 1
        field[k][0] = 1
        field[k][N-1] = 1

    print(f"#{t} {cells_left(M, cell_list)}")
