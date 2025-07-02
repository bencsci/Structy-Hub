# Fint the nodes with mutiple edges and return those edges

def extra_cable(num_computers, cables):
  roots = list(range(num_computers))
  sizes = [1] * num_computers
  
  for cable in cables:
    n1, n2 = cable
    if union(n1, n2, roots, sizes):
      return cable

def union(n1, n2, roots, sizes):
  a = find(n1, roots)
  b = find(n2, roots)

  if a == b:
    return True
  
  if sizes[a] >= sizes[b]:
    roots[b] = a
    sizes[a] += sizes[b]
  else:
    roots[a] = b
    sizes[b] += sizes[a]

  return False

def find(i, roots):
  if roots[i] == i:
    return i

  res = find(roots[i], roots)
  roots[i] = res
  return res