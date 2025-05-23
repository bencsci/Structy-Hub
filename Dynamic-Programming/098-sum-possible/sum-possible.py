def sum_possible(amount, numbers):
  memo = {}

  def dfs(amount):
    if amount in memo:
      return memo[amount]
    
    if amount < 0:
      return False
    
    if amount == 0:
      return True

    for num in numbers:
      if dfs(amount - num):
        memo[amount] = True
        return True

    memo[amount] = False
    return memo[amount]

  return dfs(amount)
