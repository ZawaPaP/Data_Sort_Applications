from FileReader import FileReader
from DataExample import data_example
import re
import os
import sys
import fileinput

class DataOrganizer():
    def __init__(self, args):
        self.args = args
        self.reader = FileReader(args)
        self.data = None

    def validate_input(self):
        self.data = self.get_input_data()

        try:
            if not self.check_is_list():
                self.change_to_list()

            if not self.check_is_int():
                self.change_to_int()
                #stringsの場合について後ほど検討
        except Exception as e:
            print(e)

        return self.data
            
    def get_input_data(self):
        if self.check_if_stdin_has_data():
            return [ int(x) for x in sys.stdin.readlines()]

        elif self.args.input_file_path and os.path.isfile(self.args.input_file_path.name):
            return self.reader.read().replace(' ','')
        else:
            return data_example()  # import example data
    
    def check_if_stdin_has_data(self):
        if fileinput.input():
            return True
        return False

    def change_to_list(self):        
        self.data = re.split(",", self.data)
        self.data = list(filter(None, self.data))

    def check_is_list(self):
        if isinstance(self.data, list):
            return True
        else:
            return False

    def check_is_int(self):
        for i in range(len(self.data)):
            if not isinstance(self.data[i], int):
                self.change_to_int(i)
        return True

    def change_to_int(self, i: int):
        self.data[i]= int(self.data[i])