from parse_options import get_args
from sort_data import sort_data
from io_controller import IOController
from data_validator import validate_data
from compare_sort_time import compare_sort_time

import sys, logging

def main():
    logger.debug("Start of main module")
    args = get_args(sys.argv[1:])
    io_controller = IOController(args)
    input = io_controller.read()
    if args.verbose >= 2:
        compare_sort_time(validate_data(input))
    else:
        data = sort_data(validate_data(input), args.sort_option)
        io_controller.write(data)
    logger.debug("End of main module")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
fh = logging.FileHandler('./log/main.log')
fh.setFormatter(f)
logger.addHandler(fh) 

if __name__ == "__main__":
    main()
