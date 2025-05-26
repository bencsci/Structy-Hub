# Create a recursive tree with each call being a decision from 1 .... step
# if our step is 0: return False
# if we move out of bounds return: False
# if we reach the end of the array: return True
# Otherwise return False

#                       2
#               1/             2\
#               4               2    
#         1/ 2/ 3\ 4\        1/  2\
#  etc.

# Optimization: use memoization to store previously calculated values


def array_stepper(numbers):

  memo = {}
  
  def dfs(i):

    if i >= len(numbers):
      return False

    if i == len(numbers) - 1:
      return True
    
    step = numbers[i]

    if step == 0:
      return False

    for choice in range(1, step+1):
      if dfs(i + choice):
        return True

    return False

  return dfs(0)

    

  
