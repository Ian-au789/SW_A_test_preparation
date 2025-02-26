
def create_subset(depth, included):
    if depth == len(input_list): 
        cnt_subset = [input_list[i] for i in range(len(input_list)) if included[i]]
        subsets.append(cnt_subset)  
        return

    included[depth] = False
    create_subset(depth + 1, included)  

    included[depth] = True
    create_subset(depth + 1, included)  

input_list = [1, 2, 3]  
subsets = []  
init_included = [False] * len(input_list) 
create_subset(0, init_included) 
print(subsets)  