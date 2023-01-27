import argparse
import sys, logging

def get_args(args):
    logger.debug('Start of parse_options')
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
        help= '1: insert_sort, 2:merge_sort, 3:quick_sort 4:bubble_sort'
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
    logger.debug('End of parse_options {}'.format(parser.parse_args(args)))
    return parser.parse_args(args)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
fh = logging.FileHandler('./log.log')
fh.setFormatter(f)
logger.addHandler(fh) 
