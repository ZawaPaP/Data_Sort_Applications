from file_io_controller import read_input_file_data
from file_io_controller import write_output_to_file

import os
import sys

class IOController():
    def __init__(self, args):
        self.args = args
            
    def get_input_data(self):
        if os.path.isfile(self.args.input_file.name):
            return read_input_file_data(self.args.input_file)        
        else:
            try:
                return [x for x in sys.stdin.readlines()]
            except RuntimeError as e:
                print("failed to get input data from stdin")
                sys.exit(1) 
        

    def output_data(self, sorted_data):
        if os.path.isfile(self.args.output_file.name):
            try:
                write_output_to_file(self.args.output_file, sorted_data)
            except Exception as e:
                print(e)
                print("failed to output the data to file")
        elif self.__check_if_stdout_is_pipe():
            try:
                return sorted_data
            except Exception as e:
                print(e)
                print("failed to output the data to pipe")  
        else:
            print(sorted_data)

    def __check_if_stdout_is_pipe(self):
        return not sys.stdout.isatty()
