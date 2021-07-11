# python-assignment #

## Pgramming fundamental using Python ##

### Fizzbuzz
Write a Python function which iterates the integers from 0 to n. For multiples of three, print "Fizz"
instead of the number, and for the multiples of five, print "buzz". For numbers which are multiples
of both three and five, print "fizzbuzz".
https://github.com/ikhanhmai/python-assignment/blob/main/fizzbuzz.py

---
### Generate list
Write a Python function that generates a list of numbers that starts at start and stops before end
and increments by step
https://github.com/ikhanhmai/python-assignment/blob/main/generate_list.py

---
### Intersection of two lists
Write a function intersection that consumes two lists of numbers and produces the list of numbers
that are in both lists. For example, [1,2,3] intersected with [2,4,6] will produce [2].
Lists may contain duplicates, but do not have duplicates in your produced lists.
https://github.com/ikhanhmai/python-assignment/blob/main/intersection_of_two_lists.py

---
### Intersection of two lists using recursion
Give two lists, output a new list with intersection numbers using recursion
https://github.com/ikhanhmai/python-assignment/blob/main/intersection_of_two_lists_recursion.py

---
### Is list increasing order
Given a list, determine if the list is increasing order using recursion
https://github.com/ikhanhmai/python-assignment/blob/main/is_list_increasing_order.py

---
### Matrices multiplication
Write a function that multiplies two matrices together. For matrix multiplication, the number of
columns in the first matrix must be equal to the number of rows in the second matrix. The result
matrix, known as the matrix product, has the number of rows of the first and the number of
columns of the second matrix.
There is a formal definition of matrix multiplication on wikipedia: https://en.wikipedia.org/wiki/Matrix_multiplication
Output None if the matrices cannot be multiplied together. Use the previous function
is_valid_matrix to validate the two matrices before you multiply them.
https://github.com/ikhanhmai/python-assignment/blob/main/matrices_multiplication.py

---
### Matrices Validation
Write a function that determines if the given list of lists is valid, meaning that for each row, it has
the same number of columns.
https://github.com/ikhanhmai/python-assignment/blob/main/matrices_validation.py

---
### Multiply without using multiplication operation
Write a Python function which multiplies two values (a and b) without using the multiplication
symbol 'asterisk'. Use addition and a while loop to write your function.
https://github.com/ikhanhmai/python-assignment/blob/main/multiply_without_multiply.py

---
### Detect number in a list
Write a function that checks if a number `n` is in a list `lst`
https://github.com/ikhanhmai/python-assignment/blob/main/number_in_list.py

---
### Output a list of number greater than a given number 
Given a list, output a new list that only retains numbers that greater than n from the orginal list
https://github.com/ikhanhmai/python-assignment/blob/main/numbers_greater_than_n.py

---
### Output the first n prime numbers
Write a Python function that outputs the first n prime numbers
https://github.com/ikhanhmai/python-assignment/blob/main/prime_number.py

---
### Reverse a list
Write a Python function which reverses a list
do not use built in list.reverse() function
https://github.com/ikhanhmai/python-assignment/blob/main/reverse_list.py

---
### Output solution helps the robot reach its home
Given a maze (m x n matrix), the robot only can go right or down, start at position pos(0,0)
i.e.  
. . . .  
. x x .  
. . . .  
x x x .  
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
https://github.com/ikhanhmai/python-assignment/blob/main/robot_maze.py

---
### Calculate best 75%
Score of best 75% days
Take your best 75% days to account for sick
days. No one is ever healthy every day. That means that even if #they didn’t get every question
correct, as long as they got 75% of the questions correct, they will get 100%. See the example
outputs below.
Write a function that produces your final score as a percentage given:
- total: the number of quizzes
- correct: the number of quizzes you correctly answered
- wrong: the number of quizzes you answered incorrectly  
https://github.com/ikhanhmai/python-assignment/blob/main/score_of_best_75_percent_days.py

---
### Sudoku solver 
Give a 9 x 9 board with 0 cells, fill in the 0s to resolve the sudoku problem  
https://github.com/ikhanhmai/python-assignment/blob/main/sudoku_solver.py
