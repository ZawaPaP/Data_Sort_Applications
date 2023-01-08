import sort_function
from sort_type import SortType, available_sort_type
import sys

def sort(data, sort_option):
    try:
        sort_type = SortType(sort_option).return_sort_type(sort_option)
    except ValueError as e:
        print("Error: ", e)
        available_sort_type()
        sys.exit(1)

    if sort_type == "INSERT_SORT":
        sorted_data = sort_function.insert_sort(data)
    elif sort_type == "MERGE_SORT":
        sorted_data = sort_function.merge_sort(data)
    elif sort_type == "QUICK_SORT":
        sorted_data = sort_function.quick_sort(data)
    elif sort_type == "BUBBLE_SORT":
        sorted_data = sort_function.bubble_sort(data)
    return sorted_data
