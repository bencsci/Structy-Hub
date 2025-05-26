# create a recursive tree with each branch adding a word on the list
# with each recursive call check if it "matches" with the original string
# if yes then return True
# if the current built string len is > the original string: return False
# default return False

# Optimization: use memoization to reuse already seen values
def can_concat(s, words):

  memo = {}
  
  def dfs(curr):
    if curr in memo:
      return memo[curr]
    
    if len(curr) > len(s):
      return False

    if match(curr, s):
      return True

    for word in words:
      if dfs(curr + word):
        memo[curr] = True
        return memo[curr]

    memo[curr] = False
    return memo[curr]

  return dfs("")

def match(w1, w2):
  s1 = {}
  s2 = {}

  for c in w1:
    s1[c] = 1 + s1.get(c, 0)
  for c in w2:
    s2[c] = 1 + s2.get(c, 0)

  return s1 == s2
