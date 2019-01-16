import unittest
from script import maxChar

class Test(unittest.TestCase):
  def test_script(self):
    self.assertEqual(maxChar('abcdefghijklmnaaaaa'), 'a')
    self.assertEqual(maxChar('a'), 'a')
    self.assertEqual(maxChar('ab1c1d1e1f1g1'), '1')

if __name__ == "__main__":
  unittest.main() 