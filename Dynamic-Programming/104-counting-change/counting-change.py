# Create recursive tree with each level representing the value of the coins
# and take 0 ... n amount of that coin while subtracting qty x coin for each node
# 

def counting_change(amount, coins):
  memo = {}

  def dfs(amount, i):
    key = (amount, i)

    if key in memo:
      return memo[key]
    
    if i == len(coins):
      return 0
    
    if amount == 0:
      return 1

    coin = coins[i]

    count = 0
    for qty in range((amount // coin) + 1):
      remainder = amount - (qty * coin)
      count += dfs(remainder, i + 1)

    memo[key] = count
    return memo[key]

  return dfs(amount, 0)
      
