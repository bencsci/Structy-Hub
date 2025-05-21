def min_change(amount, coins):
  memo = {}

  def dfs(amount):
    if amount < 0:
      return float('inf')

    if amount == 0:
      return 0

    minC = float('inf')
    for coin in coins:
      minC = min(minC, dfs(amount - coin) + 1)

    memo[amount] = minC
    return minC

  ans = dfs(amount)
  return ans if ans != float('inf') else - 1
