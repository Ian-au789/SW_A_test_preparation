# selected: 선택된 값 목록
# reamin: 선택되지 않고 남은 값 목록 
def perm(selected, remain):  
    if not remain:  
        print(selected)  
    else:  
        for i in range(len(remain)): 
            select_i = remain[i] 
            remain_list = remain[:i] + remain[i+1:]  
            perm(selected + [select_i], remain_list)

perm([], [1, 2, 3])
