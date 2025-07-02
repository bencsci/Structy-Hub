# Traverse through the grid until we find the first letter in the string
# Have an index i to keep track of which letter we are on
# Start dfs at the first letter and mark visited letteres
# look the next i+1 letter 
# if we find all letteres then return True

def string_search(grid, s):
  rows = len(grid)
  cols = len(grid[1])
  v = set()

  def dfs(row, col, i):
    if not (0 <= row < rows and 0 <= col < cols):
      return False
    
    if i == len(s):
      return True
    
    if grid[row][col] != s[i]:
      return False

    pos = (row, col)

    if pos in v:
      return False

    v.add(pos)
    
    res = (dfs(row+1,col, i + 1) 
           or dfs(row-1,col, i + 1) 
           or dfs(row,col+1, i + 1) 
           or dfs(row,col-1, i + 1))
    
    v.remove(pos)
    return res

  for row in range(rows):
    for col in range(cols):
      if dfs(row, col, 0):
        return True

  return False 