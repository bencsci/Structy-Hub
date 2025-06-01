# Create a recursive decision tree where each node is the amount - decision
# Go through each num in numbers in subtract from the amount
# if amount is negative reutrn False
# amount == zero return True

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