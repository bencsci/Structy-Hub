def connected_components_count(graph):
  v = set()

  def dfs(src):
    if src in v:
      return False

    v.add(src)
    for node in graph[src]:
      if dfs(node):
        return True