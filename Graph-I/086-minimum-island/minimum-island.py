# traverse grid until we find Land
# dfs search while keeping the count of the size
# return the size once thed dfs has completed
# compare to find min size
def minimum_island(grid):
  rows = len(grid)
  cols = len(grid[0])
  smallest = float('inf')
  
  def dfs(row, col):
    if not (0 <= row < rows) or not (0 <= col < cols):
      return 0

    if grid[row][col] != 'L':
      return 0 
    
    grid[row][col] = 'V'

    size = 1
    size += dfs(row + 1, col)
    size += dfs(row - 1, col)
    size += dfs(row, col + 1)
    size += dfs(row, col - 1)

    return size

  for row in range(rows):
    for col in range(cols):
      if grid[row][col] == 'L':
        smallest = min(smallest, dfs(row, col))

  return smallest
    
    