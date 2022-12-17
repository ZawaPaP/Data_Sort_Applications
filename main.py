from sortFunctions import sortFunctions
from writeFile  import writeFile
from readFile  import readFile

import sys
import os

class SortApp():
    def run(inputFile_path, outputFile_path):
        readData = readFile(inputFile_path)
        sortFunction = sortFunctions(readData, outputFile_path)
        sortFunction.sortOption()


    def fileHandles():
        if (sys.argv[1] == None):
            print("argument Error")

        arg = sys.argv[1]
        if not arg:
            return False

        if os.path.isfile(arg):
            return arg

def main():

    file = SortApp.fileHandles()
    read = readFile(file)
    write = writeFile(file)
    inputFile_path = read.Constructor(file)
    outputFile_path = write.Constructor(file)
    SortApp.run(inputFile_path, outputFile_path)
    write.close()

if __name__ == "__main__":
    main()