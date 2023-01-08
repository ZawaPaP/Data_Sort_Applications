from enum import Enum, auto

class SortType(Enum):
    INSERT_SORT = auto()
    MERGE_SORT = auto()
    QUICK_SORT = auto()
    BUBBLE_SORT = auto()

    def return_sort_type(self, sort_option):
        if SortType(sort_option):
            return SortType(sort_option).name


def available_sort_type():
    for i in SortType:
        print("{number}: {sort_type}".format(number = i.value, sort_type = i))