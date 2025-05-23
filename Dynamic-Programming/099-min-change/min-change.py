def min_change(amount, coins):
  memo = {}
  
  def dfs(amount):
    if amount in memo:
      return memo[amount]
    
    if amount < 0:
      return float('inf')

    if amount == 0:
      return 0

    minC = float('inf')
    for coin in coins:
      minC = min(minC, dfs(amount - coin) + 1)
      memo[amount] = minC
      
    memo[amount] = minC
    return memo[amount]

  return dfs(amount)
