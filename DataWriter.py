class DataWriter():
    def __init__(self, args):
        self.fp = args.outfile

    def write(self, sortedList):
        for element in sortedList:
            self.fp.write(str(element) + ",")
        self.fp.write("\n")
        self.close()

    def close(self):
        self.fp.close()