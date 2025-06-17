# Have an index starting at the start of the word
# for each word in words check if that word is at the beginning of s
# if it is move the index to i + len(word)
# if we reach the end of the string return True
# else False

def can_concat(s, words):

  memo = {}
  
  def dfs(i):
    if i in memo:
      return memo[i]
    
    if i == len(s) - 1:
      return True

    for word in words:
      if s.startswith(word, i):
        if dfs(i + len(word)):
          memo[i] = True
          return memo[i]

    memo[i] = False
    return memo[i]

  return dfs(0)