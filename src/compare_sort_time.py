import sort_function
import copy, time
from set_logger import SetLogger

def compare_sort_time(data):
    logger = SetLogger().set_logger(__name__)

    tmp1 = copy.copy(data)
    tmp2 = copy.copy(data)
    tmp3 = copy.copy(data)
    tmp4 = copy.copy(data)
    n = len(data)
    i_time =round(insert_time_count(tmp1), 8)
    m_time =round(merge_time_count(tmp2), 8)
    q_time =round(quick_time_count(tmp3), 8)
    b_time =round(bubble_time_count(tmp4), 8)

    t = [
        ['Insert', i_time],
        ['Merge', m_time],
        ['Quick', q_time],
        ['Bubble', b_time]
    ]
    print ("{:20}{:<8}".format('Sort type','Time(data size: {})'.format(n)))
    for i, j in t:
        print ("{:<20}{:<8}".format(i, j))

def insert_time_count(data):
    start_time = time.perf_counter()
    sort_function.insert_sort(data)
    return time.perf_counter() - start_time

def merge_time_count(data):
    start_time = time.perf_counter()
    sort_function.merge_sort(data)
    return time.perf_counter() - start_time

def quick_time_count(data):
    start_time = time.perf_counter()
    sort_function.quick_sort(data)
    return time.perf_counter() - start_time

def bubble_time_count(data):
    start_time = time.perf_counter()
    sort_function.insert_sort(data)
    return time.perf_counter() - start_time
