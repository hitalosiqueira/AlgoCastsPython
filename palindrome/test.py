import unittest
from script import palindrome

class Test(unittest.TestCase):
  def test_script(self):
    self.assertTrue(palindrome('aba'))
    self.assertFalse(palindrome(' aba'))
    self.assertFalse(palindrome('aba '))
    self.assertFalse(palindrome('greetings'))
    self.assertTrue(palindrome('1000000001'))
    self.assertFalse(palindrome('Fish hsif'))
    self.assertTrue(palindrome('pennep'))

if __name__ == "__main__":
  unittest.main() 