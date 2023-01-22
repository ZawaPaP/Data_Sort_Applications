import sys, logging


def validate_data(data):
    logger.debug('Start of validate_data {}'.format(data))
    if not data:
        logger.warning("There is no input data")
        sys.exit(1)
    
    data = __return_list(data)
    logger.debug('End of return_list {}'.format(data))
    return __return_int(data)

def __return_list(data):
    logger.debug('Start of return_list')
    if isinstance(data, list):
        return data
    else:
        return __change_to_list(data)

    
def __change_to_list(data):
    logger.debug('Start of change_to_list {}'.format(data))
    try:
        return data.split()
    except TypeError as e:
        logger.error(e)
    logger.debug('Unable to convert the data to list {}'.format(data))


def __return_int(data):
    logger.debug('Start of return_list {}'.format(data))
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
    logger.debug('End of return_list{}'.format(data))
    return data

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
fh = logging.FileHandler('./log/data_validator.log')
fh.setFormatter(f)
logger.addHandler(fh)    
