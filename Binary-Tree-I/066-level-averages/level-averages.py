# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def level_averages(root):
  levels = []

  def dfs(root, level):
    if root is None:
      return []

    if level == len(levels):
      levels.append([root.val])
    else:
      levels[level].append(root.val)

    dfs(root.left, level + 1)
    dfs(root.right, level + 1)

  dfs(root, 0)
  for i in range(len(levels)):
    level = levels[i]
    levels[i] = sum(level) / len(level)

  return levels