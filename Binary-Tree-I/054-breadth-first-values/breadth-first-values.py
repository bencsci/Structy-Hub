# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def breadth_first_values(root):
  if root is None:
    return []

  q = deque([root])
  res = []
  
  while q:
    curr = q.popleft()
    res.append(curr.val)
    if curr.left:
      q.append(curr.left)
    if curr.right:
      q.append(curr.right)

  return res