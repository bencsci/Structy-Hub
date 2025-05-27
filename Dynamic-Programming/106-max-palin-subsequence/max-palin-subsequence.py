# Create a recursive tree where each node represents the string
# each branch represents a decision on the modified string
# if the l and r equal: then move both pointers and increase count by 2
# move the l pointer only
# move the r pointer only
# if l > r: return 0

# Optimization: use memoization to store recomputed values
def max_palin_subsequence(string):
  memo = {}
  
  def dfs(l, r):
    key = (l, r)

    if key in memo:
      return memo[key]
    
    if l > r:
      return 0
    
    if l == r:
      return 1
      
    if string[l] == string[r]:
      memo[key] = 2 + dfs(l + 1,r - 1)
    else:
      memo[key] = max(dfs(l + 1, r), dfs(l, r - 1))

    return memo[key]

  return dfs(0, len(string) - 1)