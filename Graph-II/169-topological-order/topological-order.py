# Greate a adjacency list for the number of parents each node has
# Add all nodes who has 0 parents to a queue
# Add nodes from queue to result list
# Go through the queue and update the number of parents for each node in the queue
# check if the number of parents for each child is 0, if so add to queue

def topological_order(graph):
  parents = getParents(graph)
  print(parents)
  res = []
  q = [node for node in graph if parents[node] == 0]
  
  while q:
    node = q.pop()
    res.append(node)
    for child in graph[node]:
      parents[child] -= 1
      if parents[child] == 0:
        q.append(child)

  return res

def getParents(graph):
  parents = {}
  
  for node in graph:
    parents[node] = 0

  for parent in graph:
    for child in graph[parent]:
      parents[child] += 1 

  return parents