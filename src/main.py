from set_logger import SetLogger
from parse_options import get_args
from sort_data import sort_data
from io_controller import IOController
from data_validator import validate_data
from compare_sort_time import compare_sort_time

import sys

def main():
    args = get_args(sys.argv[1:])
    SetLogger.verbose = args.verbose
    SetLogger.log = args.log
    logger = SetLogger().set_logger(__name__)

    io_controller = IOController(args)
    input = io_controller.read()
    data = sort_data(validate_data(input), args.sort_option)
    io_controller.write(data)
    logger.info("Finished the application")
    
if __name__ == "__main__":
    main()
