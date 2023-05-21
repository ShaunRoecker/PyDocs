

def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):  # n // 2 is 'floor division' == the result is rounded down to nearest integer
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]
            # left to top
            matrix[layer][i] = matrix[-i - 1][layer]
            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            # top -> right
            matrix[i][-layer - 1] = top
    return matrix


def rotate_matrix_2(matrix):
    n = len(matrix)
    result = [[0] * n for i in range(n)] #empty list of 0s
    for i, j in zip(range(n), range(n-1, -1, -1)):
        for k in range(n):
            result[k][i] = matrix[j][k]
    return result


def rotate_matrix_3(matrix):
    return [list(reversed(row)) for row in zip(*matrix)]


# * unpacks a list or tuple into position arguments.
# ** unpacks a dictionary into keyword arguments.

# lis=[1, 2, 3, 4]
# dic={'a': 10, 'b':20}
# functionA(*lis, **dic)  #it is similar to functionA(1, 2, 3, 4, a=10, b=20)