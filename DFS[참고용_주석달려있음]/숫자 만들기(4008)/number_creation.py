import sys
sys.stdin = open("number_creation_input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    op_input_list = list(map(int, input().split()))
    number_list = list(map(int, input().split()))

    max_num = -100000000
    min_num = 100000000

    def create_num(op_list, idx, res):
        global max_num, min_num

        # 모든 숫자를 다 계산했다면
        if idx == N:
            max_num = max(max_num, res)  # 최대값 갱신
            min_num = min(min_num, res)  # 최소값 갱신
            return

        # 남은 연산자에 대해서 하나씩 시도
        # 0 => '+', 1 => '-', 2 => '*', 3 => '/'
        for op_idx, op_cnt in enumerate(op_list):
            if op_cnt == 0:  # 남은 연산자가 없으면 해당 연산자는 skip
                continue
            tmp_res = res
            if op_idx == 0:  # +
                tmp_res += number_list[idx]
            elif op_idx == 1:  # -
                tmp_res -= number_list[idx]
            elif op_idx == 2:  # *
                tmp_res *= number_list[idx]
            elif op_idx == 3:  # /
                if number_list[idx] == 0:  # 분모가 0인 경우는 계산 X
                    return
                # ( -2 / 3 = 0이 나와야 함 )
                tmp_res = int(tmp_res / number_list[idx])
            else:
                print("주어진 입력이 아닙니다 ~~~~ ")

            op_list[op_idx] -= 1
            create_num(op_list, idx + 1, tmp_res)
            op_list[op_idx] += 1

    init_num = number_list[0]
    init_idx = 1

    # DFS 구현에 있어서 중요한 것
    # 1. 재귀호출을 중단할 파라미터
    # 2. 누적해서 가져갈 결과 파라미터
    create_num(op_input_list, init_idx, init_num)
    print(f"#{test_case} {max_num - min_num}")
