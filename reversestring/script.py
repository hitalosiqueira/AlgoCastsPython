""" 
--- Directions
Given a string, return a new string with the reversed
order of characters
--- Examples
  reverse('apple') === 'leppa'
  reverse('hello') === 'olleh'
  reverse('Greetings!') === '!sgniteerG' 
"""
from functools import reduce

def reverse(string):
  return reduce(lambda rev, c: c + rev, string, '')
