import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser(description='Sort some integers.')
    parser.add_argument(
        '-v', 
        '--verbose', 
        action='store_true'
    )
    parser.add_argument(
        '-s', 
        '--sort_option', 
        type=int, 
        default = 1, 
        help='sort_option'
        )
    parser.add_argument(
        '-i', 
        '--input_file', 
        nargs='?', 
        type=argparse.FileType('r'),
        default=sys.stdin, 
        help='input file_path as the input source, default = <stdin>'
        )
    parser.add_argument(
        '-o', 
        '--output_file', 
        nargs='?', 
        type=argparse.FileType('w'), 
        default=sys.stdout, 
        help='output data path, default = <stdout>'
        )
    args = parser.parse_args()
    return args
