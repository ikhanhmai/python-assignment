'''Write a function that determines if the given list of lists is valid, meaning that for each row, it has
the same number of columns.'''

def validate_matrix(matrix):
  m = len(matrix)
  if(m == 0):
    return False
  n = len(matrix[0])
  for i in range(m):
    if not len(matrix[i]) == n:
       return False
  return True


print(validate_matrix([]))
print(validate_matrix([[1,2,3],[4,5,6],[7,8,9]]))
print(validate_matrix([[1,2,3],[4,6],[7,8,9]]))
print(validate_matrix([[1,2],[3,4]]))
print(validate_matrix([[1,2],[3,4],[5,6,7]]))