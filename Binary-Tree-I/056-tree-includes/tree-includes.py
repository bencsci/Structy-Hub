# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
  if root is None:
    return False

  if root.val == target:
    return True

  left = tree_includes(root.left, target)
  right = tree_includes(root.right, target)

  return left or right