# Traverse through the graph using dfs and mark visited nodes
# If we reach the target node return 0
# add the costs of each node each time we travel to a new node
# compare the cost to get the min
# remove the visited node so we can bracktrack to another path

def weighted_graph_min_path(graph, src, dst):
  v = set()

  def dfs(src):
    if src == dst:
      return 0

    if src in v:
      return float('inf')

    v.add(src)
    weight = float('inf')
    for node, w in graph[src].items():
      weight = min(weight, dfs(node)+w)

    v.remove(src)
    return weight

  return dfs(src)