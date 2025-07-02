# Get the number of parents for each node in the graph
# Add nodes who has zero parents to q
# pop from q and append to our res
# update the popped node's children num parents
# if those children num parents == 0 then add to our q

def safe_cracking(hints):
  graph = bulidGraph(hints)
  parents = getParents(graph)

  res = ''
  q = [node for node in graph if parents[node] == 0]

  while q:
    node = q.pop()
    res += str(node)
    for child in graph[node]:
      parents[child] -= 1
      if parents[child] == 0:
        q.append(child)

  return res

def bulidGraph(edges):
  graph = {}

  for edge in edges:
    a, b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []

  for edge in edges:
    graph[edge[0]].append(edge[1])

  return graph
  

def getParents(graph):
  parents = {}

  for node in graph:
    parents[node] = 0

  for node in graph:
    for child in graph[node]:
      parents[child] += 1

  return parents
    