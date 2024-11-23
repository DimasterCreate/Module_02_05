def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

result1 = get_matrix(2, 3 , 13)
result2 = get_matrix(3, 4, 55)
result3 = get_matrix(5,2,11)

