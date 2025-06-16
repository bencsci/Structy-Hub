# Have two pointers starting at the start and end of the string
# if both characters match return 2 + move both pointers inward
# if they don't match choose to move the left or right pointer inward
# Base cases:
# l == r:
# return 1

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
      memo[key] = 2 + dfs(l + 1, r - 1)
      return memo[key]

    memo[key] = max(dfs(l + 1, r), dfs(l, r - 1))
    return memo[key]

  return dfs(0, len(string)-1)