# subtract each coin in coins from the amount
# keep count of each recursive call for each branch
# if amount == 0 return the total count for that branch
# compare different successful min values for each branch
# return the min value

# Optimization: Use Memo to store seen values
# reuse those values if a calculation reappears

# time o(a*c) -> space o(n)

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
      minC = min(minC, dfs(amount-coin) + 1)

    memo[amount] = minC
    return memo[amount]

  return dfs(amount)
      

    
