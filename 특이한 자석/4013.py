# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWIeV9sKkcoDFAVH&probBoxId=AZTeuPGad_vHBIOK&type=PROBLEM&problemBoxTitle=A%ED%98%95+%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8+%EB%AA%A8%EC%9D%8C%EC%A7%91+&problemBoxCnt=20

import sys
sys.stdin = open("sample_input.txt")

'''
문제 요약
1. 자석이 회전하면서 붙어있는 다른 자석의 톱날의 자성이 반대라면 반대방향으로 끌려감
2. 모든 회전이 끝난 후에 각 자석의 화살표 방향 톱날의 자성이 S극이면 1, 2, 4, 8점 얻는다
3. 자성 정보는 빨간 화살표가 있는 톱날부터 0번 인덱스
해결 전략
1. 회전 하고자 하는 자석 번호, 회전 방향, 탐색 방향 입력
2. 양옆의 자석의 2번, 6번 인덱스 확인하며 회전 유무 확인
3. 첫 자석은 양방향 탐색, 그 이후는 탐색 방향에 있는 자석만 탐색
'''


def rotate_magnet(number, direction, order):

    if number - 1 >= 0 and order <= 0:
        if magnets[number-1][2] != magnets[number][6]:
            rotate_magnet(number - 1, direction*-1, -1)

    if number + 1 < 4 and order >= 0:
        if magnets[number + 1][6] != magnets[number][2]:
            rotate_magnet(number + 1, direction*-1, 1)

    if direction == 1:
        temp = magnets[number].pop()
        magnets[number].insert(0, temp)
    else:
        temp = magnets[number].pop(0)
        magnets[number].append(temp)

    return


T = int(input())
for t in range(1, T+1):
    K = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]
    turns = [list(map(int, input().split())) for _ in range(K)]

    for turn in turns:
        rotate_magnet(turn[0]-1, turn[1], 0)

    result = 0
    for n in range(4):
        if magnets[n][0] == 1:
            result += 2**n

    print(f"#{t} {result}")
