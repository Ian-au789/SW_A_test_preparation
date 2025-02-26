import sys
import itertools
sys.stdin = open("input.txt", "r")

"""
조합은 일단 모든 경우의 수를 만들고 시작한다. 
DFS로 풀면, 조합을 만들다가 가지치기를 할 수 있음 
"""
T = int(input())
for test_case in range(1, T + 1):
    # N = 벌통 크기 , M = 벌통의 개수, C : 꿀을 채취할 수 있는 최대 양
    N, M, C = list(map(int, input().split()))
    honey_matrix = [list(map(int, input().split())) for _ in range(N)]


    # 주어진 목록에서 각 꿀을 제곱해서 더한 값을 반환
    def cal_square_sum(num_list):
        # 담은 최대 용량이 C를 넘은 경우는 계산하지 않음
        if sum(num_list) > C:
            return 0
        # 각 꿀을 제곱해서 더하는 부분
        return sum(num ** 2 for num in num_list)

    # 주어진 목록에서 부분집합 중에서 제곱의 합이 가장 큰 값을 반환
    def cal_max_honey(honey_list):
        max_honey = 0  # 선택한 꿀들의 제곱의 합의 최대값을 저장할 변수
        for select_cnt in range(1, M + 1):  # 모든 부분집합에 대해서 순회
            # 모든 부분집합에 대해서 cal_squre_sum 함수를 실행
            # cal_squre_sum 함수는 리스트의 모든 인자의 제곱의 합을 반환하는 함수 (총 합이 C를 넘으면 0 반환)
            comb_list = list(map(cal_square_sum, itertools.combinations(honey_list, select_cnt)))
            max_honey = max(max_honey, max(comb_list))
        return max_honey

    # 총 수익을 저장할 변수
    max_sum = 0
    # 모든 꿀을 탐색하기
    for fst_i in range(N):
        # 벌통은 가로로 연속되게 선택할 수 있기 때문에
        # 일꾼이 선택할 수 있는 벌통의 개수(M) 개의 공간을 남겨두는 i(열)까지 선택하기
        # => 위를 고려안하면 리스트를 벗어났다는 에러가 발생함 ( M=2 일때, j를 끝까지 갔을 때를 예로 들기)
        for fst_j in range(N - M + 1):
            fst_select_honey_list = honey_matrix[fst_i][fst_j:fst_j+M]  # i, j 좌표로부터 m개를 선택
            fst_select_honey_max = cal_max_honey(fst_select_honey_list)

            for snd_i in range(fst_i, N):
                for snd_j in range(0, N - M + 1):
                    # i를 선택한 것 다음부터, 선택할 수 있는 경우를 찾아야함.
                    # 그러면 다음 줄의 0번째 인덱스부터 선택해서 경우를 찾아야하는데
                    # i랑 같은 줄의 경우에는 j가 i보다 이전에 있는 경우는 선택할 필요 없다.
                    if fst_i == snd_i and snd_j < fst_j + M:
                        continue
                    snd_select_honey_list = honey_matrix[snd_i][snd_j:snd_j+M]
                    snd_select_honey_max = cal_max_honey(snd_select_honey_list)

                    max_sum = max(max_sum, fst_select_honey_max + snd_select_honey_max)
    print(f"#{test_case} {max_sum}")
