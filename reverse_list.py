#Write a Python function which reverses a list
#do not use built in list.reverse() function
def reverse_list(list):
  listLen = len(list)
  if listLen <= 1:
    return list

  reversedList = []
  i = listLen - 1
  while i >= 0:
    reversedList.append(list[i])
    i -= 1
  
  return reversedList

print(reverse_list([1,2,3,4,5]))  
print(reverse_list([1]))  
print(reverse_list([]))
print(reverse_list([0,0]))