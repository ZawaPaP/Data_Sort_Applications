
import re

class FileReader():

    def __init__(self, input_file_path):
        self.file_path = input_file_path
        self.fp = open(self.file_path, 'r')
        self.list = []
        self.data = ""
        self.split_line = ""

    def read(self):
        self.data = self.fp.read()
        if self.data == "":
            return self.data == ""

    def tokenizer(self):
        self.read()
        if self.data != "":
            self.data.split()
            self.split_line = re.split(",", self.data)
            self.split_line = list(filter(None, self.split_line))
            self.list = [int(i) for i in self.split_line]

            if self.split_line == "":
                return None
            return self.list
        
        print("No Data Found")
        return None

    # check text size 
    #def fileSizeCheck(self):
