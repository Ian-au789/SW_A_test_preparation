# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AV5PoOKKAPIDFAUq&solveclubId=AZTP1QzqXnbHBIRD&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20&probBoxId=AZTeuPGad_vHBIOK

import sys
sys.stdin = open("sample_input.txt")

'''
문제 요약
1. 가장 높은 봉우리에서 시작하여 가로 세로 인접해 있는 높이가 더 낮은 봉우리로 하산하는 길을 만든다.
2. 긴 등산로를 만들기 위해 단 1번 봉우리의 높이를 K 만큼 깎을 수 있다. (깎은 지형의 높이는 1보다 낮을 수도 있다)
3. 모든 꼭대기를 탐색하며 가능한 가장 긴 등산로의 길이를 찾아서 출력하라

해결 전략
1. 델타 탐색으로 봉우리가 더 낮은 봉우리, 현재는 더 높거나 같지만 공사를 진행하면 더 낮아지는 봉우리를 찾아서 이동
2. 공사를 이미 진행했다면 그 이후로는 더 낮은 봉우리만을 탐색
3. 가능한 긴 등산로를 만들기 위해서는 공사 진행 시 현재 봉우리의 높이보다 1 낮게만 깎아야 한다 (중요!!!)
4. DFS에 input은 현재 위치의 좌표, 지금까지 지나온 경로, 공사를 시행한 유무, 현재 까지 등산로의 길이
'''


def dfs(mountain, cur_loc, path, work, cur_length):
    global N
    global K
    global result
    check = 0

    # 상하좌우 델타 탐색
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    # 아직 공사를 진행한 적 없을 경우
    if work == 1:
        for k in range(4):
            next_loc = [cur_loc[0] + di[k], cur_loc[1] +dj[k]]                                # 다음 이동할 봉우리
            if 0 <= next_loc[0] < N and 0 <= next_loc[1] < N and next_loc not in path:        # 해당 봉우리가 배열을 안 벗어나고 방문한 곳이 아니라면
                if mountain[cur_loc[0]][cur_loc[1]] > mountain[next_loc[0]][next_loc[1]]:     # 다음 봉우리 높이가 더 낮으면 그냥 진행
                    path.append(next_loc)
                    check += 1
                    dfs(mountain, next_loc, path, 1, cur_length + 1)
                    path.pop()

                elif (mountain[cur_loc[0]][cur_loc[1]] <= mountain[next_loc[0]][next_loc[1]] <    # 다음 봉우리가 더 높지만 공사하면 더 낮아질 경우
                      mountain[cur_loc[0]][cur_loc[1]] + K):
                    path.append(next_loc)
                    check += 1
                    before = mountain[next_loc[0]][next_loc[1]]                                   # 기존 봉우리 높이 기억
                    mountain[next_loc[0]][next_loc[1]] = mountain[cur_loc[0]][cur_loc[1]] - 1     # 최대한 긴 등산로를 만들려면 공사 후 높이가 딱 1 낮아야 함
                    dfs(mountain, next_loc, path, 0, cur_length + 1)
                    mountain[next_loc[0]][next_loc[1]] = before                                   # 해당 경로 탐색 후 원래 높이 복원
                    path.pop()

        # 이동할 수 있는 봉우리가 없다면 지금까지의 거리 비교해서 최댓값 갱신
        if check == 0:
            if cur_length > result:
                result = cur_length
            return

    # 이미 공사를 진행한 경우
    else:
        for k in range(4):
            next_loc = [cur_loc[0] + di[k], cur_loc[1] + dj[k]]
            if 0 <= next_loc[0] < N and 0 <= next_loc[1] < N and next_loc not in path:
                if mountain[cur_loc[0]][cur_loc[1]] > mountain[next_loc[0]][next_loc[1]]:
                    path.append(next_loc)
                    check += 1
                    dfs(mountain, next_loc, path, 0, cur_length + 1)
                    path.pop()


        if check == 0:
            if cur_length > result:
                result = cur_length
            return


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    matrix = []

    for _ in range(N):
        input_list = list(map(int, input().split()))
        matrix.append(input_list)

    top = []
    max_height = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > max_height:
                max_height = matrix[i][j]
                top = [[i,j]]

            elif matrix[i][j] == max_height:
                top.append([i, j])

    result = 0
    for loc in top:
        dfs(matrix, loc, [loc], 1, 1)

    print(f"#{t} {result}")