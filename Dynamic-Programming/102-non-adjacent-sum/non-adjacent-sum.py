# make a decision tree, taking the first item or non_adjacent_sum
# if take the first item, have an index starting after the second item reprsenting possible sums
# if the do not take the first item have an index starting at the second item repsenting possible sums
# keep track of the sums for each branch, return the highest sums out of those branches

#      [2, 4, 5, 12, 7]
#     2 /            \ 0
#[5, 12, 7]       [4, 5, 12, 7]
# include          exclude

# Better: Make a decision tree to include or exclude the first value
# have an index to keep track of what values to use in order to save time
# if take the first item, have an index starting after the second item reprsenting possible sums
# if the do not take the first item have an index starting at the second item repsenting possible sums

def non_adjacent_sum(nums):
  memo = {}
  
  def dfs(i):
    if i in memo:
      return memo[i]

    if i >= len(nums):
      return 0

    include = nums[i] + dfs(i + 2)
    exclude = dfs(i + 1)

    memo[i] = max(include, exclude)
    return memo[i]

  return dfs(0)
