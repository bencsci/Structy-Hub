def island_count(grid):
  rows = len(grid)
  cols = len(grid[0])

  def dfs(row, col):
    if not (0 <= row < rows and 0 <= col < cols):
      return False

    if grid[row][col] != 'L':
      return False

    grid[row][col] = 'V'

    dfs(row + 1, col)
    dfs(row, col + 1)
    dfs(row - 1, col)
    dfs(row, col - 1)

    return True

  count = 0
  for row in rows:
    for col in cols:
      if df(row, col):
        count += 1

  return count