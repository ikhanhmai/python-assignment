'''Write a function that multiplies two matrices together. For matrix multiplication, the number of
columns in the first matrix must be equal to the number of rows in the second matrix. The result
matrix, known as the matrix product, has the number of rows of the first and the number of
columns of the second matrix.
There is a formal definition of matrix multiplication on wikipedia:
https://en.wikipedia.org/wiki/Matrix_multiplication
Output None if the matrices cannot be multiplied together. Use the previous function
is_valid_matrix to validate the two matrices before you multiply them.'''

def validate_matrix(matrix):
  m = len(matrix)
  if(m == 0):
    return False
  n = len(matrix[0])
  for i in range(m):
    if not len(matrix[i]) == n:
       return False
  return True


def multiply_matrices(m1,m2):
  if not validate_matrix(m1) or not validate_matrix(m2):
    return 'None'
  if not len(m1[0]) == len(m2):
    return 'None'
  m = len(m1) #2
  n = len(m1[0]) #3
  p = len(m2[0]) #2
  result_matrix = []
  for i in range(m):
    result_matrix.append([])
    for j in range(p):
      temp = 0
      for k in range(n):
        temp += m1[i][k] * m2[k][j]
      result_matrix[i].append(temp)  
  return result_matrix

matrix1 = [[1,2,3],
[4,5,6]]
matrix2 = [[1,2],
[3,4],
[5,6]]

print(multiply_matrices(matrix1,matrix2))
print(multiply_matrices(matrix1,[]))