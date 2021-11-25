class Matriz:
    def __init__(self, matrix):
        self.mat = matrix
        self.line= len(matrix)
        self.column = len(matrix[0])


    def get_line(self, n):
        return [i for i in self.mat[n]]


    def get_Column(self, n):
        return [i[n] for i in self.mat]


    # opcional: dar overload no operador de multiplicação
    def __mul__(self, matrixB):
        matRes = []

        for line in range(self.line):           
            matRes.append([])

            for column in range(matrixB.column):
                listMult = [item_line * item_column for item_line, item_column in zip(self.get_line(line), matrixB.get_Column(column))]
                matRes[line].append(sum(listMult))

        return matRes


if __name__ == '__main__':
    mat1 = [[2, 3], [4, 6]]
    mat2 = [[1, 3, 0], [2, 1, 1]]

    mat1 = Matriz(mat1)
    mat2 = Matriz(mat2)

    print(mat1*mat2)
