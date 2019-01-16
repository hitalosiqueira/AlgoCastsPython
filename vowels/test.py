import unittest
from script import vowels

class Test(unittest.TestCase):
  def test_script(self):
    self.assertEqual(vowels('aeiou'), 5)
    self.assertEqual(vowels('AEIOU'), 5)
    self.assertEqual(vowels('abcdefghijklmnopqrstuvwxyz'), 5)
    self.assertEqual(vowels('bcdfghjkl'), 0)

if __name__ == "__main__":
  unittest.main() 