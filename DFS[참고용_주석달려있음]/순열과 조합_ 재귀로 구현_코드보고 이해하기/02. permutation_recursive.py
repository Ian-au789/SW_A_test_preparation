# selected: 선택된 값 목록
# reamin: 선택되지 않고 남은 값 목록 
def perm(selected, remain):  
    if not remain:  # 남은 요소들이 없는 경우
        print(selected)  # 선택된 요소들 출력
    else:  # 남은 요소들이 있는 경우
        for i in range(len(remain)):  # 남은 요소들의 인덱스 순회
            select_i = remain[i]  # 현재 인덱스 i에 해당하는 요소 선택
            remain_list = remain[:i] + remain[i+1:]  # 선택된 요소를 제외한 새로운 남은 요소 리스트 생성
            perm(selected + [select_i], remain_list)  # 선택된 요소를 추가한 리스트와 새로운 남은 요소 리스트로 재귀 호출

# 초기 호출로 빈 리스트와 [1, 2, 3] 리스트 사용
perm([], [1, 2, 3])
