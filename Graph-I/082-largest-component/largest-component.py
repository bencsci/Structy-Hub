def largest_component(graph):
  v = set()

  def dfs(src):
    if src in v:
      return 0

    count = 1
    v.add(src)
    for node in graph[src]:
      count += dfs(node)

    return count

  res = float('-inf')
  for node in graph:
    res = max(res, dfs(node))

  return res