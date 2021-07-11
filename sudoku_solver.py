"""
Sudoku solver 
Give a 9 x 9 board with 0 cells, fill in the 0s to resolve the sudoku problem
"""

board = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]
def print_board(board):
  for row in board:
    rowString = ''
    for col in row:
      rowString += str(col) + ' '
    print(rowString)
    
def find_zero(board):
  i = 0
  for row in board:
    j = 0
    for col in row:
      if col == 0:
        return [i,j]
      j+=1
    i+=1
  return []

def is_valid(board, pos_row, pos_col, value):

  if value in get_col_list_helper(board,pos_col):
    return False
  if value in get_row_list_helper(board,pos_row):
    return False
  if value in get_three_three_matrix_list_helper(board,pos_row,pos_col):
    return False        
  return True

def get_row_list_helper(board, pos_row):
  return board[pos_row]

def get_col_list_helper(board, pos_col):
  col_list = []
  for row in board:
    col_list.append(row[pos_col])
  return col_list

def get_three_three_matrix_list_helper(board, pos_row, pos_col):
  div_three_row = pos_row // 3
  div_three_col = pos_col // 3
  list = []
  for i in range(div_three_row * 3, div_three_row * 3 + 3):
    for j in range(div_three_col * 3, div_three_col * 3 + 3):
      list.append(board[i][j])
  return list


def solve(board):
  zero_cell = find_zero(board)
  return solve_board_helper(board,zero_cell,1)

def solve_board_helper(board,zero_cell,value):

  #base case 
  if not zero_cell:
    return board
  if value > 9:
    return None  

  #recursion case  
  if not is_valid(board,zero_cell[0],zero_cell[1],value):
    return solve_board_helper(board,zero_cell,value+1)

  board[zero_cell[0]][zero_cell[1]] = value
  solution = solve_board_helper(board,find_zero(board),1)

  if solution is not None:
    return solution

  board[zero_cell[0]][zero_cell[1]] = 0
  return solve_board_helper(board,zero_cell,value+1)
  




print_board(board)
print(find_zero(board))
print(get_three_three_matrix_list_helper(board, 0,0))
print(get_three_three_matrix_list_helper(board, 3,4))
print(is_valid(board, 0, 2, 1))
print(is_valid(board, 0, 2, 7))
print(is_valid(board, 0, 2, 6))
print(is_valid(board, 3, 5, 9))
print(solve(board))

