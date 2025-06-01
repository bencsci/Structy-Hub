# Go through each decision to move own or right
# once our grid position == the bottom right corner increase our count

def count_paths(grid):
  rows = len(grid)
  cols = len(grid[1])
  memo = {}
  
  def dfs(row, col):
    pos = (row, col)

    if pos in memo:
      return memo[pos]
    
    if not (0 <= row < rows) or not (0 <= col < cols):
      return 0

    if grid[row][col] != 'O':
      return 0

    if row == rows - 1 and col == cols - 1:
      return 1

    count = 0
    count += dfs(row + 1, col)
    count += dfs(row, col + 1)

    memo[pos] = count
    return memo[pos]

  return dfs(0, 0)