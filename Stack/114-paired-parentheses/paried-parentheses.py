# go through the string if we find a open brace then add to stack
# if we find matching closing brach pop from stack
# else if we see a closing brace without a opening brace return false
# if stack is empty return true
# else return false

def paired_parentheses(string):
  stack = []
  
  for s in string:
    if s == '(':
      stack.append(s)
    elif stack and s == ')':
      stack.pop()
    elif s == ')':
      return False

  if not stack:
    return True

  return False