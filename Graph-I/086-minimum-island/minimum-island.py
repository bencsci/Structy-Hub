def minimum_island(grid):
  rows = len(grid)
  cols = len(grid[0])

  def dfs(row, col):
    if not (0 <= row < rows and 0 <= col < cols):
      return 0

    if grid[row][col] != 'L':
      return 0

    grid[row][col] = 'V'

    count = 1
    count += dfs(row + 1, col)
    count += dfs(row - 1, col)
    count += dfs(row, col + 1)
    count += dfs(row, col - 1)

    return count

  minI = float('inf')
  for row in range(rows):
    for col in range(cols):
      minI = min(minI, dfs(row, col))

  return minI
  