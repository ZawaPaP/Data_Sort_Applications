from file_io_controller import read_input_file_data
from file_io_controller import write_output_to_file

import os, sys, logging

class IOController():
    def __init__(self, args):
        logger.debug('Init of io_controller')
        self.args = args
        self.input = args.input
        self.output_file = args.output_file
    
    def read(self):
        logger.debug('Start of read')
        if os.path.isfile(self.input.name):
            try:
                return read_input_file_data(self.input)
            except Exception as e:
                logger.error(e)
                sys.ext(1)        
        else:
            try:
                return [x for x in sys.stdin.readlines()]
            except RuntimeError as e:
                logger.error("failed to get input data from stdin")
                logger.error(e)
                sys.exit(1) 
        

    def write(self, data):
        logger.debug('Start of write')
        if os.path.isfile(self.output_file.name):
            try:
                write_output_to_file(self.args.output_file, data)
            except Exception as e:
                logger.error(e)
                logger.error("failed to output the data to file")
        else:
            try:
                for x in data:
                    sys.stdout.write(str(x)+'\n')
            except Exception as e:
                logger.error(e)
                logger.error("failed to output the data to stdout")  
                
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
fh = logging.FileHandler('./log.log')
fh.setFormatter(f)
logger.addHandler(fh)  
