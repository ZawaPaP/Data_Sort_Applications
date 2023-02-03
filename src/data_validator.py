import sys
from set_logger import SetLogger

def validate_data(data):
    logger = SetLogger().set_logger(__name__)
    if not data:
        logger.error("There is no input data")
        sys.exit(1)
    
    data = __return_list(data)
    return __return_int(data)

def __return_list(data):
    if isinstance(data, list):
        return data
    else:
        return __change_to_list(data)

    
def __change_to_list(data):
    logger = SetLogger().set_logger(__name__)
    try:
        return data.split()
    except TypeError as e:
        logger.error(e)
        logger.error('Unable to convert the data to list {}'.format(data))


def __return_int(data):
    logger = SetLogger().set_logger(__name__)
    for i in range(len(data)):
        if not isinstance(data[i], int):
            try:
                data[i] = int(data[i])
            except ValueError as e:
                logger.error(e)
                sys.exit(1)
            except TypeError as e:
                logger.error(e)
                sys.exit(1)
    return data
