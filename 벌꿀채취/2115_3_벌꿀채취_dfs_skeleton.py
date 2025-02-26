import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    # N = 벌통 크기 , M = 벌통의 개수, C : 꿀을 채취할 수 있는 최대 양
    N, M, C = list(map(int, input().split()))
    honey_matrix = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0  # 총 수익을 저장할 변수

    # 선택할 벌통의 인덱스, 여태까지 선택한 벌통의 이익, 벌통의 합
    def dfs(honey_idx, honey_benefit, honey_sum):
        global part_sum

        # 백트래킹 ,
        # 여태까지 선택한 꿀들의 합이 이미 C를 넘었으면, 이득을 알아봤자 뭐함 ??
        if honey_sum > C: return

        # 선택할 벌통이 M에 도달하면, 최대값 갱신한다.
        if honey_idx == M:
            part_sum = max(part_sum, honey_benefit)

        cnt_sum = honey_matrix[fst_i][fst_j + honey_idx]
        cnt_benefit = honey_benefit[fst_i][fst_j + honey_idx] ** 2

        # 오른쪽 꿀을 선택
        # BFS 오른쪽을 선택했을 때, 다 터졌을대의 총합

        # dfs(honey_idx + 1, honey_benefit + cnt_benefit, honey_sum + cnt_sum)
        dfs(honey_idx + 1, honey_benefit + "오른쪽 선택했을 때 총합")

        # 위에 꿀을 선택
        dfs(honey_idx + 1, honey_benefit + "위에 선택했을 때 값", honey_sum)

        # 왼쪽에 꿀을 선택
        dfs(honey_idx + 1, honey_benefit + "왼쪽에 선택했을 때 값", honey_sum)

        # 아래 꿀을 선택
        dfs(honey_idx + 1, honey_benefit + "아래 에 선택했을 때 값", honey_sum)

        dfs(honey_idx + 1, honey_benefit)

    for fst_i in range(N):
        for fst_j in range(N-M+1):
            part_sum = 0
            # 부분집합의 최대 이익을 구하시오.
            # 부분집합 => DFS => 한 인덱스에 대해서 선택 O, 선택 X 이걸 결정하고, 재귀적으로 다음 인덱스로 넘겨서, 그 다음 인덱스에 대해서 선택
            # DFS 함수로 호출할떄, 어떤 거부터 하면 되냐면요
            # 1) 재귀를 중단할 파라미터 => 선택할 벌통의 인덱스다. ( M에 도달하면 재귀호출을 중단 )
            # 2) 우리가 누적해서 가져가고 싶은 값 ! => ( 여태까지 선택한 꿀들의 합, 선택한 꿀들의 이익 )
            dfs(0, 0, 0)
            fst_max = part_sum

            for snd_i in range(fst_i, N):
                for snd_j in range(0, N-M+1):
                    if fst_i == snd_i and snd_j < fst_j + M: continue

                    part_sum = 0
                    dfs(0, 0, 0, snd_i, snd_j)
                    snd_max = part_sum
                    max_sum = max(max_sum, fst_max + snd_max)


    print(f"#{test_case} {max_sum}")
