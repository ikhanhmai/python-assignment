#Write a Python function that outputs the first n prime numbers:
def is_prime(n):
  #primarily test using 6k+-1 optimisation
  if n<=3:
    return n > 1 # 1 is not a prime number
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i ** 2 < n:
    if n % i == 0 or n % (i+2) == 0: #only check odd values
      return False
    i += 6
  return True



def find_prime(m):
  i = 2
  prime_numbers = ''
  while i <= m:
    if(is_prime(i)):
      prime_numbers += str(i)+','
    i += 1 

  if(prime_numbers != ''):
    return prime_numbers
  return 'No prime number found!'

print(find_prime(18)) #2,3,5,7,11,13,17,