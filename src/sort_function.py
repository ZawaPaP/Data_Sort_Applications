# time complexity O(N^2), space complexity O(N) - using space for data[]
def insert_sort(data):
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
    return data
        

# time complexity O(NlogN), space complexity O(2N) - using space for data[] and queue()
def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2

    sub_array1 = merge_sort(data[:mid])
    sub_array2 = merge_sort(data[mid:])

    return merge(sub_array1, sub_array2)

def merge(sub_array1, sub_array2):
    i = j = 0
    data = []
    while i < len(sub_array1) and j < len(sub_array2): 
        if sub_array1[i] <= sub_array2[j]: 
            data.append(sub_array1[i])
            i += 1 
        else:
            data.append(sub_array2[j])
            j += 1
    if i < len(sub_array1):
        data.extend(sub_array1[i:])
    if j < len(sub_array2):
        data.extend(sub_array2[j:]) 
        
    return data

def quick_sort(data): 
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [i for i in data if i < pivot]
    right = [i for i in data if i > pivot]
    pivot = [i for i in data if i == pivot]

    left = quick_sort(left)  
    right = quick_sort(right)

    return left + pivot + right

def bubble_sort(data):
    tmp = 0
    for i in range(0, len(data) - 1):
        for j in range(0, len(data) - 1 - i):
            if data[j] > data[j+1]:
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp
    return data


    
    



