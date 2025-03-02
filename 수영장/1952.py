# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5PpFQaAQMDFAUq&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")


def lowest_price(month, price):
    global result

    # 12달 전부 탐색하면 최소값 갱신
    if month >= 12:
        result = min(result, price)
        return

    #  중간 가격이 이미 최소값을 넘어서면 더 이상 탐색할 필요가 없음
    if result <= price:
        return

    day = schedule[month]
    if day > 0:
        price += day * fee[0]
        lowest_price(month + 1, price)
        price -= day * fee[0]

        price += fee[1]
        lowest_price(month + 1, price)
        price -= fee[1]

        price += fee[2]
        lowest_price(month + 3, price)
        price -= fee[2]

    else:
        lowest_price(month+1, price)


T = int(input())
for t in range(1, T+1):
    fee = list(map(int, input().split()))
    schedule = list(map(int, input().split()))

    result = fee[3]
    lowest_price(0, 0)

    print(f"#{t} {result}")