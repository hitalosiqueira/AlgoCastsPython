import io
import sys
import unittest
from script import fizzBuzz

class Test(unittest.TestCase):
  def test_script(self):
    capturedOutput = io.StringIO()                
    sys.stdout = capturedOutput                  
    fizzBuzz(15)                                   
    sys.stdout = sys.__stdout__ 
    output = capturedOutput.getvalue().split('\n')
    self.assertEqual(output[0], '1')
    self.assertEqual(output[1], '2')
    self.assertEqual(output[2], 'fizz')
    self.assertEqual(output[3], '4')
    self.assertEqual(output[4], 'buzz')
    self.assertEqual(output[5], 'fizz')
    self.assertEqual(output[6], '7')
    self.assertEqual(output[7], '8')
    self.assertEqual(output[8], 'fizz')
    self.assertEqual(output[9], 'buzz')
    self.assertEqual(output[10], '11')
    self.assertEqual(output[11], 'fizz')
    self.assertEqual(output[12], '13')
    self.assertEqual(output[13], '14')
    self.assertEqual(output[14], 'fizzbuzz')

if __name__ == "__main__":
  unittest.main() 