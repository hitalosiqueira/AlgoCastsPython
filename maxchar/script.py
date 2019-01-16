"""
--- Directions
Given a string, return the character that is most
commonly used in the string.
--- Examples
maxChar("abcccccccd") === "c"
maxChar("apple 1231111") === "1" 
"""

def maxChar(string):
  d = {}
  for c in string:
    if c in d:
      d[c] += 1
    else:
      d[c] = 1
  return max(d, key=d.get)
  