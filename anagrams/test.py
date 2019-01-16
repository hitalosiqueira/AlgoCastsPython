import unittest
from script import anagrams

class Test(unittest.TestCase):
  def test_script(self):
    self.assertFalse(anagrams('One one', 'One one c'))
    self.assertFalse(anagrams('One One', 'Two two two'))
    self.assertTrue(anagrams('hello', 'llohe'));
    self.assertTrue(anagrams('Whoa! Hi!', 'Hi! Whoa!'))
    self.assertFalse(anagrams('A tree, a life, a bench', 'A tree, a fence, a yard'))

if __name__ == "__main__":
  unittest.main() 