import logging

def read_input_file_data(input_file):
    logger.debug('Start of read_input_file_data')
    data = input_file.readlines()
    input_file.close()
    logger.debug('End of read_input_file_data')
    return data

def write_output_to_file(output_file, sortedList):
    logger.debug('Start of write_output_file_data')
    for x in sortedList:
        output_file.writelines(str(x)+'\n')
    output_file.close()
    logger.debug('End of write_output_file_data')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
fh = logging.FileHandler('./log.log')
fh.setFormatter(f)
logger.addHandler(fh)  
