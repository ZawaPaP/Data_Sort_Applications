import argparse
import sys

def get_args(args):
    parser = argparse.ArgumentParser(description='Sort some integers.', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '-v', 
        '--verbose', 
        action = "count",
        help ='''
            -v: logging.DEBUG if verbose else logging.ERROR\n
            -vv: try all sort options and print processed time
                '''
    )
    parser.add_argument(
        '-l',
        '--log',
        action = "store_true",
        help='create log file if log else log to <stderr>'
    )
    parser.add_argument(
        '-s', 
        '--sort_option', 
        type = int, 
        default = 1, 
        help = '''
            1: insert_sort\n
            2: merge_sort\n
            3: quick_sort\n
            4: bubble_sort\n
            5: heap sort
            '''
        )
    parser.add_argument(
        '-i', 
        '--input', 
        nargs='?', 
        type=argparse.FileType('r'),
        default=sys.stdin, 
        help='input data or input file path, default = <stdin>'
        )
    parser.add_argument(
        '-o', 
        '--output_file', 
        nargs='?', 
        type=argparse.FileType('w'), 
        default=sys.stdout, 
        help='output data path, default = <stdout>'
        )
    return parser.parse_args(args)
