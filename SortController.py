import SortFunction
from DataOrganizer import DataOrganizer

class SortController():
    def __init__(self, args):
        organizer = DataOrganizer(args)
        self.data = organizer.data_organizer()
        self.sort_type = args.sort

    def sortController(self):
        if self.sort_type == "insert":
            SortFunction.insertSort(self.data)
        elif self.sort_type == "merge":
            SortFunction.mergeSort(self.data)
        elif self.sort_type == "quick":
            SortFunction.quickSort(self.data)
        else:
            print('invalid sort_type')
        return self.data