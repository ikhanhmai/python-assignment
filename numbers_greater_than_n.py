#Given a list, output a new list that only retains numbers that greater than n from the orginal list
def filter_gt_n(list, n):
  if len(list) < 1:
    return list

  if list[0] <= n:
    return filter_gt_n(list[1:],n)
  else:
    return [list[0]] + filter_gt_n(list[1:],n)

print(filter_gt_n([1,2,3,4],2))
print(filter_gt_n([2,2,3,3],1))
print(filter_gt_n([2,2,3,3],4))
print(filter_gt_n([2,0,3,1],1))