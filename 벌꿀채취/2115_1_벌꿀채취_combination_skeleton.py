import sys
import itertools
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, 2):
    # N = 벌통 크기 , M = 벌통의 개수, C : 꿀을 채취할 수 있는 최대 양
    N, M, C = list(map(int, input().split()))
    honey_matrix = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0  # 총 수익을 저장할 변수

    def cal_square_sum(num_list):
        return sum(num ** 2 for num in num_list)


    # 일꾼 1이 전체적으로 순회하면서 M 개만큼 선택할겁니다.
    for fst_i in range(N):
        # 벌통은 M개만큼 연속되게 선택
        # 선택을 할 때, M개의 공간을 남겨야 해요. => 안하면 인덱스 에러남
        for fst_j in range(N - M + 1):
            # 일꾼 1이 선택한 M개의 벌꿀 리스트
            fst_select_honey_list = honey_matrix[fst_i][fst_j: fst_j + M]
            # 주어진 꿀을 넘지 않는 한도내에서 최대 이익을 구하자
            fst_select_honey_max = 0

            # 부분집합은 => 1부터 N개까지 각각 선택하는 조합의 모든 경우의 수
            for select_cnt in range(1, M+1):
                comb = itertools.combinations(fst_select_honey_list, select_cnt)
                # 조합에서 이익을 구한다.
                fst_comb_list = list(map(cal_square_sum, comb))
                # 이익들이 담긴 리스트에서 최대값을 구하고, 최대값이 갱신되면 갱신한다.
                fst_select_honey_max = max(fst_select_honey_max, max(fst_comb_list))

            for snd_i in range(fst_i, N):
                for snd_j in range(0, N-M+1):
                    if fst_i == snd_i and snd_j < fst_j + M: continue

                    snd_select_honey_list = honey_matrix[snd_i][snd_j:snd_j+M]
                    snd_select_honey_max = 0

                    # 부분집합은 => 1부터 N개까지 각각 선택하는 조합의 모든 경우의 수
                    for select_cnt in range(1, M + 1):
                        comb = itertools.combinations(snd_select_honey_list, select_cnt)
                        # 조합에서 이익을 구한다.
                        snd_comb_list = list(map(cal_square_sum, comb))
                        # 이익들이 담긴 리스트에서 최대값을 구하고, 최대값이 갱신되면 갱신한다.
                        snd_select_honey_max = max(snd_select_honey_max, max(snd_comb_list))
                    max_sum = max(max_sum, fst_select_honey_max + snd_select_honey_max)

    print(f"#{test_case} {max_sum}")






















