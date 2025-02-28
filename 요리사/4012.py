# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWIeUtVakTMDFAVH&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
import itertools
sys.stdin = open("sample_input.txt")


def similar_food(size):
    result = 20000
    food_list = [m+1 for m in range(size)]
    trial = list(itertools.combinations(food_list, size//2))
    length = len(trial)

    for n in range(length // 2):
        food_a = trial[n]
        food_b = trial[length - 1 - n]
        taste_a = 0
        taste_b = 0

        for a in list(itertools.combinations(food_a, 2)):
            taste_a += taste[a]

        for b in list(itertools.combinations(food_b, 2)):
            taste_b += taste[b]

        gap = abs(taste_a - taste_b)

        if result > gap:
            result = gap

    return result

T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    matrix_transpose = list(map(list, zip(*matrix)))

    # 각 식재료 번호 조합을 key로 만든 음식의 맛을 value로 가지는 dictionary
    taste = {}
    for i in range(N):
        for j in range(i+1, N):
            taste[(i+1, j+1)] = matrix[i][j] + matrix_transpose[i][j]

    print(f"#{t} {similar_food(N)}")
