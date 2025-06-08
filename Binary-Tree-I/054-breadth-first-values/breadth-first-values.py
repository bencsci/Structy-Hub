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

  while q:
    curr = q.popleft()
    
