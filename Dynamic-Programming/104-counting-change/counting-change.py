# create a tree where each level represents the value of the coin from 1 ... coin
# on each level we can choose a quantity for using that coin from 0 ... coin
# if we reach zero then we can count it as a successfull branch

#                     4
#    x0/    x1/     x2|    x3\     x4\ number of times we used 1 cent coin
#   4       3        2      1       0 
# etc.

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
      remainder = amount - (qty * coin)
      count += dfs(remainder, i + 1)

    memo[key] = count
    return memo[key]

  return dfs(amount, 0)
  
