# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):
  def dfs(root):
    if root is None:
      return []

    if root.left is None and root.right is None:
      return [[root.val]]

    left = dfs(root.left)
    right = dfs(root.right)

    paths = []
    for path in left:
      path.append(root.val)
      paths.append(path)

    for path in right:
      path.append(root.val)
      paths.append(path)

    return paths
    
  paths = [path[::-1] for path in dfs(root)]
  return paths