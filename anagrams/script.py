""" --- Directions
Check to see if two provided strings are anagrams of eachother.
One string is an anagram of another if it uses the same characters
in the same quantity. Only consider characters, not spaces
or punctuation.  Consider capital letters to be the same as lower case
--- Examples
  anagrams('rail safety', 'fairy tales') --> True
  anagrams('RAIL! SAFETY!', 'fairy tales') --> True
  anagrams('Hi there', 'Bye there') --> False """
from re import sub

def anagrams(stringA, stringB):
  charMapA = create_char_map(stringA)
  charMapB = create_char_map(stringB)

  return charMapA == charMapB

def create_char_map(string):
  string = ''.join(e for e in string if e.isalpha()).lower()
  d = {}
  for char in string:
    if char in d:
      d[char] += 1
    else:
      d[char] = 1
  return d