# get all perfect squares up to that number
# subtract each perfect square from that number 
# keep track of the count of recursive calls
# return them in of thoses calls where the base case is 0

def summing_squares(n):
  memo  = {}
  
  def dfs(n):
    squares = perfect_squares(n)

    if n in memo:
      return memo[n]
    
    if n < 0:
      return float('inf')

    if n == 0:
      return 0

    minSq = float('inf')
    for square in squares:
      minSq = min(minSq, dfs(n-square)+1)
      memo[n] = minSq

    memo[n] = minSq
    return  memo[n]

  return dfs(n)

def perfect_squares(n):
  squares = []

  if n == 1:
    return [1]
  
  for i in range(1, n):
    square = i * i
    if square > n:
      return squares
    squares.append(square)

  return squares
