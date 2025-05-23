def max_path_sum(grid):
  rows = len(grid)
  cols = len(grid[0])

  memo = {}
  
  def dfs(row, col):
    pos = (row, col)
    
    if pos in memo:
      return memo[pos]
    
    if not (0 <= row < rows) or not (0 <= col < cols):
      return 0

    val = grid[row][col]
    
    if row == rows - 1 and cols == col - 1:
      memo[pos] = val
      return val

    memo[pos] = max(dfs(row + 1, col) + val, dfs(row, col + 1) + 1)
    return memo[pos]

  return dfs(0,0)


