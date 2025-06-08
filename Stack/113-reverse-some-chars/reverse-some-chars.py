# go through each letter in s, if that letter is in chars then add to stack
# create a new string by adding letters of s, if that letter is in s then pop from stack 
# and use that instead

def reverse_some_chars(s, chars):
  stack = []
  ans = ""
  
  for c in s: 
    if c in chars:
      stack.append(c)

  for c in s:
    if c in chars:
      rev = stack.pop()
      ans += rev
    else:
      ans +=c

  return ans