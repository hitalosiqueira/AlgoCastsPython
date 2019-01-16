import unittest
from script import chunk

class Test(unittest.TestCase):
  def test_script(self):
    self.assertEqual(chunk([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    self.assertEqual(chunk([1, 2, 3], 1), [[1], [2], [3]])
    self.assertEqual(chunk([1, 2, 3, 4, 5], 3), [[1, 2, 3], [4, 5]])
    self.assertEqual(chunk([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 5), [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13]])
 
if __name__ == "__main__":
  unittest.main()