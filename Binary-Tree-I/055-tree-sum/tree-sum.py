# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  if root is None:
    return 0

  left = root.left
  right = root.right

  return root.val + tree_sum(left) + tree_sum(right)