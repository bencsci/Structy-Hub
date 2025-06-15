def sum_possible(amount, numbers):

  memo = {}
  
  def dfs(amount):

    if amount in memo:
      return amount[memo]
    
    if amount == 0:
      return True

    if amount < 0:
      return False

    for num in numbers:
      if dfs(amount - num):
        amount[memo] = True
        return True
        
    amount[memo] = False
    return amount[memo]

  return dfs(amount)
