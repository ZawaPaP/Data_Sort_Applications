
# time complexity O(N^2), space complexity O(N) - using space for data[]
def insert_sort(data):
    for i in range(1, len(data)):
        curr = data[i]

        j = i
        while (j >= 1 and data[j-1] > curr):
            data[j] = data[j-1]
            j -= 1
            yield data
        yield data
        data[j] = curr
    return data
        

# time complexity O(NlogN), space complexity O(2N) - using space for data[] and queue()
def merge_sort(data, start, end):
    if start >= end:
        return
    mid = start + ((end - start + 1) // 2) - 1
    
    yield from merge_sort(data, start, mid)
    yield from merge_sort(data, mid + 1, end)
    yield from merge(data, start, mid, end)

def merge(data, start, mid, end):
    merged = []
    l = start
    r = mid + 1
        
    while l <= mid and r<= end: 
        if data[l] <= data[r]: 
            merged.append(data[l])
            l += 1 
        else:
            merged.append(data[r])
            r += 1

    while l <= mid:
        merged.append(data[l])
        l += 1 
        
    while r <= end:
        merged.append(data[r])
        r += 1 

    for i in range(len(merged)):
        data[start + i] = merged[i]
        yield data

def quick_sort(data, l, r): 
    if l >= r:
        return
    
    pivot = data[l]
    j = l
    for i in range(l + 1, r + 1):
        if pivot >= data[i]:
            j += 1
            data[j], data[i] = data[i], data[j]
        yield data
    data[l], data[j] = data[j], data[l]
    yield data

    yield from quick_sort(data, l, j - 1)  
    yield from quick_sort(data, j + 1, r)


def bubble_sort(data):
    tmp = 0
    for i in range(0, len(data) - 1):
        for j in range(0, len(data) - 1 - i):
            if data[j] > data[j+1]:
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp
                yield data
        yield data
    yield data
    return data
