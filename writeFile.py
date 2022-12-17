
import os

class writeFile():
    def __init__(self, outputFile):
        self.outputFile = outputFile

    def Constructor(self, file):
        file_name = os.path.basename(file).split(".")[0]
        ext_name = ".txt"
        #dir_name = os.path.dirname(file).replace('./', '')
        # create subdirectory for file export
        os.makedirs("./test", exist_ok=True)
        outputFile_name = "./test/{}{}".format(file_name, ext_name)
        self.outputFile = open(outputFile_name, 'w')
        return self.outputFile

    def write(self, sortedList):
        for item in sortedList:
            self.outputFile.write(str(item) + ",")

    def close(self):
        self.outputFile.close()