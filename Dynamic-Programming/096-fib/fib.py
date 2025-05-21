def fib(n):
  memo = {}

  def dfs(n):
    if n in memo:
      return memo[n]

    if n == 0:
      return 0
    elif n == 1:
      return 1

    