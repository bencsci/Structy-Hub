def has_path(graph, src, dst):
  if src == dst:
    return True 

  for n in graph[src]:
    if has_path(n):
      return True

  return False