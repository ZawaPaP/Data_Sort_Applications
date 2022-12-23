from FileReader import FileReader
import re

class DataOrganizer():
    def __init__(self, args):
        self.args = args
        self.reader = FileReader(args)
        self.data = None

    def data_organizer(self):
        self.data = self.reader.read()
        self.data = self.data.replace(' ','')

        if not self.check_is_list():
            self.change_to_list()

        if not self.check_is_int():
            self.change_to_int()
            #stringsの場合について後ほど検討
        return self.data
            
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