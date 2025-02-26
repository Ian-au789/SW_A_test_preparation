def sum_subset(idx, num_sum):
    global result

    # 마지막 숫자까지 모두 선택한 경우 => 중단
    if idx == N: 
        if num_sum == 10:
            result += 1
        return

    # 여태까지 누적의 합이 10인 경우, 결과에 + 1
    # if idx == N:
    #     return
    # if num_sum == 10:
    #     result += 1

    # 누적의 합이 K 보다 크거나 같으면 중단 ( 가지치기 )
    # 문제에서 주어진 숫자들이 0보다 무조건 큽니다.  ( if num_sum > K: )
    # if num_sum >= 10: return


    # 선택한 경우
    sum_subset(idx + 1, num_sum + arr[idx])
    # 선택하지 않은 경우
    sum_subset(idx + 1, num_sum)

N = 10
arr = [1,2,3,4,5,6,7,8,9,10]
result = 0

# DFS 파라미터
# 1. 재귀 호출을 중단시킬 파라미터 => 현재 선택하냐/마냐를 정하는 인덱스
# 2. 우리가 원하는 누적값 => 여태까지 선택한 숫자들의 합
sum_subset(0, 0)

print(result)
