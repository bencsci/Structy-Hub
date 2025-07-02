def province_sizes(n, roads):
  roots = [i for i in range(n)]
  sizes = [1] * n
  res = []

  for road in roads:
    n1, n2 = road
    union(n1, n2, roots, sizes)

  print(roots)
  print(sizes)
  
  for i in range(len(roots)):
    if roots[i] == i:
      res.append(sizes[i])

  return res

def find(i, roots):
  if roots[i] == i:
    return i

  res = find(roots[i], roots)
  roots[i] = res
  return res

def union(n1, n2, roots, sizes):
  a = find(n1, roots)
  b = find(n2, roots)

  if a == b:
    return
  
  if sizes[a] >= sizes[b]:
    roots[b] = a
    sizes[a] += sizes[b]
  else:
    roots[a] = b
    sizes[b] += sizes[a]

