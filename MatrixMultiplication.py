# 3x3 matrix
matrix1 = [[1,2,3],
          [7,6,5],
           [9,10,2]]

# 3x4 matrix
matrix2 = [[1,2,3,4],
           [2,4,6,8],
           [3,5,7,9]]

# ans is 3x4
ans = [[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]

# iterate through rows of matrix1
for i in range(len(matrix1)):
   # iterate through columns of matrix2
   for j in range(len(matrix2[0])):
       # iterate through rows of Y
       for k in range(len(matrix2)):
           ans[i][j] += matrix1[i][k] * matrix2[k][j]

for d in ans:
   print(d)
