
import sys
import os
import re

class readFile():

    def __init__(self, inputFile_path):
        self.fp = inputFile_path
        self.list = []
        self.data = ""
        self.splitline = ""

    def Constructor(self, file):
        self.fp = open(file, 'r')
        return self.fp

    def read(self):
        self.data = self.fp.read()

        if self.data == "":
            return False
        else:
            return True

    def tokenizer(self):
        if self.read() == True:
            self.data.split()
            self.splitline = re.split(",", self.data)
            self.splitline = list(filter(None, self.splitline))
            self.list = [int(i) for i in self.splitline]

            if self.splitline == "":
                return False
            return self.list
        
        print("No Data Found")
        return False

    # check text size 
    #def fileSizeCheck(self):
