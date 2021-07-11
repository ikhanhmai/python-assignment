#Give two lists, output a new list with intersection numbers
def intersection(list1, list2):
  if not list1 or not list2:
    return []
  if not list1[0] in list2:
    return intersection(list1[1:],list2)
  else:
    return [list1[0]] + intersection(list1, remove_number(list2, list1[0]))

def remove_number(list, n):
  if not list:
    return []
  if list[0] == n:
    return remove_number(list[1:], n) 
  else:
    return [list[0]] + remove_number(list[1:],n)

print(intersection([1,2,3],[2,2,3,4]))    
print(intersection([1,2,3],[4,5,6])) 
print(intersection([2,3,2,4],[2,2,4])) 