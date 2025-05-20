# traverse the grid, if we find land
# dfs search until we explored all the land, mark the visited land
# return True to count the island
def island_count(grid):
  rows = len(grid)
  cols = len(grid[0])

  def dfs(row, col):
    if not (0 <= row < rows) or not (0 <= col < cols):
      return False

    if grid[row][col] == 'W':
      return False

    if grid[row][col] == 'V':
      return False

    grid[row][col] = 'V'

    dfs(row+1, col)
    dfs(row-1, col)
    dfs(row, col+1)
    dfs(row, col-1)

    return True

  count = 0
  for row in range(rows):
    for col in range(cols):
      if dfs(row, col):
        count += 1

  return count
        
