import os, sys, unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from sort_data import sort_data
from data_validator import validate_data
from sort_type import SortType
from generate_sample_data import generate_data
from parse_options import get_args

class Test(unittest.TestCase):  
    def test_parser_input_file_to_stdout(self):
        args = get_args(['-i', './tests/test_input.txt'])
        self.assertEqual(args.input.name, './tests/test_input.txt')
        self.assertEqual(args.output_file.name, '<stdout>')

    def test_parser_stdin_to_output_file(self):
        args = get_args(['-o', './tests/test_output.txt'])
        self.assertEqual(args.input.name, '<stdin>')
        self.assertEqual(args.output_file.name, './tests/test_output.txt')

    def test_parser_input_file_to_output_file(self):
        args = get_args([
            '-i', './tests/test_input.txt',
            '-o', './tests/test_output.txt'
                        ])
        self.assertEqual(args.input.name, './tests/test_input.txt')
        self.assertEqual(args.output_file.name, './tests/test_output.txt')
    
    def test_sort_option_is_valid(self):
        for i in range(1, 5):
            with self.subTest(i=i):
                self.assertIn(SortType(i), SortType)
        with self.assertRaises(ValueError):
            SortType(0)

    def test_sort_functions(self):
        data = generate_data()
        for i in range(1, 5):
            with self.subTest(i=i):
                self.assertEqual(sort_data(data, i), sorted(data))

    def test_validate_data(self):
        data = [5,4,3,2,1,0]
        self.assertEqual(validate_data(data), [5,4,3,2,1,0])

        data = [5, 4, 3,2 , 1, 0]
        self.assertEqual(validate_data(data), [5,4,3,2,1,0])

        data = "5 4 3 2 1 0"
        self.assertEqual(validate_data(data), [5,4,3,2,1,0])

if __name__ == '__main__':
    unittest.main()