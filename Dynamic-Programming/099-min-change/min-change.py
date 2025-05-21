# subtract each num in coins if a - c >= 0
# keep tract of the subtraction list per branch
# return the min numbers of num where the ans returns True

def min_change(amount, coins):
  memo = {}
  
  def dfs(amount):
    if amount < 0:
      return float('inf')
    
    if amount in memo:
      return memo[amount]

    if amount == 0:
      return 0
      
    minC = float('inf')
    for num in coins:
      if amount - num >= 0:
        minC = min(minC, dfs(amount - num) + 1)
        memo[amount] = minC

    memo[amount] = minC
    return minC

  ans = dfs(amount)
  return ans if ans != float('inf') else -1
