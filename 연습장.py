A = [1, 2, 3, 4, 5]

A.sort(reverse = 1)
print(A)

temp = A.pop()
A.insert(0, temp)
print(A)