# https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZTP1QzqXnbHBIRD&probBoxId=AZTeuPGad_vHBIOK&checkContestProbId=AWXRUN9KfZ8DFAUo&checkContestProbId=AWXRQm6qfL0DFAUo&checkContestProbId=AWXRJ8EKe48DFAUo&checkContestProbId=AWXRF8s6ezEDFAUo&checkContestProbId=AWXRFInKex8DFAUo&checkContestProbId=AWXRDL1aeugDFAUo&checkContestProbId=AWIeW7FakkUDFAVH&checkContestProbId=AWIeV9sKkcoDFAVH&checkContestProbId=AWIeUtVakTMDFAVH&checkContestProbId=AWIeRZV6kBUDFAVH&pageSize=10&pageIndex=2

import sys
sys.stdin = open("sample_input.txt")

'''
문제 요약
1. 열 방향으로 동일한 숫자가 K개 연속해서 있으면 성능검사 통과
2. 모든 열이 성능검사를 통과해야 함
3. 약품을 쓰면 특정 행에 있는 모든 숫자를 동일하게 통일 가능
4. 모든 열이 성능검사를 통과하기 위해 약품을 쓰게 되는 최소 횟수 구해라
해결 전략
1. 백트래킹 : 약품 사용 횟수는 K를 넘을 수 없음 (연속된 K개 행에 약품을 쓰면 무조건 통과)
2. 성능 검사를 통과하지 못하면 0번째 열부터 D-1열까지 순서대로 약품 처리
3. 재귀 호출로 약품 처리 후 성능 검사, 통과 못하면 그 다음 열부터 다시 약품 처리 후 성능검사 반복

4. kick! deepcopy는 배열 전체를 완벽하게 복사, 하지만 무거운 연산이므로 처리 시간과 메모리 다량 사용
최상위 배열은 바뀌지 않은 리스트 복사 만으로도 원하는 결과 얻을 수 있음
또한, 배열 전체가 아닌 바뀌게 되는 열만 원본을 백업해놓으면 훨씬 연산을 줄일 수 있음
'''


def quality_check(width, height, standard, films):
    check = 0
    for j in range(height):
        for i in range(width - standard + 1):
            if sum(films[j][i:i+standard]) == 0 or sum(films[j][i:i+standard]) == standard:
                check += 1
                break

    if check == height:
        return 1
    else:
        return 0


def chemical_treatment(width, height, standard, last, films, times):
    global result

    if times == standard or last == width  or times >= result:
        return

    check = quality_check(width, height, standard, films)
    if check == 1:
        if result > times:
            result = times
            return

    else:
        for i in range(last, width):
            original_col = [films[j][i] for j in range(height)]

            for j in range(height):
                films[j][i] = 1
            chemical_treatment(width, height, standard, i+1, films, times + 1)

            for j in range(height):
                films[j][i] = 0
            chemical_treatment(width, height, standard, i+1, films, times + 1)

            for j in range(height):
                films[j][i] = original_col[j]



T = int(input())
for t in range(1, T+1):
    D, W, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(D)]
    matrix_t = list(map(list, zip(*matrix)))
    result = K

    chemical_treatment(D, W, K, 0, matrix_t, 0)
    print(f"#{t} {result}")
