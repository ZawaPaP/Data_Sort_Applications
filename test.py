from sort import sort
from data_validator import validate_data

import unittest

class Test(unittest.TestCase):
        
    def test_sort_option_is_valid(self):
        data = [5,4,3,2,1]
        result = sort(data, 1)
        self.assertEqual(result, [1,2,3,4,5])
        with self.assertRaises(ValueError):
            sort(data, 10)

    def test_validate_data(self):
        data = [5,4,3,2,1]
        result = validate_data(data)
        self.assertEqual(result, [5,4,3,2,1])

        data = "5,4,3,2,1"
        result = validate_data(data)
        self.assertEqual(result, [5,4,3,2,1])
        with self.assertRaises(TypeError):
            sort("aaaaa")
        
if __name__ == '__main__':
    unittest.main()