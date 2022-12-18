class SortFunction():
    
    def __init__(self, data, writer):
        self.writer = writer
        self.data = data

    def sortHandlings(self):
        self.insertSort()

    # time complexity O(N^2), space complexity O(N) - using space for data[]
    def insertSort(self):
        if not self.data:
            print("Cannot execute insertFunction")
            return
        for i in range(1, len(self.data)):
            curr = self.data[i]

            j = i
            while j >= 1:
                if (self.data[j-1] > curr):
                    self.data[j] = self.data[j-1]
                    j -= 1
                else:
                    break
            self.data[j] = curr
        self.writer.write(self.data)

