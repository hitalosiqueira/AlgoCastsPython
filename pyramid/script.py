""" 
--- Directions
Write a function that accepts a positive number N.
The function should console log a pyramid shape
with N levels using the # character.  Make sure the
pyramid has spaces on both the left *and* right hand sides
--- Examples
  pyramid(1)
      '#'
  pyramid(2)
      ' # '
      '###'
  pyramid(3)
      '  #  '
      ' ### '
      '#####' 
"""

def pyramid(n):
  odd = 1
  tam = 2 * n - 1
  for _ in range(n):
    half = (tam - odd)//2
    print((' ' * half) + ('#' * odd) + (' ' * half))
    odd += 2