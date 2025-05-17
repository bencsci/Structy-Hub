from collections import defaultdict

def undirected_path(edges, node_A, node_B):
  graph = buildGraph(edges)
  v = set()
  
  def dfs(src):
    if src == node_B:
      return True

    for n in graph[src]:
      if n not in v and dfs(n):
        v.add(n)
        return True

    return False
    
  return dfs(node_A)

def buildGraph(edges):
  graph = defaultdict(list) 
  
  for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

  return graph

  