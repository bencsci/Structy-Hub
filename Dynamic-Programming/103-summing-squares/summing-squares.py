def summing_squares(n):
  memo = {}

  def dfs(amount):
    squares = perfect_squares(amount)
    
    if amount in memo:
      return memo[amount]
    
    if amount < 0:
      return float('inf')

    if amount == 0:
      return 0

    minS = float('inf')
    for square in squares:
      minS = min(minS, dfs(amount-square) + 1)
      memo[amount] = minS

    memo[amount] = minS
    return memo[amount]
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

