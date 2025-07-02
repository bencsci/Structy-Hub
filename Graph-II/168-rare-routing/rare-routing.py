# Traverse through the graph and mark visited nodes
# Keep track of the previous visited node so we  don't travel in the wrong direction
#  If we travel to a node we already visted return false
# Check if we visited all the nodes and if we travel through the graph without
# Revisiting a node

def rare_routing(n, roads):
  graph = buildGraph(n, roads)
  visited = set()

  def dfs(src, prev):
    if src in visited:
      return False

    visited.add(src)
    for node in graph[src]:
      if prev != node and not dfs(node, src):
        return False

    return True

  valid = dfs(0, None)
  return valid and len(visited) == n


def buildGraph(n, roads):
  graph = {}

  for i in range(n):
    graph[i] = []
  
  for road in roads:
    graph[road[0]].append(road[1])
    graph[road[1]].append(road[0])

  return graph