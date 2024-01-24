def spiral(matrix):
    len_line = len(matrix[0])
    len_matrix = len(matrix)

    result = []

    top = 0
    left = 0
    right = len_line - 1
    down = len_matrix - 1

    while left <= right and top <= down:
        # top: left -> right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # right: top -> down
        for i in range(top, down + 1):
            result.append(matrix[i][right])
        right -= 1

        # down: right -> left
        for i in range(right, left - 1, -1):
            result.append(matrix[down][i])
        down -= 1

        # left: down -> top
        for i in range(down, top - 1, -1):
            result.append(matrix[i][left])
        left += 1
    return result

print(spiral([[1,2,3],[4,5,6],[7,8,9]]))