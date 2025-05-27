# Create a recursive tree where each level represents the value of the coins 
# starting from 1 ... amount
# each branch of the tree represents the quantity and will pass in the new amount
# amount - (quantity * coin value)
# if amount is 0: return 1 
# if amount < 0: return 0

# Optimization: use memoization to store recomputed values

def counting_change(amount, coins):
  memo = {}
  
  def dfs(amount, i):
    key = (amount, i)

    if key in memo:
      return memo[key]
    
    if amount == 0:
      return 1

    if i == len(coins):
      return 0

    coin = coins[i]

    count = 0
    for qty in range((amount // coin) + 1):
      new = amount - (qty * coin)
      count += dfs(new, i + 1)

    memo[key] = count
    return memo[key]

  return dfs(amount, 0)
