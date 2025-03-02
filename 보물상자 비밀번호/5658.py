# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWXRUN9KfZ8DFAUo&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")


def password(size, order, turn, numbers, check):
    # 1/4 바퀴 돌았으면 종료
    if turn == 0:
        check.sort(reverse=True)
        return check[order-1]

    else:
        row = size // 4

        # 각 변에 있는 숫자들 계산해서 체크 리스트에 삽입
        for i in range(4):
            power = 0
            number = 0
            for n in numbers[row * i: row * (i + 1)][::-1]:
                number += (16 ** power) * ox[n]
                power += 1
            if number not in check:                   # 중복 방지
                check.append(number)

        temp = numbers.pop()
        numbers.insert(0, temp)
        return password(size, order, turn - 1, numbers, check)


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    input_list = list(map(str, input()))
    ox = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8,
          "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

    print(f"{t} {password(N, K, N // 4, input_list, [])}")
