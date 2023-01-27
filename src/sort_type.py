from enum import Enum, auto

class SortType(Enum):
    INSERT = auto()
    MERGE = auto()
    QUICK = auto()
    BUBBLE = auto()

def available_sort_type():
    for i in SortType:
        print("{number}: {sort_type}".format(number = i.value, sort_type = i))
