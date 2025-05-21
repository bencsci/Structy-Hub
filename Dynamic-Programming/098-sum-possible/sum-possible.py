def sum_possible(amount, numbers):
  memo = {}

  def dfs(amount):

    if amount in memo:
      return memo[amount]
    
    if amount == 0:
      return True

    for num in numbers:
      if amount - num >= 0:
        if dfs(amount - num):
          memo[amount] = True
          return True

    memo[amount] = False
    return False

  return dfs(amount)

  
