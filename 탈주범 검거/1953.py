# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5PpLlKAQ4DFAUq&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")


def bfs(width, height, now_step, next_step, time):
    global pos_loc

    # 탐색 횟수 종료 시 지금까지 탐색 위치 저장
    if time == 0:
        for cur_loc in now_step:
            if cur_loc not in pos_loc:
                pos_loc.append(cur_loc)
        return

    for cur_loc in now_step:
        # 현재 위치를 저장하고 터널 모양에 따른 델타 탐색 시작
        if cur_loc not in pos_loc:
            pos_loc.append(cur_loc)
            delta = tunnels[matrix[cur_loc[0]][cur_loc[1]]]

            # 다음 좌표가 아직 방문한 곳이 아니고 배열 내 범위에 들어있는 지, 터널이 존재하는지 확인
            for dc in delta:
                next_loc = [cur_loc[0] + dc[0], cur_loc[1] + dc[1]]
                if  (0 <= next_loc[0] < height and 0 <= next_loc[1] < width and next_loc not in pos_loc
                        and matrix[next_loc[0]][next_loc[1]] > 0):
                    check_delta = tunnels[matrix[next_loc[0]][next_loc[1]]]
                    connected = 0
                    # 다음 터널이 반드시 현재 터널과 연결되어 있어야 함
                    for d in check_delta:
                        if [next_loc[0] + d[0], next_loc[1] + d[1]] == cur_loc:
                            connected = 1
                            break
                    if connected:
                        next_step.append(next_loc)

    bfs(width, height, next_step, [], time - 1)


T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    tunnels = {1: [[1,0], [-1, 0], [0, 1], [0, -1]], 2: [[1, 0], [-1, 0]], 3: [[0, 1], [0, -1]],
             4: [[-1, 0], [0, 1]], 5: [[1, 0], [0, 1]], 6: [[1, 0], [0, -1]], 7: [[-1, 0], [0, -1]]}

    pos_loc = []
    bfs(M, N, [[R, C]], [], L-1)
    print(f"#{t} {len(pos_loc)}")
