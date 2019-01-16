import unittest
from script import reverse

class Test(unittest.TestCase):
  def test_script(self):
    self.assertEqual(reverse('abcd'), 'dcba')
    self.assertEqual(reverse('  abcd'), 'dcba  ')

if __name__ == "__main__":
  unittest.main()