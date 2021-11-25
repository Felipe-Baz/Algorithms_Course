def get_line(matrix, line):
    #return [x for x in matrix[line]]
    return matrix[line]


def get_column(matrix, column):
    return [x[column] for x in matrix]


def matrix_multiply(MatrixA, MatrixB):
    matResult = []
    for line in range(len(MatrixA)):
        matResult.append([])
        for column in range(len(MatrixB[0])):
            listMult = [item_line * item_column for item_line, item_column in zip(get_line(MatrixA, line), get_column(MatrixB, column))]
            matResult[line].append(sum(listMult))
    return matResult


if __name__ == '__main__':
    mat1 = [[2, 3], [4, 6]]
    mat2 = [[1, 3, 0], [2, 1, 1]]
    print(matrix_multiply(mat1, mat2))
