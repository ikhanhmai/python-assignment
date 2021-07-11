"""
Given a maze (m x n matrix), the robot only can go right or down, start at position pos(0,0)
---
i.e
. . . .
. x x .
. . . .
x x x .
---
Help to robot to reach its home pos(m-1, n-1)


Pseudo code 

Base case:
- If out of bound, return None
- If is obstacle, return None 
- If reach home, return Solution 

Recursion case:
- Solve the sub problem if the robot go right, add 'r' to the solution
-- Return the solution if the subproblem is solvable
-- If not, backtrack - remove 'r' from the solution

- Solve the sub problem if the robot go down, add 'd' to the solution
-- Return the solution if the subproblem is solvable
-- If not, backtrack - remove 'd' from the solution

"""


maze = [['.','.','.','.'],
        ['.','x','x','x'],
        ['.','.','.','.'],
        ['x','x','x','.']]

def print_maze(maze):
  for row in maze:
    rowString = ''
    for col in row:
      rowString += col + ' '
    print(rowString)

def solve_maze(maze):

  


  return []

def solve_maze_helper(maze, sol, pos_row, pos_col):
  num_row = len(maze)
  num_col = len(maze[0])
  ### Base case

  #If out of bound 
  if pos_row >= num_row or pos_col >= num_col:
    return None 
  
  #If is obstabcle
  if maze[pos_row][pos_col] == 'x':
    return None
  
  #If reach home
  if pos_row == num_row - 1 and pos_col == num_col - 1:
    return sol

  ###Recursion case 

  #Try going right
  sol.append('r')
  sol_going_right = solve_maze_helper(maze, sol, pos_row, pos_col + 1)
  if sol_going_right is not None:
    return sol_going_right

  #If not, backtrack 
  sol.pop()

  #Try going down
  sol.append('d')
  sol_going_down = solve_maze_helper(maze, sol, pos_row + 1, pos_col)
  if sol_going_down is not None:
    return sol_going_down
  
  #If not, backtrack
  sol.pop()

  return None
"""
> solve_maze(maze)
> ['d','d','r','r','r','d']
"""

print_maze(maze)
print(solve_maze_helper(maze, [], 0, 0))