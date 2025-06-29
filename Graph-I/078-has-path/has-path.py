from collections import deque

def has_path(graph, src, dst):
  q = deque([src])

  while q:
    curr = q.popleft()
    if curr == dst:
      return True
    for neighbour in graph[curr]:
      q.append(neighbour)

  return False
      