# arr 배열에서 n개의 요소를 선택하여 조합을 생성하는 함수
def comb(arr, n):
    result = []  # 결과를 저장할 빈 리스트 초기화

    if n == 1:  # 선택할 요소의 수가 1인 경우
        # n이 1이면 더 이상 조합할 요소가 필요 없음
        # 각 요소 자체가 하나의 조합이므로, 각 요소를 리스트로 감싸서 반환
        return [[i] for i in arr]

    # 배열의 각 요소에 대해 반복
    for i in range(len(arr)):
        elem = arr[i]  # 현재 요소를 선택
        # 현재 요소 이후의 나머지 요소들로 n-1개의 조합을 재귀적으로 생성
        for rest in comb(arr[i + 1:], n - 1):  # arr[i+1:]는 현재 요소 이후의 모든 요소를 포함
            result.append([elem] + rest)  # 현재 선택한 요소와 재귀 호출을 통해 얻은 조합을 합침

    return result  # 최종 조합 결과 반환

print(comb([1, 2, 3, 4], 3))  # [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4] 출력
