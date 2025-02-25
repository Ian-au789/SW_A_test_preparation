# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWIeW7FakkUDFAVH&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")

'''
활주로 건설 조건
1. 높이가 1 높아지거나 낮아지면,
2. 높이가 낮은 항목이 최소 X개 존재해야 한다
3. 건설된 활주로가 서로 겹치면 불가능
'''


def possible_runway(size, length, matrix):
    available = 0

    for row in matrix:              # 행 탐색
        unavailable = 0
        runway = [0]*size
        idx = 1

        while idx < size:
            if row[idx] == row[idx-1] + 1:              # 지형의 높이가 1 높아진 경우
                for j in range(length):                 # 경사로의 길이만큼 이전에 낮은 지형이 존재했다면 카운트
                    if 0 <= idx - 1 - j < size:

                        if row[idx - 1 - j] != row[idx] - 1:  # 경사로 길이가 부족하면 건설 불가능
                            unavailable = 1
                            break

                        else:
                            if not runway[idx - 1 - j]:     # 다른 경사로와 겹치면 건설 불가능
                                runway[idx - 1 - j] = 1
                            else:
                                unavailable = 1
                                break
                    else:
                        unavailable = 1
                        break

            elif row[idx - 1] == row[idx] + 1:          # 지형의 높이가 1 낮아진 경우
                for j in range(length):                 # 경사로의 길이만큼 이후에 낮은 지형에 존재하면 카운트
                    if 0 <= idx + j < size:

                        if row[idx+j] != row[idx]:      # 경사로 길이가 부족하면 건설 불가능
                            unavailable = 1
                            break

                        else:
                            if not runway[idx + j]:       # 다른 경사로와 겹치면 건설 불가능
                                runway[idx + j] = 1
                            else:
                                unavailable = 1
                                break
                    else:
                        unavailable = 1
                        break
                else:
                    idx += length - 1
            elif row[idx-1] == row[idx]:
                pass

            else:
                unavailable = 1
                break

            idx += 1

            if unavailable == 1:                        # 경사로 건설 불가능 하면 해당 행 탐색 종료
                break

        if unavailable == 0:                            # 건설 불가능한 경우가 없으면 활주로 가능
            available += 1

    return available


T = int(input())
for t in range(1, T+1):
    N, X = map(int, input().split())
    site = []

    for _ in range(N):
        input_list = list(map(int, input().split()))
        site.append(input_list)

    print(f"#{t} {possible_runway(N, X, site) + possible_runway(N, X, list(map(list, zip(*site))))}")
