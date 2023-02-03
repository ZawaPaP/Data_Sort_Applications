import sort_function
from sort_type import SortType, available_sort_type
import sys, logging


def sort_data(data, sort_option):
    logger.debug('Start of sort')
    try:
        if sort_option == SortType.INSERT.value:
            logger.debug('Start of insert_sort')
            sorted_data = sort_function.insert_sort(data)
        elif sort_option == SortType.MERGE.value:
            logger.debug('Start of merge_sort')
            sorted_data = sort_function.merge_sort(data)
        elif sort_option == SortType.QUICK.value:
            logger.debug('Start of quick_sort')
            sorted_data = sort_function.quick_sort(data)
        elif sort_option == SortType.BUBBLE.value:
            logger.debug('Start of bubble_sort')
            sorted_data = sort_function.bubble_sort(data)
        return sorted_data
    except UnboundLocalError as e:
        logger.info(e)
        logger.info('sort_option: ' + str(sort_option))
        available_sort_type()
        sys.exit(1)
        
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
fh = logging.FileHandler('./log/sort.log')
fh.setFormatter(f)
logger.addHandler(fh) 
