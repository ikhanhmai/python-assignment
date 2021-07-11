#Write a Python function which multiplies two values (a and b) without using the multiplication
#symbol *. Use addition and a while loop to write your function.
def multiply(a,b):
  
  i = 1
  result = 0
  abs_a = a
  abs_b = b
  if b < 0:
    abs_b = -b
  if a < 0:
    abs_a = -a   
  while i <= abs_b:
    result += abs_a
    i +=1
  if (a < 0 and b > 0) or (a > 0 and b < 0):
    result = -result 
  return result

print(multiply(3,-5))
print(multiply(-3,5))
print(multiply(12,12))
print(multiply(-3,-5))
print(multiply(-3,0))
print(multiply(0,3))
print(multiply(0,-3))
print(multiply(0,0))