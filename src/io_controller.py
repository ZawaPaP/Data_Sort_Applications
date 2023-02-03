from file_io_controller import read_input_file_data
from file_io_controller import write_output_to_file
from set_logger import SetLogger

import os, sys

class IOController():
    logger = SetLogger().set_logger(__name__)
    
    def __init__(self, args):
        self.args = args
        self.input = args.input
        self.output_file = args.output_file
    
    def read(self):
        if os.path.isfile(self.input.name):
            try:
                return read_input_file_data(self.input)
            except Exception as e:
                self.logger.error(e)
                self.logger.error("input file path exists, but unable to read")
                sys.ext(1)        
        else:
            try:
                for line in sys.stdin:
                    if 'Exit' == line.rstrip():
                        break
                    return line
                #[x for x in sys.stdin.readlines()]
            except RuntimeError as e:
                self.logger.error(e)
                self.logger.error("failed to get input data from stdin")
                sys.exit(1) 
        
    def write(self, data):
        if os.path.isfile(self.output_file.name):
            try:
                write_output_to_file(self.args.output_file, data)
            except Exception as e:
                self.logger.error(e)
                self.logger.error("failed to output the data to file")
        else:
            try:
                for x in data:
                    sys.stdout.write(str(x)+'\n')
            except Exception as e:
                self.logger.error(e)
                self.logger.error("failed to output the data to stdout")  

