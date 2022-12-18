from SortFunction import SortFunction
from FileWriter import FileWriter
from FileReader import FileReader

import sys
import os
#  
class SortApp():
    def fileHandles(self):
        if (sys.argv[1] == None):
            print("argument Error")
        arg = sys.argv[1]
        if not arg:
            return False
        if os.path.isfile(arg):
            return arg

    def run(self,reader, writer):
        data = reader.tokenizer()
        sort_function = SortFunction(data, writer)
        sort_function.sortHandlings()
        writer.close()

def main():
    file_path = SortApp().fileHandles()
    reader = FileReader(file_path)
    writer = FileWriter(file_path)
    SortApp().run(reader, writer)


if __name__ == "__main__":
    main()