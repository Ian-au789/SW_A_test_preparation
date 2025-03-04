# https://school.programmers.co.kr/learn/courses/30/lessons/87694?language=python3


def solution(rectangle, characterX, characterY, itemX, itemY):
    cnt = 0

    bound_i = []
    bound_j = []
    for rect in rectangle:
        bound_i.append(rect[2])
        bound_j.append(rect[3])

    matrix = [[0]*(max(bound_j)+2) for _ in range(max(bound_i) + 2)]

    for rect in rectangle:
        for i in [rect[0], rect[2]]:
            for j in range(rect[1], rect[3] + 1):
                matrix[i][j] = 1

        for j in [rect[1], rect[3]]:
            for i in range(rect[0], rect[2] + 1):
                matrix[i][j] = 1

    for rect in rectangle:
        for i in range(rect[0] + 1, rect[2]):
            for j in range(rect[1] + 1, rect[3]):
                matrix[i][j] = 2

    origin = [characterX, characterY]
    cur_loc = [characterX, characterY]
    item_loc = [itemX, itemY]



    return answer


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
