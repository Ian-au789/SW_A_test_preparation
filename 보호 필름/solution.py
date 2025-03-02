import sys
sys.stdin = open("sample_input.txt")

def quality_check(width, height, standard, films):
    for j in range(height):
        max_count = 1
        count = 1
        for i in range(1, width):
            if films[j][i] == films[j][i - 1]:  # 연속된 값이 같으면 카운트 증가
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1  # 연속이 끊기면 초기화

        if max_count < standard:
            return 0
    return 1


def chemical_treatment(width, height, standard, last, films, times):
    global result

    if times >= result:      # 현재 최소 횟수를 초과하면 탐색 중지 (가지치기)
        return

    if quality_check(width, height, standard, films): # 성능검사 통과하면 최소 횟수 갱신
        result = min(result, times)

    if last == width:        # 더 이상 처리할 열이 없으면 종료
        return

    # 약품처리 전에 원본 열 백업
    original_col = [films[j][last] for j in range(height)]

    # 처리 없이 다음 열로 이동
    chemical_treatment(width, height, standard, last + 1, films, times)

    # 약품 처리해서 0으로 변경
    for j in range(height):
        films[j][last] = 0
    chemical_treatment(width, height, standard, last + 1, films, times + 1)

    # 약품 처리해서 1로 변경
    for j in range(height):
        films[j][last] = 1
    chemical_treatment(width, height, standard, last + 1, films, times + 1)

    # 원래 상태로 복원
    for j in range(height):
        films[j][last] = original_col[j]

    return result


T = int(input())
for t in range(1, T + 1):
    D, W, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(D)]
    matrix_t = list(map(list, zip(*matrix)))  # 전치 행렬로 변환 (열 단위로 접근)

    result = K
    chemical_treatment(D, W, K, 0, matrix_t, 0)
    print(f"#{t} {result}")
