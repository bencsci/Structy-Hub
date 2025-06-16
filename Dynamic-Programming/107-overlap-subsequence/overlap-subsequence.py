# Traverse through both strings
# if the characters matach then return 1 + moving both strings forward
# if not then choose to move either the s1, or s2 forward

def overlap_subsequence(string_1, string_2):

  memo = {}
  
  def dfs(s1, s2):
    key = {s1, s2}

    if key in memo:
      return memo[key]
    
    if s1 >= len(string_1) or s2 >= len(string_2):
      return 0

    if string_1[s1] == string_2[s2]:
      memo[key] = 1 + dfs(s1 + 1, s2 + 1)
      return memo[key]

    memo[key] = max(dfs(s1 + 1, s2), dfs(s1, s2 + 1))
    return memo[key]

  return dfs(0, 0)