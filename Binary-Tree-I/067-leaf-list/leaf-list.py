# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def leaf_list(root):
  res = []
  def dfs(root):
    if root is None:
      return 

    if root.left is None and root.right is None:
      res.append(root.val)
      return 

    dfs(root.left)
    dfs(root.right)
    
  dfs(root)

  return res