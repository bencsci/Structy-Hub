def connected_components_count(graph):
  v = set()

  def dfs(src):
    for neighbour in graph[src]:
      if neighbour not in v:
        v.add(neighbour)
        dfs(neighbour)
        
    return 1

  count = 0
  for node in graph:
    if node not in v:
      v.add(node)
      count += dfs(node)

  return count
  
      
test = connected_components_count({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) # -> 1
print(test)
    