#Write a Python function that generates a list of numbers that starts at start and stops before end
#and increments by step
def generate_list(start, end, step):
  if(start == end):
    return [start]

  list = []
  if((step >= 0 and start < end) or (step <= 0 and start > end)):
    list.append(start)
  else:
    return list

  neg_pos = 1
  if step < 0:
    neg_pos = -1
  i = start + step
  while neg_pos * i <= end * neg_pos:
    list.append(i)
    i += step

  print(list)
  return list

generate_list(0,5,1)
generate_list(0,0,1)
generate_list(5,10,2)
generate_list(10,5,-2)