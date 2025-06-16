# Traverse the grid by moving to the right or down keep track of the running sum
# have a max to update if there is a new max
# if we are out of bounds return -inf
# if we reach the bottom right corner return our current number

def max_path_sum(grid):
  memo = {}
  rows = len(grid)
  cols = len(grid[0])
  
  def dfs(row, col):
    pos = (row, col)

    if not (0 <= row < rows and 0 <= col < cols):
      return float('-inf')

    if row == rows - 1 and col == cols - 1:
      return grid[row][col]
      
    num = grid[row][col]
    maxS = float('-inf')
    maxS = max(maxS, dfs(row+1, col) + num, dfs(row, col+1) + num)

    return maxS

  return dfs(0, 0)
  
