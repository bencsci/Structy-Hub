# Find all the squares up to and including n
# start at n and go through the squares and subtract
# count each time we do a recursive call 
# and return the min
#        8       [1,4]
#    1/    1\
#    7      4
#  1/    1/  4\
#  6     3    0
def summing_squares(n):

  def dfs(n):
    squares = getSquares(n)
    if n == 0:
      return 0

    if n < 0:
      return float('inf')

    minS = float('inf')
    for square in squares:
      minS = min(minS, dfs(n-square) + 1)

    return minS
  return dfs(n)
def getSquares(n):
  sqaure = []

  if n == 1:
    return [1]
  
  for i in range(1, n):
    if i*i > n:
      break
    sqaure.append(i*i)

  return sqaure

test = summing_squares(9) # -> 1
print(test)