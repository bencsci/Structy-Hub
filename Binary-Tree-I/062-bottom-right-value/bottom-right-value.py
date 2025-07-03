# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def bottom_right_value(root):
  q = deque([root])

  while q:
    curr = q.popleft()
    if curr.left:
      q.append(curr.left)
    if curr.right:
      q.append(curr.right)

  return curr.val