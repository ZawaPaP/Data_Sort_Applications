# time complexity O(N^2), space complexity O(N) - using space for data[]
def insertSort(data):
    if not data:
        print("There is no data")
        return
    for i in range(1, len(data)):
        curr = data[i]

        j = i
        while j >= 1:
            if (data[j-1] > curr):
                data[j] = data[j-1]
                j -= 1
            else:
                break
        data[j] = curr
        

# time complexity O(NlogN), space complexity O(2N) - using space for data[] and queue()
def mergeSort(data):
    if len(data) <= 1:
        return

    mid = len(data) // 2
    sub_array1 = data[:mid]
    sub_array2 = data[mid:]

    mergeSort(sub_array1)
    mergeSort(sub_array2)

    sub_array3 = sub_array1 + sub_array2
    i = 0
    while sub_array3:
        if sub_array3[0] <= sub_array3[-1]:
            data[i] = sub_array3.pop(0)
        else:
            data[i] = sub_array3.pop()
        i += 1


def quickSort(data):
    if right_pointer - left_pointer <= 1:
        return

    pivot_index = (left_pointer + right_pointer) // 2
    pivot = data[pivot_index]
    data[pivot_index], data[-1] = data[-1], data[pivot_index]

    i = left_pointer
    for j in range(left_pointer, right_pointer):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
    
    data[i], data[-1] = data[-1], data[i]

    self.quickSort(left_pointer, i)
    self.quickSort(i + 1, right_pointer)



