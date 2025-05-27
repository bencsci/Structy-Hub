# Create a recursive Tree, where each node represents an the current index
# Each branch is the step at the index
# If our current step is 0: return False
# If we are >= len(numbers) - 1: return True -> this means we reached the end of the array

def array_stepper(numbers):
  memo = {}
  
  def dfs(idx):
    if idx in memo:
      return memo[idx]
    
    if idx >= len(numbers) - 1:
      return True

    curr_step = numbers[idx]

    if curr_step == 0:
      return False

    for step in range(1, curr_step + 1):
      if dfs(idx + step):
        memo[idx] = True
        return True

    memo[idx] = False
    return memo[idx]

  return dfs(0)