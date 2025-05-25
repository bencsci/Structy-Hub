# get all perfect sqares up to n, in an array 
# subtract each number in that array from n
# if n == 0 return 0 indicating we reached an answer
# keep track of each recursive call to count the number of squares added
# compare the min of each success full branch to find the minimum 


def summing_squares(n):
  squares = perfect_squares(n)

  memo = {}
  
  def dfs(n):
    if n in memo:
      return memo[n]
    
    if n < 0:
      return float('inf')

    if n == 0:
      return 0

    maxSq = float('inf')
    for square in squares:
      maxSq = min(maxSq, dfs(n-square) + 1)

    memo[n] = maxSq
    return memo[n]

  return dfs(n)

def perfect_squares(n):
  squares = []

  if n == 1:
    return [n]

  for i in range(1, n):
    square = i*i
    if square > n:
      return squares
    squares.append(square)

  return squares

test = summing_squares(12) #  -> 3
print(test)