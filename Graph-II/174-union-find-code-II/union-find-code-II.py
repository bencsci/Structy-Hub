# Use an roots list to keep track of root nodes
# Keep track of the size of each component in a sizes array
# Union nodes together based on the edge list and component size
# point nodes to the large component
# compress path sizes

def count_components(n, edges):
  roots = [i for i in range(n)]
  sizes = [1] * n

  for edge in edges:
    n1, n2 = edge
    union(n1, n2, roots, sizes)

  count = 0
  for i in range(len(roots)):
    if roots[i] == i:
      count += 1

  return count

def find(i, roots):
  if roots[i] == i:
    return i

  res = find(roots[i], roots)
  roots[i] = res
  return res

def union(n1, n2, roots, sizes):
  a = find(n1, roots)
  b = find(n2, roots)

  if sizes[a] >= sizes[b]:
    roots[b] = a
    sizes[a] += sizes[b]
  else:
    roots[a] = b
    sizes[b] += sizes[a]