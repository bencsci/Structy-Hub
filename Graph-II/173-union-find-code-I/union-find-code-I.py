def count_components(n, edges):
  roots = [i for i in range(n)]

  for edge in edges:
    n1, n2 = edge
    union(n1, n2, roots)

  count = 0
  for i in range(len(roots)):
    if roots[i] == i:
      count += 1

  return count

def union(n1, n2, roots):
  val = find(n1, roots)
  idx = find(n2, roots)

  if val == idx:
    return
  
  roots[idx] = val

def find(i, roots):
  if roots[i] == i:
    return i

  return find(roots[i], roots)