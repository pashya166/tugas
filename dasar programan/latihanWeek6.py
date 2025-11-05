#Matriks dengan ukuran 2x2
matriksA = [[1,0], [0,1]]
print(matriksA)

#matriks dengan ukuran 3x3
matriksB = [[1,0,1], [0,1,0], [1,0,1]]
print(matriksB)

#matriks dengan ukuran 4x4
matriksC = [[1,0,1], [0,1,0], [1,0,1], [1,0,1]]
print(matriksC)

matrix = [
    [5,0],
    [2,6],
]

matrix1 = [
    [5,0,8],
    [7,6,5],
    [1,2,3],
]

matrix2 = [
    [5,0,8,4],
    [7,6,5,6],
    [1,2,3,4],
    [1,2,3,5],
]

mat1 = [
    [9,0],
    [3,6],
]

mat2 = [
    [6,0],
    [7,2],
]

for x in range(0, len(mat1)):
    for y in range(0, len(mat1[0])):
        print(mat1[x][y] + mat2[x][y], end=''),
    print