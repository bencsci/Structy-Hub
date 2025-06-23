from collections import defaultdict

def undirected_path(edges, node_A, node_B):
  graph = buildGraph(edges)
  visited = set()
  
  def dfs(src):
    if src == node_B:
      return True
    
    for neighbour in graph[src]:
      if neighbour not in visited:
        visited.add(neighbour)
        if dfs(neighbour):
          return True
      else:
        continue
              
    return False
  return dfs(node_A)
    

def buildGraph(edges):
  graph = defaultdict(list)

  for edge in edges:
    graph[edge[0]] = edge[1]
    graph[edge[1]] = edge[0]

  return graph