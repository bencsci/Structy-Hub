# have two pointers at the start and end of the string
# if they match return 2 and then move both pointers inward
# else take the max of the decision of increasing the left or right pointers
# return count at the end

#   l r
# luwxult

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
      return 2 + dfs(l + 1, r - 1)

    count = 0
    count += max(dfs(l + 1, r), dfs(l, r - 1))

    memo[key] = count
    return memo[key]

  return dfs(0, len(string) - 1)