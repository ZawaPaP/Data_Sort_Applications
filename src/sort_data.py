import sort_function
from sort_type import SortType, available_sort_type
import sys
from set_logger import SetLogger

def sort_data(data, sort_option):
    logger = SetLogger().set_logger(__name__)
    try:
        if sort_option == SortType.INSERT.value:
            logger.debug('Start of insert_sort')
            result = sort_function.insert_sort(data)
        elif sort_option == SortType.MERGE.value:
            logger.debug('Start of merge_sort')
            result = sort_function.merge_sort(data)
        elif sort_option == SortType.QUICK.value:
            logger.debug('Start of quick_sort')
            result = sort_function.quick_sort(data)
        elif sort_option == SortType.BUBBLE.value:
            logger.debug('Start of bubble_sort')
            result = sort_function.bubble_sort(data)
        logger.info("Processed time: " + str(result[1]) + " seconds")
        return result[0]
    except UnboundLocalError as e:
        logger.warning(e)
        logger.warning('sort_option: ' + str(sort_option))
        available_sort_type()
        sys.exit(1)

