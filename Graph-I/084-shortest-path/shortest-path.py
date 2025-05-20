# build an adjacency list from the edges
# traverse while keeping count
# if the curr node == target
# return the count
# compare the min of the counts
from collections import deque, defaultdict

def shortest_path(edges, node_A, node_B):
  graph = buildGraph(edges)
  shortest = 0
  q = deque([(node_A, 0)])
  v = set(node_A)
  while q:
    curr, dist = q.popleft()
      
    if curr == node_B:
      return dist 

    v.add(curr)
    for n in graph[curr]:
      if n not in v:
        q.append((n, dist + 1))

  return -1

def buildGraph(edges):
  graph = defaultdict(list)
  
  for edge in edges:
    graph[edge[0]].append(graph[1])
    graph[edge[1]].append(graph[0])

  return graph
  