def overlap_subsequence(string_1, string_2):
  memo = {}
  
  def dfs(s1, s2):

    key = (s1, s2)

    if key in memo:
      return memo[key]
    
    if s1 > len(string_1) - 1 or s2 > len(string_2) - 1:
      return 0
    
    if string_1[s1] == string_2[s2]:
      return 1 + dfs(s1+1, s2+1)

    memo[key] = max(dfs(s1+1, s2), dfs(s1, s2+1))
    return memo[key]

  return dfs(0, 0)
