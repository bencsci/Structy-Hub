def count_paths(grid):
  rows = len(grid)
  cols = len(grid[0])

  memo = {}
  
  def dfs(row, col):
    pos = (row, col)

    if pos in memo:
      return memo[pos]
    
    if not (0 <= row < rows) or not (0 <= col < cols) or grid[row][col] == 'X':
      return 0
    
    if row == rows - 1 and col == cols - 1:
      memo[pos] = 1
      return 1

    memo[pos] = dfs(row+1,col) + dfs(row,col+1)
    return memo[pos]

  return dfs(0,0)

    
