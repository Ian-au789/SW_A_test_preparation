# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWIeRZV6kBUDFAVH&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
import itertools
sys.stdin = open("sample_input.txt")


def dfs(idx, operator, calculation):
    global N
    if idx == N:
        result.append(calculation)
        return

    # 연산자 하나씩 시도해보면서 완전탐색
    else:
        if operator[0] > 0:
            operator[0] -= 1
            dfs(idx+1, operator, calculation + numbers[idx])
            operator[0] += 1

        if operator[1] > 0:
            operator[1] -= 1
            dfs(idx+1, operator, calculation - numbers[idx])
            operator[1] += 1

        if operator[2] > 0:
            operator[2] -= 1
            dfs(idx+1, operator, calculation * numbers[idx])
            operator[2] += 1

        if operator[3] > 0:
            operator[3] -= 1
            dfs(idx+1, operator, int(calculation / numbers[idx]))
            operator[3] += 1


T = int(input())
for t in range(1, T+1):
    N = int(input())
    op_list = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    result = []
    dfs(1, op_list, numbers[0])

    print(f"#{t} {max(result) - min(result)}")
