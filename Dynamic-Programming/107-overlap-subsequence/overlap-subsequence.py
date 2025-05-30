# have two pointers starting at each string
# if the string equal then increase both pointers, increase count
# else increase on or the other pointer

# 

#  1
# dogs
#     2 
# daogt

def overlap_subsequence(string_1, string_2):

  memo = {}
  
  def dfs(s1, s2):

    key = (s1, s2)

    if key in memo:
      return memo[key]

    if s1 >= len(string_1)  or s2 >= len(string_2):
      return 0
    
    if string_1[s1] == string_2[s2]:
      return 1 + dfs(s1 + 1, s2 + 1)

    count = 0
    count += max(dfs(s1 + 1, s2), dfs(s1, s2 + 1))

    return count

  return dfs(0, 0)

test = overlap_subsequence("xcyats", "criaotsi") # -> 4
print(test)