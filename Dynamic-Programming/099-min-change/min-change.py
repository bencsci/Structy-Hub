# Create recusrive tree where each node represents the amount
# each branch is the decision to choose one the coin the the coins
# keep track of the amount of decison in a branch 
# if amount < 0 reutrn False
# if amount == 0 updtae the minC

def min_change(amount, coins):
  memo = {}
  
  def dfs(amount):

    if amount in memo:
      return memo[amount]
    
    if amount < 0:
      return float('inf')

    if amount == 0:
      return 0

    count = 0
    minC = float('inf')
    for coin in coins:
      minC = min(minC, dfs(amount - coin) + 1)

    memo[amount] = minC
    return memo[amount]

  ans = dfs(amount)
  return ans if ans != float('inf') else -1
