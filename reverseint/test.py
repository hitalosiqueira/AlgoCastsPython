import unittest
from script import reverseInt

class Test(unittest.TestCase):
  def test_script(self):
    self.assertEqual(reverseInt(5), 5)
    self.assertEqual(reverseInt(15), 51)
    self.assertEqual(reverseInt(90), 9)
    self.assertEqual(reverseInt(2359), 9532)
    self.assertEqual(reverseInt(-5), -5)
    self.assertEqual(reverseInt(-15), -51)
    self.assertEqual(reverseInt(-90), -9)
    self.assertEqual(reverseInt(-2359), -9532)

if __name__ == "__main__":
  unittest.main() 