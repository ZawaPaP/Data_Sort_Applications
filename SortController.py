import SortFunction

def sortController(data, sort_type):
    if sort_type == "insert":
        SortFunction.insertSort(data)
    elif sort_type == "merge":
        SortFunction.mergeSort(data)
    elif sort_type == "quick":
        SortFunction.quickSort(data)
    else:
        print('invalid sort_type')
    return data