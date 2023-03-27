import unittest

def reverse(a_list):
    result = lambda x: x[:: -1] 
    return( result(a_list))
   
class TestRev(unittest.TestCase):
    def test_rev(self):
        self.assertEqual(reverse(['1','4','7','2']), ['2','7','4','1'])

if __name__ == '__main__':
    unittest.main()
##################################### 
  
import unittest

def find_largest(numbers):
    return max(numbers)

class TestAdd(unittest.TestCase):
    def test_find_largest(self):
        self.assertEqual(find_largest([167, 56, 244, -100, 56789]), 56789)
        
if __name__ == '__main__':
    unittest.main()
#####################################

import unittest

def file_evaluator(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    return lines
            
class TestFile(unittest.TestCase):
    def test_file(self):
        self.assertEqual(file_evaluator('test_data.txt'), ['John,Doe,25\n', 'Jane,Doe,30'])

if __name__ == '__main__':
    unittest.main()
#####################################

import unittest

def Only_odd(int_number_list):
    odd_list =[]
    for item in int_number_list:
        if item % 2 != 0:
            odd_list.append(item)
    return odd_list

class TestOdd(unittest.TestCase):
    def test_odd(self):
        self.assertEqual(Only_odd([24,3,78,911,7,42,11]), [3,911,7,11])


if __name__ == '__main__':
    unittest.main()
#########################################