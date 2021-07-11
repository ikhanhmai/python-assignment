#Write a function intersection that consumes two lists of numbers and produces the list of numbers
#that are in both lists. For example, [1,2,3] intersected with [2,4,6] will produce [2].
#Lists may contain duplicates, but do not have duplicates in your produced lists.
def num_in_list(n,list):
  for i in list:
    if i == n:
      return True
  return False


def intersection_lists(l1,l2):
  finalList = []
  for i in l1:
    for j in l2:
      if i == j and not num_in_list(i,finalList):
        finalList.append(i)
  return finalList

print(intersection_lists([1,2,3],[2,4,6]))
print(intersection_lists([1,2,3,5,5,6],[9,5,5,2,4,6]))