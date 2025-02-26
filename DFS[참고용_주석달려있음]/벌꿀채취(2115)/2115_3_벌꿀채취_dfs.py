import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    # N = 벌통 크기 , M = 벌통의 개수, C : 꿀을 채취할 수 있는 최대 양
    N, M, C = list(map(int, input().split()))
    honey_matrix = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0  # 총 수익을 저장할 변수

    def dfs(honey_idx, honey_benefit, honey_sum, x, y):
        global part_sum  # ci, cj 에서 M개를 선택했을 때 얻을 수 있는 최대 이익

        # 여태까지 합한 꿀의 양이 C 보다 넘으면 가지치기
        if honey_sum > C: return

        # 가리키는 꿀의 인덱스가 M에 도달하면 중단
        if honey_idx == M:
            part_sum = max(part_sum, honey_benefit)
            return

        cnt_benefit = honey_matrix[x][y + honey_idx] ** 2
        cnt_sum = honey_matrix[x][y + honey_idx]
        # 부분집합을 구하는 것과 같이 진행
        # 현재 꿀을 선택하거나
        dfs(honey_idx + 1, honey_benefit + cnt_benefit, honey_sum + cnt_sum, x, y)

        # 현재 꿀을 선택하지 않거나
        dfs(honey_idx + 1, honey_benefit, honey_sum, x, y)

    for fst_i in range(N):
        for fst_j in range(N - M + 1):
            part_sum = 0
            # 부분집합의 최대 이익을 구한다.
            # 중간에 C를 넘으면 가지치기까지 가능할 듯합니다.
            # DFS 함수를 호출할 때 필요한 것 !
            # M개의 벌통의 부분집합을 구해서, 그 부분집합들의 총 이익을 구하는 함수를 만든다.
            # 1) 재귀를 중단할 파라미터 => 선택할 벌통의 개수 (M만큼 선택하면 중단)
            # 2) 우리가 누적해서 원하는 결과값 => 여태까지 각 꿀의 제곱을 합한 꿀의 이익
            # 또 필요한게 있을 것 같아요. 이건 다들 고민을 해봐야겠지만
            # 3) 시작 위치가 있어야 한다.
            # 4) 가지치기를 위한 (여태까지 합한 꿀의 양)
            dfs(0, 0, 0, fst_i, fst_j)
            fst_max = part_sum
            for snd_i in range(fst_i, N):
                for snd_j in range(0, N-M+1):
                    if fst_i == snd_j and snd_j < fst_j + M:
                        continue
                    part_sum = 0
                    dfs()
                    snd_max = part_sum
                    max_sum = max(max_sum, fst_max + snd_max)

    print(f"#{test_case} {max_sum}")
