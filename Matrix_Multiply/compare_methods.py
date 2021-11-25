import timeit

from Matrix_Multiply.Matrix_Multiply_function import matrix_multiply



if __name__ == '__main__':
    mat1 = [[2, 3], [4, 6]]
    mat2 = [[1, 3, 0], [2, 1, 1]]

    print("-+-"*30)
    start = timeit.timeit()
    
    matrix = matrix_multiply(mat1, mat2)

    end = timeit.timeit()
    print(f'Response of Simple Matrix Multiply using Function: {matrix}')
    print(f'Elapsed time of Simple Matrix Multiply using Function: {end - start}')
    print("-+-"*30)

    mat1 = [[2, 3], [4, 6]]
    mat2 = [[1, 3, 0], [2, 1, 1]]
    start = timeit.timeit()
    
    

    end = timeit.timeit()
    print(f'Response of Simple Matrix Multiply using Class: {matrix}')
    print(f'Elapsed time of Simple Matrix Multiply using Class: {end - start}')
    print("-+-"*30)