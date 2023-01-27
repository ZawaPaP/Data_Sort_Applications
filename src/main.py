from set_logger import SetLogger
from parse_options import get_args
from sort_data import sort_data
from io_controller import IOController
from data_validator import validate_data

import sys

def main():
    try:
        args = get_args(sys.argv[1:])
        SetLogger.verbose = args.verbose
        SetLogger.log = args.log
        logger = SetLogger().set_logger(__name__)

        io_controller = IOController(args)
        input = io_controller.read()
        sorted_data = sort_data(validate_data(input), args.sort_option)
        io_controller.write(sorted_data)
        logger.info("Finished the application")
    except KeyboardInterrupt:
        print ("Shutdown requested...exiting")
        sys.exit(130)
    
if __name__ == "__main__":
    main()
