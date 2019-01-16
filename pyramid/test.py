import io
import sys
import unittest
from script import pyramid

class Test(unittest.TestCase):
  def test_script(self):
    capturedOutput = io.StringIO()                
    sys.stdout = capturedOutput                  
    pyramid(5)                                   
    sys.stdout = sys.__stdout__ 
    output = capturedOutput.getvalue().split('\n')
    self.assertEqual(output[0], '    #    ')
    self.assertEqual(output[1], '   ###   ')
    self.assertEqual(output[2], '  #####  ')
    self.assertEqual(output[3], ' ####### ')
    self.assertEqual(output[4], '#########')

if __name__ == "__main__":
  unittest.main() 