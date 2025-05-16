# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def zipper_lists(head_1, head_2):
  c1, c2 = head_1.next, head_2
  tail = head_1
  count = 0
  
  while c1 and c2:
    if count % 2 == 0:
      tail.next = c2
      c2 = c2.next
    else:
      tail.next = c1
      c1 = c1.next
    tail = tail.next
    count += 1

  if c1:
    tail.next = c1
  if c2:
    tail.next = c2

  return 