def non_adjacent_sum(nums):
  memo = {}
  
  def dfs(i):
    if i in memo:
      return memo[i]
    
    if i >= len(nums):
      return 0

    include = nums[i] + dfs(i + 2)
    exclude = dfs(i + 1)

    memo[i] = max(include, exclude)
    return memo[i]

  return dfs(0)
