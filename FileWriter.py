
import os

class FileWriter():
    def __init__(self, output_file_path):
        self.output_file_path = output_file_path
        file_name = os.path.basename(output_file_path).split(".")[0]
        ext_name = ".txt"
        print("output file name = " + str(file_name))
        #dir_name = os.path.dirname(file).replace('./', '')
        # create subdirectory for file export
        os.makedirs("./sorted", exist_ok=True)
        output_file_name = "./sorted/{}{}".format(file_name, ext_name)
        self.fp = open(output_file_name, 'w')

    def write(self, sortedList):
        for item in sortedList:
            self.fp.write(str(item) + ",")

    def close(self):
        self.fp.close()