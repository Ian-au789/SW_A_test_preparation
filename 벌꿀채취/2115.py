# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5V4A46AdIDFAWu&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")

'''
1. 벌통의 크기 N, 선택 가능한 벌통의 수 M, 채취 가능한 최대 벌꿀양 C 주어짐
2. 가로로 연속된 M개의 벌통 채취, 단 서로 겹치면 안됨
3. 벌통의 꿀은 모두 채취해야 하고 채취 가능한 최대량을 넘기면 해당 벌통은 채취 불가
4. 각 벌통의 꿀의 양의 제곱만큼의 상품 가치

전략
1. 가로로 M개의 벌통을 선택해서 얻을 수 있는 최대 가격 각각 계산해서 행렬에 저장 -> (N-M+1)*N 행렬
2. 채집할 수 있는 최대량을 넘겼을 때 허용 가능한 최대값을 찾는 것이 관건
3. 각 일꾼이 겹치지 않는 거리를 유지하면서 탐색
'''


# 벌꿀 가격 계산
def how_much(honey_list):
    return sum(h**2 for h in honey_list)


# 제한을 넘지않는 최댓값 탐색
def possible_max(size, honey_list, limit):
    honey_list.sort()
    max_honey = [0]

    # M값이 최대 5라서 부분집합 사용
    for i in range(1 << size):
        check = []
        for j in range(size):
            if i & (1 << j):
                check.append(honey_list[j])

        if sum(check) > limit:                                  # 벌꿀 최대 채취량 넘으면 배제
            continue
        else:
            if how_much(check) > how_much(max_honey):           # 벌꿀 가격 계산 해봤을 때 가장 큰 경우 반환
                max_honey = check

    return max_honey


# 가능한 최대 가격 탐색
def max_profit(n_col, n_row, space):
    total_max = 0

    # 첫 번째 일꾼 [i][j] 순회, 그 이후의 인덱스만 탐색하는 두 번째 일꾼[m][n]이 채취한 벌꿀 가격의 최댓값 찾기
    for i in range(n_row):
        for j in range(n_col):
            m = i
            n = j
            case_max = 0

            while m != n_row:
                if m == i:                          # 일꾼 둘이 같은 열에 있으면 서로 겹치지 않아야함
                    while n-j < space:
                        n += 1

                if n >= n_col:                      # 행 하나 탐색 끝나면 다음 열로
                    n = 0
                    m += 1
                if 0 <= m < n_row and 0 <= n < n_col:
                    if case_max < honey_money[m][n]:
                        case_max = honey_money[m][n]

                n += 1

            if honey_money[i][j] + case_max > total_max:
                total_max = honey_money[i][j] + case_max

    return total_max


T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    honey_farm = []

    for _ in range(N):
        honey_row = list(map(int, input().split()))
        honey_farm.append(honey_row)

    # 각 일꾼이 해당 벌통을 골라서 얻을 수 있는 최대 수익
    honey_money = []
    for row in honey_farm:
        money_row = []
        for k in range(N-M+1):
            collect = sum(row[k:k+M])
            if collect <= C:
                money_row.append(how_much(row[k:k+M]))
            else:
                money_row.append(how_much(possible_max(M, row[k:k+M], C)))
        honey_money.append(money_row)

    print(f"#{t} {max_profit(N-M+1, N, M)}")
