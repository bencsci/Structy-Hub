def tribonacci(n):
  memo = {}

  def dfs(n):

    if n in memo:
      return memo[n]

    if n == 0 or n == 1:
      return 0
    elif n == 2:
      return 1

    memo[n] = dfs(n-1) + dfs(n-2) + dfs(n-3)
    return memo[n]

  return dfs(n)
