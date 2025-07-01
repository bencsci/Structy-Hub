# Traverse through the graph and mark node as alternating colors
# use True and False to mark the colors
# keep track of the current color
# Use a dictionary to keep track of the colors
# If we visit a node in the dictionary return if the current color is the correct color
# Otherwise, mark the node the current colors

def can_color(graph):
  colored = {}

  def dfs(src, current):
    if src in colored:
      return current == colored

    colored[src] = current

    for node in graph[src]:
      if not dfs(node, not current):
        return False

    return True

  for node in graph:
    if node not in colored:
      if not dfs(node, False):
        return False

  return True