# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def path_finder(root, target):
  def dfs(root):
    if root is None:
      return None

    if root.val == target:
      return [root.val]

    left = dfs(root.left)
    right = dfs(root.right)
    if left:
      left.append(root.val)
      return left
    if right:
      right.append(root.val)
      return right

    return None
    
  res = dfs(root)
  return res[::-1] if res else None