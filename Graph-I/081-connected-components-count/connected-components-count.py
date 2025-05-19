def connected_components_count(graph):
  v = set()
  
  def dfs(src):
    if src is None:
      return False

    if src in v:
      return False

    v.add(src)
    for n in graph[src]:
      dfs(n)

    return True
    