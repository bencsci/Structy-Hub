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