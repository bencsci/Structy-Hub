# Traverse the grid moving down or to the right, if we reach the bottom right corner increase the # count by 1
# If we are out of bounds or hit an x return 0

def count_paths(grid):
  memo = {}
  rows = len(grid)
  cols = len(grid[0])
  
  def dfs(row, col):
    pos = (row, col)

    if pos in memo:
      return memo[pos]

    if not (0 <= row < rows and 0 <= col < cols):
      return 0

    if grid[row][col] == 'X':
      return 0

    if row == rows - 1 and col == cols - 1:
      return 1

    count = 0
    count += dfs(row+1, col)
    count += dfs(row, col+1)

    memo[pos] = count
    return memo[pos]

  return dfs(0,0)

grid = [
  ["O", "O", "X"],
  ["O", "O", "O"],
  ["O", "O", "O"],
]
count_paths(grid) # -> 5
test = count_paths(grid) # -> 2
print(test)
