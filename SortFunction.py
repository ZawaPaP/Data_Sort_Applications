from collections import deque

class SortFunction():
    
    def __init__(self, data, writer):
        self.writer = writer
        self.data = data
        self.left_pointer = 0
        self.right_pointer = len(self.data)


    def sortHandlings(self):
        self.mergeSort(self.left_pointer, self.right_pointer)
        self.writer.write(self.data)

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
        

    # time complexity O(NlogN), space complexity O(2N) - using space for data[] and queue()
    def mergeSort(self, left_pointer, right_pointer):
        if right_pointer - left_pointer == 1:
            return

        mid = left_pointer + (right_pointer - left_pointer) // 2
        self.mergeSort(left_pointer, mid)
        self.mergeSort(mid, right_pointer)

        queue = deque()
        print(left_pointer)
        #print(mid)
        for i in range(left_pointer, mid):
            queue.appendleft(self.data[i])
        for i in range(right_pointer-1, mid-1, -1):
            queue.append(self.data[i])
        print(queue)
        for i in range(right_pointer, left_pointer):
            if queue[0] <= queue[-1]:
                self.data[i] = queue.popleft()
            else:
                self.data[i] = queue.pop()


    def quickSort(self, left_pointer, right_pointer):
        if right_pointer - left_pointer <= 1:
            return

        pivot_index = (left_pointer + right_pointer) // 2
        pivot = self.data[pivot_index]
        self.data[pivot_index], self.data[-1] = self.data[-1], self.data[pivot_index]

        i = left_pointer
        for j in range(left_pointer, right_pointer):
            if self.data[j] < pivot:
                self.data[i], self.data[j] = self.data[j], self.data[i]
                i += 1
        
        self.data[i], self.data[-1] = self.data[-1], self.data[i]

        quickSort(left_pointer, i)
        quickSort(i + 1, right_pointer)



