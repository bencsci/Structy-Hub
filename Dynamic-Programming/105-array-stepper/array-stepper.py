# Traverse through the list and create a dicision tree of choosing steps at that index
# if we are at the end of the list or beyond return True
# if we land on a 0 return False

def array_stepper(numbers):

  memo = {}
  
  def dfs(i):

    if i in memo:
      return memo[i]
      
    if i >= len(numbers):
      return True

    step = numbers[i]
    if step == 0:
      return False

    for step in range(1, step + 1):
      if dfs(i + step):
        memo[i] = True
        return memo[i]

    memo[i] = False
    return memo[i]

  return dfs(0)