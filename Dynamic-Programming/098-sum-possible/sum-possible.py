def sum_possible(amount, numbers):
  memo = {}

  def dfs(amount):

    if n in memo:
      return memo[n]
    
    if amount == 0:
      return True

    for num in numbers:
      if amount - num >= 0:
        if dfs(amount - num):
          memo[n] = True
          return True

    memo[n] = False
    return False

  return dfs(amount)

  
