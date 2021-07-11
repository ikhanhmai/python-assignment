#Write a Python function which iterates the integers from 0 to n. For multiples of three, print "Fizz"
#instead of the number, and for the multiples of five, print "buzz". For numbers which are multiples
#of both three and five, print "fizzbuzz".
def fizzbuzz(n):
  i = 0
  while i <= n:
    if i % 3 == 0 and i % 5 == 0:
      print('fizzbuzz')
    elif i % 3 == 0:
      print('fizz')
    elif i % 5 == 0:
      print('buzz')
    else:
      print(i)
    i += 1
  return 0

fizzbuzz(15)