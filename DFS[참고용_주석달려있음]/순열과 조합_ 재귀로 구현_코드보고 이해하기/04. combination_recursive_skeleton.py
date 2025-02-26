# arr 배열에서 n개의 요소를 선택하여 조합을 생성하는 함수
def comb(arr, n):
    result = []  

    if n == 1:  
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i] 
        for rest in comb(arr[i + 1:], n - 1):
            result.append([elem] + rest)  

    return result  

print(comb([1, 2, 3, 4], 3))  # [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4] 출력
