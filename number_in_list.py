#Write a function that checks if a number `n` is in a list `lst`
def num_in_list(n,list):
  for i in list:
    if i == n:
      return True
  return False

print(num_in_list(1,[1,2,3]))
print(num_in_list(1,[5,2,3]))