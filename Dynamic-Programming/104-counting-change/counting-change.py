# Create a decision tree where each level represents the value of the coin
# 1 .. n and each branch is choosing 0 .. n coins
# each node value we subtract the qty * coin from our amount until we reach 0
# count the number of times we reach 0
# have an index so we can traverse through the coins for each call
# [1, 2, 3]
#                    4
#       0x/   1x/  2x|  3x\  4x\    1 cent coins
#       4     3    2     1    0
def counting_change(amount, coins):

  memo = {}
  
  def dfs(amount, i):

    key = (amount, i)

    if key in memo:
      return memo[key]
    
    if amount == 0:
      return 1

    if i >= len(coins):
      return 0

    coin = coins[i]

    count = 0
    for qty in range((amount // coin) + 1):
      next = amount - (qty * coin)
      count += dfs(next, i+1)

    memo[key] = count
    return memo[key]

  return dfs(amount, 0)
      

    

    