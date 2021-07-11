#Given a list, determine if the list is increasing order
def is_increasing(list):
  if len(list) < 2:
    return True
  
  return list[0] <= list[1] and is_increasing(list[1:])

print(is_increasing([1,2,3])) 
print(is_increasing([1,2,1]))

print(is_increasing([1,2,3,4,5])) 
print(is_increasing([1,2,3,4,5,5]))
print(is_increasing([1,2,1,4,5,5]))