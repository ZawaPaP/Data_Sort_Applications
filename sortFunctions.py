from writeFile import writeFile

class sortFunctions():
    
    def __init__(self,readFile, outputFile_path):
        self.outputFile_path = outputFile_path
        self.readFile = readFile
        self.writeFile = writeFile(outputFile_path)
        self.data = []

    def sortOption(self):
        self.data = self.readFile.tokenizer()
        self.insertSort()

    # time complexity O(N^2), space complexity O(1)
    def insertSort(self):
        if not self.data:
            print("Cannot execute insertFunction")
            return
        print(self.data)
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
        print("##########")
        print(self.data)
        self.writeFile.write(self.data)