# Create a recusive tree where each node represents the current string
# each branch checks if each word in words is at the start of the curr string
# if it starts with that word, increase the index to pass the end of that that word
# marking the start of a new string
# if we reach the end of the string then we return True

def can_concat(s, words):
  memo = {}
  
  def dfs(idx):
    if idx in memo:
      return memo[idx]

    if idx == len(s):
      return True

    for word in words:
      if s.startswith(word, idx):
        if dfs(idx + len(word)):
          memo[idx] = True
          return True

    memo[idx] = False
    return memo[idx] 

  return dfs(0)

