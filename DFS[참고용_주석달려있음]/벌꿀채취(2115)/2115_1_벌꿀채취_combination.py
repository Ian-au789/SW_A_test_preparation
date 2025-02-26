import sys
import itertools
sys.stdin = open("input.txt", "r")

"""
벌통의 개수만큼 선택을 하고, 그 안에서 부분집합을 구한 후에
최대 수익을 찾아내고, 그 수익의 합을 구하자!
"""
T = int(input())
for test_case in range(1, T + 1):
    # N = 벌통 크기 , M = 벌통의 개수, C : 꿀을 채취할 수 있는 최대 양
    N, M, C = list(map(int, input().split()))
    honey_matrix = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0  # 총 수익을 저장할 변수

    # 수 목록이 들어오면 각 인자를 제곱해서 더한 값을 반환
    def cal_square_sum(num_list):
        # 넘어온 num_list (꿀의 조합), 이 조합이 최대 용량 C 를 넘으면 계산하지 않는다.
        if sum(num_list) > C:
            return 0

        # 각 꿀을 제곱해서 더하는 부분이다.
        return sum(num ** 2 for num in num_list)


    # 일꾼 1이 전체적으로 순회를 한다.
    # 단, 벌통의 개수(M) 직전까지만 순회를 한다.(j에서)
    for fst_i in range(N):
        # 벌통은 가로로 연속되게 선택해야한다.
        # 일꾼이 선택할 수 있는 벌통의 개수(M) 개의 공간을 남겨야한다.
        # 고려하지 않으면 인덱스 에러난다.
        for fst_j in range(N - M + 1):
            # 일꾼 1이 선택한 인덱스에서 M개의 벌통을 선택한 리스트
            fst_select_honey_list = honey_matrix[fst_i][fst_j:fst_j + M]
            # 위에서 일꾼 1이 선택한 M개의 리스트에서의 부분집합을 구하고,
            # 그 부분집합에서 가장 이익이 높은 값을 찾아보자.
            fst_select_honey_max = 0
            # 주어진 리스트에서 1개, 2개, ..., 전부를 선택하는 조합을 전부 구한다.
            for select_cnt in range(1, M+1):
                # 모든 부분집합을 구하고, 그 조합의 이익을 구해야한다.
                comb = itertools.combinations(fst_select_honey_list, select_cnt)
                # 각각의 조합들의 이익을 구한다.
                fst_comb_list = list(map(cal_square_sum, comb))
                # 위에 선언한 가장 이익이 높은 값으로 갱신할 수 있으면 갱신한다.
                fst_select_honey_max = max(fst_select_honey_max, max(fst_comb_list))

                # fst_i 줄부터 시작을 하고
                for snd_i in range(fst_i, N):
                    # 여기서는 처음부터 시작한다.
                    for snd_j in range(0, N - M +1):
                        # 근데 snd_i 랑 fst_i가 같은 줄에 있으면,
                        # snd_j 는 fst_i + M보다 앞의 선택을 하면 안된다
                        if fst_i == snd_i and snd_j < fst_j + M: continue

                        snd_select_honey_list = honey_matrix[snd_i][snd_j:snd_j + M]
                        # 위에서 일꾼 1이 선택한 M개의 리스트에서의 부분집합을 구하고,
                        # 그 부분집합에서 가장 이익이 높은 값을 찾아보자.
                        snd_select_honey_max = 0
                        # 주어진 리스트에서 1개, 2개, ..., 전부를 선택하는 조합을 전부 구한다.
                        for select_cnt in range(1, M + 1):
                            # 모든 부분집합을 구하고, 그 조합의 이익을 구해야한다.
                            comb = itertools.combinations(snd_select_honey_list, select_cnt)
                            # 각각의 조합들의 이익을 구한다.
                            snd_comb_list = list(map(cal_square_sum, comb))
                            # 위에 선언한 가장 이익이 높은 값으로 갱신할 수 있으면 갱신한다.
                            snd_select_honey_max = max(snd_select_honey_max, max(snd_comb_list))
                        # 우리가 결국 원하는건 first, second 최대 이익의 합이다.
                        max_sum = max(max_sum, fst_select_honey_max + snd_select_honey_max)

    print(f"#{test_case} {max_sum}")






















