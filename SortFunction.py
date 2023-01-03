# time complexity O(N^2), space complexity O(N) - using space for data[]
def insertSort(data):
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

    k = 0
    i = j = 0
    while i < len(sub_array1) and j < len(sub_array2): 
        if sub_array1[i] <= sub_array2[j]: 
            data[k] = sub_array1[i] 
            i += 1 
        else:
            data[k] = sub_array2[j]
            j += 1
        k += 1

    while i < len(sub_array1):
        data[k] = sub_array1[i]
        i += 1
        k += 1

    while j < len(sub_array2):
        data[k] = sub_array2[j]
        j += 1
        k += 1


""" code is wrong
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

    quickSort(left_pointer, i)
    quickSort(i + 1, right_pointer)
"""


