"""
--- Directions
Given an integer, return an integer that is the reverse
ordering of numbers.
--- Examples
  reverseInt(15) === 51
  reverseInt(981) === 189
  reverseInt(500) === 5
  reverseInt(-15) === -51
  reverseInt(-90) === -9 
"""
from functools import reduce 
from re import sub

def reverseInt(n):
  n_sign = sign(n)
  n_str = ''.join(e for e in str(n) if e.isdigit())
  n_str = reduce(lambda x, y: y + x, n_str, '')
  return int(n_str) * n_sign

def sign(n): return 1 if n >= 0 else -1