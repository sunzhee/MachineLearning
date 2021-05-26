"""
Sparse Matrix Multiplication
Write a function that takes in two integer
matrices and multiplies them together.
Both matrices will be sparse, meaning that
most of their elements will be zero. Take
advantage of that to reduce the number of
total computations that your function
performs.
If the matrices can't be multiplied together,
your function should return [[]] .


Sample Input
matrix_a = [
 [0, 2, 0],
 [0, -3, 5],
]
matrix_b = [
 [0, 10, 0],
 [0, 0, 0],
 [0, 0, 4],
]


Sample Output
[
 [0, 0, 0],
 [0, 0, 20],
]


"""
# 先建立一个字典，只保存两个矩阵中非0的数值和坐标
# 然后只处理非0的值做矩阵乘法，可以减少很多计算量
def sparse_matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    
    sparse_a = getDictOfNonzeroCells(matrix_a)
    sparse_b = getDictOfNonzeroCells(matrix_b)

    matrix_c = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

    for i,k in sparse_a.keys():
        for j in range(len(matrix_b[0])):
            if(k,j) in sparse_b.keys():
                matrix_c[i][j] += sparse_a[(i,k)] * sparse_b[(k,j)]
    return matrix_c

def getDictOfNonzeroCells(matrix):
    dictCells = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                dictCells[(i,j)] = matrix[i][j]
    return dictCells
