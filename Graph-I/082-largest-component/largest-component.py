# dfs traverse through each neighbour, mark them as visited
# count each neighbour until dfs ends. return the size of the component and 
# compare with max from previous max. Return max

def largest_component(graph):
  largest = 0
  v = set()
  
  def dfs(src):
    if src is None:
      return 0

    if src in v:
      return 0

    v.add(src)
    count = 1
    for n in graph[src]:
      count += dfs(src)
    
    return count

  for n in graph:
      largest = max(largest, dfs(n))

  return largest