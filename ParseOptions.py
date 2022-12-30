import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser(description='Sort some integers.')

    parser.add_argument(
        '-d', 
        '--data',
        type=int, 
        nargs='+', 
        help='an integer for the sort, give dummy data without input [0,9,8,7,6,5,4,3,2,1]'
        )
    parser.add_argument(
        '-s', 
        '--sort', 
        type=str, 
        default = 'insert', 
        help='sort_type,default = insertSort'
        )
    parser.add_argument(
        '-i', 
        '--input_file_path', 
        nargs='?', 
        type=argparse.FileType('r'),
        default=sys.stdin, 
        help='input file_path as the input source, default = <stdin>'
        )
    parser.add_argument(
        '-o', 
        '--outfile', 
        nargs='?', 
        type=argparse.FileType('w'), 
        default=sys.stdout, 
        help='output data path, default = <stdout>'
        )
    args = parser.parse_args()
    return args